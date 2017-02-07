import csv
with open('names.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print str(''.join(row))
        #print(str(row))
