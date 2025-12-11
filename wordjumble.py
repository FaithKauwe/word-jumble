#!python3

# READ ME (INSTRUCTIONS): This starter code is for the Word Jumble Challenge.
# You should first commit this file as provided to your repo before editing.
# Then read through the functions below to see how the program is structured.
# Several functions provided are already implemented and work without changes.
# You need to complete 2 functions: solve_one_jumble and solve_final_jumble,
# and you can optionally add more code to the __main__ section at the bottom.
# These places are marked with TODO and YOUR CODE HERE to help you find them.
# There are also several placed marked HINT, but you do not need to use them.

# Try running this code to see its test case output before changing anything.
# Python 3 is required, so run with this command:  python3 wordjumble.py
# While you are implementing your solution in the solve_one_jumble function,
# you can run this code to see if you can solve any of the jumble test cases.
# If your solution works, it should also solve the final jumble in test case 1
# because part of the solve_final_jumble function has been provided for you.
# If you can solve all 4 single word jumbles in all 4 test cases, great work!
# You made significant progress on this challenging computer science problem.
# Be sure to commit your solution to your repo, and take a break to celebrate!
# Then, come back and try to solve the final jumble for the other test cases.

# itertools is a built-in Python module with efficient tools for working with iterables (things you can loop over). It's great for:
# Generating combinations, permutations, products
# Infinite sequences
# Grouping/filtering data
from itertools import combinations


def get_file_lines(filename='/usr/share/dict/words'):
    """Return a list of strings on separate lines in the given text file with
    any leading and trailing whitespace characters removed from each line."""
    # Open given file in a context so it automatically closes when done
    with open(filename) as file:
        # Iterate over each line, remove whitespace and make upper case
        lines = [line.strip().upper() for line in file]
    return lines


# HINT: You may want to sort scrambled letters, so here is a helper function
def sorted_letters(scrambled_letters):
    """Return a string with all the same letters as the given scrambled string
    but with letters sorted in lexicographical (English dictionary) order."""
    # Sort given letters and concatenate them together with no space between
    return ''.join(sorted(scrambled_letters))


def build_sorted_dict(words_list):
    """Build a dictionary of words where the key is the letters of the word sorted alphebetaically
     and the value is a list of english languagewords that have the same sorted letters."""
    sorted_dict = {}
    for word in words_list:
        # use the helper function to sort the letters of the word alphebetically
        key = sorted_letters(word)
        if key in sorted_dict:
            # if the key already exists, add the word to the set
            sorted_dict[key].add(word)
        else:
        # store the value words temporarily in a set (sets exclude duplicates). {word} creates a new set with one element
            sorted_dict[key] = {word}
    for key in sorted_dict:
        # convert all the values from sets of words to lists
        sorted_dict[key] = list(sorted_dict[key])
    return sorted_dict


def solve_one_jumble(letters):
    """Solve a single jumbled word by unscrambling the given letters.
    Parameters:
    - letters: string, the scrambled letters for a single word
    Return value:
    - list of strings, all valid words that the given letters unscramble to
    """
    # Create a list to store all valid words the final letters unscramble to
    # Returned data should be a list of strings (words)
    # Example: solve_one_jumble('ILST') --> ['LIST', 'SILT', 'SLIT']

    # use the sorting helper function to sort the letters of the jumbled word alphebetically
    key = sorted_letters(letters)
    # use the sorted letters as a key to look up the value in the dictionary
    valid_words = anagram_dict.get(key, [])
    # if the key has a match in the dict, return the value of the key, which is a list of words
    if valid_words:
        return valid_words
    else:
        return []



