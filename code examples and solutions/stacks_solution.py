# This is one way to implement a sentance flipper.
def flipped(the_string):
    # Make the string a list so we can use pop()
    sentence = list(the_string)
    flipped = []
    for i in range(len(sentence)):
        # Use pop() for each character
        flipped.append(sentence.pop())
    # Returning the string after turning it back
    # into a string.
    return ''.join(flipped)

print(f'Flipped: {flipped("this is a sentance")}')