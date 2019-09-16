import csv
with open('toy_complet.csv') as csvFile:
    reader = list(csv.reader(csvFile))
    print(reader[0][0].split())
    #for row in reader:
    #    print(','.join(row))