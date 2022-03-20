from datetime import datetime
from time import strptime

from celery import shared_task

from api.constants.news import RSS_FEED_TYPES
from api.models.news import News
from scraper.constants.rss_feed_util import RSS_FEED_UTIL_SYMBOLS
from scraper.utils.rss_feed_util import RSSFeedUtil


def parse_date(date_string):
    date_string = date_string[5:]
    return datetime(
        day=int(date_string.split(' ')[0]),
        month=strptime(date_string.split(' ')[1], '%b').tm_mon,
        year=int(date_string.split(' ')[2]),
        hour=int(date_string.split(' ')[3].split(':')[0]),
        minute=int(date_string.split(' ')[3].split(':')[1]),
        second=int(date_string.split(' ')[3].split(':')[2])
    )

@shared_task
def initiate_fetch():
    print('Scraping...')
    for symbol in RSS_FEED_UTIL_SYMBOLS:
        fetch_news(symbol)

@shared_task
def fetch_news(symbol: str):
    for item in RSSFeedUtil.get(symbol):
        if News.objects.filter(id=item.get('guid')).exists():
            continue

        News.objects.create(
            id=item.get('guid'),
            description=item.get('description'),
            link=item.get('link'),
            title=item.get('title'),
            created_at=parse_date(item.get('pubDate')),
            symbol=RSS_FEED_TYPES[RSS_FEED_UTIL_SYMBOLS.index(symbol)][0]
        )
