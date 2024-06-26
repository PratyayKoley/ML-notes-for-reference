# Tuple

It is an immutable object _(value cannot be changed)_ and can store multiple values. Tuples allows dupliacte objects.
We cannot append or insert any elements once tuple is created.

- `scholarhat_articles = ("C", "C++", "Python", "Java")`
- `tuple = (1, 2, 3.5, 'Hello', True)`

## Tuple Operations

- all()	- Returns true if all element are true or if tuple is empty

- any() - Return true if any element of the tuple is true. if tuple is empty, return false

- len() - Returns length of the tuple or size of the tuple

- enumerate() - Returns enumerate object of tuple

- max() - Return maximum element of given tuple

- min() - Return minimum element of given tuple

- sum() - Sums up the numbers in the tuple

- sorted() - Input elements in the tuple and return a new   sorted list

- tuple() - Convert an iterable to a tuple.  
`list = [1, 2, 3, 4, 4, 5]`  
`tuple1 = tuple(list)`


- Concatenate - Combines two tuple   
`tuple1 + tuple2`

- Multiply - Multiplies the occurrence of elements in a tuple  
`tuple * 3`