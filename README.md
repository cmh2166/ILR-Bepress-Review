#ILR Bepress Review

##S3 Backup Metadata Review

Total records in all feeds as of this review: 24889
Data harvested last on May 9th, 2016.

```
                            abstract: |======                   |   6685/24889 |  26%
                           articleid: |=========================|  24889/24889 | 100%
                             authors: |=========================|  24889/24889 | 100%
                      authors/author: |==============           |  14021/24889 |  56%
                authors/author/email: |=                        |   1237/24889 |   4%
                authors/author/fname: |====                     |   4316/24889 |  17%
          authors/author/institution: |==                       |   2859/24889 |  11%
                authors/author/lname: |====                     |   4316/24889 |  17%
                authors/author/mname: |==                       |   2301/24889 |   9%
         authors/author/organization: |=======                  |   6990/24889 |  28%
               authors/author/suffix: |                         |    264/24889 |   1%
                         context-key: |=========================|  24889/24889 | 100%
                       coverpage-url: |=========================|  24889/24889 | 100%
                         disciplines: |=                        |   1397/24889 |   5%
              disciplines/discipline: |=                        |   1397/24889 |   5%
                       document-type: |=========================|  24889/24889 | 100%
                              fields: |======================== |  24847/24889 |  99%
                        fields/field: |======================== |  24847/24889 |  99%
                  fields/field/@name: |=                        |   1956/24889 |   7%
                  fields/field/@type: |=                        |   1956/24889 |   7%
                  fields/field/value: |=                        |   1956/24889 |   7%
                            file_dir: |=========================|  24889/24889 | 100%
                               files: |=========================|  24889/24889 | 100%
                        fulltext-url: |======================== |  24682/24889 |  99%
                            keywords: |=======================  |  23586/24889 |  94%
                    keywords/keyword: |=======================  |  23586/24889 |  94%
                               label: |=========================|  24889/24889 | 100%
                          native-url: |                         |    503/24889 |   2%
                    publication-date: |=========================|  24889/24889 | 100%
                   publication-title: |=========================|  24889/24889 | 100%
                       subject-areas: |                         |    404/24889 |   1%
          subject-areas/subject-area: |                         |    348/24889 |   1%
                     submission-date: |=========================|  24889/24889 | 100%
                     submission-path: |=========================|  24889/24889 | 100%
                  supplemental-files: |                         |    451/24889 |   1%
             supplemental-files/file: |                         |    451/24889 |   1%
supplemental-files/file/archive-name: |                         |    429/24889 |   1%
 supplemental-files/file/description: |                         |    296/24889 |   1%
   supplemental-files/file/mime-type: |                         |    429/24889 |   1%
 supplemental-files/file/upload-name: |                         |    429/24889 |   1%
         supplemental-files/file/url: |                         |    429/24889 |   1%
                               title: |=========================|  24889/24889 | 100%
                                type: |=========================|  24889/24889 | 100%
                           withdrawn: |                         |      1/24889 |   0%
```

##Web Scraping Metadata/Microdata Review
Total URLs/records scraped: 24,829 URLS (OAI document/coverpage-url)
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

Total records in all feeds as of this review: 24,824
Data harvested last on April 25th, 2016.

OAI-PMH Metadata Formats available via the Bepress OAI feed:

- document export
- oai-dc
- simple dublin core
- qualified dublin core
- oai etdms

###Document Export Review
**File**: [ilr-bepress.oai.docexport.xml](data/OAIPMH/ilr-bepress.oai.docexport.xml)

