import csv

flesch_data = open("../Texts/Data/open/open_sent_data.csv", "r")
reader = csv.reader(flesch_data)

sum = 0
i = 0
for line in reader:
    sum += float(line[0])
    i+=1
print(sum)