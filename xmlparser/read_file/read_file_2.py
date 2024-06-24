import xml.etree.ElementTree as ET
import csv
import os

path = "C:/Users/fkz_tmp/Documents/Projet Power BI/Local Tests/Export_U2020_CN/"
dir_list = os.listdir(path)

tree = ET.parse(
    "C:/Users/fkz_tmp/Documents/Projet Power BI/Local Tests/Export_U2020_CN/" + 'HOST02_pmresult_83888217_60_202406190000_202406190100.xml')
root = tree.getroot()
cols = ['start_time', 'MSC']

for field in root.findall('.//mt'):
    cols.append(field.text)

with open('fh.csv', 'a', newline='', encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(cols)

# Loop through the directory
for file in dir_list:
    tree = ET.parse("C:/Users/fkz_tmp/Documents/Projet Power BI/Local Tests/Export_U2020_CN/" + file)
    root = tree.getroot()
    start_time = root.find('.//mts').text
    # Added this date formatter
    start = f"{start_time[:4]}-{start_time[4:6]}-{start_time[6:8]} {start_time[8:10]}:{start_time[11:]}0"
    with open('fh.csv', 'a', newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        for record in root.findall('.//mv'):
            row = []
            for field in record:
                row.append(field.text)
            writer.writerow([start] + row)
