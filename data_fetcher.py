#!/usr/bin/python

from pytopsy import fetch, clean
from pprint import pprint
import json

api_key = fetch.read_key()

SPIKE_DATES_PATH = 'data/spike_dates.json'

def run():

    # mentions_data_paths = mentions()
    # print 'mentions data written to: ' 
    # pprint(mentions_data_paths, indent=2)

    # tweets()

    # sentiment()

    geo()


def mentions():
    
    years = ['2010','2011','2012', '2013', '2014']
    
    keyword_lists1 = [
        ['patent troll', '#patenttroll'],
        ['"patent assertion entity"', '#pae'],
        ['"patent monitization entity"', '#pme'],
        ['"nonpracticing entity', 'non-practicing entity', '#npe'],
    ]
    conjunctions1 = ['OR','OR','OR','OR']

    data_paths = []
    for year in years:
        mintime = year + '-01-01'
        maxtime = year + '-12-31'
        outname = 'mentions1-' + year + fetch.JSON_APPENDAGE

        queries = fetch.build_queries(api_key, keyword_lists1, 
                                conjunctions=conjunctions1,
                                mintime=mintime, maxtime=maxtime, 
                                is_timestamp=False)
        responses = fetch.send_queries('metrics', 'mentions', queries)

        clean_data = clean.clean_responses(responses, convert_timestamps=True)
        data_path = clean.write_data(clean_data, out_names=[outname])
        data_paths.append(data_path)


    # keyword_lists2 = [
    #     ['patent', 'infringe'],
    #     ['patent', 'troll']
    # ]
    # conjunctions2 = ['AND','AND']

    # for year in years:
    #     mintime = year + '-01-01'
    #     maxtime = year + '-12-31'
    #     outname = 'mentions2-' + year + fetch.JSON_APPENDAGE

    #     queries = fetch.build_queries(api_key, keyword_lists2, 
    #                             conjunctions=conjunctions2,
    #                             mintime=mintime, maxtime=maxtime, 
    #                             is_timestamp=False)
    #     responses = fetch.send_queries('metrics', 'mentions', queries)

    #     clean_data = clean.clean_responses(responses, convert_timestamps=True)
    #     data_path = clean.write_data(clean_data, out_names=[outname])
    #     data_paths.append(data_path)

    return data_paths


def tweets():
    dates = []
    with open(SPIKE_DATES_PATH, 'r') as file:
        dates = json.load(file)

    keywords = [
        '"patent monitization entity"',
        '"patent troll"',
        '#patenttroll'
    ]

    queries = fetch.query_tweets_by_date(api_key, keywords, dates)

    responses = fetch.send_queries('content', 'tweets', queries)

    out_path = 'data/responses/spike_tweets.json'
    with open(out_path, 'w') as out_file:
        json.dump(responses, out_file, indent=2, separators=(',', ':'))
        print 'wrote tweets to %s' % out_path

    clean_data = clean.clean_tweets(responses)

    out_path = 'data/responses/spike_tweets-CLEAN.json'
    with open(out_path, 'w') as out_file:
        json.dump(clean_data, out_file, indent=2, separators=(',', ':'))
        print 'wrote tweets to %s' % out_path

    tweets_authors = clean.clean_tweets(responses, include_author=True)

    out_path = 'data/responses/spike_tweets_authors-CLEAN.json'
    with open(out_path, 'w') as out_file:
        json.dump(tweets_authors, out_file, indent=2, separators=(',', ':'))
        print 'wrote tweets to %s' % out_path


def sentiment():
    years = ['2010','2011','2012', '2013', '2014']
    
    keyword_lists = [
        ['patent troll', '#patenttroll'],
        ['"patent assertion entity"', '#pae'],
        ['"patent monitization entity"', '#pme'],
        ['"nonpracticing entity', 'non-practicing entity', '#npe'],
    ]
    conjunctions = ['OR','OR','OR','OR']

    data_paths = []
    for year in years:
        mintime = year + '-01-01'
        maxtime = year + '-12-31'
        outname = 'sentiment-' + year + fetch.JSON_APPENDAGE

        queries = fetch.build_queries(api_key, keyword_lists, 
                                conjunctions=conjunctions,
                                mintime=mintime, maxtime=maxtime, 
                                is_timestamp=False)
        responses = fetch.send_queries('metrics', 'sentiment', queries)

        clean_data = clean.clean_responses(responses, convert_timestamps=True)
        data_path = clean.write_data(clean_data, out_names=[outname])
        data_paths.append(data_path)


def geo():
    keyword_lists = [
        ['patent troll', '#patenttroll', '"patent monitization entity"']
    ]
    conjunctions = ['OR']

    mintime = '2010-01-01'
    maxtime = '2014-12-22'
    outname = 'mentions-by-state.json'
    params = {'scope': 225, 'types': 'state'}

    queries = fetch.build_queries(api_key, keyword_lists, 
                            conjunctions=conjunctions,
                            mintime=mintime, maxtime=maxtime, 
                            is_timestamp=False, other_params=params)
    responses = fetch.send_queries('metrics', 'geo', queries)

    clean_data = clean.clean_geodata(responses[0])
    data_path = clean.write_data(clean_data, out_names=[outname])

    return data_path


if __name__ == "__main__":
    run()