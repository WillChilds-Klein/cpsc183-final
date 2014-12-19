#!/usr/bin/python

from pprint import pprint
import requests
from datetime import datetime
import json
import os.path
import sys
import io
import re

BASE_TOPSY_URL = 'http://api.topsy.com/v2/'

with open ("topsy.key", "r") as key:
    API_KEY = key.read().rstrip()
print 'API_KEY: %s' % API_KEY

MENTIONS = 'metrics/mentions.json'
SENTIMENT = 'metrics/sentiment.json'

BASE_MINTIME = 1167609600 # 1/1/07
BASE_MAXTIME = 1418905900 # 12/18/14

ROOT_DIR = 'cpsc183-final'
DATA_DIR = 'data'
SCRIPTS_DIR = 'scripts'

JSON_APPENDAGE = '.json'
CLEAN_JSON_APPENDAGE = '-CLEAN' + JSON_APPENDAGE

def run():
    print 'data_fetcher.py running!!'
    keyword_lists = [
        ['patent troll', '#patenttroll'],
        ['pae', '#pae'],
        ['pme', '#pme'],
        ['npe', '#npe']
    ]
    print 'keyword_lists:'
    pprint(keyword_lists, indent=2)

    base_url = BASE_TOPSY_URL + MENTIONS
    queries = build_mentions_queries(keyword_lists)

    responses = make_requests(base_url, queries)
    if responses == None or len(responses) == 0:
        print 'requests came up empty! exiting...'
        sys.exit(1)

    data_path = DATA_DIR
    parent_dir = os.path.basename(os.path.dirname(os.getcwd()))
    if parent_dir == ROOT_DIR:
        data_path = os.path.join('..', DATA_DIR)

    mentions_filenames = write_raw_files(responses, path=data_path)

    clean_mentions_data(mentions_filenames, path=data_path)


# keywords are disjoint --> OR
def build_mentions_queries(keyword_lists, slice=86400, cumulative=0, 
                         mintime=BASE_MINTIME, maxtime=BASE_MAXTIME):
    queries = []

    for keyword_list in keyword_lists:
        query_str = ''
        for keyword in keyword_list:
            query_str += (keyword + ' OR ')

        if query_str.endswith(' OR '):
            query_str = query_str[:-4]
    
        query = {}
        query['apikey'] = API_KEY
        query['q'] = query_str
        query['slice'] = slice
        query['cumulative'] = cumulative
        query['mintime'] = mintime
        query['maxtime'] = maxtime

        queries.append(query)

    return queries

def clean_mentions_data(filenames, path='./'):
    clean_filenames = []

    for filename in filenames:
        filepath = os.path.join(path, filename)
        try:
            with open(filepath, "r") as file:
                file_json = json.load(file)
        except:
            print 'whoops! couldn\'t read %s !!' % filepath
            continue
    
        try:
            clean_data = file_json['response']['results'][1]['data']
        except:
            print 'whoops! bad response in file %s !!' % filepath
            continue
        
        # convert from UNIX time to human date
        for data_point in clean_data:
            dtime = datetime.fromtimestamp(data_point['timestamp'])
            data_point['date'] = dtime.strftime('%Y-%m-%d')
            del data_point['timestamp']
        # print 'CLEAN SHIT: '
        # pprint(clean_data, indent=2)
        # print '-' * 40 + '\n\n'

        clean_filepath = filepath.rstrip(JSON_APPENDAGE) + CLEAN_JSON_APPENDAGE

        with open(clean_filepath, 'w') as outfile:
            json.dump(clean_data, outfile, indent=2, separators=(',', ':'))

        print 'wrote clean file %s' % clean_filepath
        clean_filenames.append(os.path.basename(clean_filepath))

    if len(clean_filenames) > 0:
        print 'data cleaned and written!'
    return clean_filenames


def make_requests(base_url, queries):
    responses = []

    for query in queries:
        r = requests.get(base_url, params=query)
        print '-' * 35 + '\n'
        print 'REQUEST: %s' % r.url
        print 'STATUS: %s' % r.status_code
        print 'RESPONSE HEADERS: %s' % r.headers['content-type']
        responses.append(r.json())
    print '-' * 35 + '\n\n'

    return responses

def write_raw_files(responses, path=('./')):
    if path == None or path == '':
        return

    filenames = []
    for response in responses:
        query_str = ''
        try:
            q  = response['request']['parameters']['q']
        except NameError:
            print 'whoops! bad response: %s' % pformat(response, indent=2)
        else:
            for query in q:
                query_str += query

            filename = re.sub('[^#^a-z^A-Z^0-9]', '', query_str) 
            filename = re.sub('OR', '-OR-', filename) + JSON_APPENDAGE
            filepath = os.path.join(path, filename)

            with open(filepath, 'w') as outfile:
                json.dump(response, outfile, indent=2, separators=(',', ':'))
            print 'wrote file %s' % filepath
            filenames.append(filename)

    print 'all files written!'
    return filenames

if __name__ == "__main__":
    run()