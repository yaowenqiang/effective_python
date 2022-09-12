x = b'mongoose'
y = x[::-1]
print(y)


a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(a[::-2])
print(a[2::2])
print(a[-2::-2])
print(a[-2:2:-2])
print(a[2:2:-2])

b = a[::2]
c = b[1:-1]
print(a)
print(b)
print(c)
