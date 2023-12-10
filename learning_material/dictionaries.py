my_dict = {}
my_dict['Jan'] = 31
my_dict['Feb'] = 28
my_dict['Mar'] = 31

print(my_dict)

my_dict2 = {'Jan': 31, 'Feb': 28, 'Mar': 31}
print(my_dict2)

for k, v in my_dict2.items():
    print(f'{k}={v}')


print(type(my_dict2.keys()))
print(my_dict2.keys())
print(my_dict2.values())
print(my_dict2.items())

for k in my_dict2.keys():
    print(f'{k}={my_dict2[k]}')

for v in my_dict2.values():
    print(v)

print(sum(my_dict2.values()))






