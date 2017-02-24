import json
import pprint
import string
import re
import anagram_score

# The words are stored as a list
json_data = open('json/words.json').read()
words = json.loads(json_data)[0:]
regex = re.compile('[^a-z0-9]')

sorted_words = {}

for word in words:
  clean_word = anagram_score.convert(word)
  # In order to check if it's an anagram it's only necessary to compare to
  # one normalized form NOT every possible permutation
  # Using alphabetical sorted isn't required, but it is the most straightforward
  sorted_word = ''.join(sorted(clean_word))
  # Since we're looking for the most interesting anagrams those have scores > 10
  # The max possible score for a pair of words is the length of that word
  if len(sorted_word) < 8:
    continue
  if sorted_word in sorted_words:
    # Not required, but urban dictionary has an unfortunate habit
    # of calling 2 words separate if they differ by punctuation or capitals
    if anagram_score.convert(sorted_words[sorted_word][0]) == clean_word:
      continue
    sorted_words[sorted_word].append(word)
  else:
    sorted_words[sorted_word] = [word]

count = 0
scored_anagrams = []
for sorted_word in sorted_words:
  out_words = sorted_words[sorted_word]
  if len(out_words) > 1:
    score = anagram_score.score(out_words[0], out_words[1])
    scored_anagrams.append({'score': score, 'words': out_words[0] + ' - ' + out_words[1]})
    count+=1
print count, 'anagrams scored'


scored_anagrams.sort(key = lambda x:x['score'], reverse=True)
for score in scored_anagrams[0:400]:
  print score['score'], score['words']