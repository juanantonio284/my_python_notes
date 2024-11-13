# dictionaries in python

## TLDR: Basic Operations

```Python

# starting dictionary
animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'} 


# 0. looking up characteristics of the dictionary ..................................................

animals.keys() # tells you the keys in the dictionary
# dict_keys(['a', 'b', 'c', 'd'])

animals.values() # tells you the values in the dictionary
#dict_values(['anteater', 'coati', 'donkey'])


# 1. subsetting ....................................................................................

animals['b'] # returns the value associated with the key 'b' ('baboon')

animals['baboon'] # KeyError: 'baboon'
# i.e. a key is expected inside []; 'baboon' is a value, there is no key 'baboon'


# 2. checking ......................................................................................

'baboon' in animals.values() # returns True because the value 'baboon' is in there

'b' in animals.keys() # returns True, there is a key 'b'
'b' in animals # same as above (this is to show that key is the first "layer" accessed)

'baboon' in animals.keys() # returns False, there is no key "baboon"
'baboon' in animals # same as above (again, this is to show that key is the first "layer" accessed)


# 3. changing a value ..............................................................................
animals['b'] = 'boa' # i.e. change baboon to boa
animals['b'] # returns the value in key 'b' (now 'boa')

del animals['b'] # deletes the key,value pair related to key 'b'
animals['b'] # KeyError: 'b' (there is no key 'b')

animals['b'] = 'baboon' # i.e. re-introduce the baboon value to the dictionary
animals['b'] # returns 'baboon'

animals.keys() # returns dict_keys(['a', 'c', 'b']), the order has changed
# after the changes above, 'b' is the last key/value pair inputted


# 4. popping .......................................................................................

# pull out the value and remove many entries from dictionary at once
animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'} # dictionary
entries_to_remove = ["a", "b"] # list (also works with tuple ("a", "b"))
for entry in entries_to_remove:
    animals.pop( entry )
animals # just to show how the dictionary mutated
# https://stackoverflow.com/questions/8995611/removing-multiple-keys-from-a-dictionary-safely

```


<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈***≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
## 1. Introduction

[Dictionary][gloss_link_dict]: an associative array, where arbitrary keys are mapped to values.
The keys can be any object with `__hash__()` and `__eq__()` methods. 

* A dictionary stores `(key,value)` pairs of data

* Dictionaries don't have any particular order other than how the data was inputted


### Dictionary keys and values
<!-- [Slide 23] -->

**values** 

* The values that go into the dictionary could be of any type

  - immutable types, like ints or strings; or mutable types like lists
  
* anything can be used as a value:

  - functions
  - duplicates (i.e. the same value associated with different keys)
  - lists
  - even other dictionaries
  
**keys**

* must be unique 

* immutable type (int, float, string, tuple, bool)

  - actually need an object that is [hashable][gloss_link_hashable] (more on the term later, and
    immutable types are hashable)

  - exercise care when using a *float* type as a key (if the float has an accuracy issue, I may not
    find the value I wanted to associate with that key)
  
**no order to keys or values!**

Example: one key is an int, another key is a tuple, the third key is a string:

`d = { 4:{1:0}, (1,3):"twelve", 'const':[3.14,2.7,8.44] }`


#### Hashable
<!-- pdf 134 -->

An object is hashable if it has:

* a `__hash__` method that maps the object of the type to an int, and the value returned by
  `__hash__` does not change during the lifetime of the object

* an `__eq__` method that is used to compare it for equality to other objects.

In Python, an object of:

* a *scalar immutable type* is hashable
* a *built-in mutable types* is NOT hashable
* a *non-scalar immutable type* (e.g. tuple) is hashable if all of its elements are hashable 

————————————

Another definition:

An object is hashable if it has a hash value which never changes during its lifetime and can be
compared to other objects. Hashable objects which compare equal must have the same hash value.
Hashability makes an object usable as a dictionary key and a set member, because these data
structures use the hash value internally.


<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
### List vs Dictionary
<!-- [Slide 24] -->

**List**

* ordered sequence of elements
* look up elements by an integer index
* indices have an order
* index is an integer

**Dictionary**

* matches "keys" to "values"
* look up one item by another item
* no order is guaranteed
* key can be any immutable type


<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈***≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
## 2. Deeper into theory

### Clarification

<!-- https://realpython.com/iterate-through-dictionary-python/#getting-started-with-python-dictionaries -->

Before Python 3.6, dictionaries were unordered data structures. This means that the order of items typically wouldn’t match the insertion order:

```Python

# Python 3.5
likes = {"color": "blue", "fruit": "apple", "pet": "dog"}

likes
# {'color': 'blue', 'pet': 'dog', 'fruit': 'apple'}

```

Note how the order of items in the resulting dictionary doesn’t match the order in which you originally inserted the items.

In Python 3.6 and greater, the keys and values of a dictionary retain the same order in which you insert them into the underlying dictionary. From 3.6 onward, dictionaries are compact ordered data structures:

