#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 15:43:14 2020

@author: simonsmith
"""

#%% 

import speedtest 
import json

#%% https://github.com/sivel/speedtest-cli/wiki

def run_speed_test(): 
    
    servers = []
    # If you want to test against a specific server
    # servers = [1234]
    
    threads = None
    # If you want to use a single threaded test
    # threads = 1
    
    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download(threads=threads)
    s.upload(threads=threads)
    s.results.share()

    return s.results.dict()

#%% 
    
results = run_speed_test()
data = json.dumps(results)

with open('Users/simonsmith/Desktop/speed_test.csv', 'a') as file:
    
    file.write(data + "\n")