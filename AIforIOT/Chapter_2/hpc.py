import csv
import os

data_folder = "."
data_file = "household_power_consumption.csv"

with open(os.path.join(data_folder,data_file), newline='') as csvfile:
  csvreader = csv.reader(csvfile)
  for row in csvreader:
    print (row)
