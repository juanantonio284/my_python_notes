# Merge sort
<!-- pdf 265 -->

A *divide-and-conquer* algorithm can do a lot better than quadratic time. 

The basic idea behind a *divide-and-conquer* algorithm is to combine solutions of simpler instances
of the original problem and, in general, this type of algorithm is characterized by: 

* A threshold *input size* below which the problem is not subdivided (the threshold is sometimes
  called the *recursive base*)
* The size and number of sub-instances into which an instance is split
* The algorithm used to combine sub-solutions

**Merge sort** is a prototypical divide-and-conquer algorithm and, like many of these algorithms, it
is most easily described recursively:

1. If the list is of length 0 or 1, it is already sorted.
2. If the list has more than one element, split the list into two lists, and use *merge sort* to
sort each of them.
3. Merge the results.

Merge sort was invented in 1945 by John von Neumann, who made a key observation that *two sorted
lists can be efficiently merged into a single sorted list*. The idea is to look at the first
element of each list and move the smaller of the two to the end of a new "result" list. When one of
the lists is empty, all that remains is to copy the remaining items from the other list to
the "result" list.

### The merge process

Consider, for example, merging the two lists `L_1 = [1,5,12,18,19,20]` and `L_2 = [2,3,4,17]`:

```

Elements still in list 1  Elements still in list 2    Compare      Result
    [1,5,12,18,19,20]             [2,3,4,17]            1, 2       [1]
    [5,12,18,19,20]               [2,3,4,17]            5, 2       [1,2]
    [5,12,18,19,20]               [3,4,17]              5, 3       [1,2,3]
    [5,12,18,19,20]               [4,17]                5, 4       [1,2,3,4]
    [5,12,18,19,20]               [17]                  5, 17      [1,2,3,4,5]
    [12,18,19,20]                 [17]                  12, 17     [1,2,3,4,5,12]
    [18,19,20]                    [17]                  18, 17     [1,2,3,4,5,12,17]
    [18,19,20]                    []                    18, --     [1,2,3,4,5,12,17,18,19,20]
    []                            []                               

```

**What is the complexity of the merge process?** 

It involves two constant-time operations, `comparing the values of elements` and `copying elements
from one list to another`. The number of comparisons is order `θ( len(L) )`, where L is the longer
of the two lists. The number of copy operations is order `θ( len(L1) + len(L2) )`, because each
element is copied exactly once.[^big_theta] (The time to copy an element depends on the size of the
element. However, this does not affect the order of the growth of sort as a function of the number
of elements in the list.) 

Therefore, merging two sorted lists is linear in the length of the lists, order `θ( len(L) )`.


<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈***≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
## An implementation of the merge sort algorithm

Our implementation of the merge sort algorithm (`merge_sort`) makes use of another function,
`merge`.

```Python

# this function is used by the merge_sort function below, which passes a value for compare
def merge(left, right, compare):
    
    """
    left and right are sorted lists. 
    compare defines an ordering on the elements x < y by default (but can be switched to x > y)
    
    Returns a new sorted (by compare) list containing the same elements as (left + right) would
    contain.
    """
    
    result = []
    i,j = 0, 0
    
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while (i < len(left)):
        result.append(left[i])
        i += 1
    
    while (j < len(right)):
        result.append(right[j])
        j += 1
    
    return result

```

```Python

def merge_sort(L, compare = lambda x, y: x < y):
    
    """
    Assumes L is a list, compare defines an ordering on elements of L.
    Returns a new sorted list with the same elements as L
    """
    
    if len(L) < 2: # base case
        return L[:]
    
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare) # notice that this line calls the merge function

# Given a list L:
# * If there are 0 or 1 elements (i.e. len(L) < 2), return a copy of the list
# * Else, divide the list in half and recursively call the function for the left and for the 
#   right side of the list

```

Note the difference: 

* In the `merge` function, the `compare` parameter is passed a value (a `True` or a `False`)

* In the `merge_sort` function, the `compare` parameter is passed an operation (`x<y`) which returns
  a value

Thus in the `merge_sort` function there is not a default value passed (i.e. a `True` or a `False`),
but there is a default operation passed (`x<y`). To pass an operation to a parameter we use
a *lambda* expression[^lambda_exp]; the user could pass his own desired operation by changing this
expression, e.g. `merge_sort(L, lambda x, y: x > y)`.

