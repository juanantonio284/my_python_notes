# A Recursion to Generate Subsets From a List

I have a list `L` with various elements, i.e. a set, and I'd like to find all possible subsets. The
result will, itself, be a list (each subset is also expressed as a list). 

If, for example, I've got a list of the integers 1, 2, 3, and 4: 

The empty list is counted as a subset. The list that only contains the number 1 is a subset(in fact,
every list that contains a single number would be a subset). Other subsets would be lists of 
` (1, 2)`, `(1, 3)`, `(1, 4)`, `(2, 3)`, `(2, 4)`, etc.

**The strategy** to generate all of the subsets of a list `L1` is to first generate all the subsets
for a list that is smaller by one element (call this `L2`) and, later, add more subsets that include
the element that was taken off. 

## Code and explanation

1. My base case is when there is nothing in the list. But I still get all possible subsets from it
(i.e. just one empty list), and return the result—a list with an empty list inside. 
`if len(L) == 0: return [[]]`

2. I re-call the function `smaller = genSubsets( L[ :-1] )` and, in this call, the input passed is a
new list `L2` that contains *everything but* the last element of `L1`. The result of this call is
assigned to `smaller`, and is a list of all possible subsets of `L1`, except those that would
include the last element. 

    - The mind trick here is that instead of looking at `smaller` as all the subsets of `L2`
      (which it is), you look at it as all the subsets of `L1`, except those that would include the
      last element

```Python

# Unit 6, Lecture 11, Segment 3, Slide 41
# Take a list and generate subset lists from it

def genSubsets(L):
        
    # Base case of the recursion: when L is empty
    if len(L) == 0:
        return [[]]  # Return list of empty list

                     # Remember that we always get to the base case at some point and this is where
                     # the function ends. In this example, we end the function by 
                     # returning the empty set.

    # Recursion
    smaller = genSubsets( L[ :-1] )  # This calls the function with a list that does not include 
                                     # the last element of the current list. 
                                     # The end result (the return) of this call is assigned to 
                                     # "smaller". ("smaller" is thus a list of lists.)

    # The rest of the program
    extra = L[-1: ]  # extra is a single element, the last of the list passed to THIS call, and
                     # will be used to create the remaining subsets.
    new = [] # This is where the "new" subsets discovered in this call will be put
             # this is created and filled for every separate call of the function
    
    for small in smaller:
        new.append(small+extra)
        # the "smaller" used at this point is the smaller that comes from the NEXT function call
        # (i.e. the one with a smaller list that was completed BEFORE the current call)
        
        # since "smaller" is a list of lists, "small" is a list 
        # (which is to say don't treat it as some other type as that may create an error)

    return smaller+new  # take the "smaller" mentioned above (which uses a list one element 
                        # smaller than the one in the current call) and add the new sets discovered 
                        # in this call (which include that "extra" element)
    
```

3. `extra = L[-1: ]` is a single element, the last of the list that was passed as an argument to
THIS call of the function, and will be used to create the remaining subsets.

    * Notice that the function call used this `L[ :-1]`, which means *everything except the last
      element*. This `extra` statement uses this `[-1: ]`, which means *the last element and
      nothing else*

4. `new = []` initializes a list where the "new" subsets discovered in this call will be put.

5. `for small in smaller:` iterates through `smaller`, creating new subsets that add the last
element (the one in `extra`). Each new subset is the union of small and extra (`small+extra`), and
will be appended to the `new` list.

6. Finally, the function returns `smaller` (the result from the previous call) attached to the `new`
list created in this call.


<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈***≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
## Step By Step

After running this code with debugs[^note_1], for `sample_list = [1,2]` we get the output below,
which is useful to see how the code works. 

This section presents details one by one, chopping up the output. (The appendix section presents the
whole output as it comes in the terminal.)

### 1

Every time the function is called, these are the first two steps:

  * the `if` structure is skipped (except in the last call when the list is empty `len(L) == 0`)
  * the function is called with a list that is smaller by one `smaller = genSubsets( L[ :-1] )`

In other words, the function is called over and over before anything really happens.

```Python

def genSubsets(L):

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

After all the recursive calls, and the completion to base case, the rest of the code runs.

```Python

    # The rest of the program
    extra = L[-1: ]  # (i)
    new = []         # (ii)
        
    for small in smaller: # (iii)
        new.append(small+extra) # (iv)

    return smaller+new  # (v)
    
```

* (i) `extra = L[-1: ]` is a single element, the last of the list that was passed as an argument to
  THIS call

    - Notice that the function call used this `L[ :-1]`, which means *everything except the last
      element*. This `extra` statement uses this `[-1: ]`, which means *the last element and
      nothing else*
      
* (ii) `new` is initialized empty (this is created and filled for every separate call of the
  function)

* (iii) the `smaller` used at this point is the end result of the NEXT function call (i.e. the one
  with a smaller list that was completed BEFORE the current call). 
  
    - `smaller`, as its name suggests, is the solution to a smaller problem (the first `smaller`
      ever seen comes from the base case and is a list with an empty list `[[]]`)
  
    - the `for` loop iterates over this list and every element it pulls out, `small`, is, in itself,
      a list (the first `small` seen is an empty list `[]` pulled from `[[]]`)
      
* (iv) inside the loop a new subset is created with `small+extra` and appended to `new`
  which—remember—is unique to every call

    - `new` grows with the *new* sets (more than one) found in every iteration of the loop

* (v) At the end of the function `new` is added to the working `smaller` and returned. This return
  is then assigned to the same name `smaller` (overwriting the older one)

```

--------------------
After recursive call to function
         this corresponds to function called with list: [1] (original list minus the last element)
         extra: [1] <-- the last element of this call
         smaller (from next call): [[]] <-- this is the result of the base case
         --------
         inside loop
                 small: [] <-- this is the empty set inside the smaller above
                 new: []   <-- this is always initialized empty (different thing from line above)
                 append (small+extra) to new: [[1]]
         end of function, return smaller+new: [[], [1]]
         
         
--------------------
After recursive call to function
         this corresponds to function called with list: [1, 2] (finally getting to original call)
         extra: [2]
         smaller (from next call): [[], [1]]
         --------
         inside loop
                 small: []
                 new: []
                 append (small+extra) to new: [[2]]
         --------
         inside loop
                 small: [1]
                 new: [[2]]
                 append (small+extra) to new: [[2], [1, 2]]
         end of function, return smaller+new: [[], [1], [2], [1, 2]]


Note that "next" call refers to the call that was made after this one but was actually completed
before this one (look further up in the page for the result of the next call, as opposed to looking
below)

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
         smaller (from next call): [[]]
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
         smaller (from next call): [[], [1]]
         --------
         inside loop
                 small: []
                 new: []
                 append (small+extra) to new: [[2]]
         --------
         inside loop
                 small: [1]
                 new: [[2]]
                 append (small+extra) to new: [[2], [1, 2]]
         end of function, return smaller+new: [[], [1], [2], [1, 2]]
[[], [1], [2], [1, 2]]

```

[^note_1]: Code with debug statements in a separate file if you want to run it; but it's not
recommended to use lists much bigger than `sample_list = [1,2]` as the order of this code is
exponential.
