#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status """

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    response = response.read()
    print('Body response:')
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
    print("\t- utf8 content: {}".format(response.decode(encoding='utf-8')))
