import csv
import os

data_folder = "."
data_file = "household_power_consumption.csv"

with open(os.path.join(data_folder,data_file), newline='') as csvfile, open(os.path.join(data_folder, 'temp.csv'), 'w', newline='') as tempfile:
    csvreader = csv.reader(csvfile)
    csvwriter = csv.writer(tempfile)
    for row, i in zip(csvreader, range(10)):
      csvwriter.writerow(row)
with open(os.path.join(data_folder, "temp.csv"), newline='') as tempfile:
  csvreader = csv.reader(tempfile)
  for row in csvreader:
    print (row)
