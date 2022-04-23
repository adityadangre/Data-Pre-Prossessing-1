import csv

data = []

with open('Detailed Exoplanet Data.csv') as f:
    reader = csv.reader(f)
    
    for row in reader:
        data.append(row)

headers = data[0]
planet_data = data[1:]

for data_point in planet_data:
    data_point[0] = data_point[0].lower()

planet_data.sort(key = lambda planet_data: planet_data[0])

with open('Sorted Exoplanet Data.csv', 'a+') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(planet_data)