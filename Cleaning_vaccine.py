import pandas as pd
import numpy as np

vaccine_types = pd.read_excel('vaccine_types.xlsx')

#Drop unwanted columns - only focussing on first dose - binary vaccinated or not
vaccine_types.drop(['Denominator', 'NumberDosesReceived', 'NumberDosesExported', 'FirstDoseRefused', 'SecondDose', 'DoseAdditional1', 'DoseAdditional2', 'DoseAdditional3', 'DoseAdditional4', 'DoseAdditional5', 'UnknownDose'], axis = 1)

#Add year column
vaccine_types['Year'] = vaccine_types['YearWeekISO'].str[:4].str.strip()

#Just focus on 'All' vaccine count per week - remove age splits
vaccine_types = vaccine_types[vaccine_types['TargetGroup'] == 'ALL']

#Remove regions - only want total vaccine count for country that week
vaccine_types = vaccine_types[vaccine_types['ReportingCountry'] == vaccine_types['Region']]

#Drop duplicate rows
drop_dupes = total_vaccinated.drop_duplicates(subset = ['YearWeekISO', 'ReportingCountry', 'FirstDose'])



#There are still some porblems with the outputs for some countries