def solve_final_jumble(letters, final_circles):
    """Solve the final jumbled phrase by unscrambling the given letters.
    Parameters:
    - letters: string, the scrambled letters for a single word, A scrambled string like "TUMUTHT"
    - final: list of strings with O (letter "oh") the  that shows
        how the final jumble's letters are arranged into a word or phrase.
    Return value: A pattern like ['OOOO', 'OOO'] telling you the answer is 4 + 3 letters
    - list of tuples, all valid phrases that the given letters unscramble to
    """
    # Check if the number of circles given matches the number of letters given
    num_circles = sum(len(circles) for circles in final_circles)
    # If the numbers do not match, display an error message and return early
    if num_circles != len(letters):
        print('Number of circles does not match number of letters.')
        # Return a valid data type to represent that there are no solutions
        return []

    # Check if the final jumble is just one word, then it's simply one jumble
    num_groups = len(final_circles)
    if num_groups == 1:
        # Solve the final jumble by unscrambling the letters into a single word
        words = solve_one_jumble(letters)
        # Store each word result in a tuple to make it look like a phrase
        return [(word,) for word in words]

    # Otherwise, the circles for the final jumble are a phrase (multiple words)
    # so it requires a more complex approach than unscrambling a single word

    # Calculate the size of each word (letter group) in the final phrase
    # HINT: This could be useful for narrowing down the search for possible
    # words into only words of the lengths expected in the given circles
    group_sizes = [len(circles) for circles in final_circles]

    # Create a list to store valid phrases the final letters unscramble to
    # Returned data should be a list of tuples (phrases) of strings (words)
    # Example: [('FIRST', 'SOLUTION'), ('SECOND', 'SOLUTION')]
    valid_phrases = []
    # seen_phrases is a helper set that deltes duplicates. bc combinations() only returns number combos,
    # the numbers get applied to indices, whose values are letters, which is how wqe generate all possible 4 letter
    # combinations from a 7 letter array. but the number combos returned by combiantions are unique, while the letter combos are not, allowing for duplications
    # which the helper set prevents
    seen_phrases = set()
    
    # the numerical length of the first word in the final phrase, this method only solves for 2 word phrases
    # if >2 words, would need branching logic to handle longer phrases and checks for the length of the whole phrase
    first_size = group_sizes[0]
    # combinations(iterable, r) method from itertools to generate all possible combinations of r items
    # returns a list of tuples
    for indices in combinations(range(len(letters)), first_size):
        
        # use the numeric indices from the tuples to get the actual letters and create a string
        first_letters = ''.join(letters[i] for i in indices)
        
        # remaining_indices is a list of indices that are not in the first word, using list comprhension (shorthand) to build the list
        remaining_indices = [i for i in range(len(letters)) if i not in indices]
        
        # repeat the process of converting the numbers to indices and getting the letter values at those indexes
        second_letters = ''.join(letters[i] for i in remaining_indices)

        # use the sorting helper function to sort the letters of the first and second words alphebetically
        first_key = sorted_letters(first_letters)
        second_key = sorted_letters(second_letters)

        # use the sorted letters as a key to look up the value in the dictionary, returns empty list if key not found
        first_words = anagram_dict.get(first_key, [])
        second_words = anagram_dict.get(second_key, [])

        if first_words and second_words:
            # Loop through every combination of first + second word
            for w1 in first_words:
                for w2 in second_words:
                    phrase = (w1, w2)
                    # use the helper set to prevent duplicates
                    if phrase not in seen_phrases:
                        seen_phrases.add(phrase)
                        valid_phrases.append(phrase)

    return valid_phrases


def solve_word_jumble(letters, circles, final):
    """Solve a word jumble by unscrambling four jumbles, then a final jumble.
    Parameters:
    - letters: list of strings, each is the scrambled letters for a single word
    - circles: list of strings, each marks whether the letter at that position
        in the solved anagram word will be used to solve the final jumble.
        This string contains only two different characters:
        1. O (letter "oh") = the letter is in the final jumble
        2. _ (underscore) = the letter is not in the final jumble
    - final: list of strings in the same format as circles parameter that shows
        how the final jumble's letters are arranged into a word or phrase."""
    # Create a string to collect circled letters for the final jumbled phrase
    # track if there are multiple solutions to the single jumble
    final_letters = ''
    has_multiple_solutions = False
    all_jumble_results = []

    for index in range(len(letters)):
        # Get the scrambled letters and circled blanks for one jumbled word
        scrambled_letters = letters[index]
        circled_blanks = circles[index]

        # Unscramble the letters to solve a single jumbled word
        words = solve_one_jumble(scrambled_letters)

        # Display this jumble's scrambled letters and any results
        print(f'Jumble {index+1}: {scrambled_letters} => ', end='')
        # Check if no solution was found, then skip to the next jumble
        if len(words) == 0:
            print('(no solution)')
            all_jumble_results.append((scrambled_letters, [], circled_blanks))
            continue

        print(f'unscrambled into {len(words)} words: {" or ".join(words)}')
        all_jumble_results.append((scrambled_letters, words, circled_blanks))

        if len(words) > 1:
            has_multiple_solutions = True

        for letter, blank in zip(words[0], circled_blanks):
            if blank == 'O':
                final_letters += letter

    # If no jumbles were solved, then do not attempt to solve the final jumble
    # if multiple solutions for a single jumble are found, display the options for th user to choose from
    if has_multiple_solutions:
        print('\n--- MULTIPLE SOLUTIONS DETECTED ---')
        print('Human choice required. Here are the options with circle positions:\n')
        for i, (scrambled, words, circles_pattern) in enumerate(all_jumble_results):
            if len(words) > 1:
                print(f'Jumble {i+1}: {scrambled}')
                print(f'  Circle pattern: {circles_pattern}')
                for word in words:
                    circled = ''.join(letter for letter, blank in zip(word, circles_pattern) if blank == 'O')
                    print(f'    {word} -> circled letters: {circled}')
                print()
        return

    if len(final_letters) == 0:
        print('Did not solve any jumbles, so could not solve final jumble.')
        return

    # Otherwise, attempt to solve the final jumble using the circled letters
    final_results = solve_final_jumble(final_letters, final)

    # Display the final jumble's scrambled letters and any results
    print(f'Final Jumble: {final_letters} => ', end='')
    # Check if no solution was found, then return early
    if len(final_results) == 0:
        print('(no solution)')
        return
    # Otherwise, display the unscrambled phrases, each on a separate line
    print(f'unscrambled into {len(final_results)} possible phrases:')
    for num, result in enumerate(final_results):
        print(f'    Option {num+1}: {" ".join(result)}')


