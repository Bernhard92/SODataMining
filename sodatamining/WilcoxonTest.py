from scipy import stats
import csv
import numpy as np

flesch_data = open("../Texts/Data/accepted/flesch_data.csv", "r")
flesch_data_nac = open("../Texts/Data/accepted/nac_flesch_data.csv", "r")


flesch = []
flesch_nac = []

reader = csv.reader(flesch_data)
reader2 = csv.reader(flesch_data_nac)
"""
for line in reader:
    list = []
    list.append(float(line[0]))
    list.append(0)
    flesch.append(list)
for line in reader2:
    list = []
    list.append(float(line[0]))
    list.append(1)
    flesch_nac.append(list)
"""

for line in reader:
    flesch.append(line[0])
for line in reader2:    
    flesch_nac.append(line[0])



#print(stats.mannwhitneyu(flesch, flesch_nac))
print(flesch[:50])
print(flesch_nac[:50])

data = np.array(flesch+flesch_nac)
print(data)
print(len(data))

stat, p = stats.mannwhitneyu(flesch, flesch_nac)

print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
    print('Same distribution (fail to reject H0)')
else:
    print('Different distribution (reject H0)')