**Overview**:
```
                                                     oai:header/oai:datestamp: |=========================|  24829/24829 | 100%
                                                    oai:header/oai:identifier: |=========================|  24829/24829 | 100%
                                                       oai:header/oai:setSpec: |=========================|  24829/24829 | 100%
                                                            document/abstract: |======                   |   6680/24829 |  26%
                                                           document/articleid: |=========================|  24829/24829 | 100%
                                                document/authors/author/email: |==                       |   2300/24829 |   9%
                                                document/authors/author/fname: |======                   |   6685/24829 |  26%
                                          document/authors/author/institution: |=====                    |   5000/24829 |  20%
                                                document/authors/author/lname: |======                   |   6685/24829 |  26%
                                                document/authors/author/mname: |===                      |   3869/24829 |  15%
                                         document/authors/author/organization: |=======                  |   7406/24829 |  29%
                                               document/authors/author/suffix: |                         |    343/24829 |   1%
                                                         document/context-key: |=========================|  24829/24829 | 100%
                                                       document/coverpage-url: |=========================|  24829/24829 | 100%
                                              document/disciplines/discipline: |=                        |   1395/24829 |   5%
                                                       document/document-type: |=========================|  24829/24829 | 100%
                                                  document/fields/field/value: |======================== |  24787/24829 |  99%
            document/fields/field[@name=acknowledgements][@type=string]/value: |                         |    138/24829 |   0%
                        document/fields/field[@name=city][@type=string]/value: |                         |    113/24829 |   0%
                    document/fields/field[@name=comments][@type=string]/value: |=====================    |  21754/24829 |  87%
           document/fields/field[@name=contract_location][@type=string]/value: |                         |    836/24829 |   3%
             document/fields/field[@name=create_openurl][@type=boolean]/value: |                         |    589/24829 |   2%
                  document/fields/field[@name=embargo_date][@type=date]/value: |                         |    237/24829 |   0%
                    document/fields/field[@name=employer][@type=string]/value: |                         |    836/24829 |   3%
               document/fields/field[@name=expiration_date][@type=date]/value: |                         |    823/24829 |   3%
 document/fields/field[@name=expiration_date_date_format][@type=string]/value: |                         |    822/24829 |   3%
                  document/fields/field[@name=geolocate][@type=special]/value: |==                       |   2913/24829 |  11%
                   document/fields/field[@name=institute][@type=string]/value: |=                        |   1496/24829 |   6%
                     document/fields/field[@name=item_id][@type=string]/value: |                         |    836/24829 |   3%
                    document/fields/field[@name=latitude][@type=string]/value: |==                       |   2907/24829 |  11%
       document/fields/field[@name=letters_to_reviewers][@type=special]/value: |                         |    185/24829 |   0%
                   document/fields/field[@name=longitude][@type=string]/value: |==                       |   2907/24829 |  11%
           document/fields/field[@name=multimedia_format][@type=string]/value: |                         |     45/24829 |   0%
              document/fields/field[@name=multimedia_url][@type=string]/value: |                         |     45/24829 |   0%
                       document/fields/field[@name=naics][@type=string]/value: |                         |    836/24829 |   3%
              document/fields/field[@name=number_workers][@type=string]/value: |                         |    709/24829 |   2%
              document/fields/field[@name=peer_reviewed][@type=boolean]/value: |                         |    990/24829 |   3%
               document/fields/field[@name=playback_time][@type=string]/value: |                         |     44/24829 |   0%
              document/fields/field[@name=publication_date][@type=date]/value: |======================== |  24430/24829 |  98%
document/fields/field[@name=publication_date_date_format][@type=string]/value: |                         |    895/24829 |   3%
                   document/fields/field[@name=publisher][@type=string]/value: |                         |    113/24829 |   0%
                      document/fields/field[@name=sector][@type=string]/value: |                         |    836/24829 |   3%
                 document/fields/field[@name=short_title][@type=string]/value: |                         |    214/24829 |   0%
         document/fields/field[@name=source_fulltext_url][@type=string]/value: |                         |      3/24829 |   0%
               document/fields/field[@name=special_issue][@type=string]/value: |                         |    182/24829 |   0%
                       document/fields/field[@name=union][@type=string]/value: |                         |    836/24829 |   3%
                 document/fields/field[@name=union_local][@type=string]/value: |                         |    318/24829 |   1%
         document/fields/field[@name=upload_cover_image][@type=special]/value: |                         |    113/24829 |   0%
                                                        document/fulltext-url: |======================== |  24622/24829 |  99%
                                                    document/keywords/keyword: |=======================  |  23526/24829 |  94%
                                                               document/label: |=========================|  24829/24829 | 100%
                                                          document/native-url: |                         |    503/24829 |   2%
                                                    document/publication-date: |=========================|  24829/24829 | 100%
                                                   document/publication-title: |=========================|  24829/24829 | 100%
                                          document/subject-areas/subject-area: |                         |    344/24829 |   1%
                                                     document/submission-date: |=========================|  24829/24829 | 100%
                                                     document/submission-path: |=========================|  24829/24829 | 100%
                                document/supplemental-files/file/archive-name: |                         |    451/24829 |   1%
                                 document/supplemental-files/file/description: |                         |    316/24829 |   1%
                                   document/supplemental-files/file/mime-type: |                         |    451/24829 |   1%
                                 document/supplemental-files/file/upload-name: |                         |    451/24829 |   1%
                                         document/supplemental-files/file/url: |                         |    451/24829 |   1%
                                                               document/title: |=========================|  24829/24829 | 100%
                                                                document/type: |=========================|  24829/24829 | 100%
```

###OAI-DC Review
**File**: [ilr-bepress.oai.oaidc.xml](data/OAIPMH/ilr-bepress.oai.oaidc.xml)

**Overview**:
```
    {http://purl.org/dc/elements/1.1/}creator: |==============           |  13960/24824 |  56%
       {http://purl.org/dc/elements/1.1/}date: |=========================|  24824/24824 | 100%
{http://purl.org/dc/elements/1.1/}description: |======                   |   6676/24824 |  26%
     {http://purl.org/dc/elements/1.1/}format: |======================== |  24802/24824 |  99%
 {http://purl.org/dc/elements/1.1/}identifier: |=========================|  24824/24824 | 100%
  {http://purl.org/dc/elements/1.1/}publisher: |=========================|  24824/24824 | 100%
     {http://purl.org/dc/elements/1.1/}source: |=========================|  24824/24824 | 100%
    {http://purl.org/dc/elements/1.1/}subject: |=======================  |  23554/24824 |  94%
      {http://purl.org/dc/elements/1.1/}title: |=========================|  24824/24824 | 100%
       {http://purl.org/dc/elements/1.1/}type: |=========================|  24824/24824 | 100%
```

