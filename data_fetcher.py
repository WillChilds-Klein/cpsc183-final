#!/usr/bin/python

from pytopsy import fetch, clean
from pprint import pprint

api_key = fetch.read_key()

def run():

    mentions_data_paths = mentions()
    print 'mentions data written to: ' 
    pprint(mentions_data_paths, indent=2)


def mentions():
    keyword_lists = [
        ['patent troll', '#patenttroll'],
        ['pae', '#pae'],
        ['pme', '#pme'],
        ['npe', '#npe']
    ]
    conjunctions = ['OR','OR','OR','OR','OR']

    years = ['2010','2011','2012', '2013', '2014']

    data_paths = []
    for year in years:
        mintime = year + '-01-01'
        maxtime = year + '-12-31'
        outname = 'mentions-' + year + fetch.JSON_APPENDAGE

        queries = fetch.build_queries(api_key, keyword_lists, 
                                mintime=mintime, maxtime=maxtime, 
                                is_timestamp=False)
        responses = fetch.send_queries('metrics', 'mentions', queries)

        clean_data = clean.clean_responses(responses, convert_timestamps=True)
        data_path = clean.write_data(clean_data, out_names=[outname])
        data_paths.append(data_path)

    return data_paths


def sentiment():
    return


def geo():
    return



if __name__ == "__main__":
    run()