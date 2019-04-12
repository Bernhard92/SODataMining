    
# generate gaussian data samples
from numpy import mean
from numpy import std
import csv
from scipy.stats import ttest_ind


flesch_data = open("../Texts/Data/accepted/sent_data.csv", "r")
flesch_data_nac = open("../Texts/Data/accepted/nac_sent_data.csv", "r")


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
print('Statistics=%.3f, p=%.31f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
    print('Same distributions (fail to reject H0)')
else:
    print('Different distributions (reject H0)')

