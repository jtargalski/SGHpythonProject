import os.path

temp_dir = os.getenv('TEMP')
print(f'Temp dir is {temp_dir}')

#my_file = 'Desktop\nyfile.txt'
my_file = os.path.join('data', 'nyfile.txt')
#my_file = 'data/nyfile.txt'

working_dir = os.getcwd()
print(f'I\'m now in {working_dir}')

print(os.listdir('.'))

if os.path.exists(my_file):
    print('My File exists')
else:
    print(f'{my_file} not found')
    exit(536)

print('Dir of my file: {}'.format(os.path.dirname(my_file)))
print('Name of my file: {}'.format(os.path.basename(my_file)))



with open(my_file, 'r') as f:
    lines = f.readlines()
    i = 0
    for line in lines:
        i += 1
        print(f'{i}: {line}', end='')

print()
# . - same folder
# .. - parent folder
print(os.listdir('.'))