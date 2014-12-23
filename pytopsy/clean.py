# clean.py

from pprint import pprint
import requests
from datetime import datetime
import json
import os.path
import sys
import io
import re

def clean_responses(responses, convert_timestamps=True):
    clean_data = []

    for response in responses:
        try:
            data = response['response']['results'][1]['data']
        except:
            print 'whoops! bad response in file %s !!' % filepath
            clean_data.append([])
            continue
        else:
            for data_point in data:
                # convert from UNIX time to human date
                if convert_timestamps:
                    dtime = datetime.fromtimestamp(data_point['timestamp'])
                    data_point['date'] = dtime.strftime('%Y-%m-%d')
                    del data_point['timestamp']

            clean_data.append(data)

    return clean_data

def clean_tweets(responses, include_author=False):
    clean_data = []

    for response in responses:
        tweets = response['response']['results']['list']
        for tweet in tweets:
            dtime = datetime.fromtimestamp(tweet['firstpost_date'])
            date = dtime.strftime('%Y-%m-%d')

            tweet_data = {}
            tweet_data['date'] = date
            tweet_data['text'] = tweet['tweet']['text']
            tweet_data['id'] = tweet['tweet']['id']

            if include_author:
                author = {}
                try:
                    author['name'] = tweet['author']['name']
                    author['username'] = tweet['author']['nick']
                    author['influence'] = tweet['author']['influence_level']
                    author['description'] = tweet['author']['description']
                except:
                    pass
                tweet_data['author'] = author

            clean_data.append(tweet_data)

    return clean_data

def clean_geodata(response):
    clean_data = []

    states = response['response']['results']['list']
    for state in states:
        if state['type'] == 'state': #or state['type'] == 'country':
            state_data = {}
            state_data['state'] = state['human_name']
            state_data['mentions'] = state['data'][1]['mentions']
            clean_data.append(state_data)

    return clean_data


def write_data(clean_data, out_names=['merged.json'], out_dir='data/',
               merge=True):
    # if merge=True, outfile will be named by out_names[0]
    if merge:
        merged = []
        for data in clean_data:
            merged.append(data)
        clean_data = [merged]

    out_paths = []
    for data, out_name in zip(clean_data, out_names):
            out_path = os.path.join(out_dir, out_name)

            with open(out_path, 'w') as out_file:
                json.dump(data, out_file, indent=2, separators=(',', ':'))
            print 'wrote file %s' % out_path
            out_paths.append(out_path)

    return out_paths