```Python

# Python 3.6
likes = {"color": "blue", "fruit": "apple", "pet": "dog"}

likes
# {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

```

Keeping the items in order is a pretty useful feature. However, if you work with code that supports older Python versions, then you must not rely on this feature, because it can generate buggy behaviors.

<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
### Traversing a Dictionary Directly

<!-- https://realpython.com/iterate-through-dictionary-python/#traversing-a-dictionary-directly -->

 .__iter__() is a method that Python automatically calls when you require an iterator for a container data type. This method should return a new iterator object, which allows you to iterate through all the items in the underlying container type.

For Python dictionaries, .__iter__() allows direct iteration over the keys by default. This means that if you use a dictionary directly in a for loop, Python will automatically call .__iter__() on that dictionary, and you’ll get an iterator that goes over its keys:

```Python

likes = {"color": "blue", "fruit": "apple", "pet": "dog"}

for key in likes:
    print(key)
# color
# fruit
# pet

```

This is the primary way to iterate through a dictionary in Python. You just need to put the dictionary directly into a for loop, and you’re done!

If you use this approach along with the [key] operator, then you can access the values of your dictionary while you loop through the keys:


```Python

for key in likes:
    print(key, "->", likes[key])
...
color -> blue
fruit -> apple
pet -> dog

```

In this example, you use key and likes[key] at the same time to access your target dictionary’s keys and the values, respectively. This technique enables you to perform different operations on both the keys and the values of likes.

<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
### Looping Over Dictionary Items: The `.items()` Method

<!-- https://realpython.com/iterate-through-dictionary-python/#looping-over-dictionary-items-the-items-method -->

 The .items() method allows you to iterate over both the keys and values at the same time.
 
 The method returns a [view object][gloss_view_object] containing the dictionary’s items as
 key-value tuples:

```Python

likes = {"color": "blue", "fruit": "apple", "pet": "dog"}

likes.items()
dict_items( [('color', 'blue'), ('fruit', 'apple'), ('pet', 'dog')] )

```

Dictionary view objects provide a dynamic view of the dictionary’s items. Here, dynamic means that when the dictionary changes, the views reflect those changes.

Views are iterable, so you can iterate through the items of a dictionary using the view object that results from calling .items(), as you can see in the example below. (Note that they’re tuple objects)

```Python

for item in likes.items():
    print(item)
    print(type(item))
...
('color', 'blue')
<class 'tuple'>
('fruit', 'apple')
<class 'tuple'>
('pet', 'dog')
<class 'tuple'>

```

To achieve parallel iteration through keys and values, you just need to unpack the elements of every item into two different variables, one for the key and another for the value:

```Python

for key, value in likes.items():
    print(key, "->", value)
...
color -> blue
fruit -> apple
pet -> dog


```

The key and value variables in the header of your for loop do the unpacking. Every time the loop runs, key gets a reference to the current key, and value gets a reference to the value. This way, you have more control over the dictionary content. Therefore, you’ll be able to process the keys and values separately in a readable and Pythonic manner.

<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
### Sorting a Dictionary With a Comprehension

What if you need to sort an existing dictionary and build a sorted one? As you already know, since Python 3.6, dictionaries remember the insertion order of their items. This feature allows you to sort the items of a dictionary using sorted() while you build a new dictionary with a comprehension:

```Python

old_dictionary = { "c": 2, "a": 2, "b": 2 } # not sorted ascending or descending

sorted_dict = { key: old_dictionary[key] for key in sorted( old_dictionary ) }
rev_sorted_dict = { key: old_dictionary[key] for key in sorted( old_dictionary, reverse=True ) }
# {key mapped to value for key in the sorted old dictionary}
# note that the sorting is done by the key (alphabetically)

print( old_dictionary )
print( sorted_dict )
print( rev_sorted_dict )

# ..................................................................................................

cows = { 'Maggie': 3, 'Herman': 7, 'Betsy': 9, 'Oreo': 6, 
         'Moo Moo': 3, 'Milkshake': 2, 'Millie': 5, 'Lola': 2, 
         'Florence': 2, 'Henrietta': 9 }

cows2 = {
    cow_name: cows[cow_name] for cow_name in sorted(cows, key=cows.__getitem__, reverse=True)
}
# cows2 is created to avoid mutation of the original cows dictionary
# cows2 is not sorted by the dictionary's key, which is the default way and is alphabetical;
# it is sorted by value (this is why key=cows.__getitem__ is needed)
# it is sorted with the largest value first (reverse=TRUE) to help the greedy algorithm

```


```Python

old_dictionary = { "c": 3, "a": 1, "b": 2 } # not sorted ascending or descending
sorted_dict = { key: old_dictionary[key] for key in sorted( old_dictionary ) }
rev_sorted_dict = { key: old_dictionary[key] for key in sorted( old_dictionary, reverse=True ) }
# {key mapped to value for key in the sorted old dictionary}
print( old_dictionary )
print( sorted_dict )
print( rev_sorted_dict )

```

