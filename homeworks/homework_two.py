# Jakub Targalski 131438
# Please submit the result as individual files to teams (not zipped). These should include: the code, the text file and the graphics files (i.e. png) with the appropriate charts and word clouds.

import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 1. open and read file, save all words into a list

my_file = 'sometext.txt'

with open(my_file, 'r') as f:
    text = f.read()
    words = text.split()

special_symbols = [',', '.', '"', '!', '?', '(', ')', '[', ']', ';', ':']

# this takes into consideration the possessive nouns (ending with 's or s')
words_edited = []
for word in words:
    for char in special_symbols:
            word = word.replace(char, '')
    if word[-2:] == "s'":
        word = word
    elif word[0] == "'" or word[-1] == "'":
        word = word.replace("'", '')
    words_edited.append(word)

# 1. a and b

words_set = set(words_edited)

words_dict = {}
for key in words_set:
    if len(key) >= 4 and (key[0].isupper() or key.isupper()):
        words_dict[key] = text.count(key)

# 2. Print a list of those words and the number of their occurrences
# (either print dict or format dict to a list and then print)

dict_as_list = [(key, words_dict[key]) for key in words_dict]
print(dict_as_list)

# 3. Use matplotlib or plotly and generate a bar chart showing the top 10 most common words
# (same conditions 1a) and 1b) apply) with the number of their occurrences in descending order.
# Save this plot to a file and submit it along the code.

sorted_dict_as_list = sorted(dict_as_list, key=lambda x: x[1], reverse=True)

words_bar, values_bar = zip(*sorted_dict_as_list)

plt.bar(words_bar[0:11], values_bar[0:11])

plt.xlabel('Words')
plt.ylabel('Values')
plt.title('Top 10 most common words')

plt.show()

# 4. For an extra 1 point play with packages that generate clouds of words
# and generate one for this set of words (conditions 1a) and 1b)) as well as for the whole text.

# whole text cloud
cloud_text = WordCloud().generate(text)

plt.imshow(cloud_text, interpolation='bilinear')
plt.axis("off")
plt.show()

# set of words with conditions 1a and 1b cloud
filtered_words = [word for word in words if word in words_bar]
filtered_text = ' '.join(filtered_words)
cloud_text2 = WordCloud().generate(filtered_text)

plt.imshow(cloud_text2, interpolation='bilinear')
plt.axis("off")
plt.show()

