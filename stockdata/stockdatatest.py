import os

folder_path = 'C:\\Users\\razze\\PycharmProjects\\SGHpythonProject\\stockdata\\'

csv_files = []
for filename in os.listdir(folder_path):
    if filename.endswith('_stock.csv'):
        csv_files.append(os.path.join(folder_path, filename))

for csv_file in csv_files:
    with open(csv_file, 'r') as f:
        rows = f.readlines()
        print(rows)