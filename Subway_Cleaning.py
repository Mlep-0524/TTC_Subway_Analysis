import pandas as pd
import numpy as np

"""
 To use: 
 Read data sets into seperate dataframes
 Call merge_data_sets() function with thoses dataframes
 Call cleanData() function with the merged dataframe

 This script file provides helper functions used to clean the TTC data files. 
 All of the processing is performed by calling the cleanData() function in the Jupyter notebook.
 This file should be imported for these functions to be used there.

 Operations include removing erronious/unclear station names, duplicates, missing field entries,
 unknown delay codes, and stations passengers can't access. 
 This script also handles station categorization by line, direction of train travel, etc.
"""

# Data files for testing purposes
#----------------------------------------------------
# Cleaned ttc code descriptions & categories
ttc_clean_codes = pd.read_csv('CSV Files/Code_Desc_Categories_Clean.csv')
# Original TTC data sets. Add more datasets here
ttc_subway_delay_24 = pd.read_csv('CSV Files/ttc-subway-delay-data-2024.csv')
ttc_subway_delay_25 = pd.read_csv('CSV Files/TTC Subway Delay Data since 2025.csv')

# Takes in any number of dataframe data sets and merges them into one dataframe
# Data must be entered in order from oldest to newest for expected results. 
# Assumes all datasets have the same columns
def merge_data_sets(*args):
    df = pd.DataFrame()
    for frame in args:
       df = pd.concat([df, frame],ignore_index=True)
    return df

ttc_all_delays = merge_data_sets(ttc_subway_delay_24,ttc_subway_delay_25)
print(ttc_all_delays)

# Cuong Functions
#-------------------------------------------------------------------------------

# Verify station as non-passenger, passenger, range, or unkown

# Verify linecodes

# Verify delay codes. Sets unkown delay codes to NaN & prints what they were.

# Add delay description and categorizations to data


# Megan Functions
#-----------------------------------------------------------------------

'''
clean/standardize station names. Assume non-passenger and range stations 
have been removed.
'''


''' 
Seperate range stations
'''



# Output
#------------------------------------------------------------------------
# Single function to call in main file
def cleanData(df):
    return df

def cleanRangeStations(df):
    return df