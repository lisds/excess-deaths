import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

def plot_vax(vaccine_dict, vax, mean):
    
    
    fig, axes = plt.subplots(nrows=3, ncols=6, figsize=(18, 9))

    
    axes = axes.flatten()

   
    for i, (vaccine, table) in enumerate(vaccine_dict.items()):
        
        ax = axes[i]


        ax.scatter(table[vax], table[mean])

        
        ax.set_title(vaccine)
        ax.set_xlabel('Percentage Vaccinated')
        ax.set_ylabel('Excess Death Mean 2023')

    
    plt.tight_layout()
    
 
    plt.show()







#def plot_vax(vaccine_dict, vax, mean):
    #for vaccine, table in vaccine_dict.items():
        #plt.scatter(table[vax], table[mean])
        #plt.title(vaccine)
        #plt.xlabel('Percentage Vaccinated')
        #plt.ylabel('Excess Death Mean 2023')
        #plt.show()
