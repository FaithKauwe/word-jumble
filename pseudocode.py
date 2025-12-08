# given 4 scrambled words, unscramble each word one at a time, given a standard english lang dictinary
# compare the scrambled_word to each dictionary_candidate, if they match, save dict word as a match to be returned to user
# if not a match, continue loop. loop will proceed until all matches are cleared
# to compare scrambled_word to dictionary_candidate, can compare 2 possible ways
# method 1: compare the frequency of each letter in the scrambled_word to the frequency of each letter in the dictionary_candidate
# if the frequwncies match, the word is an anagram
# method 2: sort the letters alphabetically with a helper function, if the sorted versions match, they are anagrams
# can pre-sort the dictionary_candidates to make this faster and try to shrink the pool of available candidates

# next question in cursor chat: but how will it know to look up ILST key? if I give the presorted structure TILS as a key, how does it look up all anagrams for that word?