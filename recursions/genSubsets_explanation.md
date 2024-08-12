# A Recursion to Generate Subsets From a List

```Python

# Unit 6, Lesson 11, Session 3, Slide 41
# Take a list and generate subset lists from it

def genSubsets(L):

    res = [] # this is created and re-filled everytime the function runs
        
    # Base case of the recursion: when L is empty
    if len(L) == 0:
        return [[]]  # Return list of empty list

                     # Remember that we always get to the base case at some point and this is where
                     # the function ends. In this example, we end the function by 
                     # returning the empty set.

    # Recursion
    smaller = genSubsets( L[ :-1] )  # this calls the function with a list that does not include 
                                     # the last element and assigns the end result (the return) of 
                                     # the function to "smaller". 
                                     # "smaller" is thus a list of lists.

    # The rest of the program
    extra = L[-1: ]  # extra is a list that contains just the last element of the list that was 
                     # passed as an argument to this call of the function 
                     # (every call, the list passed gets less big)
    new = [] # this is created and re-filled everytime the function runs 
             # it is where the "new" subsets discovered in this call will be put
    
    for small in smaller:
        new.append(small+extra)
        # the "smaller" used at this point is the smaller that comes from the previous function call
        # since "smaller" is a list of lists, "small" is a list (don't treat it as some other
        # type)

    return smaller+new  # take the "smaller" which came from the last call and add the new 
                        # sets discovered in this call
    

# Note that all of the above is within a function. If that function is called recursively,
# everything will happen over and over, including the creation of all the lists. Indeed, it seems
# this takes a lot of computing power.

# assuming append takes constant time

# total time includes (time to solve smaller problem) plus (time needed to make a copy of all
# elements in the smaller problem)

```

<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈***≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
## Explanation

After running this code with debugs[^note_1], for `sample_list = [1,2]` we get the output below,
which is useful to see how the code works. 

This section presents details one by one, chopping up the output. The *Appendix* section presents
the whole output as it comes in the terminal.

### 1

Every time the function is called, these are the first three steps:

* `res` is initialized empty (`res = []`)
* the `if` structure is skipped (except in the last call when the list is empty `len(L) == 0`)
* the function is called with a list that is smaller by one `smaller = genSubsets( L[ :-1] )`

In other words, the function is called over and over before anything really happens.

```Python

def genSubsets(L):

    res = []         
    
    # Base case of the recursion: when L is empty
    if len(L) == 0:
        return [[]]
        
    # Recursion
    smaller = genSubsets( L[ :-1] ) 
                                     
```
```

>>> genSubsets(sample_list)

function start
         function called with list: [1, 2]
                 re-calling function with list: [1]
function start
         function called with list: [1]
                 re-calling function with list: []
function start
         function called with list: []
         base case, ending function
         
```

### 2

After the function has been called n times, got to the base case, and the first called has finished
(returning `[[]]`, a list with an empty list), we start seeing the results of the calls.

The first results seen correspond to the first recursive call made (which uses original list without
the last element, call it "list 2"). 

So, **after all the recursive calls, and the completion to base case, the rest of the code runs as
such**:

* (i) The `extra = L[-1: ]` statement takes the last element of list 2

    - Notice that the function call used this `L[ :-1]`, which means *everything except the last
      element*. This `extra` statement uses this `[-1: ]`, which means *the last element and
      nothing else*
      
* (ii) `new` is initialized empty (`new = []`)

```Python

    # The rest of the program
    extra = L[-1: ]  # (i)
    new = []         # (ii)
        
    for small in smaller: # (iii)
        
        new.append(small+extra) # (iv)

    return smaller+new  # (v)
    
```

* (iii) the `smaller` used at this point is the end result of the previous function call (the first
  `smaller` ever seen comes from the base case and is a list with an empty list `[[]]`)
  
    - the `for` loop iterates over this list and every element it pulls out (`small`) is, in itself,
      a list. The first `small` seen is an empty list `[]` pulled from `[[]]`
      
* (iv) inside the loop `small+extra` is appended to `new` which—remember—was initialized empty.

    - `new` grows with the *new* sets (more than one) found in every iteration

    - in the first instance of the output below, `small+extra` is `[],[1]` but this is only
      represented as `[1]` and thus `new` becomes `[[],[1]]`, which is represented as `[[1]]`
      
```

After recursive call to function
         this corresponds to function called with list: [1]
         extra: [1]
         smaller (from last call): [[]]
         --------
         inside loop
                 small: []  <-- this is an empty set inside smaller
                 new: []    <-- this is initialized empty, different thing from the line above
                 append (small+extra) to new: [[1]]
                 end of function, return smaller+new: [[], [1]]

```

* (v) At the end of the function `new` is added to the current `smaller` (which comes from the
  previous call) and returned

```
--------------------
After recursive call to function
         this corresponds to function called with list: [1, 2]
         extra: [2]
         smaller (from last call): [[], [1]]
         --------
         inside loop
                 small: []
                 new: []
                 append (small+extra) to new: [[2]]
                 end of function, return smaller+new: [[], [1], [2]]
         --------
         inside loop
                 small: [1]
                 new: [[2]]
                 append (small+extra) to new: [[2], [1, 2]]
                 end of function, return smaller+new: [[], [1], [2], [1, 2]]

```

**The end result is**: `[[], [1], [2], [1, 2]]`


<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
## Appendix

```
>>> genSubsets(sample_list)

function start
         function called with list: [1, 2]
                 re-calling function with list: [1]
function start
         function called with list: [1]
                 re-calling function with list: []
function start
         function called with list: []
         base case, ending function
--------------------
After recursive call to function
         this corresponds to function called with list: [1]
         extra: [1]
         smaller (from last call): [[]]
         --------
         inside loop
                 small: []
                 new: []
                 append (small+extra) to new: [[1]]
                 end of function, return smaller+new: [[], [1]]
--------------------
After recursive call to function
         this corresponds to function called with list: [1, 2]
         extra: [2]
         smaller (from last call): [[], [1]]
         --------
         inside loop
                 small: []
                 new: []
                 append (small+extra) to new: [[2]]
                 end of function, return smaller+new: [[], [1], [2]]
         --------
         inside loop
                 small: [1]
                 new: [[2]]
                 append (small+extra) to new: [[2], [1, 2]]
                 end of function, return smaller+new: [[], [1], [2], [1, 2]]
[[], [1], [2], [1, 2]]

```

[^note_1]: Code with debug statements in a separate file if you want to run it. But it's not
recommended to use lists much bigger than `sample_list = [1,2]`.
