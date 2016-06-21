# -*- coding: utf-8 -*-
'''
Reads all the CSV file inside 'data/' folder as a Pandas DataFrame
Calculates average population per city both for Urban and Rural population 
Plots it to a Line Chart for each year under output/ folder

@author: pekzeki
'''

import commons

import pygal      
import glob
import os
import collections

years_urban = {}
years_rural = {}

files = glob.glob(os.path.join('data','*.csv'))
for file in files:
    year = int(commons.get_year(file))
    tmp = commons.get_population(file)
   
    city_count = len(tmp.index) - 1

    total_urban = commons.convert_integer(tmp['Sehir_Toplam'].irow(0))
    total_rural = commons.convert_integer(tmp['Koy_Toplam'].irow(0))
    
    years_urban[year] = total_urban/city_count
    years_rural[year] = total_rural/city_count
 
#sort dictionary   
sorted_urban = collections.OrderedDict(sorted(years_urban.items()))
sorted_rural = collections.OrderedDict(sorted(years_rural.items()))

#Plotting the data
line_chart = pygal.Line(y_title='Population Count', x_title='Years')
line_chart.title = 'Average of Urban and Rural Population in a City'
line_chart.x_labels = map(str, sorted_urban.keys())
line_chart.add('Urban', sorted_urban.values())
line_chart.add('Rural', sorted_rural.values())
line_chart.render_to_file('output/average_urban_rural.svg')

