#ILR Bepress Review

##S3 Backup Metadata Review
Data harvested, reviewed last on August 15th, 2016.

**S3 backup record total**: 21433 (missing 4547 records in backup?)

```
                            abstract: |=======                  |   6777/21433 |  31%
                           articleid: |=========================|  21433/21433 | 100%
                             authors: |=========================|  21433/21433 | 100%
                      authors/author: |================         |  14424/21433 |  67%
                authors/author/email: |=                        |   1256/21433 |   5%
                authors/author/fname: |=====                    |   4674/21433 |  21%
          authors/author/institution: |===                      |   2905/21433 |  13%
                authors/author/lname: |=====                    |   4674/21433 |  21%
                authors/author/mname: |==                       |   2557/21433 |  11%
         authors/author/organization: |========                 |   7000/21433 |  32%
               authors/author/suffix: |                         |    282/21433 |   1%
                         context-key: |=========================|  21433/21433 | 100%
                       coverpage-url: |=========================|  21433/21433 | 100%
                         disciplines: |=                        |   1440/21433 |   6%
              disciplines/discipline: |=                        |   1440/21433 |   6%
                       document-type: |=========================|  21433/21433 | 100%
                              fields: |======================== |  21387/21433 |  99%
                        fields/field: |======================== |  21387/21433 |  99%
                  fields/field/@name: |==                       |   2223/21433 |  10%
                  fields/field/@type: |==                       |   2223/21433 |  10%
                  fields/field/value: |==                       |   2223/21433 |  10%
                            file_dir: |=========================|  21433/21433 | 100%
                               files: |=========================|  21433/21433 | 100%
                        fulltext-url: |======================== |  21225/21433 |  99%
                            keywords: |=======================  |  20134/21433 |  93%
                    keywords/keyword: |=======================  |  20134/21433 |  93%
                               label: |=========================|  21433/21433 | 100%
                          native-url: |                         |    498/21433 |   2%
                    publication-date: |=========================|  21433/21433 | 100%
                   publication-title: |=========================|  21433/21433 | 100%
                       subject-areas: |                         |    414/21433 |   1%
          subject-areas/subject-area: |                         |    358/21433 |   1%
                     submission-date: |=========================|  21433/21433 | 100%
                     submission-path: |=========================|  21433/21433 | 100%
                  supplemental-files: |                         |    452/21433 |   2%
             supplemental-files/file: |                         |    452/21433 |   2%
supplemental-files/file/archive-name: |                         |    429/21433 |   2%
 supplemental-files/file/description: |                         |    296/21433 |   1%
   supplemental-files/file/mime-type: |                         |    429/21433 |   2%
 supplemental-files/file/upload-name: |                         |    429/21433 |   2%
         supplemental-files/file/url: |                         |    429/21433 |   2%
                               title: |=========================|  21433/21433 | 100%
                                type: |=========================|  21433/21433 | 100%
                           withdrawn: |                         |     22/21433 |   0%
```

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
    oai:metadata/oai_dc:dc/dc:creator: |=============            |  14396/26069 |  55%
       oai:metadata/oai_dc:dc/dc:date: |=========================|  26069/26069 | 100%
oai:metadata/oai_dc:dc/dc:description: |======                   |   6779/26069 |  26%
     oai:metadata/oai_dc:dc/dc:format: |======================== |  26047/26069 |  99%
 oai:metadata/oai_dc:dc/dc:identifier: |=========================|  26069/26069 | 100%
  oai:metadata/oai_dc:dc/dc:publisher: |=========================|  26069/26069 | 100%
     oai:metadata/oai_dc:dc/dc:source: |=========================|  26069/26069 | 100%
    oai:metadata/oai_dc:dc/dc:subject: |=======================  |  24799/26069 |  95%
      oai:metadata/oai_dc:dc/dc:title: |=========================|  26069/26069 | 100%
       oai:metadata/oai_dc:dc/dc:type: |=========================|  26069/26069 | 100%

```

###Simple Dublin Core Review
**File**: [ilr-bepress.oai.sdc.xml](data/OAIPMH/ilr-bepress.oai.dc.xml)

**Overview**:
```

             oai:header/oai:datestamp: |=========================|  26116/26116 | 100%
            oai:header/oai:identifier: |=========================|  26116/26116 | 100%
               oai:header/oai:setSpec: |=========================|  26116/26116 | 100%
   oai:metadata/oai_dc:dc/dc:coverage: |==                       |   3020/26116 |  11%
    oai:metadata/oai_dc:dc/dc:creator: |=============            |  14396/26116 |  55%
       oai:metadata/oai_dc:dc/dc:date: |======================== |  25320/26116 |  96%
oai:metadata/oai_dc:dc/dc:description: |=======================  |  24394/26116 |  93%
 oai:metadata/oai_dc:dc/dc:identifier: |======================== |  25403/26116 |  97%
  oai:metadata/oai_dc:dc/dc:publisher: |=                        |   1623/26116 |   6%
    oai:metadata/oai_dc:dc/dc:subject: |=======================  |  24846/26116 |  95%
      oai:metadata/oai_dc:dc/dc:title: |======================== |  25403/26116 |  97%
       oai:metadata/oai_dc:dc/dc:type: |==                       |   2485/26116 |   9%
