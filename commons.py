# -*- coding: utf-8 -*-

'''
Includes commons fuctions used by other scripts and modules 

@author: pekzeki
'''

import os
import pandas as pd

def convert_integer(population):
    '''
    Replaces all occurrence of comas(,) with empty string and converts from string to integer
    '''
    return int(population.replace(",",""))

def get_year(file_path):
    '''
    Finds the year string from the given file and returns it
    '''
    start_index = 5
    return file_path[start_index:start_index+4]

def get_population(file_path):    
    '''
    Creates the output/ folder if it does not exist 
    Read the full csv and return it as a DataFrame
    '''
    if not os.path.exists('output'):
        os.makedirs('output')
    
    df = pd.read_csv(file_path, names=['Sehir','Toplam','Erkek','Kadin','Sehir_Toplam','Sehir_Erkek','Sehir_Kadin','Koy_Toplam','Koy_Erkek','Koy_Kadin'])
    return df

def get_population_skipfirst(file_path):
    '''
    Creates the output/ folder if it does not exist 
    Read the full csv and return it as a DataFrame but skips the first row
    '''
    if not os.path.exists('output'):
        os.makedirs('output')
        
    df = pd.read_csv(file_path, names=['Sehir','Toplam','Erkek','Kadin','Sehir_Toplam','Sehir_Erkek','Sehir_Kadin','Koy_Toplam','Koy_Erkek','Koy_Kadin'], skiprows=1)
    return df