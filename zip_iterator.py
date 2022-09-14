# from itertools import izip

# from itertools import izip_longest python 2
from itertools import zip_longest

names = ['Cellia', 'Lise', 'Marie']
letters = [len(n) for n in names]

names.append('Rosalind')

longest_name = None
max_letters = 0

for i in range(len(letters)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count

print(max_letters)
print(longest_name)


print(list(zip(names, letters)))
# print(izip(names, letters)) python 2

for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count

print(max_letters)
print(longest_name)

for name, count in zip_longest(names, letters):
    if count is None:
        print(f'{name} has unknown length')
    else:
        print(f'{name} has {count} letters')
