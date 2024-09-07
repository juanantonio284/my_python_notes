# Asymptotic Notation

<!-- guttag 3rd ed pdf 241 -->

Asymptotic notation is a notation used to provide a formal way to talk about the relationship
between *the running time of an algorithm* and *the size of its inputs*. As a proxy for "very
large", **asymptotic notation describes the complexity of an algorithm as the size of its inputs
approaches infinity**. (Almost any algorithm is sufficiently efficient when run on small inputs;
what we typically need to worry about is the efficiency of the algorithm when run on very large
inputs.) 

Consider the code below.

```Python

# Figure 11-3 Asymptotic complexity

def f(x):
    """Assume x is an int > 0"""
    ans = 0
    
    # Loop that takes constant time
    for i in range(1000):
        ans += 1
    print("Number of additions so far", ans)
    
    # Loop that takes time X
    for i in range(x):
        ans += 1
    print("Number of additions so far", ans)
    
    # Nested loops that take time x**2
    for i in range(x):
        for j in range(x):
            ans += 1
            ans += 1 # my note: should this be less indented (at the level of first loop)?
    print("Number of additions so far", ans)
    
    return ans

```

If we assume that each line of code takes one unit of time to execute, the running time of this
function can be described as `1000 + x + 2*x^2`. 

* The constant `1000` corresponds to the number of times the first loop is executed
* `x` corresponds to the number of times the second loop is executed
* `2*x^2` corresponds to the time spent executing the two statements in the nested for loop

Note that while the call `f(10)` prints:

```

Number of additions so far 1000
Number of additions so far 1010
Number of additions so far 1210

```

The call `f(1000)` prints:

```

Number of additions so far 1000
Number of additions so far 2000
Number of additions so far 2002000

```

This shows that for small values of `x` the constant term dominates (if `x = 10`, over 80% of the
steps are accounted for by the first loop), but that this changes for large values of `x`.

* For `x = 1000`, each of the first two loops accounts for about `0.05%` of the steps
* For `x = 1,000,000`, the first loop takes about `0.00000005%` of the total time and the second
  loop about `0.00005%`
    - A full `2,000,000,000,000` of the `2,000,001,001,000` steps are in the body of the inner 
      `for` loop

This means that, by considering only the inner loop (i.e. the quadratic component), we can get a
**meaningful notion** of how long this code will take to run on very large inputs.

Should we care about the fact that this loop takes `2*x^2` steps rather than `x^2` steps? If your
computer executes roughly 100 million steps per second, evaluating `f` will take about 5.5 hours.
If we could reduce the complexity to `x^2` steps, it would take about 2.25 hours. (In either case,
the moral is the same: we should probably look for a more efficient algorithm.) 

