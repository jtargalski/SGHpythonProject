my_text = 'In a competitive research environment, publishing is not enough anymore. You have to make your research accessible, findable and visible. Your online identity is the central key for your career and your recognition, particularly for young researchers. This session will help you to build your online research profile by applying best practices. You will learn how to evaluate your online identity and promote your work by using the tools best suited to your needs. A special focus on ORCID will be presented.'

#TODO
# 1. Delete special symbols (.,",')
# 2. Create a dictionary containing each word and the number of occurrences (count)

special_symbols = [',', '.', '\'', '"', ]
# my_text_edited = []
# for char in my_text:
#     if char in special_symbols:
#         char = ''
#     my_text_edited += char

my_text_edited = my_text
for char in my_text_edited:
    if char in special_symbols:
        my_text_edited = my_text_edited.replace(char,'')

print(my_text_edited)
# my_text_edited_string = ''.join(my_text_edited)

my_text_edited = my_text_edited.lower()

print(my_text_edited)

my_text_list = my_text_edited.split(' ')

print(f'\n\n{my_text_list}\n\n')

my_text_list_set = set(my_text_list)

print(f'\n\n{my_text_list_set}\n\n')

my_text_dict = {}

for key in my_text_list_set:
    my_text_dict[key] = my_text.count(key)

print(my_text_dict)