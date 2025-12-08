# given 4 scrambled words, unscramble each word one at a time, given a standard english lang dictinary
# compare the scrambled_word to each dictionary_candidate, if they match, save dict word as a match to be returned to user
# if not a match, continue loop. loop will proceed until all matches are cleared
# to compare scrambled_word to dictionary_candidate, can compare 2 possible ways
# method 1: compare the frequency of each letter in the scrambled_word to the frequency of each letter in the dictionary_candidate
# if the frequwncies match, the word is an anagram
# method 2: sort the letters alphabetically with a helper function, if the sorted versions match, they are anagrams
# can pre-sort the dictionary_candidates to make this faster and try to shrink the pool of available candidates

#Final PLan
# preprocess the word file to create a dictionary of words and their sorted letters
# for each item in the word file, sort the letters alphebetically and use the sorted letters as the key,
# check if this key already exists, if so, just add the original word to the value list for that key
# if not, add the key and add the original word as the value for the key
# this creates a dictionary of words and their sorted letters, when given the jumbled word, I will sort it alphebetically as well. if it has any real word matches,
# then it will be a key in the dict. Otherwise, I will return the letters as there is no known word to match