[I don't think he actually answers the question "should we care ...". The answer is technically 
*no*, but the passage is unclear. If he wanted to convey that we shouldn't care, perhaps he should
have used an example that doesn't save/cost 2.25 hours.]

This kind of analysis leads us to use the following:

### Rules of thumb in describing the asymptotic complexity of an algorithm

* If the running time is the sum of multiple terms, keep the one with the largest growth rate and
  drop the others
* If the remaining term is a product, drop any constants

**Order of common operations**
<!-- this comes from handout -->

* If each statement is "simple" (only involves basic operations) then the time for each statement is
  constant and the total time is also constant: `O(1)`
  
* A loop executes `N` times, so the sequence of statements also executes `N` times. If we assume the
  statements are `O(1)`, the total time for the for loop is `N * O(1)`, which is `O(N)` overall

* In a chain of if-then-else statements: if block 1 takes `O(1)` and block 2 takes `O(N)`, the
  if-then-else statement as a whole would be `O(N)`
    
* For nested loops, the outer loop executes `N` times and, every time the outer loop executes, the
  inner loop executes `M` times. As a result, the statements in the inner loop execute a total of
  `N * M` times. Thus, the complexity is `O(N * M)`

  - There is a common special case where the inner loop also executes `N` times and the total
    complexity for the two loops is `O(N^2)`

* When a statement involves a function/procedure call, the complexity of the statement includes the
  complexity of the function/procedure


<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈***≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
## Big O notation

Since we are particularly interested in **an upper bound on the asymptotic growth of a function**
(which is often called the **order** of growth), we use a special notation for this upper bound:
"Big O" notation.[^note_1] 

Thus we may say something like "the function f of x belongs to omicron X^2": `f(x) ∈ O(x^2)`. This
statement, means that the function `f` *grows no faster than* the quadratic polynomial `x^2`, in an
asymptotic sense. 

Many computer scientists will abuse Big O notation by making statements like, 
"the complexity of f(x) **is** O(x^2)"; by this they mean that in the worst case `f` will take no more than `O(x^2)` steps to run. 
But the difference between a function "*being in* O(x^2)" and "*being* O(x^2)" is **subtle but
important**. 
Saying that `f(x) ∈ O(x^2)`—which is the correct terminology—does not preclude the worst-case
running time of `f` from being considerably less than `O(x^2)`. (To avoid this kind of confusion we 
will use Big Theta (`θ`) when we are describing something that is both an upper and a lower bound on
the asymptotic worst-case running time. This is called a tight bound.)

<!-- continue at page 243 -->
<!-- 11.3 Some Important Complexity Classes -->


<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
## Classes of functions
<!-- this comes from handout -->

Here is a list of classes of functions that are commonly encountered when analyzing algorithms. The
slower growing functions are listed first. `c` is some arbitrary constant.

|   **Notation**  |     **Name**    |
|:---------------:|:---------------:|
|      `O(1)`     |     constant    |
|   `O(log(n))`   |   logarithmic   |
| `O((log(n))^c)` | polylogarithmic |
|      `O(n)`     |      linear     |
|     `O(n^2)`    |    quadratic    |
|     `O(n^c)`    |    polynomial   |
|     `O(c^n)`    |   exponential   |


The above list is useful because of the following fact: 

> If a function `f(n)` is a sum of functions, one of which grows faster than the others, then the
  faster growing one determines the order of `f(n)`. (The number of summands has to be constant and
  may not depend on `n`.)

Example: **If** `f(n) = 10 log(n) + 5(log(n))^3 + 7n + 3n^2 + 6n^3`, **then** `f(n) = O(n^3)`.

* Note that `O(n^c)` and `O(c^n)` are very different. The latter grows much, much faster, no matter
  how big the constant `c` is

    - A function that grows faster than any power of `n` is called superpolynomial. One that grows
      slower than an exponential function of the form `c^n` is called subexponential. An algorithm
      can require time that is both superpolynomial and subexponential; examples of this include
      the fastest algorithms known for integer factorization

* Note, too, that `O(log n)` is exactly the same as `O(log(n^c))`; the logarithms differ only by a
  constant factor, and the big O notation ignores that. Similarly, logs with different constant
  bases are equivalent


<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
## Another explanation 

[From the handout. It might be complimentary to the one in the book, but you may skip reading it if
you want]

How efficient is an algorithm or piece of code?

Be careful to differentiate between:

1. Performance: how much time/memory/disk/network is actually used when a program is run. This
depends on the machine, compiler, etc. as well as the code.

2. Complexity: how do the resource requirements of a program or algorithm scale, i.e. what happens
as the size of the problem being solved gets larger? (this is more related to CPU time)

Complexity affects performance but not the other way around. The time required by a
function/procedure is proportional to the number of "basic operations" that it performs. Here are
some examples of basic operations:

* one arithmetic operation (e.g.  `+`, `*`)
* one assignment (e.g. `x := 0`)
* one test (e.g. `x = 0`)
* one read of a primitive type (integer, float, character, boolean)
* one write of a primitive type

Some functions/procedures perform the same number of operations every time they are called. For
example, StackSize in the Stack implementation always returns the number of elements currently in
the stack or states that the stack is empty, then we say that StackSize takes constant time.

Other functions/ procedures may perform different numbers of operations, depending on the value of a
parameter. For example, in the BubbleSort algorithm, the number of elements in the array,
determines the number of operations performed by the algorithm. This parameter (number of elements)
is called the problem size/input size.


<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
## References

* Guttag, John, *Introduction to computation and programming using Python: with application to
  computational modeling and understanding data* (Third edition. ISBN 9780262542364)

* [Handout][] from MIT 16.070 Introduction to Computers and Programming

[Handout]: https://web.mit.edu/16.070/www/lecture/big_o.pdf

<!-- http://web.mit.edu/16.070/www/ -->

<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->

[^note_1]: 
The O is actually the Greek capital letter Omicron `Ο`, unicode U+039F, and used to evoke **O**rder 
of growth.
