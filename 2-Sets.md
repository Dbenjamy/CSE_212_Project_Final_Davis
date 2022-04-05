### Sets
- [Home]("0-Welcome.md")
- [Previous - Stacks]("1-Stacks.md")
- [Next - Trees]("3-Trees.md")

#### Setting Sets Apart
Last time we went over Stacks. They are useful when you must work with items in sequential order. In stacks and lists, values are remembered in order. But sometimes when we work with data, we are not worried about the order we look at it. 

When you check for a value in a list, you must search the entire list, which takes **O(n)** time.

**Sets** are unordered. Since we don't know where a value in a set might be, we use another operation to check for values, called **hashing**. Hashing is incredibly efficient. Operations that you can performon a list, such as checking membership or addingremoving values, can be performed on a set in **O(1)** or constant time.

Sets also differ because there can be no duplicate values, unlike lists. Attempting to add a duplicate value to a set in Python will make no changes to the set.

#### How Hashing Works
The reason it takes time to search a list is because we have no way of knowing where our value might be. We must check each value in the list. One way we can get around this is to put items in an index based on the value we want to store. Take the following:
|...  |83 |84 |   |   |87 |   |...|
|---  |---|---|---|---|---|---|---|
|Index|83 |84 |85 |86 |87 |88 |...|

In this array of 100 numbers, the numbers we store go to their corresponding index value. So, if you want to check if the array contains the number 84, we can check the array at ```index[84]```, which is an **O(1)** operation. This type of array does leave empty spots where we are not storing values, though. This type of array is a **sparse list**. 

If you tried to use a sparse list this way, you would run into a problem if you wanted to store larger values, such as 396,086. Using our current method, we would have to make an array of at least ***396,086*** in length to give this number a unique index. For larger values, we can determine their index in a smaller array by using modulo on these values. 

If we want to choose a spot in our 100-length array, we calculate 396,086 % 100, which gives us 86. 
|...    |83   |84   |     |396,086|87   |     |...  |
|:---:  |:---:|:---:|:---:|:---:  |:---:|:---:|:---:|
|Index()|83   |84   |85   |86     |87   |88   |...  |
Now if we want to check if our big number is in our set, we check that ```index[396,086 % 100] == 396,086```.

To store other values like strings, we can turn those into numbers and do similar operations on them. This is where we use hashing. We convert strings, floats, or large numbers into integers using a hash and then use a modulo to determine where that value should be stored. 
#### Conflict Resolution

Since we are using the modulo operation to choose a location, there is a chance that two or more values could be assigned to the same index in a set. Two ways to deal with this conflict are **open addressing** and **chaining**.

**I. Open Addressing**
If we come to an index that already has a value stored, we can store our value in the next open slot. Doing this can help us, but it also takes the spot of another index and can cause more conflicts if we need those positions later.

**II. Chaining**
An alternative is to create a list at the index location if more than one value is assigned to it. Then checking for a value would mean going to the index location and searching the list.

Both methods introduce inefficiencies that we were trying to avoid in the beginning. If we use either method to resolve conflicts, searching for a value can start looking like searching a list. One way we can get around this would be too sparse a new list with more positions. We can do this if we run into too many conflicts.

#### Uses for Sets

The properties of sets make them useful for certain problems. You can quickly search for values. Due to how hashing works, you cannot have duplicate values in a set. But this is helpful because we can quickly compare sets and look for unique values. Many more math operations can be performed on sets as well.

##### Example in Python

In Python, we declare a set like a list but with ```{thing1,thing2,thing3}``` instead of ```[thing1,thing2,thing3]```. If we are declaring an empty set, we do it like ```my_set = set()```. If we tried to declare an empty set in Python like this: ```my_set = {}``` we would create an empty dictionary instead.

Below is an example of how sets can be used. Two roommates are putting together a shopping list. They each make their own list. And when they put it together, they only need to keep what isn't on the other's list.
```python
def assemble_grocery_list(gro_one,gro_two):
    final_grocery_list = set()
    for item in gro_one:
        final_grocery_list.add(item)
    # Since sets cannot have duplicates, this will only add
    # new values.
    for item in gro_two:
        final_grocery_list.add(item)
    return final_grocery_list

first_grocery_list = {'eggs','milk','bread','apples','carrets','beef'}
second_grocery_list = {'milk','butter','cheese','lettuce','tomatos','carrets','onions','cabbage'}

combined_list = assemble_grocery_list(first_grocery_list, second_grocery_list)
print(combined_list)
```
The main body of the function is the two ```for``` loops. When the second loop trys to add elements to the set, values already in ```final_grocery_list``` will not be added again since it is a set.

The code above already has a Python implementation. To combine to sets, you write:
```final_grocery_list = first_grocery_list.union(second_grocery_list)``` or 
```final_grocery_list = first_grocery_list | second_grocery_list```

List of operations you can perform on a set:

1. ```this_set.add(item)``` Add an item to a set.
2. ```this_set.remove(item)``` Removes an item from a set.
3. ```if item in this_set:``` Check if item is in a set.
4. ```len(this_set)``` Get the number of items in a set.

These four operations take **O(1)** time.

##### Try it Yourself
Another opperation you can perform on a set is the intersection opperation. This opperation will make a set only containging items that are in **both** sets. In Python, you write:

```availability = first_schedule.intersection(second_schedule)``` or 
```availability = first_schedule & second_schedule```

Your task is to make a function that will find what time is open on both people's schedules. To do this, you will need to implement the **intersection** function without using ```intersection()``` or ```set1 & set2```.
When you are ready, you can look at a sample solution [here](./code%20examples%20and%20solutions/sets_solution.py) and compare you solution.
You can start with the following code block.
```python
def find_openings(sched1,sched2):
    # Your code goes here
    pass

stacy_schedule = {'9AM','10AM','12PM','1PM','2PM','4PM','5PM'}
markus_schedule = {'7AM','8AM','11PM','2PM','3PM'}

print(find_openings(stacy_schedule,markus_schedule))
```
- [Home]("0-Welcome.md")
- [Previous - Stacks]("1-Stacks.md")
- [Next - Trees]("3-Trees.md")
