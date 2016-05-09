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


def removeS3(rootdir):
    """Remove S3 directory stored locally."""
    print('removing s3 copy locally.')
    if not os.listdir(rootdir):
        print('no s3 backup copy locally.')
    else:
        s3rm = 'rm -rf ' + rootdir
        os.system(s3rm)


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


def collect_stats(stats_aggregate, stats):
    # increment the record counter
    stats_aggregate["record_count"] += 1
    for field in stats:
        # get the total number of times a field occurs
        stats_aggregate["field_info"].setdefault(field, {"field_count": 0})
        stats_aggregate["field_info"][field]["field_count"] += 1
        # get average of all fields
        stats_aggregate["field_info"][field].setdefault("field_count_total", 0)
        stats_aggregate["field_info"][field]["field_count_total"] += stats[field]


def create_stats_averages(stats_aggregate):
    for field in stats_aggregate["field_info"]:
        field_count = stats_aggregate["field_info"][field]["field_count"]
        field_count_total = stats_aggregate["field_info"][field]["field_count_total"]

        field_count_total_average = (float(field_count_total) / float(stats_aggregate["record_count"]))
        stats_aggregate["field_info"][field]["field_count_total_average"] = field_count_total_average

        field_count_element_average = (float(field_count_total) / float(field_count))
        stats_aggregate["field_info"][field]["field_count_element_average"] = field_count_element_average

    return stats_aggregate


def pretty_print_stats(stats_averages):
    record_count = stats_averages["record_count"]
    # get header length
    element_length = 0
    for element in stats_averages["field_info"]:
        if element_length < len(element):
            element_length = len(element)

    print("\n\n")
    for element in sorted(stats_averages["field_info"]):
        percent = (stats_averages["field_info"][element]["field_count"] / float(record_count)) * 100
        percentPrint = "=" * (int((percent) / 4))
        columnOne = " " * (element_length - len(element)) + element
        print("%s: |%-25s| %6s/%s | %3d%% " % (
                    columnOne,
                    percentPrint,
                    stats_averages["field_info"][element]["field_count"],
                    record_count,
                    percent
                ))

    print("\n")


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

    s3colls = []
    with open('data/s3colls.txt') as fh:
        s3colls = fh.read().splitlines()

    stats_aggregate = {
            "record_count": 0,
            "field_info": {}
        }
    for coll in s3colls:
        print(coll)
        if not os.path.exists(args.rootdir + coll):
            os.makedirs(args.rootdir + coll)
        grabS3(args.s3url + coll, args.rootdir + coll)

        output = {}
        output['documents'] = []
        (output, records) = parseS3(args.rootdir, output)

        fields = set()
        for n in range(len(output['documents'])):
            stats = {}
            if 'supplemental-files' in output['documents'][n]['document'].keys():
                output['documents'][n]['document']['supplemental-files']
            for key in output['documents'][n]['document'].keys():
                fields.add(key)
                stats.setdefault(key, 0)
                stats[key] += 1
                try:
                    for key2 in output['documents'][n]['document'][key].keys():
                        fields.add(key + '/' + key2)
                        stats.setdefault(key + '/' + key2, 0)
                        stats[key + '/' + key2] += 1
                        try:
                            for key3 in output['documents'][n]['document'][key][key2].keys():
                                fields.add(key + '/' + key2 + '/' + key3)
                                stats.setdefault(key + '/' + key2 + '/' + key3, 0)
                                stats[key + '/' + key2 + '/' + key3] += 1
                        except:
                            pass
                except:
                    pass
            collect_stats(stats_aggregate, stats)
        pprint.pprint(stats_aggregate)
        try:
            removeS3(args.rootdir + coll)
        except Exception as e:
            print(e)
            pass
    stats_averages = create_stats_averages(stats_aggregate)
    pretty_print_stats(stats_averages)

if __name__ == "__main__":
    main()
