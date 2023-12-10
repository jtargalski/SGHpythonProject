import json

my_file = 'hello_out.json'

# r - read (text)

with open(my_file, 'r') as f:
    my_dict = json.load(f)
    print(my_dict)
    print(my_dict['Jan'])
    #print(points[1][1])

