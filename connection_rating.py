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

import umbrella_API
from operator import itemgetter
from dotenv import load_dotenv
from ping3 import ping

from rich.console import Console
from rich.table import Table

import os

load_dotenv()

'''
Returns the mean latency to a specific IPsec-enabled data center based on ping.
Thereby, the count, timeout and TTL value are configureable. 
'''
def mean_latency_ping_test(host):
    
    latency_list = []
    COUNT = int(os.environ.get('COUNT', default=4))
    TIMEOUT = int(os.environ.get('TIMEOUT', default=4))
    TTL = int(os.environ.get('TTL', default=64))

    for _ in range(COUNT):
        result = ping(host, timeout=TIMEOUT, ttl=TTL) #returns Float for latency, False if unknown host, None for timeout
        latency_list.append(result)

    numberic_latency_list = list(filter(None, latency_list)) # Filters out None and False values

    if numberic_latency_list == []:
        return 100000000   #Returns high latency value in case of unknown or timeout hosts
    else:
        rounded_mean_latency = round(sum(numberic_latency_list)/COUNT,3)
        return rounded_mean_latency



'''
Triggers the latency test for all data center dictionaries in the provided 
list and created a new list with all gatherings.
'''
def get_dc_latency_results(dc_list):

    print('Testing latency per IPsec-enabled data center. This might take some time ...')

    dc_latency_list = []

    for continent in dc_list['continents']:
        for dc in continent['cities']:
            
            dc_ip = dc['range'].removesuffix("/32")
            
            ping_latency = mean_latency_ping_test(dc_ip)

            dc_result = dc.copy()
            dc_result['ip'] = dc_ip
            dc_result['latency'] = ping_latency
            dc_result['continent'] = continent['name']
            
            dc_latency_list.append(dc_result)

    return dc_latency_list


'''
Creates a table to output the gathered content. 
'''
def create_cli_table(dc_list_w_latency):

    print('Creating formatted CLI output ...')

    table = Table(title="Umbrella IPsec-enabled data centers sorted by mean latency")
    
    table.add_column("LATENCY (s)", justify="left", style="cyan", no_wrap=True)
    table.add_column("CITY/CONTINENT", justify="left", style="gold1", no_wrap=True)
    table.add_column("Data Center", justify="left",style="gold1", no_wrap=True)
    table.add_column("IP", justify="left", style="gold1", no_wrap=True)
    table.add_column("LAT/LONG", justify="left", style="gold1", no_wrap=True)

    for dc in dc_list_w_latency:
        table.add_row(str(dc['latency']), str(dc['name'])+'/'+str(dc['continent']), str(dc['dc']), str(dc['ip']), str(dc['latitude'])+'/'+str(dc['longitude']))

    console = Console()
    console.print(table)


if __name__ == "__main__":

    API_KEY = os.environ.get('API_KEY')
    API_SECRET = os.environ.get('API_SECRET')
    api = umbrella_API.UmbrellaAPI(API_KEY, API_SECRET)
    
    dc_list = api.list_data_centers()

    dc_list_w_latency = get_dc_latency_results(dc_list)

    dc_list_latency_sorted = sorted(dc_list_w_latency, key=itemgetter('latency'), reverse=False) #Sorts the list based on the latency value
    
    create_cli_table(dc_list_latency_sorted)
