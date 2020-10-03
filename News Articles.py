from newsapi import NewsApiClient
import datetime
from datetime import date
import json

newsapi = NewsApiClient(api_key='dedc8562f8444e6894993d4a522b64c1')

newssites = {

    'associated-press': {
        'bias': -1.20,
        'URL': 'https://apnews.com/'
    },
    'cnn': {
        'bias': -8.65,
        'URL': 'https://www.cnn.com/'
    },
    'the-wall-street-journal': {
        'bias': 5.30,
        'URL': 'https://www.wsj.com/'
    },
    'abc-news': {
        'bias': -3.64,
        'URL': 'https://abcnews.go.com'
    },
    'fox-news': {
        'bias': 22.23,
        'URL': 'https://abcnews.go.com'
    },

    'fortune': {
        'bias': 1.39,
        'URL': "http://fortune.com",
    }

}

# newssites.setdefault('default',dict(bias=0))

'''top_headlines = newsapi.get_top_headlines(q='trump',
                                          language='en',
                                          country='us')
print(top_headlines)'''

# /v2/everything

today = date.today()
yesterday = today - datetime.timedelta(days=1)
today = today.strftime('%Y-%m-%d')
yesterday = yesterday.strftime('%Y-%m-%d')


def getSources():
    sources = list(newssites.keys())
    sourcesStr = ''
    for source in sources:
        print('loop')
        sourcesStr += source + ','
    sourcesStr = sourcesStr[:-1]
    print(sourcesStr)
    return sourcesStr


def getSourcesURL():
    sources = list(newssites.keys())
    sourcesStr = ''
    for source in sources:
        print('loop')
        sourcesStr += source + ','
    sourcesStr = sourcesStr[:-1]
    print(sourcesStr)
    return sourcesStr


def getPoliticsStories():

    all_articles = newsapi.get_everything(q='politics',
                                          sources=getSources(),
                                          from_param=yesterday,
                                          to=today,
                                          language='en',
                                          sort_by='relevancy',
                                          page=1)
    # print(all_articles)
    sources = newsapi.get_sources()
    print('test', len(all_articles))
    for news in all_articles['articles']:
        print(news['title'], newssites[news['source']['id']]['bias'])
    return all_articles['articles']


def saveToJSON(articles):
    data = {}
    data['articles'] = []
    for article in articles:
        data['articles'].append({
            'Title': article['title'],
            'Source': article['source'],
            'Bias': newssites[article['source']['id']]['bias'],
            'Author': article['author'],
            'Description': article['description'],
            'URL': article['url'],
            'LinkToImage': article['urlToImage'],
            'Date': article['publishedAt'],
            'Content': article['content']
        })
    return data


with open('data.json', 'w') as outfile:
    json.dump(saveToJSON(getPoliticsStories()), outfile)
