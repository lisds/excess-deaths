import pandas as pd
import numpy as np

base_vaccine_data = pd.read_excel('data/vaccine_types.xlsx')

#Drop unwanted columns - only focussing on first dose - binary vaccinated or not
base_vaccine_data = base_vaccine_data.drop(['Denominator', 'NumberDosesReceived', 'NumberDosesExported', 'FirstDoseRefused', 'SecondDose', 'DoseAdditional1', 'DoseAdditional2', 'DoseAdditional3', 'DoseAdditional4', 'DoseAdditional5', 'UnknownDose'], axis = 1)

#Add year column
base_vaccine_data['Year'] = base_vaccine_data['YearWeekISO'].str[:4].str.strip()

#Remove regions - only want total vaccine count for country that week
base_vaccine_data = base_vaccine_data[base_vaccine_data['ReportingCountry'] == base_vaccine_data['Region']]

#Drop duplicate rows
base_vaccine_data = base_vaccine_data.drop_duplicates(subset = ['YearWeekISO', 'ReportingCountry', 'FirstDose'])



#There are still some problems with the outputs for some countries I think