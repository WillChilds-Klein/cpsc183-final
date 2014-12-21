# topsy.py

from pprint import pprint
import requests
from datetime import datetime
import json
import os.path
import sys
import io
import re



ROOT_DIR_NAME = 'cpsc183-final'
DATA_DIR_NAME = 'data'
SCRIPTS_DIR_NAME = 'scripts'

JSON_APPENDAGE = '.json'
CLEAN_JSON_APPENDAGE = '-CLEAN' + JSON_APPENDAGE

# class fetch:

BASE_TOPSY_URL = 'http://api.topsy.com/v2/'

MENTIONS = 'metrics/mentions.json'
SENTIMENT = 'metrics/sentiment.json'

BASE_MINTIME = 1167609600 # 1/1/07
# BASE_MINTIME = 1293840001 # 1/1/11
BASE_MAXTIME = 1418905900 # 12/18/14

def read_key(dir='./'):
    key_path = os.path.join(dir,"topsy.key")

    with open (key_path, "r") as key:
        API_KEY = key.read().rstrip()

    return API_KEY

def build_query():
    print 'blah'


def send_query():
    print 'blah'



# class clean():

def write():
    print 'blah'