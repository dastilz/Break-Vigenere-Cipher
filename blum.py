# Author: David Stilz
# Language: Python 3.7.7
# Source: https://asecuritysite.com/encryption/blum

import math

p = 1000003
q = 2001911
x = 3
n = 100000
M = p * q

random = ""

for i in range(0, 100000):
    x = x*x % M
    bit = x % 2
    random += str(int(bit))

sum = 0
count = 0

for i in range(0, len(random) - 10000):
    substr = random[i:i+10000]
    sum += substr.count('0')
    count = count + 1

mean = sum / count
print('Average number of 0\'s in sequences of 10000 bits:')
print(mean)
print('\n')

count = 0

for i in range(0, len(random) - 4):
    if(random[i:i+4] == "0000"):
        count += 1

print('0000 occurrences: ')
print(count)
print('\n')

count = 0

for i in range(0, len(random) - 4):
    if(random[i:i+4] == "0001"):
        count += 1

print('0001 occurrences: ')
print(count)
print('\n')

count = 0

for i in range(0, len(random) - 4):
    if(random[i:i+4] == "0010"):
        count += 1

print('0010 occurrences: ')
print(count)
print('\n')

count = 0

for i in range(0, len(random) - 4):
    if(random[i:i+4] == "0011"):
        count += 1

print('0011 occurrences: ')
print(count)
print('\n')

count = 0

for i in range(0, len(random) - 4):
    if(random[i:i+4] == "0100"):
        count += 1

print('0100 occurrences: ')
print(count)
print('\n')

count = 0

for i in range(0, len(random) - 4):
    if(random[i:i+4] == "0101"):
        count += 1

print('0101 occurrences: ')
print(count)
print('\n')

count = 0

for i in range(0, len(random) - 4):
    if(random[i:i+4] == "0110"):
        count += 1

print('0110 occurrences: ')
print(count)
print('\n')

count = 0

for i in range(0, len(random) - 4):
    if(random[i:i+4] == "0111"):
        count += 1

print('0111 occurrences: ')
print(count)
print('\n')

count = 0

for i in range(0, len(random) - 4):
    if(random[i:i+4] == "1000"):
        count += 1

print('1000 occurrences: ')
print(count)
print('\n')

count = 0

for i in range(0, len(random) - 4):
    if(random[i:i+4] == "1001"):
        count += 1

print('1001 occurrences: ')
print(count)
print('\n')

count = 0

for i in range(0, len(random) - 4):
    if(random[i:i+4] == "1010"):
        count += 1

print('1010 occurrences: ')
print(count)
print('\n')

count = 0

for i in range(0, len(random) - 4):
    if(random[i:i+4] == "1011"):
        count += 1

print('1011 occurrences: ')
print(count)
print('\n')

count = 0

for i in range(0, len(random) - 4):
    if(random[i:i+4] == "1100"):
        count += 1

print('1100 occurrences: ')
print(count)
print('\n')

count = 0

for i in range(0, len(random) - 4):
    if(random[i:i+4] == "1101"):
        count += 1

print('1101 occurrences: ')
print(count)
print('\n')

count = 0

for i in range(0, len(random) - 4):
    if(random[i:i+4] == "1110"):
        count += 1

print('1110 occurrences: ')
print(count)
print('\n')

count = 0

for i in range(0, len(random) - 4):
    if(random[i:i+4] == "1111"):
        count += 1

print('1111 occurrences: ')
print(count)
print('\n')
