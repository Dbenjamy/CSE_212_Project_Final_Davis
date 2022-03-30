#%%

def word_flip(the_string):
    flipped = ''
    current_word = ''
    for i in range(len(the_string)):
        if the_string[i].isalpha():
            current_word += the_string[i]

        if not the_string[i].isalpha() or i + 1 > len(the_string):
            if current_word != '':
                
        # else:
        #     if current_word != '':
        #         flipped += current_word[-1:]
        #         current_word = ''
        #         current_word += letter
    return flipped

print('flipped: [' + word_flip(' how are YOU!') + ']')





#%%
from random import randint

# Used to encode the message. You will need to use
# it when you decode the message.
key = randint(1,26)
# Only lowercase letters are encoded. This range is
# the decimel representation for those characters.
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
#%%
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