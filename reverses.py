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


print("Enter a sentence and this program will reverses this sentence")
val = input("Enter a sentence: ")
val = reverse(val)
print(val)