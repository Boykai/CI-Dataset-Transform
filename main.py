# -*- coding: utf-8 -*-
"""
Created on Tue May 23 15:51:13 2017

@author: Boykai
"""

import pandas as pd       

if __name__ == '__main__':
    '''
    Reads in multiple .csv files, stores them as Pandas DataFrame object.
    
    Seperates 'device_name' into proper attributes of 'age', 'cluster', 'device'
    and possibily 'date'.
    
    Creates new XLSX file output, grouping by different features.
    Columns of XLSX output sheets includes:
        'spend'
        'impressions'
        'storied_engagement'
        'cpvv' = 'spend'/'video_views', or 'cpvv' = 0
        'count' = number of distinct 'campaign_names' from input1 CSV per row
        
    Exports 1 table per tab in XLSX file.
    '''
    df1 = pd.read_csv('CI_Analyst_-_input1.csv')
    df2 = pd.read_csv('CI_Analyst_-_input2.csv')
    
    
    