import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import scipy.stats as sps


def linregress_table(vaccine_dict):
    value_table = pd.DataFrame(columns=['slope', 'p-value', 'r-value'])

    for vaccine_type, column in vaccine_dict.items():
        x = column['% vaxed']
        y = column['Mean 2023']

        slope, intercept, r_value, p_value, blah = sps.linregress(x,y)


        value_table.loc[vaccine_type] = [slope, p_value, r_value]

    return value_table







