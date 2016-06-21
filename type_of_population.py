# -*- coding: utf-8 -*-
'''
Reads all the CSV file inside 'data/' folder as a DataFrame
Categorize the population according to Women-Urban / Men-Urban / Women-Rural / Men-Rural
Calculates the percentage of category
Plots the percentage each category with a StackedLine Chart for each year under output/ folder

@author: pekzeki
'''

from __future__ import division
import commons

import pygal      
import glob
import os
import collections

years_urban_women = {}
years_urban_men = {}
years_rural_women = {}
years_rural_men = {}

files = glob.glob(os.path.join('data','*.csv'))
for file in files:
    year = int(commons.get_year(file))
    tmp = commons.get_population(file)
   
    city_count = len(tmp.index) - 1
    total_urban_women = commons.convert_integer(tmp['Sehir_Kadin'].irow(0))
    total_urban_men = commons.convert_integer(tmp['Sehir_Erkek'].irow(0))
    total_rural_women = commons.convert_integer(tmp['Koy_Kadin'].irow(0))
    total_rural_men = commons.convert_integer(tmp['Koy_Erkek'].irow(0))

    sum_of_population = total_urban_women + total_urban_men + total_rural_women + total_rural_men
    
    years_urban_women[year] = total_urban_women*100/sum_of_population
    years_urban_men[year] = total_urban_men*100/sum_of_population
    years_rural_women[year] = total_rural_women*100/sum_of_population
    years_rural_men[year] = total_rural_men*100/sum_of_population

#sort dictionary    
sorted_urban_women = collections.OrderedDict(sorted(years_urban_women.items()))
sorted_urban_men = collections.OrderedDict(sorted(years_urban_men.items()))
sorted_rural_women = collections.OrderedDict(sorted(years_rural_women.items()))
sorted_rural_men = collections.OrderedDict(sorted(years_rural_men.items()))

#Plotting the data
stackedline_chart = pygal.StackedLine(fill=True, y_title='Population', x_title='Years')
stackedline_chart.title = 'Population Type of Turkey'
stackedline_chart.x_labels = map(str, sorted_urban_women.keys())
stackedline_chart.add('Women - Urban', sorted_urban_women.values())
stackedline_chart.add('Men - Urban', sorted_urban_men.values())
stackedline_chart.add('Women - Rural', sorted_rural_women.values())
stackedline_chart.add('Men - Rural', sorted_rural_men.values())
stackedline_chart.render_to_file('output/type_of_population.svg')
