""" Copyright (c) 2022 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied. 
"""

import requests
from requests.auth import HTTPBasicAuth

'''
Class for Umbrella API. Takes API key and secret. Offers methods to return list of IPsec-enabled data centers.
'''
class UmbrellaAPI:
    def __init__(self, key, secret):
        
        self.key = key
        self.secret = secret

    '''
    Method that requests and returns Umbrella API token.
    '''
    def get_authorization_token(self):

        print('Requesting Umbrella token ...')

        url = "https://api.umbrella.com/auth/v2/token"
        token = requests.post(url, auth=HTTPBasicAuth(self.key, self.secret)).json()

        return token


    '''
    Method that requests and returns a list of the IPsec-enabled Umbrella data centers.
    The data center information includes the IP address and location details.
    '''
    def list_data_centers(self):

        token = self.get_authorization_token()

        print('Requesting Umbrella IPsec-enabled data centers ...')

        api_headers = {'Authorization': "Bearer " + token['access_token']}
        req = requests.get('https://api.umbrella.com/deployments/v2/datacenters', headers=api_headers).json()
          
        return req



