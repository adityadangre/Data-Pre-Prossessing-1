import csv

dataset1 = []
dataset2 = []

with open('final.csv') as f:
    reader = csv.reader(f)
    
    for data in reader:
        dataset1.append(data)

with open('Sorted Exoplanet Data.csv') as f:
    reader = csv.reader(f)

    for data in reader:
        dataset2.append(data)
    
headers1 = dataset1[0]
headers2 = dataset2[0]
planet_data1 = dataset1[1:]
planet_data2 = dataset2[1:]

final_headers = headers1 + headers2
final_planet_data = planet_data1 + planet_data2

with open('Complete Data.csv', 'a+') as f:
    writer = csv.writer(f)
    writer.writerow(final_headers)
    writer.writerows(final_planet_data)