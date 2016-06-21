# -*- coding: utf-8 -*-
'''
Reads all the CSV file inside 'data/' folder as a Pandas DataFrame
Plot total population of each city w.r.t their plate numbers to a Line Chart for each year under output/ folder

@author: pekzeki
'''

import commons

import pygal      
import glob
import os
from operator import itemgetter

files = glob.glob(os.path.join('data','*.csv'))
for file in files:
    year = commons.get_year(file)
    tmp = commons.get_population_skipfirst(file)
    
    city_population_list = []
    
    total_population = tmp['Toplam']
    city_names = tmp['Sehir']
    sum_population = 0

    for index, row in total_population.iteritems():
        city_population = commons.convert_integer(row)
        city_name = city_names.irow(index)
        city_population_list.append((index+1, city_population))
        sum_population += city_population
    
    #sort list
    sorted_list = sorted(city_population_list, key=itemgetter(0))

    #calculate the mean
    mean = sum_population / index
    
    #Plotting the data
    xy_chart = pygal.XY(stroke=True, y_title='Population Count', x_title='Plate Number of the City')
    xy_chart.title = 'Population per City in ' + str(year)
    xy_chart.add('Cities', sorted_list)
    xy_chart.add('Average', [(0, mean), (index, mean)])
    xy_chart.render_to_file('output/population_per_city_'+year+'.svg')