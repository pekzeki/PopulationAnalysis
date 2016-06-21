# -*- coding: utf-8 -*-
'''
Gets the given sys.argv[1] as a city_name
Reads all the CSV file inside 'data/' folder as a DataFrame
Calculates total population of each city both for Urban and Rural
Plots it to a Histogram Chart for each year under output/ folder

@author: pekzeki
'''

import commons

import pygal      
import glob
import os
import sys

if len(sys.argv) > 1:

    city_name = sys.argv[1].decode('utf-8')
    population_urban = []
    population_rural = []
    years = []
    
    files = glob.glob(os.path.join('data','*.csv'))
    for file in files:
        year = int(commons.get_year(file))
        tmp = commons.get_population(file)

        row = tmp.loc[tmp['Sehir'] == sys.argv[1]]
        
        population_urban.append(commons.convert_integer(row['Sehir_Toplam'].irow(0)))
        population_rural.append(commons.convert_integer(row['Koy_Toplam'].irow(0)))
        years.append(year)
               
    #sort list       
    sorted_population_urban = sorted(population_urban)
    sorted_population_rural = sorted(population_rural)
    sorted_years = sorted(years)
                  
    #Plotting the data                                                             
    bar_chart = pygal.Bar(y_title='Population', x_title='Years')                
    bar_chart.title = 'Population/Years for ' + city_name + ' (Urban and Rural)'       
    bar_chart.add('Rural', sorted_population_rural)
    bar_chart.add('Urban', sorted_population_urban)
    bar_chart.x_labels = map(str, sorted_years)
    bar_chart.render_to_file('output/evolution_urban_rural_'+city_name+'.svg')   

else:
    print "Missing Argument: City_Name"