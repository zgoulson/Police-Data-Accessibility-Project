import os
import sys
import requests
import pandas as pd
import datetime
import time

from utils import get_api_key

token = get_api_key()
url = 'https://www.muckrock.com/api_v1/'

headers = {'Authorization': 'Token %s' % token, 'content-type': 'application/json'}
page_size = 200
next_ = url + 'jurisdiction' + '/?page_size=%d' % (page_size)

SUPRESS_ERRORS = False
page = 1
d=[]

while next_ is not None:
    r = requests.get(next_, headers=headers)
    try:
        json = r.json()
        next_ = json['next']
        d.append(r.json())
        print('Page %d of %d' % (page, json['count'] / page_size + 1))
        page += 1
    except Exception as e:
        print('Error ', e)
        if not SUPRESS_ERRORS:
            raise
df = pd.json_normalize(data=d,max_level=0,record_path='results')

df.to_csv('muckrock_jurisdictions.csv', index=False)
