This code, and a full tutorial, can be found at:  
https://realpython.com/python-thinking-recursively/  
Here I present a condensed version that I find clearer (changed explanations and some code)

# Get an intuition of how recursion works

The original problem uses an analogy of elves delivering presents to houses:

* If an elf is responsible for only 1 house, he delivers himself. 

* If an elf is responsible for more than one house, he does not deliver and, instead, delegates two
  elves (one for half of the houses, another for the other half). This delegation keeps happening
  until an elf only has one house.

```Python

houses = [ "house_1", "house_2", "house_3", "house_4" ]

# iterative ......................................

def deliver_presents_iteratively():
    for house in houses:
        print("Delivering presents to", house)

# recursive ......................................

def deliver_presents_recursively(houses):
    
    if len(houses) == 1:
        house = houses[0] # first item on the list
        print("Delivering presents to", house)

    else:        
        # Note: 
        # the recursion is double (there are two calls to the function); one takes care of the first
        # half of the list, the other one the second half.
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)
        
deliver_presents_recursively(houses)

```


# Maintaining State

When dealing with recursive functions, keep in mind that each recursive call has its own execution
context, so to maintain state during recursion you have to either:

1. Thread the state through each recursive call so that the current state is part of the current
call’s execution context (i.e. pass the updated current state to each recursive call as arguments)

2. Keep the state in global scope

## Example 1. Thread the state

Let’s calculate 1 + 2 + 3 ⋅⋅⋅⋅ + 10 using recursion. 

The state that we have to maintain is: (current number we are adding, sum up to this point).

```Python

def sum_all_in_range(current_number, accumulated_sum):
    
    # Base case
    if current_number == 11:
        return accumulated_sum # Return the final state

    # Recursive case
    else:
        # Thread the state through the recursive call
        return sum_all_in_range(current_number + 1, accumulated_sum + current_number)

# Call the function with an initial state (starting at 1, with accumulated sum = 0)
sum_all_in_range(1, 0)

```

## Example 2. Keep the state in global scope

Note:

* a function **can access** a variable defined inside and outside of its scope (outside the
  function's scope means in the global scope). 

* a function **cannot modify** a variable that's defined outside of its scope

The `global` statement tells Python that these variables will be modified in the global scope rather
than within the scope of the function.

```Python

# Global mutable state
current_number = 1
accumulated_sum = 0

def sum_all_in_range_global_scope():
    
    # The `global` statement tells Python that these variables will be modified in the global scope
    # rather than within the scope of the function.
    global current_number
    global accumulated_sum
    
    # Base case
    if current_number == 11:
        return accumulated_sum
    
    # Recursive case
    else:
        accumulated_sum = accumulated_sum + current_number
        current_number = current_number + 1
        return sum_all_in_range_global_scope()

```

> "The indiscriminate use of global variables can lead to lots of problems. The key to making
   programs readable is locality. One reads a program a piece at a time, and the less context
   needed to understand each piece, the better. Since global variables can be modified or read in a
   wide variety of places, the sloppy use of can destroy locality. Nevertheless, there are times
   when they are just what is needed." — John V. Guttag (Introduction to Computation and
   Programming using Python, 2nd ed.)


# Recursive Data Structures in Python

A data structure is recursive if it can be deﬁned in terms of a smaller version of itself. A list is
an example of a recursive data structure. 

Assume that you have only an empty list at your disposal, and the only operation you can perform on
it is this:

```Python

# Return a new list that is the result of
# adding element to the head (i.e. front) of input_list
def attach_head(element, input_list):
    return [element] + input_list

```

List is not the only recursive data structure. Other examples include set, tree, dictionary, etc.

The recursive function’s structure can often be modeled after the definition of the recursive data
structure it takes as an input. Let me demonstrate this by calculating the sum of all the elements
of a list recursively:

```Python

def sum_all_in_list(input_list):
    
    # Base case
    if input_list == []:
        return 0

    # Recursive case
    # Decompose the original problem into simpler instances of the same problem
    # by making use of the fact that the input is a recursive data structure
    # and can be deﬁned in terms of a smaller version of itself
    else:
        head = input_list[0] # the first element in the list
        smaller_list = input_list[1:] # all elements from second to last
        
        print( "head:", head )                  #debug .....
        print( "smaller_list:", smaller_list )  #debug .....
        
        return head + sum_all_in_list(smaller_list)


# call
sum_all_in_list([1, 2, 3])

```
