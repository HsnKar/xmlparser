import xml.etree.ElementTree as ET
import os
import csv

tree = ET.parse("test.xml")
root = tree.getroot()
start_time = root.find('.//mts').text
print(start_time)
cols = ['start_time', 'MSC']

for field in root.findall('.//mt'):
    cols.append(field.text)

with open('../fh.csv', 'w', newline='', encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(cols)
    for record in root.findall('.//mv'):
        row = []
        for field in record:
            row.append(field.text)
        writer.writerow([start_time] + row)