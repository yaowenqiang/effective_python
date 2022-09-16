import json


UNDEFINED = object()

def load_json_key(data, key):
    try:
        result_dict = json.loads(data)
    except ValueError as e:
        raise KeyError from e
    else:
        return result_dict[key]



def divide_json(path):
    handle = open(path, 'r+')
    try:
        data = handle.read()
        op = json.loads(data)
        value = op['numerator'] / op['denominator']
    except ZeroDivisionError:
        return UNDEFINED
    else:
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result)
        return value
    finally:
        handle.close()


temp_path = '/tmp/random_data.json'

with open(temp_path, 'w') as handle:
    handle.write('{"numerator": 1, "denominator": 0}')


print(divide_json(temp_path) is UNDEFINED)


try:
    load_json_key('{"foo":"bad payload"', 'foo')
    assert False
except KeyError:
    print('Saw KeyError')

handle = open('/tmp/random_data.txt', 'w', encoding='utf-8')
handle.write('success\nand\nnew\nlines')
handle.close()

handle = open('/tmp/random_data.txt', 'w', encoding='utf-8')
try:
    data = handle.read()
finally:
    handle.close()

print(data)