def test_solve_word_jumble_1():
    print('='*20 + ' WORD JUMBLE TEST CASE 1 ' + '='*20)
    # Cartoon prompt for final jumble:
    # "What her ears felt like at the rock concert: _______."
    letters = ['ACOME', 'FEROC', 'REDDEG', 'YURFIP']
    circles = ['___O_', '__OO_', 'O_O___', 'O__O__']
    final = ['OOOOOOO']  # Final jumble is 1 word with 7 letters
    solve_word_jumble(letters, circles, final)


def test_solve_word_jumble_2():
    print('\n' + '='*20 + ' WORD JUMBLE TEST CASE 2 ' + '='*20)
    # Cartoon prompt for final jumble:
    # "What a dog house is: ____ ___."
    letters = ['TARFD', 'JOBUM', 'TENJUK', 'LETHEM']
    circles = ['____O', '_OO__', '_O___O', 'O____O']
    final = ['OOOO', 'OOO']  # Final jumble is 2 words with 4 and 3 letters
    solve_word_jumble(letters, circles, final)


def test_solve_word_jumble_3():
    print('\n' + '='*20 + ' WORD JUMBLE TEST CASE 3 ' + '='*20)
    # Cartoon prompt for final jumble:
    # "A bad way for a lawyer to learn the justice system: _____ and _____."
    letters = ['LAISA', 'LAURR', 'BUREEK', 'PROUOT']
    circles = ['_OOO_', 'O_O__', 'OO____', '__O_OO']
    final = ['OOOOO', 'OOOOO']  # Final jumble is 2 words with 5 and 5 letters
    solve_word_jumble(letters, circles, final)


def test_solve_word_jumble_4():
    print('\n' + '='*20 + ' WORD JUMBLE TEST CASE 4 ' + '='*20)
    # Cartoon prompt for final jumble:
    # "Farley rolled on the barn floor because of his __-______."
    letters = ['TEFON', 'SOKIK', 'NIUMEM', 'SICONU']
    circles = ['__O_O', 'OO_O_', '____O_', '___OO_']
    final = ['OO', 'OOOOOO']  # Final jumble is 2 words with 2 and 6 letters
    solve_word_jumble(letters, circles, final)


if __name__ == '__main__':
    # Get a list of all words in the built-in English dictionary words file
    words_list = get_file_lines('/usr/share/dict/words')
    # Note that variables defined here are accessible from the global scope,
    # so you can use the words_list variable, but do not try to reassign it.

    # TODO: Create any data structures you may want to help unscramble words
    # HINT: You may want to store the words list in a different data structure
    # that could help you look up candidate words faster than searching a list
    anagram_dict = build_sorted_dict(words_list)

    # Test solving several word jumble example inputs
    # You can comment out these lines to test fewer example inputs at a time
    test_solve_word_jumble_1()
    test_solve_word_jumble_2()
    test_solve_word_jumble_3()
    test_solve_word_jumble_4()