# Author: David Stilz
# Language: Python 3.7.7
import math

english_to_index = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'm': 12,
    'n': 13,
    'o': 14,
    'p': 15,
    'q': 16,
    'r': 17,
    's': 18,
    't': 19,
    'u': 20,
    'v': 21,
    'w': 22,
    'x': 23,
    'y': 24,
    'z': 25
}

# Source: book
english_letter_frequency = {
    'a': 0.082,
    'b': 0.015,
    'c': 0.028,
    'd': 0.043,
    'e': 0.127,
    'f': 0.022,
    'g': 0.020,
    'h': 0.061,
    'i': 0.070,
    'j': 0.002,
    'k': 0.008,
    'l': 0.040,
    'm': 0.024,
    'n': 0.067,
    'o': 0.075,
    'p': 0.019,
    'q': 0.001,
    'r': 0.060,
    's': 0.063,
    't': 0.091,
    'u': 0.028,
    'v': 0.010,
    'w': 0.023,
    'x': 0.001,
    'y': 0.020,
    'z': 0.001
}

cipher_letter_frequency = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0,
    'i': 0,
    'j': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'o': 0,
    'p': 0,
    'q': 0,
    'r': 0,
    's': 0,
    't': 0,
    'u': 0,
    'v': 0,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0
}

raw_text = 'hdsfgvmkoowafweetcmfthskucaqbilgjofmaqlgspvatvxqbiryscpcfrmvswrvnqlszdmgaoqsakmlupsqforvtwvdfcjzvgsoaoqsacjkbrsevbelvbksarlscdcaarmnvrysywxqgvellcyluwwveoafgclazowafojdlhssfiksepsoywxafowlbfcsocylngqsyzxgjbmlvgrggokgfgmhlmejabsjvgmlnrvqzcrggcrghgeupcyfgtydycjkhqluhgxgzovqswpdvbwsffsenbxapasgazmyuhgsfhmftayjxmwznrsofrsoaopgauaaarmftqsmahvqecevvhasfbxluoxznfhongml'
ALPHABET_LETTERS = 26

matches = []

# Shift ciphertext by 1 and compare with original ciphertext looking for matches, loop repetitively and record match count for each shift
# Only do for a subset (in this case, fourth) as this will be enough to find a pattern
for i in range(1, int(len(raw_text))):
    numMatches = 0
    for j in range(0, len(raw_text) - i):
        if (raw_text[j] == raw_text[j+i]):
            numMatches += 1

    matches.append([i, numMatches])

# Determine mean and standard deviation on match occurences, then determine an adequate upper bound (mean + stdDev) to find outliers
count = 0
sum = 0
for i, match in matches:
    sum += match
    count += 1

mean = sum / count

sum = 0
for i, match in matches:
    sum += math.pow(match - mean, 2)

# Determine standard deviation
stdDev = math.sqrt(sum / count)

# Determine upper bound
upperBound = mean + stdDev

outlierMatches = []

# Find all matches that are above upper bound aka outliers
for i, match in matches:
    if match > upperBound:
        outlierMatches.append([i, match])

# Determine distances between each shift among outliers and each distances number of occurences
distances = {}

for i in range(0, len(outlierMatches) - 1):
    distance = abs(outlierMatches[i][0] - outlierMatches[i+1][0])
    if distance in distances.keys():
        distances[distance] += 1
    else:
        distances[distance] = 1

# Guess the key by getting the most common distance
key = max(distances, key=distances.get)

print('The key length is: ')
print(key)
print('\n')

# Divide raw text into substrings based on key length
split = {}

for i in range(0, key):
    split[i] = ""

for i in range(0, len(raw_text) - key, key):
    for j in range(0, key):
        split[j] += raw_text[i+j]

# I made a function at this point to avoid horribly complicated nested maps
def solveCaesar(cipher):
    frequencies = []

    for i in range(0, ALPHABET_LETTERS):
        frequencies.append(cipher_letter_frequency.copy())

    for i in range(0, ALPHABET_LETTERS):
        shifted = ""
        for j in range(0, len(cipher)):
            shifted += chr((ord(cipher[j]) + i - 97) % 26 + 97)

        # Determine letter frequency 
        for letter in shifted:
            frequencies[i][letter] += 1
        
    for i in range(len(frequencies)):
        for letter, amount in frequencies[i].items():
            frequencies[i][letter] = amount / len(cipher)

    # Determine max english vector DOT cipher vector and record index (this should be the key)
    sums = {}
    maxSum = -999
    maxSum_i = 0

    for i in range(len(frequencies)):
        sum = 0
        for letter, amount in frequencies[i].items():
            # Dot product
            sum += frequencies[i][letter] * english_letter_frequency[letter]
        
        sums[i] = sum    
        if (sum > maxSum):
            maxSum = sum
            maxSum_i = i
    
    return maxSum_i

print('The key is: ')

for i in range(0, len(split)):
    print(solveCaesar(split[i]))