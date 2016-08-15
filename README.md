#ILR Bepress Review

##S3 Backup Metadata Review
Data harvested, reviewed last on August 15th, 2016.

S3 backup record total:

```
                            abstract: |=======                  |   6718/23441 |  28%
                           articleid: |=========================|  23441/23441 | 100%
                             authors: |=========================|  23441/23441 | 100%
                      authors/author: |==============           |  13385/23441 |  57%
                authors/author/email: |=                        |   1242/23441 |   5%
                authors/author/fname: |====                     |   4328/23441 |  18%
          authors/author/institution: |===                      |   2871/23441 |  12%
                authors/author/lname: |====                     |   4328/23441 |  18%
                authors/author/mname: |==                       |   2307/23441 |   9%
         authors/author/organization: |======                   |   6321/23441 |  26%
               authors/author/suffix: |                         |    264/23441 |   1%
                         context-key: |=========================|  23441/23441 | 100%
                       coverpage-url: |=========================|  23441/23441 | 100%
                         disciplines: |=                        |   1418/23441 |   6%
              disciplines/discipline: |=                        |   1418/23441 |   6%
                       document-type: |=========================|  23441/23441 | 100%
                              fields: |======================== |  23399/23441 |  99%
                        fields/field: |======================== |  23399/23441 |  99%
                  fields/field/@name: |==                       |   1956/23441 |   8%
                  fields/field/@type: |==                       |   1956/23441 |   8%
                  fields/field/value: |==                       |   1956/23441 |   8%
                            file_dir: |=========================|  23441/23441 | 100%
                               files: |=========================|  23441/23441 | 100%
                        fulltext-url: |======================== |  23234/23441 |  99%
                            keywords: |=======================  |  22138/23441 |  94%
                    keywords/keyword: |=======================  |  22138/23441 |  94%
                               label: |=========================|  23441/23441 | 100%
                          native-url: |                         |    503/23441 |   2%
                    publication-date: |=========================|  23441/23441 | 100%
                   publication-title: |=========================|  23441/23441 | 100%
                       subject-areas: |                         |    413/23441 |   1%
          subject-areas/subject-area: |                         |    357/23441 |   1%
                     submission-date: |=========================|  23441/23441 | 100%
                     submission-path: |=========================|  23441/23441 | 100%
                  supplemental-files: |                         |    451/23441 |   1%
             supplemental-files/file: |                         |    451/23441 |   1%
supplemental-files/file/archive-name: |                         |    429/23441 |   1%
 supplemental-files/file/description: |                         |    296/23441 |   1%
   supplemental-files/file/mime-type: |                         |    429/23441 |   1%
 supplemental-files/file/upload-name: |                         |    429/23441 |   1%
         supplemental-files/file/url: |                         |    429/23441 |   1%
                               title: |=========================|  23441/23441 | 100%
                                type: |=========================|  23441/23441 | 100%
                           withdrawn: |                         |      1/23441 |   0%
```

##Web Scraping Metadata/Microdata Review
Total URLs/records scraped: 24,829 URLS (OAI document/coverpage-url).

Data harvested last on April 28th, 2016.

###Fields pulled from the HTML:

- meta[@name] and meta[@content] when meta[@name] is not 'viewport'
- div[@id='alpha']/div[@id=title]/p/a[@href] attribute and text
- div[@id='alpha']/div[@id=author]/p text
- div[@id='alpha']/div[@id=publication-date]/p text
- div[@id='alpha']/div[@id=comments]/p text


###HTML Analysis

```

```

###Present in OAI feed and/or backup metadata?



##OAI-PMH Metadata Review

OAI-PMH Data harvested last on August 15th, 2016

OAI-PMH Metadata Formats available via the Bepress OAI feed:

- document export (full metadata)
- oai-dc
- simple dublin core
- qualified dublin core
- oai etdms

###Document Export Review
**File**: [ilr-bepress.oai.docexport.xml](data/OAIPMH/ilr-bepress.oai.docexport.xml)
**Number of records in feed**: 25,980

