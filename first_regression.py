import pandas as pd
import numpy as np
import Cleaning_deaths
import Cleaning_vaccine 
import scipy.stats as sps 
import matplotlib.pyplot as plt 

total_vaxed_up_to_23 = Cleaning_vaccine.base_vaccine_data[Cleaning_vaccine.base_vaccine_data['Year'] != '2023'][Cleaning_vaccine.base_vaccine_data['TargetGroup'] == 'ALL'].groupby(['TargetGroup', 'ReportingCountry'])['FirstDose'].sum()
population_wk1_23 = Cleaning_vaccine.base_vaccine_data[Cleaning_vaccine.base_vaccine_data['YearWeekISO'] == '2023-W01'].groupby('ReportingCountry')['Population'].first()

percent_vaxed_wk1_23= total_vaxed_up_to_23/population_wk1_23
percent_vaxed_wk1_23

just_code_and_mean = Cleaning_deaths.excess_deaths_values[['ReportingCountry', 'Mean 2023']]

merged = pd.merge(just_code_and_mean, pd.DataFrame(percent_vaxed_wk1_23), on = 'ReportingCountry')

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