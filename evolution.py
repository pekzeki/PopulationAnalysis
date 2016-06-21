# -*- coding: utf-8 -*-
'''
Gets the given sys.argv[1] as a city_name
Reads all the CSV file inside 'data/' folder as a DataFrame
Calculates total population of each city
Plots it to a Histogram Chart for each year under output/ folder

@author: Salih Zeki Irkdas, Refik Anil Bayraktar, Metin Gemici
'''

import commons

import pygal      
import glob
import os
import sys

if len(sys.argv) > 1:

    city_name = sys.argv[1].decode('utf-8')
    population = []
    years = []
    
    files = glob.glob(os.path.join('data','*.csv'))
    for file in files:
        year = int(commons.get_year(file))
        tmp = commons.get_population(file)

        row = tmp.loc[tmp['Sehir'] == sys.argv[1]]
        
        population.append(commons.convert_integer(row['Toplam'].irow(0)))
        years.append(year)

    #sort list           
    sorted_population = sorted(population)
    sorted_years = sorted(years)
        
    #Plotting the data                                                                       
    bar_chart = pygal.Bar(y_title='Population', x_title='Years')                
    bar_chart.title = 'Population/Years for ' + city_name       
    bar_chart.add(city_name, sorted_population)
    bar_chart.x_labels = map(str, sorted_years)
    bar_chart.render_to_file('output/evolution_'+city_name+'.svg')   

else:
    print "Missing Argument: City_Name"