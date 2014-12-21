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
# BASE_MINTIME = 1293840001 # 1/1/11
BASE_MAXTIME = 1418905900 # 12/18/14

ROOT_DIR_NAME = 'cpsc183-final'
DATA_DIR_NAME = 'data'
SCRIPTS_DIR_NAME = 'scripts'

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

    data_path = DATA_DIR_NAME
    parent_dir = os.path.basename(os.path.dirname(os.getcwd()))
    if parent_dir == ROOT_DIR_NAME:
        data_path = os.path.join('..', DATA_DIR_NAME)

    mentions_filenames = write_raw_files(responses, path=data_path)

    clean_filenames = clean_mentions_data(mentions_filenames, path=data_path)

    merged_filename = merge_files(clean_filenames, path=data_path, 
                                  outfilename='mentions_data.json')


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

        clean_filepath = filepath.rstrip(JSON_APPENDAGE) + CLEAN_JSON_APPENDAGE

        with open(clean_filepath, 'w') as outfile:
            json.dump(clean_data, outfile, indent=2, separators=(',', ':'))
            print 'wrote clean file %s' % clean_filepath
        clean_filenames.append(os.path.basename(clean_filepath))

    if len(clean_filenames) > 0:
        print 'data cleaned and written!'
    return clean_filenames

def merge_files(filenames, path='./', outfilename='merged.json'):
    merged = []
    for filename in filenames:
        filepath = os.path.join(path, filename)
        try:
            with open(filepath, "r") as file:
                file_json = json.load(file)
        except:
            print 'whoops! couldn\'t read %s !!' % filepath
            continue

        merged.append(file_json)

    outfilename = os.path.join(path, outfilename)
    with open(outfilename, 'w') as outfile:
        json.dump(merged, outfile, indent=2, separators=(',', ':'))
        print 'files successfully merged into %s' % outfilename


if __name__ == "__main__":
    run()