###Simple Dublin Core Review
**File**: [ilr-bepress.oai.sdc.xml](data/OAIPMH/ilr-bepress.oai.dc.xml)

**Overview**:
```
   {http://purl.org/dc/elements/1.1/}coverage: |===                      |   3020/24824 |  12%
    {http://purl.org/dc/elements/1.1/}creator: |==============           |  13960/24824 |  56%
       {http://purl.org/dc/elements/1.1/}date: |======================== |  24031/24824 |  96%
{http://purl.org/dc/elements/1.1/}description: |=======================  |  23392/24824 |  94%
 {http://purl.org/dc/elements/1.1/}identifier: |======================== |  24111/24824 |  97%
  {http://purl.org/dc/elements/1.1/}publisher: |=                        |   1611/24824 |   6%
    {http://purl.org/dc/elements/1.1/}subject: |=======================  |  23557/24824 |  94%
      {http://purl.org/dc/elements/1.1/}title: |======================== |  24111/24824 |  97%
       {http://purl.org/dc/elements/1.1/}type: |==                       |   2466/24824 |   9%
```


###QDC Review
**File**: [ilr-bepress.oai.qdc.xml](data/OAIPMH/ilr-bepress.oai.qdc.xml})

**Overview**:
```
     {http://purl.org/dc/elements/1.1/}coverage.spatial: |                         |    113/24824 |   0%
 {http://purl.org/dc/elements/1.1/}coverage.spatial.lat: |==                       |   2907/24824 |  11%
{http://purl.org/dc/elements/1.1/}coverage.spatial.long: |==                       |   2907/24824 |  11%
              {http://purl.org/dc/elements/1.1/}creator: |==============           |  13960/24824 |  56%
       {http://purl.org/dc/elements/1.1/}date.available: |                         |      9/24824 |   0%
         {http://purl.org/dc/elements/1.1/}date.created: |======================== |  24029/24824 |  96%
          {http://purl.org/dc/elements/1.1/}description: |======================   |  22130/24824 |  89%
 {http://purl.org/dc/elements/1.1/}description.abstract: |======                   |   6677/24824 |  26%
           {http://purl.org/dc/elements/1.1/}identifier: |======================== |  24111/24824 |  97%
            {http://purl.org/dc/elements/1.1/}publisher: |=                        |   1611/24824 |   6%
              {http://purl.org/dc/elements/1.1/}subject: |=======================  |  23557/24824 |  94%
                {http://purl.org/dc/elements/1.1/}title: |======================== |  24111/24824 |  97%
                 {http://purl.org/dc/elements/1.1/}type: |==                       |   2466/24824 |   9%
```

###ETDMS Review
**File**: [ilr-bepress.oai.etdms.xml](data/OAIPMH/ilr-bepress.oai.etdms.xml)

**Overview**:
```
     {http://www.ndltd.org/standards/metadata/etdms/1.0/}coverage.spatial: |                         |    113/24824 |   0%
 {http://www.ndltd.org/standards/metadata/etdms/1.0/}coverage.spatial.lat: |==                       |   2907/24824 |  11%
{http://www.ndltd.org/standards/metadata/etdms/1.0/}coverage.spatial.long: |==                       |   2907/24824 |  11%
              {http://www.ndltd.org/standards/metadata/etdms/1.0/}creator: |==============           |  13960/24824 |  56%
       {http://www.ndltd.org/standards/metadata/etdms/1.0/}date.available: |                         |      9/24824 |   0%
         {http://www.ndltd.org/standards/metadata/etdms/1.0/}date.created: |======================== |  24029/24824 |  96%
          {http://www.ndltd.org/standards/metadata/etdms/1.0/}description: |======================   |  22130/24824 |  89%
 {http://www.ndltd.org/standards/metadata/etdms/1.0/}description.abstract: |======                   |   6677/24824 |  26%
           {http://www.ndltd.org/standards/metadata/etdms/1.0/}identifier: |======================== |  24111/24824 |  97%
            {http://www.ndltd.org/standards/metadata/etdms/1.0/}publisher: |=                        |   1611/24824 |   6%
              {http://www.ndltd.org/standards/metadata/etdms/1.0/}subject: |=======================  |  23557/24824 |  94%
                {http://www.ndltd.org/standards/metadata/etdms/1.0/}title: |======================== |  24111/24824 |  97%
                 {http://www.ndltd.org/standards/metadata/etdms/1.0/}type: |==                       |   2466/24824 |   9%
```