**Overview**:
```
                                                            document/abstract: |======                   |   6778/25980 |  26%
                                                           document/articleid: |=========================|  25980/25980 | 100%
                                                document/authors/author/email: |==                       |   2345/25980 |   9%
                                                document/authors/author/fname: |======                   |   7061/25980 |  27%
                                          document/authors/author/institution: |====                     |   5084/25980 |  19%
                                                document/authors/author/lname: |======                   |   7061/25980 |  27%
                                                document/authors/author/mname: |===                      |   4131/25980 |  15%
                                         document/authors/author/organization: |=======                  |   7461/25980 |  28%
                                               document/authors/author/suffix: |                         |    362/25980 |   1%
                                                         document/context-key: |=========================|  25980/25980 | 100%
                                                       document/coverpage-url: |=========================|  25980/25980 | 100%
                                              document/disciplines/discipline: |=                        |   1443/25980 |   5%
                                                       document/document-type: |=========================|  25980/25980 | 100%
                                                  document/fields/field/value: |======================== |  25937/25980 |  99%
            document/fields/field[@name=acknowledgements][@type=string]/value: |                         |    138/25980 |   0%
                        document/fields/field[@name=city][@type=string]/value: |                         |    113/25980 |   0%
                    document/fields/field[@name=comments][@type=string]/value: |=====================    |  22615/25980 |  87%
           document/fields/field[@name=contract_location][@type=string]/value: |                         |    836/25980 |   3%
             document/fields/field[@name=create_openurl][@type=boolean]/value: |                         |    589/25980 |   2%
                  document/fields/field[@name=embargo_date][@type=date]/value: |                         |    238/25980 |   0%
                    document/fields/field[@name=employer][@type=string]/value: |                         |    836/25980 |   3%
               document/fields/field[@name=expiration_date][@type=date]/value: |                         |    823/25980 |   3%
 document/fields/field[@name=expiration_date_date_format][@type=string]/value: |                         |    822/25980 |   3%
                  document/fields/field[@name=geolocate][@type=special]/value: |==                       |   2913/25980 |  11%
                   document/fields/field[@name=institute][@type=string]/value: |=                        |   1510/25980 |   5%
                     document/fields/field[@name=item_id][@type=string]/value: |                         |    836/25980 |   3%
                    document/fields/field[@name=latitude][@type=string]/value: |==                       |   2907/25980 |  11%
       document/fields/field[@name=letters_to_reviewers][@type=special]/value: |                         |    185/25980 |   0%
                   document/fields/field[@name=longitude][@type=string]/value: |==                       |   2907/25980 |  11%
           document/fields/field[@name=multimedia_format][@type=string]/value: |                         |     45/25980 |   0%
              document/fields/field[@name=multimedia_url][@type=string]/value: |                         |     45/25980 |   0%
                       document/fields/field[@name=naics][@type=string]/value: |                         |    836/25980 |   3%
              document/fields/field[@name=number_workers][@type=string]/value: |                         |    709/25980 |   2%
              document/fields/field[@name=peer_reviewed][@type=boolean]/value: |                         |    990/25980 |   3%
               document/fields/field[@name=playback_time][@type=string]/value: |                         |     44/25980 |   0%
              document/fields/field[@name=publication_date][@type=date]/value: |======================== |  25578/25980 |  98%
document/fields/field[@name=publication_date_date_format][@type=string]/value: |                         |    895/25980 |   3%
                   document/fields/field[@name=publisher][@type=string]/value: |                         |    113/25980 |   0%
                      document/fields/field[@name=sector][@type=string]/value: |                         |    836/25980 |   3%
                 document/fields/field[@name=short_title][@type=string]/value: |                         |    214/25980 |   0%
         document/fields/field[@name=source_fulltext_url][@type=string]/value: |                         |      3/25980 |   0%
               document/fields/field[@name=special_issue][@type=string]/value: |                         |    182/25980 |   0%
                       document/fields/field[@name=union][@type=string]/value: |                         |    836/25980 |   3%
                 document/fields/field[@name=union_local][@type=string]/value: |                         |    318/25980 |   1%
         document/fields/field[@name=upload_cover_image][@type=special]/value: |                         |    113/25980 |   0%
                                                        document/fulltext-url: |======================== |  25773/25980 |  99%
                                                    document/keywords/keyword: |=======================  |  24677/25980 |  94%
                                                               document/label: |=========================|  25980/25980 | 100%
                                                          document/native-url: |                         |    504/25980 |   1%
                                                    document/publication-date: |=========================|  25980/25980 | 100%
                                                   document/publication-title: |=========================|  25980/25980 | 100%
                                          document/subject-areas/subject-area: |                         |    358/25980 |   1%
                                                     document/submission-date: |=========================|  25980/25980 | 100%
                                                     document/submission-path: |=========================|  25980/25980 | 100%
                                document/supplemental-files/file/archive-name: |                         |    452/25980 |   1%
                                 document/supplemental-files/file/description: |                         |    316/25980 |   1%
                                   document/supplemental-files/file/mime-type: |                         |    452/25980 |   1%
                                 document/supplemental-files/file/upload-name: |                         |    452/25980 |   1%
                                         document/supplemental-files/file/url: |                         |    452/25980 |   1%
                                                               document/title: |=========================|  25980/25980 | 100%
                                                                document/type: |=========================|  25980/25980 | 100%
                                                     oai:header/oai:datestamp: |=========================|  25980/25980 | 100%
                                                    oai:header/oai:identifier: |=========================|  25980/25980 | 100%
                                                       oai:header/oai:setSpec: |=========================|  25980/25980 | 100%
```

