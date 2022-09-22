from collections import defaultdict
names = ['Socrates','Achimedes', 'Plato', 'Aristatle']
helper = lambda x : len(x)
names.sort(key=lambda x: len(x))
# names.sort(key=helper)
print(names)


class Sortable(object):
    def get_key(self,x):
        return NotImplementedError


def log_missing():
    print('Key added')
    return 0

d = defaultdict(int)
print(d['foo'])

d = defaultdict(lambda : 100)
print(d['foo'])
print(d['bar'])
d['foo'] = 55
print(d)

f = defaultdict(log_missing)
f['foo'] = 500
print(f['bar'])
print(f)


def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count
        added_count += 1
        return 0

    result = defaultdict(missing, current)

    for key, offset in increments:
        result[key] = offset

    return result, added_count




current = {'green':12, 'blue': 3}
increments = [('red', 5), ('blue', 17), ('orange', 9)]
print(increment_with_report(current, increments))
