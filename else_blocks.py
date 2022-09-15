for i in range(3):
    print(f'loop {i}')
    if i == 1:
        break
else:
    print('Else Block')


x = 4
if x > 5:
    print('Greater')
else:
    print('Less')


try:
    raise Exception('Ooh!')
    print('Not reatched')
except:
    print('Caught exception')

try:
    x = 3
except:
    print('Caught exception after try')
else:
    print('Everything was fine')


for i in []:
    print('Never runs')
else:
    print('Else block runs')


while False:
    print('Never Run while False')
else:
    print('Run after while False')


a = 4
b = 9



def coprime(a,b):
    for i in range(2, min(a,b) + 1):
        if a%i == 0 and b%i == 0:
            return False
    return True

def coprime2(a,b):
    is_cprime = True
    for i in range(2, min(a,b) + 1):
        if a%i == 0 and b%i == 0:
            is_cprime = False
            break
    return is_cprime

print(coprime(4,9))
print(coprime(3,6))

try:
    raise Exception('Doh')
finally:
    print('This always runs')



