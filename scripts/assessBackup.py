import os
import argparse
import xmltodict
import pprint


def grabS3(s3url, rootdir):
    """Grab S3 stored backup if not present in s3 directory (root dir)."""
    print('checking for s3 copy locally.')
    if not os.listdir(rootdir):
        print('no s3 backup copy locally. Syncing now.')
        if not s3url.startswith('s3:') or rootdir.startswith('s3:'):
            print('check your arguments for s3 sync or run manually.')
        else:
            s3cmd = 's3cmd sync ' + s3url + ' ' + rootdir
        os.system(s3cmd)
    else:
        print('have s3 copy locally.')


def convertXMLtoDict(xmlfile):
    with open(xmlfile) as fh:
        data = xmltodict.parse(fh.read())
    doc = data['documents']
    return(doc)


def parseS3(rootdir, output):
    records = 0
    for subdir, dirs, files in os.walk(rootdir):
        if 'archive_manifest.json' not in files and 'metadata.xml' in files:
            workingdir = subdir.replace(rootdir, '')
            for file in files:
                if file == 'metadata.xml':
                    records += 1
                    doc = convertXMLtoDict(os.path.join(subdir, file))
                    doc['document'].update({'files': files})
                    doc['document'].update({'file_dir': workingdir})
                    output['documents'].append(doc)
    return(output, records)


def main():
    """Assess the S3 Bepress backup instance data."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--root", dest="rootdir",
                        help="root directory of backup")
    parser.add_argument("-s", "--s3", dest="s3url",
                        help="s3 (backup location) url")

    args = parser.parse_args()

    if not args.rootdir and not args.s3url:
        parser.print_help()
        parser.exit()

    grabS3(args.s3url, args.rootdir)

    output = {}
    output['documents'] = []

    (output, records) = parseS3(args.rootdir, output)
    fields = set()
    print(records)
    for n in range(len(output['documents'])):
        if 'supplemental-files' in output['documents'][n]['document'].keys():
            output['documents'][n]['document']['supplemental-files']
        for key in output['documents'][n]['document'].keys():
            fields.add(key)
            try:
                for key2 in output['documents'][n]['document'][key].keys():
                    fields.add(key + '/' + key2)
                    try:
                        for key3 in output['documents'][n]['document'][key][key2].keys():
                            fields.add(key + '/' + key2 + '/' + key3)
                    except:
                        pass
            except:
                pass
    pprint.pprint(fields)


if __name__ == "__main__":
    main()
