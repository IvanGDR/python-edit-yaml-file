#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 17:01:05 2022

@author: ivan.garciadelrisco
"""

import os
import sys
import yaml


fn = sys.argv[1]
if os.path.exists(fn) and fn.endswith('.yaml'):
    filename = (fn.split("/")[-1])
    filename_lenght = len(filename)
    path = (fn[:-filename_lenght])
    print('#'*80)
    print("Your filepath is: ", path)
    print("Your filename is: ", filename)
else:
    print("Not a valid path or filename.")
    exit()

print('#'*80)
print("Type the values for the following keys.")
print("If not values to be changed, leave blank and press enter.")
print('#'*80)

# Edit this list, adding as many values as you would like to change
List = ["fullnameOverride"]
Dict = {}

for e in range(0,len(List)):
    val = input(List[e]+': ')
    if val == '':
        continue
    else:
        Dict[List[e]] = val

if len(Dict) == 0:
    print("Nothing to change, not new Yaml file has been generated.")
else:
    # Opening Original YAML file
    with open(fn, 'r') as file:
        file_yaml = yaml.safe_load(file)
    
    # Iteration can be modified to meet nested key/values
    for key in Dict:
        file_yaml[key] = Dict[key]
    
    # Saving new YAML file
    with open(path + 'copy.yaml', 'w') as file:
        yaml.dump(file_yaml, file, default_flow_style=False, sort_keys=False)
