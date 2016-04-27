import requests
from lxml import html
import pprint

def grabURLs():
    URLS = []
    with open('data/urls.txt') as fh:
        URLS = fh.readlines()
    return(URLS)


def scrapeURLs(URLS):
    webdata = {}
    for url in URLS:
        resp = requests.get(url)
        tree = html.fromstring(resp.content)
        metatags = {}
        for meta in tree.xpath('//meta'):
            if meta.get('name') is not 'viewport':
                metatags[meta.get('name')] = meta.get('content')
        webdata[url] = {}
        webdata[url]['meta'] = metatags
        series_titles = tree.xpath("//div[@id='series-header']/h2[@id='series-title']/a")
        for title in series_titles:
            series_title = title.text
            webdata[url]['series_title'] = series_title
        series_urls = tree.xpath("//div[@id='series-header']/h2[@id='series-title']/a")
        for url in series_urls:
            series_url = url.get('href')
            webdata[url]['series_url'] = series_url
        for elem in tree.xpath('//div[@id="alpha"]/*'):
            if elem.get('id') == 'title':
                for val in elem.xpath('p/a'):
                    webdata[url]['fulltext_url'] = val.get('href')
                    webdata[url][elem.get('id')] = val.text
            else:
                for val in elem.xpath('p'):
                    webdata[url][elem.get('id')] = val.text
    pprint.pprint(webdata)


def main():
    URLS = grabURLs()
    scrapeURLs(URLS)

if __name__ == '__main__':
    main()
