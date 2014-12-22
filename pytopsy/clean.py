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







