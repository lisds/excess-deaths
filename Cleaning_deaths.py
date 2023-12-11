import pandas as pd
import numpy as np

excess_deaths = pd.read_excel('data/excess_death.xlsx', sheet_name = 'Sheet 1', skiprows=7, skipfooter=6)

# Remove columns labelling rates that are estimated or provisional data ** RETURN TO THIS
excess_deaths_values = excess_deaths.loc[:, ~excess_deaths.columns.str.startswith('Unnamed')][1:]

# Make index country names
excess_deaths_values = excess_deaths_values.set_index('TIME').rename_axis('Country')

# Add a mean excess death by EU country for 2023 
excess_deaths_values = excess_deaths_values.apply(pd.to_numeric, errors='coerce')
excess_deaths_values['Mean 2023'] = excess_deaths_values.iloc[:, -9:].mean(axis = 1)
excess_deaths_values.sort_values('Mean 2023')


country_code_dict = {
    'Belgium': 'BE', 
    'Bulgaria': 'BG', 
    'Czechia': 'CZ', 
    'Denmark': 'DK', 
    'Germany': 'DE', 
    'Estonia': 'EE',
    'Ireland': 'IE', 
    'Greece': 'GR', 
    'Spain': 'ES', 
    'France': 'FR', 
    'Croatia': 'HR', 
    'Italy': 'IT',
    'Cyprus': 'CY', 
    'Latvia': 'LV', 
    'Lithuania': 'LT', 
    'Luxembourg': 'LU', 
    'Hungary': 'HU', 
    'Malta': 'MT',
    'Netherlands': 'NL', 
    'Austria': 'AT', 
    'Poland': 'PL', 
    'Portugal': 'PT', 
    'Romania': 'RO',
    'Slovenia': 'SI', 
    'Slovakia': 'Sk', 
    'Finland': 'FI', 
    'Sweden': 'SE', 
    'Iceland': 'IS',
    'Liechtenstein': 'LI',
    'Norway': 'NO', 
    'Switzerland': 'CH', 
    }

excess_deaths_values['ReportingCountry'] = excess_deaths_values.index.map(country_code_dict)

print(excess_deaths_values)