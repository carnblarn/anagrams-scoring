import re

regex = re.compile('[^a-z0-9]')

# Stripping the word of spaces/punctuation/caps
def convert(word):
  word = word.lower()
  word = regex.sub('', word)
  return ''.join(word)

# The goal is to rank an anagram based on the number
# of steps to get from the first word to the second
# Scoring is a tricky problem covered elsewhere
# Appears to be NP hard
# This is an imperfect solution that sees how many matching
# chunks exist from the first to the second
# Is not guaranteed to give the right score because
# If letters are repeated there are multiple different ways
# of chunking the first word
# But it does give a reasonable score, quickly
def score(word1, word2):
  word1 = convert(word1)
  word2 = convert(word2)
  i = 0
  chunks = []
  if len(word1) != len(word2):
    return -1
  while i < len(word1) + 1:
    chunk = ''
    for j in range(i+1, len(word1)+1):
      if word1[i:j] not in word2:
        break
      else:
        chunk = word1[i:j]
    if chunk:
      i = i + len(chunk)
      chunks.append(chunk)
    else:
      i = i + 1
  return len(chunks)