```


###QDC Review
**File**: [ilr-bepress.oai.qdc.xml](data/OAIPMH/ilr-bepress.oai.qdc.xml})

**Overview**:
```
                       oai:header/oai:datestamp: |=========================|  26116/26116 | 100%
                      oai:header/oai:identifier: |=========================|  26116/26116 | 100%
                         oai:header/oai:setSpec: |=========================|  26116/26116 | 100%
     oai:metadata/oai_dc:dc/dc:coverage.spatial: |                         |    113/26116 |   0%
 oai:metadata/oai_dc:dc/dc:coverage.spatial.lat: |==                       |   2907/26116 |  11%
oai:metadata/oai_dc:dc/dc:coverage.spatial.long: |==                       |   2907/26116 |  11%
              oai:metadata/oai_dc:dc/dc:creator: |=============            |  14396/26116 |  55%
       oai:metadata/oai_dc:dc/dc:date.available: |                         |     10/26116 |   0%
         oai:metadata/oai_dc:dc/dc:date.created: |======================== |  25318/26116 |  96%
          oai:metadata/oai_dc:dc/dc:description: |======================   |  23131/26116 |  88%
 oai:metadata/oai_dc:dc/dc:description.abstract: |======                   |   6779/26116 |  25%
           oai:metadata/oai_dc:dc/dc:identifier: |======================== |  25403/26116 |  97%
            oai:metadata/oai_dc:dc/dc:publisher: |=                        |   1623/26116 |   6%
              oai:metadata/oai_dc:dc/dc:subject: |=======================  |  24846/26116 |  95%
                oai:metadata/oai_dc:dc/dc:title: |======================== |  25403/26116 |  97%
                 oai:metadata/oai_dc:dc/dc:type: |==                       |   2485/26116 |   9%
```

###ETDMS Review
**File**: [ilr-bepress.oai.etdms.xml](data/OAIPMH/ilr-bepress.oai.etdms.xml)

**Overview**:
```

```

##Web Scraping Metadata/Microdata Review
Total URLs/records scraped: 24,829 URLS (OAI document/coverpage-url).

Data harvested last on April 28th, 2016.

###Fields pulled from the HTML:

- meta[@name] and meta[@content] when meta[@name] is not 'viewport':
    - /meta[@name="bepress_citation_pdf_url"][@content]
    - /meta[@name="bepress_citation_publisher"][@content]
    - /meta[@name="description"][@content]
    - /meta[@name="bepress_citation_online_date"][@content]
    - /meta[@name="bepress_citation_author"][@content]
    - /meta[@name="bepress_citation_author_institution"][@content]
    - /meta[@name="bepress_citation_abstract_html_url"][@content]
    - /meta[@name="bepress_citation_volume"][@content]
    - /meta[@name="bepress_citation_issue"][@content]
    - /meta[@name="bepress_citation_firstpage"][@content]
    - /meta[@name="bepress_is_article_cover_page"][@content]
    - /meta[@name="bepress_citation_title"][@content]
    - /meta[@name="keywords"][@content]
    - /meta[@name="bepress_citation_journal_title"][@content]
    - /meta[@name="bepress_citation_date"][@content]
    - /meta[@name="bepress_citation_series_title"][@content]
- Content divs:
    - div[@id='alpha']/div[@id=title]/p
    - div[@id='alpha']/div[@id=publication_date]/p
    - div[@id='alpha']/div[@id=comments]/p
    - div[@id='alpha']/div[@id=sector]/p
    - div[@id='alpha']/div[@id=abstract]/p
    - div[@id='alpha']/div[@id=fulltext_url]/p
    - div[@id='alpha']/div[@id=keywords]/p
    - div[@id='alpha']/div[@id=city]/p
    - div[@id='alpha']/div[@id=union]/p
    - div[@id='alpha']/div[@id=employer]/p
    - div[@id='alpha']/div[@id=bp_categories]/p
    - div[@id='alpha']/div[@id=number_workers]/p
    - div[@id='alpha']/div[@id=contract_location]/p
    - div[@id='alpha']/div[@id=playback_time]/p
    - div[@id='alpha']/div[@id=authors]/p
    - div[@id='alpha']/div[@id=item_id]/p
    - div[@id='alpha']/div[@id=document_type]/p
    - div[@id='alpha']/div[@id=publisher]/p
    - div[@id='alpha']/div[@id=recommended_citation]/p
    - div[@id='alpha']/div[@id=naics]/p
    - div[@id='alpha']/div[@id=expiration_date]/p
    - div[@id='alpha']/div[@id=series_url]/p
    - div[@id='alpha']/div[@id=union_local]/p

###Present in OAI feed and/or backup metadata?

Most of the fields in the HTML paths targeted is captured in the various other metadata sources, albeit sometimes the HTML metadata display/generation is a number of fields concatenated (i.e. author first and last names going into a meta tag for author), or the fields are taken from 1 metadata field value (i.e. the object in context URL from which you can get journal volume, issue, and starting page number).
