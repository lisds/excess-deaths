import pandas as pd
import numpy as np


def merge_vaccines(type_dataframe, means, v_types):
    merged = {}
    for x in v_types:
        merged[x] = pd.merge(type_dataframe[type_dataframe['VaccineType'] == x][['VaccineType', 'ReportingCountry', '% vaxed']], means, on = 'ReportingCountry')
    return merged
