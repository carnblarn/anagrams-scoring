# Anagrams Scoring
Inspired by: http://blog.plover.com/lang/anagram-scoring.html

### Using
Running `anagram.py` will look into `json/words.json` for a list of words and print out the highest scoring anagrams found in that list.

### How do you match anagrams?
By converting every word to a normalized version sorted by letter alphabetically and storing that in hash map. With that approach even large lists of words, like a million plus, can be matched up relatively quickly.

### How do you score anagrams?
An anagram is deemed to be interesting if it takes a significant amount of rearranging the letters to convert from the first word to the second. There are complex approaches to solve this, like http://cs.stackexchange.com/questions/2259/finding-interesting-anagrams, but this program uses an imperfect, but reasonably accurate substitute. It will chunk up the first word starting at the beginning and see how many chunks are found matching in the second word. This is _not_ guaranteed to produce the right score, and often won't, but it gets close very often. Where it breaks down is when letters are repeated in the first word and there are, as a result, multiple different ways to split it up which can lead to different scores.
