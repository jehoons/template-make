#!/usr/local/bin/python
import json, os, sys

config = { 
    'global': {
        'k': 100
        }, 
        
    'test_1': {
        'P_x':0.1, 
        'P_y': 0.2,
        'P_lambda': 0.3
        }, 

    'test_2': {
        'P_x':0.4, 
        'P_y': 0.5,
        'P_lambda': 0.6
        }        
    }

if __name__ == '__main__': 
    # jsonfile = sys.argv[1]
    key = sys.argv[1]
    # _data = json.load(open(jsonfile, 'r'))

    _data = config
    _data0 = _data.copy()

    for k in key.split('/'): 
        _data0 = _data0[k]
        
    print (_data0) 

