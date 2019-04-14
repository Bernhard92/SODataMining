
import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import ttest_ind

"""

In this class i calculate the distribution of the changes to the positive
and negative of a given file, separated 

"""

flesch_data = open("../Texts/Data/open/open_sent_data.csv", "r")

reader = csv.reader(flesch_data)


pos = 0
null = 0
neg = 0

pos_values = []
neg_values = []
null_values = []

flesch = []

for line in reader:
    number = float(line[0])
    flesch.append(number)
    if number > 0:
        pos += 1
        pos_values.append(number)
    elif number < 0:
        neg += 1 
        neg_values.append(number)
    elif number == 0:
        null += 1
        null_values.append(number)
    else:
        print("error with ", number)
        
flesch_data.close()

print("pos: ", pos)
print("neg: ", neg)
print("null: ", null)
print(pos+neg+null)

print("sum pos: ", sum(pos_values))
print("sum neg: ", sum(neg_values))
print("sum neu: ", sum(null_values))

print(len(flesch))
print("gesammt: ", sum(flesch)/len(flesch))

# compare samples
stat, p = ttest_ind(pos_values, neg_values)
print('Statistics=%.3f, p=%.31f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
    print('Same distributions (fail to reject H0)')
else:
    print('Different distributions (reject H0)')


plt.figure(1, figsize=(12,5))
#plt.suptitle('Flesch Reading Ease evolution of open posts')
plt.subplot(121)
plt.ylabel("Change to positive")
plt.boxplot(np.array(pos_values).astype(np.float), showfliers=False)
plt.subplot(122)
plt.ylabel("Change to negative")
plt.boxplot(np.array(neg_values).astype(np.float), showfliers=False)
plt.show()
"""
plt.subplot(133)
plt.ylabel("complete data")
plt.boxplot(np.array(flesch).astype(np.float), showfliers=False)
plt.show()
"""







flesch_data = open("../Texts/Data/open/closed_sent_data.csv", "r")

reader = csv.reader(flesch_data)


pos = 0
null = 0
neg = 0

pos_values = []
neg_values = []
null_values = []

flesch = []

for line in reader:
    number = float(line[0])
    flesch.append(number)
    if number > 0:
        pos += 1
        pos_values.append(number)
    elif number < 0:
        neg += 1 
        neg_values.append(number)
    elif number == 0:
        null += 1
        null_values.append(number)
    else:
        print("error with ", number)
        
flesch_data.close()

print("pos: ", pos)
print("neg: ", neg)
print("null: ", null)
print(pos+neg+null)

print("sum pos: ", sum(pos_values))
print("sum neg: ", sum(neg_values))
print("sum neu: ", sum(null_values))

print(len(flesch))
print("gesammt: ", sum(flesch)/len(flesch))

# compare samples
stat, p = ttest_ind(pos_values, neg_values)
print('Statistics=%.3f, p=%.31f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
    print('Same distributions (fail to reject H0)')
else:
    print('Different distributions (reject H0)')


plt.figure(1, figsize=(12,5))
ax1 = plt.subplot(121)
plt.ylabel("Change to positive")
plt.boxplot(np.array(pos_values).astype(np.float), showfliers=False)
ax2=plt.subplot(122)
plt.ylabel("Change to negative")
plt.boxplot(np.array(neg_values).astype(np.float), showfliers=False)
plt.show()
"""
ax3=plt.subplot(133)
plt.ylabel("complete data")
plt.boxplot(np.array(flesch).astype(np.float), showfliers=False)
plt.show()
""" 
    



    

