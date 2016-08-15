import xmltodict
import pprint
import os
import json


output = []


def main():
    with open('data/OAIPMH/ilr-bepress.oai.docexport.xml') as fh:
        data = xmltodict.parse(fh.read())

    docs = data['OAI-PMH']['ListRecords']['record']

    for n in range(len(docs)):
        record = {}
        for key in docs[n].keys():
            if key == 'header':
                for key2 in docs[n][key].keys():
                    if key2 == 'datestamp':
                        record['oai:datestamp'] = docs[n][key][key2]
                    elif key2 == 'setSpec':
                        record['oai:setSpec'] = docs[n][key][key2]
                    elif key2 == 'identifier':
                        record['oai:identifier'] = docs[n][key][key2]
            elif key == 'metadata':
                meta = docs[n][key]['document-export']['documents']['document']
                for key2 in meta.keys():
                    if key2 in ['abstract', 'articleid', 'context-key', 'coverpage-url', 'document-type', 'fulltext-url', 'label', 'native-url', 'publication-date', 'publication-title', 'submission-date', 'submission-path', 'title', 'type']:
                        if meta.get(key2):
                            if record.get(key2) is None:
                                record[key2] = meta[key2]
                            else:
                                prelim = record.get(key2)
                                record[key2] = prelim + '|' + meta[key2]
                        if key2 == 'submission-path':
                            s3url = 's3://dc-ilr-cornell-edu-archive/archive/digitalcommons.ilr.cornell.edu/'
                            subpath = meta[key2]
                            s3cmd = 's3cmd ls ' + s3url + subpath + '/ > output.txt'
                            os.system(s3cmd)
                            with open('output.txt', 'r') as fh:
                                filenames = fh.read().split()
                            for filename in filenames:
                                if not filename.startswith('s3') or filename[0].isdigit():
                                    filenames.remove(filename)
                            # not sure why i need to run this twice to get rid
                            # of timestamps, but whatevs for now
                            for filename in filenames:
                                if not filename.startswith('s3') or filename[0].isdigit():
                                    filenames.remove(filename)
                            clean_files = []
                            for filename in filenames:
                                clean_files.append(filename.replace(s3url, ''))
                            record['filenames'] = clean_files
                    elif key2 == 'disciplines':
                        if not record.get(key2):
                            record[key2] = meta['disciplines']['discipline']
                        else:
                            prelim = record.get(key2)
                            record[key2] = prelim + '|' + meta['disciplines']['discipline']
                    elif key2 == 'subject-areas':
                        if meta.get(key2):
                            if meta[key2].get('subject-area'):
                                if not record.get(key2):
                                    record[key2] = meta['subject-areas']['subject-area']
                                else:
                                    prelim = record.get(key2)
                                    record[key2] = prelim + '|' + meta['subject-areas']['subject-area']
                    elif key2 == 'keywords':
                        if not record.get(key2):
                            record[key2] = meta['keywords']['keyword']
                        else:
                            prelim = record.get(key2)
                            record[key2] = prelim + '|' + meta['keywords']['keyword']
                    elif key2 == 'authors':
                        if meta.get('authors'):
                            record['authors'] = meta['authors']['author']
                    elif key2 == 'supplemental-files':
                        if meta.get('supplemental-files'):
                            record['supplemental-files'] = meta['supplemental-files']['file']
                    elif key2 == 'fields':
                        if meta.get('fields'):
                            if isinstance(meta['fields']['field'], list):
                                for field in meta['fields']['field']:
                                    fieldkey = field['@name']
                                    if 'value' in field:
                                        if not record.get(fieldkey):
                                            record[fieldkey] = field['value']
                                        else:
                                            prelim = record.get(fieldkey)
                                            record[fieldkey] = prelim + '|' + field['value']
                            else:
                                fieldkey = meta['fields']['field']['@name']
                                if not record.get(fieldkey):
                                    record[fieldkey] = meta['fields']['field']['value']
                                else:
                                    prelim = record.get(fieldkey)
                                    record[fieldkey] = prelim + '|' + meta['fields']['field']['value']
                output.append(record)
                pprint.pprint(record)
    with open('output.json', 'w') as outputdata:
        json.dump(output, outputdata)


if __name__ == '__main__':
    main()
