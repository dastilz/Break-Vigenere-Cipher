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

# Source: https://en.wikipedia.org/wiki/Letter_frequency
english_letter_frequency = {
    'a': 8.167,
    'b': 14.492,
    'c': 2.202,
    'd': 4.523,
    'e': 12.702,
    'f': 2.228,
    'g': 2.015,
    'h': 6.094,
    'i': 6.966,
    'j': 0.153,
    'k': 1.292,
    'l': 4.025,
    'm': 2.406,
    'n': 6.749,
    'o': 7.507,
    'p': 1.929,
    'q': 0.095,
    'r': 5.987,
    's': 6.327,
    't': 9.356,
    'u': 2.758,
    'v': 0.978,
    'w': 2.560,
    'x': 0.150,
    'y': 1.994,
    'z': 0.077
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

# Divide raw text into substrings based on key length
split = {}

for i in range(0, key):
    split[i] = ""

for i in range(0, len(raw_text) - key, key):
    for j in range(0, key):
        split[j] += raw_text[i+j]
        

# Use frequency analysis on all substrings
frequencies = []

for i in range(0, key):
    frequencies.append(cipher_letter_frequency.copy())

# Determine letter frequency of ciphertext
for i, substr in split.items():
    for letter in substr:
        frequencies[i][letter] += 1

print(frequencies)

# Sort letter frequencies and map to english frequencies
sorted_cipher_letter_frequencies = []
sorted_english_letter_frequencies = []

for i in range(0, key):
    sorted_cipher_letter_frequencies.append(sorted(frequencies[i], key = frequencies[i].get, reverse=True))

sorted_english_letter_frequencies = sorted(english_letter_frequency, key = english_letter_frequency.get, reverse=True)


# Determine the shift between english and cipher when comparing most common letters for each subgroup
shifts = {}

for i in range(0, len(sorted_cipher_letter_frequencies)):
    shifts[i] = []

for i in range(0, len(sorted_cipher_letter_frequencies)):
    for j in range(0, len(sorted_cipher_letter_frequencies[i])):
        shifts[i].append((english_to_index[sorted_english_letter_frequencies[j]] + english_to_index[sorted_cipher_letter_frequencies[i][j]]) % 26)
