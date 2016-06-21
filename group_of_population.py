# -*- coding: utf-8 -*-
'''
Reads all the CSV file inside 'data/' folder as a DataFrame
Divides the population size into several groups 
Calculates total population of each city
Categorize the cities w.r.t defined groups
Plots the size of each group in a Scatter Chart for each year under output/ folder

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
   
    p_1000k = 0
    p_600k = 0
    p_300k = 0
    p_50k = 0
    
    total_population = tmp['Toplam']
    for index, row in total_population.iteritems():
        city_population = commons.convert_integer(row)
        
        if city_population > 1000000:
            p_1000k += 1
        elif city_population > 600000:
            p_600k += 1
        elif city_population > 300000:
            p_300k += 1
        else:
            p_50k += 1
            
    
    city_population_list = [p_50k, p_300k, p_600k, p_1000k] 
    years[year] = city_population_list
    

#sort dictionary 
sorted_years = collections.OrderedDict(sorted(years.items()))  
items = sorted_years.items()
items.reverse()
reverse_years = collections.OrderedDict(items) 

#Plotting the data
dot_chart = pygal.Dot(x_label_rotation=30, y_title='Years', x_title='Population')
dot_chart.title = 'Population Groups in Each Year'
dot_chart.x_labels = ['0-300000', '300000-600000', '600000-1000000', '>1000000']
for year in reverse_years.keys():
    dot_chart.add(str(year), reverse_years.get(year))
dot_chart.render_to_file('output/group_of_population.svg')
