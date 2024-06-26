# Set

It is an immutable object _(value cannot be changed)_ and can store multiple values. Sets does not allow dupliacte objects.
Vut we can append or insert or delete any elements once set is created.

- `thisset = {"apple", "banana", "cherry", "apple"}`  
Output :   
`{'banana', 'cherry', 'apple'}`
- `myset = {"apple", "banana", "cherry"}`

## Set Operations

### Set Methods and Operations in Python

- add() - Adds an element to the set.
- clear() - Removes all the elements from the set.
- copy() - Returns a copy of the set.
- difference() (`-`) - Returns a set containing the difference between two or more sets.
- difference_update() (`-=`) - Removes the items in this set that are also included in another, specified set.
- discard() - Removes the specified item.
- intersection() (`&`) - Returns a set that is the intersection of two other sets.
- intersection_update() (`&=`) - Removes the items in this set that are not present in other, specified set(s).
- isdisjoint() - Returns whether two sets have an intersection or not.
- issubset() (`<=`) - Returns whether another set contains this set or not.
  - `<` - Returns whether all items in this set are present in another, specified set.
- issuperset() (`>=`) - Returns whether this set contains another set or not.
  - `>` - Returns whether all items in another, specified set are present in this set.
- pop() - Removes an element from the set.
- remove() - Removes the specified element.
- symmetric_difference() (`^`) - Returns a set with the symmetric differences of two sets.
- symmetric_difference_update() (`^=`) - Inserts the symmetric differences from this set and another.
- union() (`|`) - Returns a set containing the union of sets.
- update() (`|=`) - Updates the set with the union of this set and others.
