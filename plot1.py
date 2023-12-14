import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 



def plot_vax(vaccine_dict, vax, mean):
    for vaccine, table in vaccine_dict.items():
        plt.scatter(table[vax], table[mean])
        plt.title(vaccine)
        plt.xlabel('Percentage Vaccinated')
        plt.ylabel('Excess Death Mean 2023')
        plt.show()
