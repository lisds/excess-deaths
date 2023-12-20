import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import scipy.stats as sps

#These are my step-by-step attempts at creating a permutation test based on last year's textbook.

#PFI = sps.linregress(vaccine_dict['Pfizer']['% vaxed'], vaccine_dict['Pfizer']['Mean 2023'])
#ASTRA = sps.linregress(vaccine_dict['Astrazeneca']['% vaxed'], vaccine_dict['Astrazeneca']['Mean 2023'])
#SDIFF = ASTRA.slope - PFI.slope

#astra_array = vaccine_dict['Astrazeneca']['% vaxed']
#pfizer_array = vaccine_dict['Pfizer']['% vaxed']
#pooled = np.concatenate([astra_array, pfizer_array])

#rng = np.random.default_rng()
#shuffled = rng.permutation(pooled)
#shuffled
#shuffled[0:26]
#shuffled[26:]
#fakePFI = sps.linregress(shuffled[26:], vaccine_dict['Pfizer']['Mean 2023'])
#fakeASTRA = sps.linregress(shuffled[0:26], vaccine_dict['Astrazeneca']['Mean 2023'])
#fakeDIFF = fakeASTRA.slope - fakePFI.slope
#fakeDIFF

#fake_differences = np.zeros(10000)
#for i in np.arange(10000):
#    shuffle = rng.permutation(pooled)
#    fakePFIloop = sps.linregress(shuffle[26:], vaccine_dict['Pfizer']['Mean 2023'])
#    fakeASTRAloop = sps.linregress(shuffle[0:26], vaccine_dict['Astrazeneca']['Mean 2023'])
#    fake_diff = fakeASTRAloop.slope - fakePFIloop.slope
#    fake_differences[i] = fake_diff
#plt.hist(fake_differences);




def permute(Vax1_str, Vax2_str, dict):
    rng = np.random.default_rng()
    Vax1 = sps.linregress(dict[Vax1_str]['% vaxed'], dict[Vax1_str]['Mean 2023'])
    Vax2 = sps.linregress(dict[Vax2_str]['% vaxed'], dict[Vax2_str]['Mean 2023'])
    real_diff = Vax1.slope - Vax2.slope
    first_array = dict[Vax1_str]['% vaxed']
    second_array = dict[Vax2_str]['% vaxed']
    pool = np.concatenate([first_array, second_array])

    
    fake_difference = np.zeros(10000)
    
    for i in np.arange(10000):
        shuff = rng.permutation(pool)
        fakeVax1 = sps.linregress(shuff[0:len(first_array)], dict[Vax1_str]['Mean 2023'])
        fakeVax2 = sps.linregress(shuff[len(first_array):], dict[Vax2_str]['Mean 2023'])
        fake_diff = fakeVax1.slope - fakeVax2.slope
        fake_difference[i] = fake_diff
        diff_act = np.count_nonzero(fake_difference <= real_diff)
    return plt.hist(fake_difference), plt.xlabel('Difference in permuted slopes'), plt.ylabel('Count'), plt.title('Distribution of permuted slope differences') and print('Number of times real difference in slopes occurs in permutation: ', diff_act);
