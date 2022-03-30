### Sets

<p style="text-align:left;">
    <a href="1-Stacks.md">Previous - Stacks</a>
    <span style="float:right;">
        <a href="3-Trees.md">Next - Trees</a>
    </span>
</p>

From the last lesson, we went over Stacks. They are useful when you have to work with items in sequential order. In stacks and lists, values are remembered in order. But sometimes when we work with data, we are not worried about the order that we look at it. 
#### Setting Sets Apart
 When you check for a value in a list, you have to search the entire list, which takes $O(n)$ time.
 
 <span style='color:red'>Sets</span> are unordered. Since we don't know where a value in a set might be, we use another operation to check for values, called <span style='color:red'>hashing</span>. Hashing is incredibly efficient. Operations that you can perform on a list, such as checking membership or adding/removing values, can be performed on a set in $O(1)$ or constant time.

Sets also differ because there can be no duplicate values, unlike lists. Attempting to add a duplicate value to a set in Python will make no changes to the set.

#### How Hashing Works
The reason it takes time to search a list is because we have no way of knowing where our value might be. We have to check each value in the list. One way we can get around this is to put items in an index based off of the value we want to store. Take the following:
|...  |83 |84 |   |   |87 |   |...|
|---  |---|---|---|---|---|---|---|
|Index|83 |84 |85 |86 |87 |88 |...|

In this array of 100 numbers, numbers we store go to their corresponding index value. So if you want to check if the array contains the number 84, we can check the array at index[84], which is an $O(1)$ operation. This type of array does leave empty spots where we are not storing values, though. This type of array is a <span style='color:red'>sparse list</span>. 

If you tried to use a sparse list this way, you would run into a problem if you wanted to store larger values, such as 396,086. Using our current method, we would have to make an array of at least 396,086 in legth to give this number a uniqe index. For larger values, we can determine their index in a smaller array by using modulo on these values. If we want to choose a spot in our 100 length array, we calculate 396,086 % 100, which gives us 86. 
|...    |83   |84   |     |396,086|87   |     |...  |
|:---:  |:---:|:---:|:---:|:---:  |:---:|:---:|:---:|
|Index()|83   |84   |85   |86     |87   |88   |...  |
Now if we want to check if our big number is in our set, we check index(396,086 \% 100) $\rightarrow$ index(86).

To store other values like strings, we can turn those into into numbers and do similar operations on them. This is where we use hashing. We convert strings, floats, or large numbers into integers using a hash and then use modulo to determine where that value should be stored. 
#### Conflict Resolution

Since we are using the modulo opperation to choose a location, there is a chance that two or more values could be assigned to the same index in a set. Two ways to deal with this conflict are <span style='color:red'>open addressing</span> and <span style='color:red'>chaining</span>.

<span style='color:blue'>I. Open Addressing</span>
If we come to an index that already has a value stored, we can store our value in the next open slot. Doing this can help us, but it also takes the spot of another index and can cause more conflicts if we need those positions later.

<span style='color:blue'>II. Chaining</span>
An alternative is to create a list at the index location if more than one value is assigned to it. Then checking for a value would mean going to the index location and searching the list.

Both methods introduce inefficiancies that we were trying to avoid in the beginning. If we use either method to resolve conflics, searching for a value can start looking like searching a list. One way we can get around this would be to sparse a new list with more positions. We can do this if we run into too many conflicts.

#### Uses for Sets

The properties of sets make them useful for certain problems. You can quickly search for values. Due to how hashing workes, you cannot have duplicate values in a set. But this is helpful because we are able to quickly compare sets and look for unique values. Many more math operations can be performed on sets as well.

##### Example in Python

In Python we declare a set like a list but with {} instead of []. Below is an example of how sets can be used.
```python

```