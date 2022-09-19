import random

with open('/tmp/my_file.txt', 'w') as f:
    for _ in range(10):
        f.write('a' * random.randint(0, 100))
        f.write('\n')

#value = [len(x) for x in open('/tmp/my_file.txt')]
value = (len(x) for x in open('/tmp/my_file.txt'))
print(value)
print(next(value))


root = ((x, x** 0.5 ) for x in value)

print(root)
print(next(root))