*Sample usage*: 

```Python

L = [2,1,4,5,3]

print( merge_sort(L) ) # this uses the default value for compare
# [1, 2, 3, 4, 5]

print( merge_sort(L, lambda x, y: x > y) ) # this changes the default value for compare
# [5, 4, 3, 2, 1]

```

### Complexity of `merge_sort`
<!-- pdf 268 -->

Let's analyze the complexity of `merge_sort`. 

* At each level of recursion the total number of elements to be merged is `len(L)` (and as we saw
  above, the time complexity of `merge` is order `θ( len(L) )`)

* Therefore, the time complexity of `merge_sort` is order `θ( len(L) )` multiplied by the number `n`
  of levels of recursion, i.e. however many times the `merge` function is called

    - Since the function divides the list in half, each time, we know that the number of
      levels of recursion `n` is of logarithmic order: `θ( log(len(L)) )`
      
    - Thus we take `θ( len(L) )` and multiply by `θ( log(len(L)) )`, which gives 
    `θ( len(L) * log(len(L)) )`

    - And, substituting `len(L)` with `n`, we have that the time complexity of `merge_sort` is 
    `θ( n*log(n) )`

This is a lot better than selection sort's `θ( len(L)^2)`. 

For example, if `L` has 10,000 elements, `len(L)^2` is 100 million but `len(L)*log_2(len(L))` is
about 130,000. 

This improvement in time complexity comes with a price. Selection sort is an example of an in-place
sorting algorithm. Because it works by swapping the place of elements within the list, it uses only
a constant amount of extra storage (one element in our implementation). In contrast, the merge sort
algorithm involves making copies of the list. This means that its space complexity is order 
`θ(len (L))`. This can be an issue for large lists but you could consider *quicksort*.[^quicksort]


<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈***≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
## Exercise

Suppose we want to sort a list of names written as first name followed by last name. We defined two
ordering functions, one that sorts `last name, first name`, another that sorts `first name, last
name` 

```Python

def lastNameFirstName(name1, name2):
    arg1 = name1.split(' ')
    arg2 = name2.split(' ')
    if arg1[1] != arg2[1]:
        return arg1[1] < arg2[1]
    else: #last names the same, sort by first name
        return arg1[0] < arg2[0]

def firstNameLastName(name1, name2):
    arg1 = name1.split(' ')
    arg2 = name2.split(' ')
    if arg1[0] != arg2[0]:
        return arg1[0] < arg2[0]
    else: #first names the same, sort by last name
        return arg1[1] < arg2[1]

# .split is a method of type str

```

These functions are then passed as arguments in a call to `merge_sort`.

```Python

L = ['Tom Brady', 'Eric Grimson', 'Gisele Bundchen']

newL = merge_sort(L, lastNameFirstName)
print('Sorted by last name =', newL)

newL = merge_sort(L, firstNameLastName)
print('Sorted by first name =', newL)

```


<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
## References

* Guttag, John, *Introduction to computation and programming using Python: with application to
  computational modeling and understanding data* (Third edition. ISBN 9780262542364)


[^big_theta]: 
Notice that this was not expressed with Big `O` but rather Big Theta (`θ`), used when we are
describing something that is both an upper and a lower bound on the asymptotic worst-case running
time. This is called a tight bound.

[^lambda_exp]: 
Python supports the creation of anonymous functions (i.e. functions that are not bound to a name),
using the reserved word `lambda`. The general form of a lambda expression is 
`lambda sequence of variable names : expression`.
For example, the lambda expression `lambda x, y: x*y` returns a function that returns the product of
its two arguments. Lambda expressions are frequently used as arguments to higher-order functions.
<!-- pdf 107 "Section 4.4 Functions as objects" -->

[^quicksort]: 
Quicksort, which was invented by C.A.R. Hoare in 1960, is conceptually similar to merge sort, but
considerably more complex. It has the advantage of needing only log(n) additional space. Unlike
merge sort, its running time depends upon the way the elements in the list to be sorted are ordered
relative to each other. Though its worst-case running time is `O(n^2)`, its expected running time
is only `O(n*log(n))`.
