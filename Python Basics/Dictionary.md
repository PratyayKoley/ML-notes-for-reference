# Dictionary

Dictionaries are used to store data values in key:value pairs.
It is an mutable object _(value can be changed)_ and can store multiple values. Dictionary does not allow dupliacte objects.

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
```

## Dictionary Operations

- `clear()` - Removes all elements from the dictionary.
- `copy()` - Returns a shallow copy of the dictionary.
- `fromkeys(iterable, value=None)` - Creates a new dictionary with keys from the given iterable and values set to the specified value.
- `get(key, default=None)` - Returns the value for the specified key if the key is in the dictionary; otherwise, returns the default value.
- `items()` - Returns a view object containing the dictionary's key-value pairs as tuples.
- `keys()` - Returns a view object containing the dictionary's keys.
- `pop(key, default=None)` - Removes the specified key and returns its value. If the key is not found, returns the default value.
- `popitem()` - Removes and returns the last key-value pair inserted into the dictionary.
- `setdefault(key, default=None)` - Returns the value of the specified key. If the key does not exist, inserts the key with the specified default value.
- `update([other])` - Updates the dictionary with the key-value pairs from another dictionary or from an iterable of key-value pairs.
- `values()` - Returns a view object containing the dictionary's values.


## Looping Through a Dictionary in Python

You can loop through a dictionary in several ways to access its keys, values, or key-value pairs.

#### Looping Through Keys

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for key in thisdict:
    print(key)
```

#### Looping Through Values

```python
for value in thisdict.values():
    print(value)
```

#### Looping Through Key-Value Pairs

```python
for key, value in thisdict.items():
    print(key, value)
```

#### Looping Through Keys

```python
for key in thisdict.keys():
    print(key)
```