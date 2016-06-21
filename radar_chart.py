# -*- coding: utf-8 -*-
'''
Reads all the CSV file inside 'data/' folder as a DataFrame
Categorize the population according to Women-Urban / Men-Urban / Women-Rural / Men-Rural
Plots the size of each group in a Radar Chart for each year under output/ folder

@author: pekzeki
'''

from __future__ import division
import commons

import pygal      
import glob
import os
import collections

years = {}

files = glob.glob(os.path.join('data','*.csv'))
for file in files:
    year = int(commons.get_year(file))
    tmp = commons.get_population(file)
   
    city_count = len(tmp.index) - 1
    total_urban_women = commons.convert_integer(tmp['Sehir_Kadin'].irow(0))
    total_urban_men = commons.convert_integer(tmp['Sehir_Erkek'].irow(0))
    total_rural_women = commons.convert_integer(tmp['Koy_Kadin'].irow(0))
    total_rural_men = commons.convert_integer(tmp['Koy_Erkek'].irow(0))
    
    years[year] = [total_urban_women, total_urban_men, total_rural_women, total_rural_men]
    
#sort dictionary 
sorted_years = collections.OrderedDict(sorted(years.items()))  

#Plotting the data
from pygal.style import NeonStyle
radar_chart = pygal.Radar(fill=True, style=NeonStyle)
radar_chart.title = 'Population Type of Turkey (Radar Chart)'
radar_chart.x_labels = ['Women - Urban','Men - Urban','Women - Rural','Men - Rural']
for i in sorted_years.keys():
    radar_chart.add(str(i), sorted_years.get(i))
radar_chart.render_to_file('output/type_of_population_radar.svg')
