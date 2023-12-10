import pandas as pd
import numpy as np

excess_death = pd.read_excel('data/excess_death.xlsx', sheet_name = 'Sheet 1', skiprows=7, skipfooter=6)

# Remove columns labelling rates that are estimated or provisional data ** RETURN TO THIS
justnumbs = excess_deaths.loc[:, ~excess_deaths.columns.str.startswith('Unnamed')][1:]

# Make index country names
justnumbs = justnumbs.set_index('TIME')

# Add a mean excess death by EU country for 2023 
justnumbs = justnumbs.apply(pd.to_numeric, errors='coerce')
justnumbs['Mean 2023'] = justnumbs.iloc[:, -9:].mean(axis = 1)
justnumbs.sort_values('Mean 2023')
