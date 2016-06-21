# -*- coding: utf-8 -*-
'''
Reads all the CSV file inside 'data/' folder as a DataFrame
Defines the color scale for each population group
Gets the blank data/turkey_map.svg file
Finds the position of each city in SVG file
Changes the color of each city w.r.t population
Create a new colored color_map for each year under output/ folder

@author: pekzeki
'''

import commons

import glob
import os
from BeautifulSoup import BeautifulSoup

files = glob.glob(os.path.join('data','*.csv'))
for file in files:

    population_df = commons.get_population(file)
    year = int(commons.get_year(file))
    
    # Read in population rates
    population = {}
    max_value = 100000000; min_value = 0
    
    row_iterator = population_df.iterrows()
    row_iterator.next()  # take first item from row_iterator
    for row in row_iterator:
        total = row[1]['Toplam']
        rate = commons.convert_integer(total)
        population[row[0]] = rate
        if rate > min_value:
            min_value = rate
        if rate < max_value:
            max_value = rate
    
    ### Red color scheme.
    colors = ["#CCCCCC", "#FFFF99", "#FFFF00", "#FFCC00", "#FF9900", "#FF6600", "#FF3300", "#FF0000", "#CC0000", "#990000", "#660000", "#330000"]
    
    # Load the SVG map
    svg = open('data/turkey_map.svg', 'r').read()
    soup = BeautifulSoup(svg)
    paths = soup.findAll('path')
    
    # Change colors accordingly
    path_style_colorful = 'opacity:1;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:1, 8;stroke-dashoffset:0;stroke-opacity:1;fill:'
    
    for p in paths:
        try:
            plate_number = p['id']
            rate = population[int(plate_number[3:])] 
    
            if rate > 4000000:
                color_class = 11
            elif rate > 2000000:
                color_class = 10
            elif rate > 1500000:
                color_class = 9
            elif rate > 1200000:
                color_class = 8
            elif rate > 1100000:
                color_class = 7
            elif rate > 1000000:
                color_class = 6
            elif rate > 700000:
                color_class = 5
            elif rate > 400000:
                color_class = 4
            elif rate > 200000:
                color_class = 3
            elif rate > 100000:
                color_class = 2
            elif rate > 80000:
                color_class = 1
            else:
                color_class = 0
        except: 
            color_class = 0
            
        color = colors[color_class]
        p['style'] = path_style_colorful + color
    
    #Write to a file
    f = open('output/color_map_'+str(year)+'.svg','w')
    f.write(soup.prettify())
    f.close() 
