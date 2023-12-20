import pandas as pd
import numpy as np

#defining the function
def merge_vaccines(type_dataframe, means, v_types):
    #creating an empty dict to store values in
    merged = {}
    #a loop that does the merging of the dataframes and stores them in my dict
    for x in v_types:
        merged[x] = pd.merge(type_dataframe[type_dataframe['VaccineType'] == x][['VaccineType', 'ReportingCountry', '% vaxed']], means, on = 'ReportingCountry')
    return merged
