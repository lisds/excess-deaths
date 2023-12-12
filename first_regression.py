import pandas as pd
import numpy as np
import Cleaning_deaths
import Cleaning_vaccine 
import scipy.stats as sps 
import matplotlib.pyplot as plt 
#Working out the number of people in each country vaxed by the end of 2022, filtering so only data for 'ALL' target group is considered as age specific counts were unreliable, summing the first dose after grouping by target group and reporting country
total_vaxed_up_to_23 = Cleaning_vaccine.base_vaccine_data[Cleaning_vaccine.base_vaccine_data['Year'] != '2023'][Cleaning_vaccine.base_vaccine_data['TargetGroup'] == 'ALL'].groupby('ReportingCountry')['FirstDose'].sum()
#taking the population for each country in as of the first week of 2023
population_wk1_23 = Cleaning_vaccine.base_vaccine_data[Cleaning_vaccine.base_vaccine_data['YearWeekISO'] == '2023-W01'].groupby('ReportingCountry')['Population'].first()
#Converting the number of people vaccinated into a proportion of the population
percent_vaxed_wk1_23= total_vaxed_up_to_23/population_wk1_23
percent_vaxed_wk1_23

just_code_and_mean = Cleaning_deaths.excess_deaths_values[['ReportingCountry', 'Mean 2023']]

#Merging the data frames on the ReportingCountry column, resulting in a data frame with ReportingCountry code, mean excess deaths in 2023 and 
# % of population vaxed as of the end of 2022
merged = pd.merge(just_code_and_mean, pd.DataFrame(percent_vaxed_wk1_23), on = 'ReportingCountry')

#Regressing  the percent vaxed against the mean excess deaths
regression = sps.linregress(merged[0], merged['Mean 2023'])
regression.slope 
regression.intercept




    


plt.scatter(merged[0],merged['Mean 2023'])

for i in range(len(merged)):
    plt.text(merged[0][i] + 0.01, merged['Mean 2023'][i], merged['ReportingCountry'][i], fontsize=8)

plt.xlabel('Percent Vaccinated as of 2023')
plt.ylabel('Mean Excess Deaths 2023')
plt.title('Vaccination uptake versus mean excess deaths')

plt.show()