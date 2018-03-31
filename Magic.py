#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 14:06:31 2018

@author: andrewcoogan

This is the start of a machine learning algo to reccomend cards using keywords
in each card along with using decklists from the top competitive decks to see 
if there is a smart way putting together decks and possible discovering new 
strategies.
"""

import json
import pandas
from pprint import pprint

with open('/Users/andrewcoogan/Documents/Source Control/'+
                      'MagicTutor/AllCards.json') as data_file:    
    magic_data = json.load(data_file)

type(magic_data)

test = pandas.dataframe.from_dict(magic_data)