```Python

# example from website ...........................
incomes = {"apple": 5600.00, "orange": 3500.00, "banana": 5000.00}

# {key (named fruit) mapped to incomes[name_of_key] for name_of_key in sorted (incomes)}
{fruit: incomes[fruit] for fruit in sorted(incomes)}
# {'apple': 5600.0, 'banana': 5000.0, 'orange': 3500.0}

{
     fruit: income
     for fruit, income in
     sorted(incomes.items(), key=lambda item: item[1])
}
# {'orange': 3500.0, 'banana': 5000.0, 'apple': 5600.0}

```

These comprehensions allow you to create new dictionaries with their items sorted by key and value, respectively. In both cases, the comprehension iterates over the original dictionary in sorted order and builds a new dictionary.


<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
### Iterating Through a Dictionary in Reverse-Sorted Order

<!-- note this says "iterating", the previous section was about sorting -->

If you need to traverse your dictionaries in reverse-sorted order, then you can use the reverse argument to sorted(). This argument takes a Boolean value. If you use True, then the items are sorted in reverse order:

https://docs.python.org/3/howto/sorting.html#sortinghowto

```Python

incomes = {"apple": 5600.00, "orange": 3500.00, "banana": 5000.00}

for fruit in sorted(incomes, reverse=True):
    print(fruit, "->", incomes[fruit])
# ...
# orange -> 3500.0
# banana -> 5000.0
# apple -> 5600.0

```



In this example, you iterate over the keys of incomes in reverse-sorted order by using the reverse argument to sorted() in the header of your for loop. This example sorts the keys. Why don’t you try writing an example that sorts the values in reverse order?


<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
### Iterating Over a Dictionary Destructively With `.popitem()`

<!-- https://realpython.com/iterate-through-dictionary-python/#iterating-over-a-dictionary-destructively-with-popitem -->

Sometimes you need to iterate through a dictionary and delete its items after use. To accomplish
this task, you can use the `.popitem()` method, which removes and returns key-value pairs from a
dictionary in last-in, first-out (LIFO) order. When the target dictionary is empty, `.popitem()` 
raises a KeyError exception.

Here, you used a while loop instead of a for loop. The reason for this is that it’s not safe to
iterate through a dictionary with a for loop when you need to remove items from the dictionary at
hand. 

<!-- You continue this until the dictionary becomes empty, and .popitem() raises the KeyError exception. -->


```Python

likes = {"color": "blue", "fruit": "apple", "pet": "dog"}

while True:
    
    try:
        print( f"Dictionary length: {len(likes)}" )
        item = likes.popitem()
        # Do something with the item here...
        print( f"Item {item} removed" )
    
    except KeyError:
        print("Your dictionary is now empty.")
        break

# Dictionary length: 3
# Item ('pet', 'dog') removed
# Dictionary length: 2
# Item ('fruit', 'apple') removed
# Dictionary length: 1
# Item ('color', 'blue') removed
# Dictionary length: 0
# Your dictionary is now empty.

```



```Python


```


```Python


```



```Python


```





[gloss_link_dictionary]: https://docs.python.org/3/glossary.html#term-dictionary
[gloss_link_hashable]: https://docs.python.org/3/glossary.html#term-hashable
[gloss_view_object]: https://docs.python.org/3/library/stdtypes.html#dict-views

<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈***≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
## extra: dir function

https://realpython.com/python-scope-legb-rule/#dir

dir()

You can use dir() without arguments to get the list of names in the current Python scope. If you call dir() with an argument, then the function attempts to return a list of valid attributes for that object:

```Python

dir()  # With no arguments
['__annotations__', '__builtins__',..., '__package__', '__spec__']
dir(zip)  # With a function object
['__class__', '__delattr__',..., '__str__', '__subclasshook__']
import sys
dir(sys)  # With a module object
['__displayhook__', '__doc__',..., 'version_info', 'warnoptions']
var = 100
dir(var)  # With an integer variable
['__abs__', '__add__',..., 'imag', 'numerator', 'real', 'to_bytes']

```

If you call dir() with no arguments, then you get a list containing the names that live in the global scope. You can also use dir() to inspect the list of names or attributes of different objects. This includes functions, modules, variables, and so on.

Even though the official documentation says that dir() is intended for interactive use, you can use the function to provide a comprehensive list of attributes of a given object. Note that you can also call dir() from inside a function. In this case, you’ll get the list of names defined in the function scope:

```Python

def func():
    var = 100
    print(dir())
    another = 200  # Is defined after calling dir()
...
func()
['var']

```

In this example, you use dir() inside func(). When you call the function, you get a list containing the names that you define in the local scope. It’s worth noting that in this case, dir() only shows the names you declared before the function call.

https://docs.python.org/3/library/functions.html#dir



## Extra

https://docs.python.org/3/glossary.html#term-dictionary-comprehension

A compact way to process all or part of the elements in an iterable and return a dictionary with the `results.results = {n: n ** 2 for n in range(10)}` generates a dictionary containing key n mapped to value `n ** 2`. See Displays for lists, sets and dictionaries.
