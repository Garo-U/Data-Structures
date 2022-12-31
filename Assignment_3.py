def longest_word(string):
  words = string.split()
  longest_word = ''
  for word in words:
    if len(word) > len(longest_word):
      longest_word = word
  return longest_word


def character_frequency(string, char):
  count = 0
  for c in string:
    if c == char:
      count += 1
  return count


def is_palindrome(string):
  return string == string[::-1]

def find_substring(string, substring):
  return string.find(substring)


def word_count(string):
  words = string.split()
  word_counts = {}
  for word in words:
    if word in word_counts:
      word_counts[word] += 1
    else:
      word_counts[word] = 1
  return word_counts

string = "The quick brown fox jumps over the lazy dog."

print(longest_word(string))

print(character_frequency(string, "o"))

print(is_palindrome(string))

print(find_substring(string, "fox"))

print(word_count(string))
