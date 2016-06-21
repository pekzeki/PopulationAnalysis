# -*- coding: utf-8 -*-
'''
Reads all the CSV file inside 'data/' folder as a DataFrame
Defines the domination of Men or Women for each city 
Gets the blank data/turkey_map.svg file
Finds the position of each city in SVG file
Changes the color of each city w.r.t domination
Create a new colored domination_map for each year under output/ folder

@author: pekzeki
'''

import commons

import glob
import os
from BeautifulSoup import BeautifulSoup

files = glob.glob(os.path.join('data','*.csv'))
for file in files:

    tmp = commons.get_population(file)
    year = commons.get_year(file)
    
    tmp['Man_Is_Bigger'] = True
    tmp['Man_Is_Bigger'][tmp['Kadin'] > tmp['Erkek']] = False
    
    dominance_df = tmp['Man_Is_Bigger']
    
    ### Color scheme.
    colors = ["#CCCCCC", "#3399FF", "#FF00FF"]
    
    # Load the SVG map
    svg = open('data/turkey_map.svg', 'r').read()
    soup = BeautifulSoup(svg)
    paths = soup.findAll('path')
    
    # Change colors accordingly
    path_style_colorful = 'opacity:1;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:1, 8;stroke-dashoffset:0;stroke-opacity:1;fill:'
    
    for p in paths:
        try:
            plate_number = p['id']
            rate = dominance_df.irow([int(plate_number[3:])]) 
            
            if rate.irow(0) == True:
                color_class = 1
            elif rate.irow(0) == False:
                color_class = 2
        except: 
            color_class = 0
            
        color = colors[color_class]
        p['style'] = path_style_colorful + color
    
    #Write to a file
    f = open('output/dominance_map_'+str(year)+'.svg','w')
    f.write(soup.prettify())
    f.close() 
