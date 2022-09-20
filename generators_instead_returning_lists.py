def _index_words(text):
    result = []
    if text:
        result.append(0)

    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)

    return result


def __index_words(text):
    if text:
        yield 0

    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


def index_words(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset





#address = """Four score and seven years
#ago our fathers brought forth on this
#continent a new nation, conceived in liberty,
#and dedicated to the proposition that all men
#are created equal."""

#print(result)
#print(next(result))
#result =  index_words(address_lines)

address_lines = """Four score and seven years
ago our fathers brought forth on this
continent a new nation, conceived in liberty,
and dedicated to the proposition that all men
are created equal."""
with open('/tmp/address.txt', 'w') as f:
    f.write(address_lines)


with open('/tmp/address.txt') as f:
    it = index_words(f)
    print(next(it))
    print(next(it))
    print(list(it))

