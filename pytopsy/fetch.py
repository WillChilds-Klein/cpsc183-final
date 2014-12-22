# fetch.py

import pprint 
import requests
from datetime import datetime
import calendar
import json
import os.path
import posixpath
import sys
import io
import re


JSON_APPENDAGE = '.json'

BASE_TOPSY_URL = 'http://api.topsy.com/v2/'

MENTIONS = 'metrics/mentions.json'
SENTIMENT = 'metrics/sentiment.json'

VALID_CONJUNTIONS = ['AND','OR','NOT']
VALID_API_TYPES = ['contents','metrics','insights']

# BASE_MINTIME = 1167609600 # 1/1/07
DEFAULT_MINTIME = 1293840001 # 1/1/11
DEFAULT_MAXTIME = 1418905900 # 12/18/14

def read_key(key_dir='.', key_name='topsy.key'):
    key_path = os.path.join(key_dir, key_name)

    try:
        with open (key_path, "r") as key_file:
            api_key = key_file.read().rstrip()
    except:
        api_key = ''
        print 'couldn\'t read API key at %s' % key_path

    return api_key


def build_queries(api_key, keyword_lists, conjunctions=[], slice=86400, 
                  cumulative=0, mintime=DEFAULT_MINTIME, maxtime=DEFAULT_MAXTIME, 
                  is_timestamp=True, date_format='%Y-%m-%d'):
    if not len(api_key) == 32:
        print 'please specify valid api_key!!'
        return []

    if not is_timestamp:
        # convert to UNIX timestamp if needed
        d_mintime = datetime.strptime(mintime, date_format)
        d_maxtime = datetime.strptime(maxtime, date_format)

        mintime = calendar.timegm(d_mintime.utctimetuple())
        maxtime = calendar.timegm(d_maxtime.utctimetuple())

    for conj in conjunctions:
        if conj not in VALID_CONJUNTIONS:
            print 'invalid conjunction: %s, replacing with: \'\'' % conj
            conj = ''
    for i in range(len(keyword_lists) - len(conjunctions)):
        conjunctions.append('OR')

    queries = []

    for keyword_list, conjunction in zip(keyword_lists, conjunctions):       
        query_str = '' 
        conjunction_str = ' ' + conjunction + ' '

        for keyword in keyword_list:
            query_str += keyword + conjunction_str
        if query_str.endswith(conjunction_str):
            query_str = query_str[:-1*len(conjunction_str)] 

        query = {}
        query['apikey'] = api_key
        query['q'] = query_str
        query['slice'] = slice
        query['cumulative'] = cumulative
        query['mintime'] = mintime
        query['maxtime'] = maxtime

        queries.append(query)

    return queries
    


def send_queries(api_type, api_name, queries, response_format=JSON_APPENDAGE):
    if api_type.strip('/') not in VALID_API_TYPES:
        print ('please specify valid api_type in: %s' % 
                pprint.pformat(VALID_API_TYPES))
        return []
    # TODO: check for valid api_name...long list...
    # TODO: check for valid resposnse format.
    response_format = response_format.lstrip('.')

    url = str(posixpath.join(posixpath.join(BASE_TOPSY_URL, api_type),
                             api_name))
    url += ('.' + response_format)

    query_sep = '-' * 35 + '\n\n'
    responses = []

    for query in queries:
        r = requests.get(url, params=query)

        print query_sep
        print 'REQUEST: %s' % r.url
        print 'STATUS: %s' % r.status_code
        print 'RESPONSE HEADERS: %s' % r.headers['content-type']

        responses.append(r.json())

    print query_sep + '\n'

    return responses


def write_responses(responses, out_names=[], out_dir='data/responses'):

    if len(out_names) < len(responses):
        for i in range(len(out_names), len(responses)):
            response = responses[i]
            try:
                q  = response['request']['parameters']['q']
            except NameError:
                print ('whoops! bad response: %s' % 
                        pformat(response['request']['parameters'], indent=2))
            else:
                query_str = ''
                for query in q:
                    query_str += query
                query_str = query_str.strip()

                out_name = re.sub('[\W]+', '_', query_str) + JSON_APPENDAGE
                out_names.append(out_name)


    out_paths = []
    for response, out_name in zip(responses, out_names):
            out_path = os.path.join(out_dir, out_name)

            with open(out_path, 'w') as out_file:
                json.dump(response, out_file, indent=2, separators=(',', ':'))
            print 'wrote file %s' % out_path
            out_paths.append(out_path)

    print 'all files written!'
    return out_paths
