
import csv
import matplotlib.pyplot as plt
import numpy as np

"""

In this class i calculate the distribution of the changes to the positive
and negative of a given file, separated 

"""

flesch_data = open("../Texts/Data/accepted/flesch_data.csv", "r")

reader = csv.reader(flesch_data)


pos = 0
null = 0
neg = 0

pos_values = []
neg_values = []
null_values = []



for line in reader:
    number = float(line[0])
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



plt.figure(1, figsize=(12,5))
plt.subplot(121)
plt.ylabel("Change to positive")
plt.boxplot(np.array(pos_values).astype(np.float), showfliers=False)
plt.subplot(122)
plt.ylabel("Change to negative")
plt.boxplot(np.array(neg_values).astype(np.float), showfliers=False)
plt.show()








flesch_data = open("../Texts/Data/accepted/nac_flesch_data.csv", "r")

reader = csv.reader(flesch_data)


pos = 0
null = 0
neg = 0

pos_values = []
neg_values = []
null_values = []



for line in reader:
    number = float(line[0])
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



plt.figure(1, figsize=(12,5))
plt.subplot(121)
plt.ylabel("Change to positive")
plt.boxplot(np.array(pos_values).astype(np.float), showfliers=False)
plt.subplot(122)
plt.ylabel("Change to negative")
plt.boxplot(np.array(neg_values).astype(np.float), showfliers=False)
plt.show()



