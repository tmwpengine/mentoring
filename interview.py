'''
Uniqueness of words in a sentence!

Description: Given a sentence as a string, determine if all the words in the sentence are unique

Example
“the quick brown fox jumps over the lazy dog” -> False (“the” is repeated)
“My clever monkey jumps slowly under nine planets” -> True

Follow up examples to expand the question

“The quick brown fox jumps over the lazy dog” -> False (case insensitivity)
“Water, Water! Everywhere! But not a drop to drink” -> False (dealing with punctuation)
“I have too many extra  spaces in   this sentence” -> True (but the empty string comes up multiple times on naive splitting)
“One two three twenty-one twenty-two twenty-three” -> Up to the examiner (prompts the candidate for how to handle hyphenation)
A million random numbers represented in decimal separated by spaces … a billion? (scaling)

'''

import re


def is_unique_regex(s):
    # Match any word (including dashes) bounded by a word boundary
    # words = re.findall(r"(\b[\w-]+\b)", string)
    map = {}

    for word in s:
        lower_case_word = word.lower()
        if lower_case_word in map:
            return False
        map[lower_case_word] = 1

    return True


def is_unique(s):
    s = s.lower()

    word_list = [''.join([i for i in word if i.isalpha()]) for word in s.split()]
    removed_dupe_list = set(word_list)

    if len(word_list) == len(list(removed_dupe_list)):
        return True

    return False

s = is_unique("twenty-one twenty-two")
print(s)
