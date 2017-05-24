# -*- coding: utf-8 -*-
"""
Created on Tue May 23 15:51:13 2017

@author: Boykai
"""

import pandas as pd
from ast import literal_eval
import process
        
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
    # Read in .csv files to their respective Pandas DataFrame
    df1_input = pd.read_csv('CI_Analyst_-_input1.csv')
    df2_input = pd.read_csv('CI_Analyst_-_input2.csv', 
                            converters={'actions':literal_eval})
    
    # Create new instance of ProcessInput1, get new df with appended columns
    df1_obj = process.ProcessInput1(df1_input)
    df1_processed = df1_obj.create_new_df()\
                           .drop_duplicates(subset='key')
    
    # Create new instance of ProcessInput2, get new df with appended columns
    df2_obj = process.ProcessInput2(df2_input)
    df2_processed = df2_obj.create_new_df()\
                           .drop_duplicates(subset='key')
    
    # Create 'count' column
    # 'count' = count of unquie keys, for each group of keys
    df1_processed['count'] = 1
    
    # Merge df1 and df2 by 'key'
    df_output = df1_processed.merge(df2_processed, on='key', how='inner')
    # Calculate 'CPPV' as 'spend'/'video_views', if 'object_type' is 'VIDEO',
    # otherwise set 'CPPV' = 0
    df_output['CPPV'] = (df_output['spend']/df_output['video_views'])\
                        .where((df_output['object_type'] == 'VIDEO') &\
                               (df_output['video_views'] > 0))\
                        .fillna(0)\
                        .round(decimals = 2)
    
    # Create table groups, groupby key, age, cluster, device
    # Calculate sum of each group
    # Append 'Totals' row to end of DataFrame
    df_groupby_key = df_output.groupby('key').sum()
    df_groupby_key.loc['Totals'] = df_groupby_key.sum()
                              
    df_groupby_age = df_output.groupby('age').sum()
    df_groupby_age.loc['Totals'] = df_groupby_age.sum()
    
    df_groupby_cluster = df_output.groupby('cluster').sum()
    df_groupby_cluster.loc['Totals'] = df_groupby_cluster.sum()
                                  
    df_groupby_device = df_output.groupby('device').sum()
    df_groupby_device.loc['Totals'] = df_groupby_device.sum()
    
    # Output groupby Pandas DataFrames to different sheets in same .xlsx
    # Keeps only the desired columns for each sheet
    keep_columns = ['spend', 'impressions', 'CPPV', 'count']
    
    writer = pd.ExcelWriter('output.xlsx')
    df_groupby_key[keep_columns].to_excel(writer, 'Sheet1')
    df_groupby_age[keep_columns].to_excel(writer, 'Sheet2')
    df_groupby_cluster[keep_columns].to_excel(writer, 'Sheet3')
    df_groupby_device[keep_columns].to_excel(writer, 'Sheet4')
    writer.save()