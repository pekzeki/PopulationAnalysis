# -*- coding: utf-8 -*-
'''
Reads all the CSV file inside 'data/' folder as a Pandas DataFrame
Plots the population of Turkey with a Box Plot Chart for each year under output/ folder

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
    tmp = commons.get_population_skipfirst(file)

    city_population_list = []
    
    total_population = tmp['Toplam']
    for index, row in total_population.iteritems():
        city_population = commons.convert_integer(row)
        city_population_list.append(city_population)
    
    years[year] = city_population_list

#sort dictionary    
sorted_years = collections.OrderedDict(sorted(years.items()))  

#Plotting the data
box_plot = pygal.Box(y_title='Population Count', x_title='Years')
box_plot.title = 'Box Plot of Population by Years'
for year in sorted_years.keys():
    box_plot.add(str(year), sorted_years.get(year))
box_plot.render_to_file('output/box_plot.svg')
