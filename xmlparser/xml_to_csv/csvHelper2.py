import xml.etree.ElementTree as ET
import csv


def getfile(path):
    tree = tree = ET.parse(path)
    root = tree.getroot()
    return root


def getheaders():
    for field in root.findall('.//mt'):
        cols.append(field.text)


def writedata(path):
    with open(path, 'w', newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(cols)
        for record in root.findall('.//mv'):
            row = []
            for field in record:
                row.append(field.text)
            writer.writerow([start_time] + row)


if __name__ == '__main__':
    root = getfile('test.xml')
    start_time = root.find('.//mts').text
    cols = ['start_time', 'MSC']
    getheaders()
    writedata('ours.csv')
