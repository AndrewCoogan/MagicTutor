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
import math
import pandas as pd
import numpy as np

with open('/Users/andrewcoogan/Documents/Source Control/'+
                      'MagicTutor/AllCards.json') as data_file:    
    magic_data_json = json.load(data_file)

### Remove Gleemax as it has a CMC of 100k and will blow out the scaling later
del magic_data_json["Gleemax"]
#  We should remove all "schemes" and all other non legal cards (best efforts)
#  Remove all "types" that are ""

md_df = pd.DataFrame.from_dict(magic_data_json).transpose()
md_df.replace(math.nan, 0)

tt = md_df.types.str.match('*token card*')


md_df['types2'] = [item for sublist in md_df.types for item in sublist]

# For this I want to take all of the 'types' and give them their own row
#  The elements of that row will be 1 or 0 if each card possesses that type

flat_list = list()

temp = md_df.head(20)

#flat_list = [item for sublist in temp.types for item in sublist]

for sublist in temp.types:
    print(sublist)
    for item in sublist:
        flat_list.append(item)