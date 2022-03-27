### Stacks
<p style="text-align:left;">
    <a href="0.5-Big-O-Notation.md">Previous - Big O Notation</a>
    <span style="float:right;">
        <a href="2-Sets.md">Next - Sets</a>
    </span>
</p>

#### Stocking a Woodpile
A <span style='color:red'>stack</span> is a data structure that is organized by the order which items or taskes are added or removed.

Let's say you have a woodburning stove to keep you warm in the winter. During the summer months you stock up on wood by cutting wood into small logs. You put those on a log pile that is elevated and protected from moisture so it will be dry by the time you need to burn it. Every time you add a log to the stack, we call that a <span style='color:red'>push</span> operation.  

To use the logs, it would be a hassle to pull them from the bottom, or the <span style='color:red'>front</span> of the stack, so we pull them from the top, or the <span style='color:red'>back</span> of the stack. When we remove a log, we call this a <span style='color:red'>pop</span>. You cannot get to the logs below the top of the pile until you remove the logs on top.

#### Function Calls
When you work with functions in Python or other programming languages, you are using stacks. 
Consider the following code:
```python
# Turning string into numbers
def to_nums(num_string):
    num_string_list = num_string.split()
    nums = []
    for letter in num_string_list:
        nums.append(float(letter))
    return nums        

# Returns product of numbers in a string
def mult(num_string):
    nums = to_nums(num_string)
    product = 1
    for num in nums:
        product *= num
    return product

product = mult('1 6.4 34 9 20.7 71')
print(product)
```
When you call a function, the main program running becomes the front of the stack, and the function called is <span style='color:red'>pushed</span> to the stack. 

When the function is executed, it points back to where it is called and the function is removed from the stack. In this code, **main** call ***mult()*** to determine what value to assign to product. While ***mult()*** is running, **main** is waiting for ***mult()*** to return a value and cannot move on until it does. ***mult()*** makes a call to ***to_nums()*** to format the list of numbers, and now ****mult()**** and **main** have to wait until ***to_nums()*** is finished.

You cannot finish a line of code until the functions it has called have been executed. The stack can only be worked on from <span style='color:red'>top</span> to <span style='color:red'>bottom</span>.

#### Example Code
The following code counts how many times each character in a string occurs.
```python
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
print(freq) # {'!': 1, 'd': 1, 'l': 3, 'r': 1, 'o': 2, 'w': 1, ' ': 1, 'e': 1, 'H': 1}
```
#### Try it Yourself
Below is a simple function to encode a string message. Your goal is to make the decoding function. Try your best, and when you're done, look at the provided sample solution and compare your work.
You are to assume that all letters in the message will be lowercase. Numbers, spaces, and symbols are not changed.

```python
# Used to generate the encode/decode key.
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

```






