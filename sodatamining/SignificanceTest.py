    
# generate gaussian data samples
from numpy.random import seed
from numpy.random import randn
from numpy import mean
from numpy import std
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# seed the random number generator
seed(1)
# generate two sets of univariate observations
data1 = 5 * randn(100) + 50
data2 = 5 * randn(100) + 51
# summarize


#print('data1: mean=%.3f stdv=%.3f' % (mean(data1), std(data1)))
#print('data2: mean=%.3f stdv=%.3f' % (mean(data2), std(data2)))



"""
# Student's t-test
from numpy.random import seed
from numpy.random import randn
from scipy.stats import ttest_ind
# seed the random number generator
seed(1)
# generate two independent samples
data1 = 5 * randn(100) + 50
data2 = 5 * randn(100) + 51
# compare samples
stat, p = ttest_ind(data1, data2)
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
    print('Same distributions (fail to reject H0)')
else:
    print('Different distributions (reject H0)')

"""


flesch_data = open("../Texts/Data/accepted/flesch_data.csv", "r")
flesch_data_nac = open("../Texts/Data/accepted/nac_flesch_data.csv", "r")


flesch = []
flesch_nac = []

reader = csv.reader(flesch_data)
reader2 = csv.reader(flesch_data_nac)

for line in reader:
    flesch.append(float(line[0]))
for line in reader2:
    flesch_nac.append(float(line[0]))
    
    
print('data1: mean=%.3f stdv=%.3f' % (mean(flesch), std(flesch)))
print('data1: mean=%.3f stdv=%.3f' % (mean(flesch_nac), std(flesch_nac)))


# compare samples
stat, p = ttest_ind(flesch, flesch_nac)
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
    print('Same distributions (fail to reject H0)')
else:
    print('Different distributions (reject H0)')
    
plt.ylabel('number of occurrences')
plt.xlabel('change of flesch score') 
plt.hist(np.array(flesch), bins=np.arange(np.array(flesch).min(), np.array(flesch).max()+1),)
plt.show()
    
    