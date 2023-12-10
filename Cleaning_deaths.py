import pandas as pd
import numpy as np

excess_deaths = pd.read_excel('data/excess_death.xlsx', sheet_name = 'Sheet 1', skiprows=7, skipfooter=6)

# Remove columns labelling rates that are estimated or provisional data ** RETURN TO THIS
excess_deaths_values = excess_deaths.loc[:, ~excess_deaths.columns.str.startswith('Unnamed')][1:]

# Make index country names
excess_deaths_values = excess_deaths_values.set_index('TIME')

# Add a mean excess death by EU country for 2023 
excess_deaths_values = excess_deaths_values.apply(pd.to_numeric, errors='coerce')
excess_deaths_values['Mean 2023'] = excess_deaths_values.iloc[:, -9:].mean(axis = 1)
excess_deaths_values.sort_values('Mean 2023')


print(excess_deaths_values)