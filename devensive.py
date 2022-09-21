data = [15, 20, 25]
def normalize(numbers):
    total = sum(numbers)
    result = []

    for value in numbers:
        percent = 100 * value / total
        result.append(percent)

    return result

output = normalize(data)
# print(output)

print(sum(output))


path = '/tmp/my_numbers.txt'
with open(path, 'w') as f:
    for i in [15, 80, 35]:
        f.write(f'{i}\n')

def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

it = read_visits(path)
#print(list(it))
# print(it)

#print(normalize(it))

def normalize2(numbers):
    numbers = list(numbers) # Copy the iterator
    total = sum(numbers)
    result = []

    for value in numbers:
        percent = 100 * value / total
        result.append(percent)

    return result

print(normalize2(it))


def normalize3(get_iter):
    total = sum(get_iter())
    result = []

    for value in get_iter():
        percent = 100 * value / total
        result.append(percent)

    return result


get_iter = lambda: read_visits(path)
print(normalize3(get_iter))



a = [1,2,3]
for x in a:
    pass

def normalize4(numbers):
    total = sum(numbers)
    result = []

    for value in numbers:
        percent = 100 * value / total
        result.append(percent)

    return result


class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)

def normalize5(numbers):
    if iter(numbers) is iter(numbers):
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []

    for value in numbers:
        percent = 100 * value / total
        result.append(percent)

    return result


visits = ReadVisits(path)
print(list(iter(visits)))
print(list(iter(visits)))
print(list(iter(visits)))
print(list(iter(visits)))
print(list(iter(visits)))

print(normalize4(visits))
print(normalize4(visits))
print(normalize4(visits))

it = iter(visits)
it2 = iter(it)
it3 = iter(visits)
print(it, it2, it3)

it4 = iter(visits)
print(normalize5(it))
