import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import scipy.stats as sps


def linregress_table(vaccine_dict):
    value_table = pd.DataFrame(columns=['intercept', 'slope', 'p-value', 'r-value'])
#pull out data to run regression on
    for vaccine_type, column in vaccine_dict.items():
        x = column['% vaxed']
        y = column['Mean 2023']
#remove any vaccines with identical values as otherwise regression will not run
        if np.std(x) == 0:
            print("Skipping "+vaccine_type+" due to identical x values.")
            continue

        slope, intercept, r_value, p_value, blah = sps.linregress(x,y)
#create a table with regressions variables as columns for all vaccines
        value_table.loc[vaccine_type] = [intercept, slope, p_value, r_value]

    return value_table










