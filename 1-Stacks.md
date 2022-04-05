### Stacks
- [Home]("0-Welcome.md")
- [Previous - Big O Notation]("0.5-Big-O-Notation.md")
- [Next - Sets]("2-Sets.md")

#### Stocking a Woodpile
A **stack** is a data structure that is organized by the order in which items or tasks are added or removed.

Let's say you have a wood-burning stove to keep you warm in the winter. During the summer months, you stock up on wood by cutting wood into small logs. You put those on a log pile that is elevated and protected from moisture so it will be dry by the time you need to burn it. Every time you add a log to the stack, we call that a **push** operation.  

To use the logs, it would be a hassle to pull them from the bottom, or the **front** of the stack, so we pull them from the top, or the **back** of the stack. When we remove a log, we call this a **pop**. You cannot get to the logs below the top of the pile until you remove the logs on top.

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
When you call a function, the main program running becomes the front of the stack, and the function called is **pushed** to the stack. 

When the function is executed, it points back to where it is called, and the function is removed from the stack. In this code:
1. **main** calls **mult()** to determine what value to assign to product. While **mult()** is running, **main** is waiting for **mult()** to return a value and cannot move on until it does.
2. **mult()** makes a call to **to_nums()** to format the list of numbers, and now **mult()** and **main** must wait until **to_nums()** is finished.

You cannot finish a line of code until the functions it has called has been executed. The stack can only be worked on from **top** to **bottom**.

The following are common operations you can perform on a stack. Depending on the stack you are working with, some of these operations may be automated (such a the stack in functions). We will use a list as an example.
|Python Code|Explanation|Automated example|
|---|---|---|
|list.append(item)|Adds item to end of list. Takes O(**1**) time.|Function is called, and **pushed** to function stack.
|list.pop()|Removes item from end of list. Takes O(**n**) time.|When a function is finished, it is **popped** off function stack and returns a value.|

#### Example Code
The following code counts how many times each character in a string occurs by using stack opperations.
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
    # Return our character frequency
    return counts

freq = char_frequency('Hello world!')
print(freq) # {'!': 1, 'd': 1, 'l': 3, 'r': 1, 'o': 2, 'w': 1, ' ': 1, 'e': 1, 'H': 1}
```
The following are the opperations you can perform on a stack using a list as an example.
1. ```this_list.append(item)```
Add an item to the end of a stack.
2. ```this_list.pop()```
Removes item from the end of a stack.
4. ```len(this_list)```
Get the number of items in a stack.

#### Try it Yourself
Your task is to implement a function that flips a sentance. ```'this i$ a s3ntance'``` should become ```'ecnatn3s a $i siht'```. When you are done you can look at the [sample solution](./code%20examples%20and%20solutions/stacks_solution.py) and compare your work.


```python
def flipped(the_string):
    # Your code here
    pass

print(f'Flipped: {flipped("this is a sentance")}')
```
- [Home]("0-Welcome.md")
- [Previous - Big O Notation]("0.5-Big-O-Notation.md")
- [Next - Sets]("2-Sets.md")