###OAI-DC Review
**File**: [ilr-bepress.oai.oaidc.xml](data/OAIPMH/ilr-bepress.oai.oaidc.xml)

**Overview**:
```
                                                                                  oai:header/oai:datestamp: |=========================|  26069/26069 | 100%
                                                                                 oai:header/oai:identifier: |=========================|  26069/26069 | 100%
                                                                                    oai:header/oai:setSpec: |=========================|  26069/26069 | 100%
    oai:metadata/{http://www.openarchives.org/OAI/2.0/oai_dc/}dc/{http://purl.org/dc/elements/1.1/}creator: |=============            |  14396/26069 |  55%
       oai:metadata/{http://www.openarchives.org/OAI/2.0/oai_dc/}dc/{http://purl.org/dc/elements/1.1/}date: |=========================|  26069/26069 | 100%
oai:metadata/{http://www.openarchives.org/OAI/2.0/oai_dc/}dc/{http://purl.org/dc/elements/1.1/}description: |======                   |   6779/26069 |  26%
     oai:metadata/{http://www.openarchives.org/OAI/2.0/oai_dc/}dc/{http://purl.org/dc/elements/1.1/}format: |======================== |  26047/26069 |  99%
 oai:metadata/{http://www.openarchives.org/OAI/2.0/oai_dc/}dc/{http://purl.org/dc/elements/1.1/}identifier: |=========================|  26069/26069 | 100%
  oai:metadata/{http://www.openarchives.org/OAI/2.0/oai_dc/}dc/{http://purl.org/dc/elements/1.1/}publisher: |=========================|  26069/26069 | 100%
     oai:metadata/{http://www.openarchives.org/OAI/2.0/oai_dc/}dc/{http://purl.org/dc/elements/1.1/}source: |=========================|  26069/26069 | 100%
    oai:metadata/{http://www.openarchives.org/OAI/2.0/oai_dc/}dc/{http://purl.org/dc/elements/1.1/}subject: |=======================  |  24799/26069 |  95%
      oai:metadata/{http://www.openarchives.org/OAI/2.0/oai_dc/}dc/{http://purl.org/dc/elements/1.1/}title: |=========================|  26069/26069 | 100%
       oai:metadata/{http://www.openarchives.org/OAI/2.0/oai_dc/}dc/{http://purl.org/dc/elements/1.1/}type: |=========================|  26069/26069 | 100% 

```

###Simple Dublin Core Review
**File**: [ilr-bepress.oai.sdc.xml](data/OAIPMH/ilr-bepress.oai.dc.xml)

**Overview**:
```

```


###QDC Review
**File**: [ilr-bepress.oai.qdc.xml](data/OAIPMH/ilr-bepress.oai.qdc.xml})

**Overview**:
```

```

###ETDMS Review
**File**: [ilr-bepress.oai.etdms.xml](data/OAIPMH/ilr-bepress.oai.etdms.xml)

**Overview**:
```

```
