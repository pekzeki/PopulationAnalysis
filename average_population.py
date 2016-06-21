# -*- coding: utf-8 -*-
'''
Reads all the CSV file inside 'data/' folder as a Pandas DataFrame
Calculates average population per city 
Plots it to a Line Chart for each year under output/ folder

@author: pekzeki
'''

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
    total_population = commons.convert_integer(tmp['Toplam'].irow(0))
    
    years[year] = total_population/city_count
 
#sort dictionary   
sorted_years = collections.OrderedDict(sorted(years.items()))

#Plotting the data
line_chart = pygal.Line(y_title='Population Count', x_title='Years')
line_chart.title = 'Rise of the Average Population by City'
line_chart.x_labels = map(str, sorted_years.keys())
line_chart.add('Average Population by City', sorted_years.values())
line_chart.render_to_file('output/rise_of_average_population_by_city.svg')

