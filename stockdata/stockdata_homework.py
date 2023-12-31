# Jakub Targalski 131438
# necessary imports
import os
import csv
from urllib.request import urlopen

# insert the folder path below
folder_path = 'C:\\Users\\razze\\PycharmProjects\\SGHpythonProject\\stockdata\\'


# download files

urlGOOG = 'https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1672480188&period2=1704016188&interval=1d&events=history&includeAdjustedClose=true'
urlMSFT = 'https://query1.finance.yahoo.com/v7/finance/download/MSFT?period1=1672480331&period2=1704016331&interval=1d&events=history&includeAdjustedClose=true'
urlIBM = 'https://query1.finance.yahoo.com/v7/finance/download/IBM?period1=1672480341&period2=1704016341&interval=1d&events=history&includeAdjustedClose=true'

local_path = os.path.join(folder_path, 'GOOG_stock.csv')
with urlopen(urlGOOG) as image, open(local_path, 'wb') as f:
    f.write(image.read())

local_path = os.path.join(folder_path, 'MSFT_stock.csv')
with urlopen(urlMSFT) as image, open(local_path, 'wb') as f:
    f.write(image.read())

local_path = os.path.join(folder_path, 'IBM_stock.csv')
with urlopen(urlIBM) as image, open(local_path, 'wb') as f:
    f.write(image.read())

# define the entire program as function
def calculate_change(directory):
    # for the sake of the program, the files with stock prices are ending with '_stock.csv'
    # first, the function creates a list of paths to the stock prices csv files
    csv_files = []
    for filename in os.listdir(directory):
        if filename.endswith('_stock.csv'):
            csv_files.append(os.path.join(directory, filename))

    # here, the function transforms the csv file into a list, where each element is the row in form of a list
    for csv_file in csv_files:
        with open(csv_file, 'r') as f:
            rows = f.readlines()

        csv_file_as_list = []

        for row in rows:
            els = row.strip().split(',')
            csv_file_as_list.append(els)

        #change Open and Close to float data type
        for row in range(1, len(csv_file_as_list)):
            csv_file_as_list[row][1] = float(csv_file_as_list[row][1])
            csv_file_as_list[row][4] = float(csv_file_as_list[row][4])

        #add a header for the new column in the csv called 'Change'
        csv_file_as_list[0].append('Change')

        #add Change value in the new column for all rows containing stock prices
        #csv_file_as_list[1:] to omit headers row
        for row in csv_file_as_list[1:]:
            price_open = row[1]
            price_close = row[4]
            price_change = round((((price_close-price_open) / price_open) * 100), 3)
            row.append(str(price_change) + '%')

        print(csv_file_as_list)

        # the program writes the new data in a new .csv file but in the same folder
        # I struggled a little with creating the file in a new folder, so it would be nice if you could let me know how
        # to do it in this particular program, thanks!
        csv_file_new = csv_file.replace('_stock.csv', '_stock_change.csv')

        with open(csv_file_new, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(csv_file_as_list)

#use of the final function

calculate_change(folder_path)
