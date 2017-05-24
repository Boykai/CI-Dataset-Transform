# -*- coding: utf-8 -*-
"""
Created on Tue May 23 15:51:13 2017

@author: Boykai
"""

import pandas as pd
from ast import literal_eval

class Process(object):
    def __init__(self, dataframe):
        '''
        Initializes Pandas DataFrame, saves all parameters as attributes of the 
        instance. 
        
        Represents the processing of the csv input files, converted into a 
        Pandas DataFrame.

        dataframe: To initalize Process 'df' attribute (a Pandas DataFrame 
                   object).
        
        df: Keeps track of the dataframe (a Pandas DataFrame object).
        age: The age category of the device_name (a list of strings).
        cluster: The cluster category of the device_name (a list of strings).
        device: The device category of the device_name (a list of strings).
        '''
        self.df = dataframe
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
        Sets the Process attribute for 'df' (a Pandas DataFrame object).
        
        dataframe: To set Process 'df' attribute (a Pandas DataFrame object).
        '''
        self.df = dataframe
        
    def get_age(self):
        '''
        @Returns: Process attribute for 'age' (a list of strings).
        '''
        return self.age
        
    def set_age(self, age_value):
        '''
        Appends 'age_value' to Process 'age' attribute.
        
        age_value: An age range for the 'device_name' (a string)
        '''
        self.age.append(age_value)
        
    def get_cluster(self):
        '''
        @Returns: Process attribute for 'cluster' (a list of strings).
        '''
        return self.cluster
        
    def set_cluster(self, cluster_value):
        '''
        Appends 'cluster_value' to Process 'cluster' attribute.
        
        cluster_value: A cluster for the 'device_name' (a string)
        '''
        self.cluster.append(cluster_value)
        
    def get_device(self):
        '''
        @Returns: Process attribute for 'device' (a list of strings).
        '''
        return self.device
        
    def set_device(self, device_value):
        '''
        Appends 'device_value' to Process 'device' attribute.
        
        device_value: A device for the 'device_name' (a string)
        '''
        self.device.append(device_value)
        
    def split_full_campaign_name(self, campaign_name_value):
        '''
        Converts an intance of 'campaign_name' feature into age, cluster, device
        and appends the values to their respective class attribute list.
        
        campaign_name_value: contains the age, cluster, device, and possibly 
                             date information for each 'campaign_name' 
                             (a string).
        '''
        expected_ages = ['<21',
                         '21-30',
                         '31-40',
                         '41-50',
                         '51+']
        expected_clusters = ['notarget',
                             'cluster1',
                             'cluster2',
                             'cluster3',
                             'allclusters']
        
        split_string = campaign_name_value.split('_')
                             
        for i in range(len(split_string)):
            if split_string[i] in expected_ages:
                # If string is an 'expected_age' append to age attribute
                # then replace with '' in 'split_string' list
                self.set_age(split_string[i])
                split_string[i] = ''
            elif split_string[i].lower() in expected_clusters:
                # If string is a cluster append to cluster attribute 
                # then replace with '' in 'split_string' list
                self.set_cluster(split_string[i])
                split_string[i] = ''
            elif unicode(split_string[i], 'utf-8').isnumeric():
                # If string is a date 
                # then replace with '' in 'split_string' list
                split_string[i] = ''
            else:
                # Format strings to lower case for 'device' string
                split_string[i] = split_string[i].lower()
        
        # Remove empty string values from list
        device_name = filter(None, split_string)
        
        self.set_device('_'.join(device_name))
    
    def create_keys(self):
        '''
        Creates list of keys from the 'campaign_name' feature. Adds 'key' column
        to 'df' attribute. A 'key' is a tuple of (age, cluster, device) derived
        from the 'campaign_name' column of the 'df'.
        '''
        df = self.get_df()
        
        df['campaign_name'].apply(self.split_full_campaign_name)
        
        age = self.get_age()
        cluster = self.get_cluster()
        device = self.get_device()
        
        df['key'] = zip(age, cluster, device)

        self.set_df(df)

class ProcessInput1(Process):
    '''
    Child of Process() Class.
    
    Represents the processing of the first csv input file, 
    'CI_Analyst_-_input1' converted into a Pandas DataFrame.

    ProcessInput1 takes in a Pandas DataFrame object, created from the given
    input file 'CI_Analyst_-_input1.csv'. This class allows for the Pandas 
    Dataframe to be mutated to include the following features:
        
        key: Created from 'campain_name' feature. Seperating 'age', 'cluster',
             'device' into a tuple. (a tuple) 
             Ex. ('31-40', 'notarget', 'htc_one_1GB')
        age: The age category of the device_name (a string).
        cluster: The cluster category of the device_name (a string).
        device: The device category of the device_name (a list of strings).
        spend: Definition of feature not given. (a float)
        impressions: Definition of feature not given. (an integer)
        clicks: Definiton of feature not given. (an integer)
        count: Number of distinct campaign names from per row (an integer)          
    
    Assumptions:
        The campaign data is from, 'date', is not needed or used.
    '''
    
    def __init__(self, dataframe):
        '''
        Initializes Pandas DataFrame, saves all parameters as attributes of the 
        instance, within the Process() parent class.
        
        Represents the processing of the first csv input files, converted into a 
        Pandas DataFrame.

        dataframe: To initalize Process 'df' attribute (a Pandas DataFrame 
                   object).
        '''
        super(ProcessInput1, self).__init__(dataframe)
        
class ProcessInput2(Process):
    '''
    Child of Process() Class.
    
    Represents the processing of the first csv input file, 
    'CI_Analyst_-_input1' converted into a Pandas DataFrame.

    ProcessInput2 takes in a Pandas DataFrame object, created from the given
    input file 'CI_Analyst_-_input2.csv'. This class allows for the Pandas 
    Dataframe to be mutated to include the following features:
        
        key: Created from 'campain_name' feature. Seperating 'age', 'cluster',
             'device' into a tuple. (a tuple) 
             Ex. ('31-40', 'notarget', 'htc_one_1GB')
        age: The age category of the device_name (a string).
        cluster: The cluster category of the device_name (a string).
        device: The device category of the device_name (a list of strings).
        actions: List of dicts with {'action_type':value'. (a list of dicts)
        object_type: Definition of feature not given. (a string)
    '''
    
    def __init__(self, dataframe):
        '''
        Initializes Pandas DataFrame, saves all parameters as attributes of the 
        instance, within the Process() parent class.
        
        Represents the processing of the first csv input files, converted into a 
        Pandas DataFrame.

        dataframe: To initalize Process 'df' attribute (a Pandas DataFrame 
                   object).
        storied_engagements: The sum of like, comment, and share 'action_types'
                             for each given sample. (an list of integers).
        video_views: The sum of 'video_view' for a given sample. (a list of 
                     integers).
        '''
        super(ProcessInput2, self).__init__(dataframe)
        self.storied_engagements = []
        self.video_view = []
    
    def get_storied_engagements(self):
        '''
        @Returns: ProcessInput2 attribute for 'storied_engagements' (a list 
                  integers).
        '''
        return self.storied_engagements
        
    def set_storied_engagements(self, storied_engagements_value):
        '''
        Appends 'storied_engagements' to ProcessInput2 'storied_engagements'
        attribute.
        
        storied_Engagements_value: A value for the 'storied_engagements_value' 
                                  (an integer)
        '''
        self.storied_engagements.append(storied_engagements_value)
        
    def get_video_view(self):
        '''
        @Returns: ProcessInput2 attribute for 'video_view' (a list of strings).
        '''
        return self.video_view
        
    def set_video_view(self, video_view_value):
        '''
        Appends 'video_view_value' to ProcessInput2 'video_view' attribute.
        
        video_view_value: The sum of video view action types. (an integer)
        '''
        self.video_view.append(video_view_value)
    
    def process_actions(self, action_value):
        video_views = 0
        storied_engagement = 0
        valid_storied_engagements = ['like',
                                     'comment',
                                     'share']
        
        for item in action_value:
            if item['action_type'] in valid_storied_engagements:
                storied_engagement += item['value']
            elif item['action_type'] == 'video_view':
                video_views += item['value']
            else:
                pass
        
        self.set_storied_engagements(storied_engagement)
        self.set_video_view(video_views)
        
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
    df_input1 = pd.read_csv('CI_Analyst_-_input1.csv')
    df_input2 = pd.read_csv('CI_Analyst_-_input2.csv', 
                            converters={'actions':literal_eval})
    
    
    
    
    