'''There is a text file. Print the longest line in file.
If there's several lines of maximum length, print the last one.
Do not use built-in max, sorted functions and file read/readlines method.'''

with open('text.txt', 'w', encoding="utf-8") as file:
    lst = file.writelines(['ffdfdfdfdrferfrefrtfrtfrfrtfrfrtfrfrfrf','Looonoooooooooog','\nsmall','\nmediumm','\nLooonoooooooooog','\ngfhfhgfjghfgfjhgfjhgfjhgfjhgfgf'])

with open('text.txt', 'r', encoding="utf-8") as file:
    str_list = []
    for i in file:
        if i.endswith('\n'):
            i = i[:-1]
            str_list.append(i)
        else:
            str_list.append(i)
        longest_line = ''
        for line in str_list:
            if len(line) > len(longest_line):
                longest_line = line
    print(longest_line)
