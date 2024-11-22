# The program has a line `string`.
# Print the all words, containing the letter 'o' (in any case (upper/lower)) twice, as a title.

string = "This tool is cool. But that owl is awful. MAGIC TOOLS Ltd."

list_words = string.split(' ')

result = []

for word in list_words:
    if word.find('oo') != -1  or word.find('OO') != -1:
        result.append(word)
formatted_result = " ".join(word.capitalize() for word in result)
print('Result: ' + formatted_result)



