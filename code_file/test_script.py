#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 14:13:18 2023

@author: hyunseo
"""
import subprocess

#dist_list = ["1", "5", "10", "15", "20", "25", "30", "35"]

dist_list = ["10", "30", "50", "100"]
for i in range(len(dist_list)):
    #1m test execute
    print(dist_list[i] + "m test execute by pressing enter.")
    input()
    
    subprocess.call(['iperf3','-c','192.168.3.1','--bidir', '-t', '30'])
    
    print(dist_list[i] + "m test executed")   
    input()
print("all the test process are done.")
