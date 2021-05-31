#
# reverses a sentence
# ask the user for a sentence: a long string containing multiple words
# Return to the user the same string,  with the words in backward order
#   Input - My name is V Tadimeti.
#   Output - Tadimeti V is name My.
#

def reverse( input_str ):

    words = input_str.split(' ')
    reversed_str = ' '.join(reversed(words)) 

    return reversed_str