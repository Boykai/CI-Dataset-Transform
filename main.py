# -*- coding: utf-8 -*-
"""
Created on Tue May 23 15:51:13 2017

@author: Boykai
"""

import pandas as pd

class Process(object):
    def __init__(self, df):
        '''
        Represents the processing of the csv input files, converted into a 
        Pandas DataFrame.
    
        Initializes Pandas DataFrame, saves all parameters as attributes of the 
        instance.     

        df: Keeps track of the dataframe (a Pandas DataFrame object).
        age: The age category of the device_name (a list of strings).
        cluster: The cluster category of the device_name (a list of strings).
        device: The device category of the device_name (a list of strings).
        '''
        self.df = df
        self.age = []
        self.cluster = []
        self.device = []
        
    def get_df(self):
        '''
        @Returns: Process attribute for 'df' (a Pandas Dataframe object).
        '''
        return self.df
        
    def set_df(self, dataframe):
        '''
        dataframe: To set Process 'df' attribute (a Pandas DataFrame object).
        
        Sets the Process attribute for 'df' (a Pandas DataFrame object).
        '''
        self.df = dataframe
        
    def get_age(self):
        '''
        @Returns: Process attribute for 'age' (a list of strings).
        '''
        return self.age
        
    def set_age(self, age_value):
        '''
        age_value: An age range for the 'device_name' (a string)
        
        Appends 'age_value' to Process 'age' attribute.
        '''
        self.age.append(age_value)
        
    def get_cluster(self):
        '''
        @Returns: Process attribute for cluster (a list of strings).
        '''
        return self.cluster
        
    def set_cluster(self, cluster_value):
        '''
        cluster_value: A cluster for the 'device_name' (a string)
        
        Appends 'cluster_value' to Process 'cluster' attribute.
        '''
        self.cluster.append(cluster_value)
        
    def get_device(self):
        '''
        @Returns: Process attribute for device (a list of strings).
        '''
        return self.device
        
    def set_device(self, device_value):
        '''
        device_value: A device for the 'device_name' (a string)
        
        Appends 'device_value' to Process 'device' attribute.
        '''
        self.device.append(device_value)
        
        
    

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
    
    
    