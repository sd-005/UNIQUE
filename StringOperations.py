# a) Longest word
def longest_word(s):
    word = ''
    longest = ''
    s += ' '
    for ch in s:
        if ch != ' ':
            word += ch
        else:
            if word != '':
                length = 0
                for _ in word:
                    length += 1
                longest_len = 0
                for _ in longest:
                    longest_len += 1
                if length > longest_len:
                    longest = word
                word = ''
    return longest

# b) Frequency of a character
def char_frequency(s, ch):
    count = 0
    for c in s:
        if c == ch:
            count += 1
    return count

# c) Palindrome check
def is_palindrome(s):
    clean = ''
    for c in s:
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
            if 'A' <= c <= 'Z':
                c = chr(ord(c) + 32)
            clean += c
    reverse = ''
    i = 0
    while i < len(clean):
        reverse = clean[i] + reverse
        i += 1
    return clean == reverse

# d) Index of first appearance of substring
def substring_index(s, sub):
    s_len = 0
    sub_len = 0
    for _ in s:
        s_len += 1
    for _ in sub:
        sub_len += 1
    for i in range(s_len - sub_len + 1):
        match = True
        for j in range(sub_len):
            if s[i + j] != sub[j]:
                match = False
                break
        if match:
            return i
    return -1

# e) Word count
def word_count(s):
    s += ' '
    word = ''
    words = []
    for ch in s:
        if ch != ' ':
            word += ch
        else:
            if word != '':
                words.append(word)
                word = ''
    counts = []
    seen = []
    for w in words:
        if w not in seen:
            count = 0
            for x in words:
                if x == w:
                    count += 1
            counts.append((w, count))
            seen.append(w)
    return counts

# Main
text = input("Enter a string: ")

# a) Longest word
print("\na) Longest word: " + longest_word(text))

# b) Frequency of character
ch = input("Enter a character: ")
print("b) Frequency of character '" + ch + "': " + str(char_frequency(text, ch)))

# c) Palindrome check
if is_palindrome(text):
    print("c) Is palindrome? Yes")
else:
    print("c) Is palindrome? No")

# d) Index of first appearance of substring
sub = input("Enter a substring: ")
index = substring_index(text, sub)
if index != -1:
    print("d) Index of first appearance: " + str(index))
else:
    print("d) Index of first appearance: Not found")

# e) Word occurrences
print("e) Word occurrences:")
counts = word_count(text)
for pair in counts:
    print("   " + pair[0] + ": " + str(pair[1]))
