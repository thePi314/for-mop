import requests
from xml.etree.ElementTree import fromstring

from scraper.constants.rss_feed_util import RSS_FEED_UTIL_AGENT


class RSSFeedUtil:
    @staticmethod
    def get(symbol):
        return RSSFeedUtil.parse(RSSFeedUtil.fetch(symbol))

    @staticmethod
    def fetch(symbol):
        url = 'https://feeds.finance.yahoo.com/rss/2.0/headline?region=US&lang=en-US'
        resp = requests.get(f'{url}&s={symbol}', headers={
            'User-Agent': RSS_FEED_UTIL_AGENT
        })
        return fromstring(resp.content)

    @staticmethod
    def parse(xml):
        data = []

        for elem in xml.iter('item'):
            item = {}
            for child in elem:
                item[child.tag] = child.text
            data.append(item)

        return data
