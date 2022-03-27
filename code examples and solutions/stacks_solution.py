# Alternative sample
def char_frequency(the_string):
    # Turning the string into a list so we can use
    # stack operations
    char_list = list(the_string)
    # This will hold the counts
    counts = dict()
    for i in range(len(the_string)):
        # Removing the last item from the list
        char = char_list.pop()
        # Check if we have it: increment if we do,
        # create a new entry if we do not.
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    # Return our charactor frequency
    return counts

freq = char_frequency('Hello world!')
print(freq)
#%%
from random import randint


key = randint(1,26)

char_range = list(range(97,123))

def encoder(message):
    encoded_string = ''
    for char in message:
        # Check that it is a letter
        if char.isalpha():
            # Get the decimal representation and
            # add key to change it.
            char_num =  ord(char.lower()) + key
            if char_num not in char_range:
                char_num = char_num - 26
            # Turn char_num into encoded letter and
            # add it to the encoded string.
            encoded_string += chr(char_num)
        else:
            # We are not encoding any other symbol.
            encoded_string += char
    return encoded_string
