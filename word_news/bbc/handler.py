import requests
import xmltodict

HEADER = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept': 'application/xhtml+xml,application/xml --compressed',
}

BBC_URL = 'https://feeds.bbci.co.uk/news/world/rss.xml'


def get_news(event, context):
    response = requests.get(BBC_URL, HEADER)
    dict_response = dict(xmltodict.parse(response.content))

    data = {
        'news': []
    }

    for post in dict_response.get('rss').get('channel').get('item'):
        data['news'].append(
            {
                'title': post.get('title'),
                'published': post.get('pubDate')
            })

    return data
