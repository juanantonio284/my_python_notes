# `for` loops in Python

The purpose of this document is to give some simple examples of `for` loops and show some of their
characteristics in Python. This will hopefully serve to contrast with how `for` loops behave in
other languages.

## 1

```Python

# basic for loop with numbers
passes = 3 # an integer argument to the range function below
    
for i in range(passes):
    print("---------")
    print("i:", i)
    print("loop pass:", i + 1)

```

```

---------
i: 0
loop pass: 1
---------
i: 1
loop pass: 2
---------
i: 2
loop pass: 3

```

This shows that the loop iterates over the sequence `0, 1, ...`. The [`range` *constructor*][range] 
is a function used for loops, specifically, and it creates a range *object* (or range *type*):

The advantage of the range *type* over a regular list or tuple is that a range object will always
take the same small amount of memory, no matter the size of the range it represents (as it only
stores the `start`, `stop`, and `step` values and calculates individual items and subranges as
needed).

Function syntax: 

* `range(stop)`
* `range(start, stop[, step])`

If the start argument is omitted, it defaults to 0.  
If the step argument is omitted, it defaults to 1.

<!-- should this be compared to R where you would do something like "for seq(1,3)"? -->


```Python

# decreasing counter
for i in range(3, 0, -1):
    print("i:", i)
# you must specify a negative step, e.g -1 something like range(3,0) would not work

```

```

i: 3
i: 2
i: 1

```

Note that this ends at 1, while the positive example before started at 0. This is because

* For a positive step, the contents of a range r are determined by the formula 
  `r[i] = start + step*i` where `i >= 0` and `r[i] < stop`.

* For a negative step, the contents of the range are still determined by the formula 
  `r[i] = start + step*i`, but the constraints are `i >= 0` and `r[i] > stop`.


<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈***≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
## 2

```Python

# basic for loop with letters
letters = "abc"
loop_pass = 1 # since, in this case, "i" is a letter we need a separate integer to count
    
for i in letters:
    print("---------")
    print("i:", i)
    print("loop pass:", loop_pass)
    loop_pass = loop_pass + 1 

```
```

---------
i: a
loop pass: 1
---------
i: b
loop pass: 2
---------
i: c
loop pass: 3

```

This shows that the loop iterates over the "letters" string. In fact, a loop can run over any
[iterable][], an object capable of returning its members one at a time. Examples of iterables
include all sequence types (such as `list`, `str`, and `tuple`) and some non-sequence types like 
`dict` ...  The `for` statement creates an [iterator][] out of the iterable object and creates a 
temporary unnamed variable to hold the iterator for the duration of the loop.

If you just wanted to count the loop passes, the code below would be another option

```Python

letters = "abc"
    
for i in range( len(letters) ):
    print("---------")
    print("i:", i)

```


<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->

[range]: https://docs.python.org/3/library/stdtypes.html#ranges

[iterable]: https://docs.python.org/3/glossary.html#term-iterable

[iterator]: https://docs.python.org/3/glossary.html#term-iterator
