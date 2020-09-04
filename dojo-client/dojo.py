#!/usr/bin/env python3

import requests
import configargparse

p = configargparse.ArgParser(default_config_files=['~/.dojo_settings'])
p.add('-t', '--token', required=True, env_var='TOKEN', help='token for accessing the api')

options = p.parse_args()

# Read the APIv2 docs!

# Some endpoints:
# api/v2/products
# api/v2/findings

url = 'http://127.0.0.1:8080/api/v2/products'
headers = {'content-type': 'application/json',
           'Authorization': f'Token {options.token}'}

r = requests.get(url, headers=headers, verify=True)  # set verify to False if ssl cert is self-signed

r.raise_for_status()

print(r.text)