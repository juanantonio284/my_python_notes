# Asymptotic Notation

<!-- guttag 3rd ed pdf 241 -->

**Asymptotic notation** is a notation used to provide a formal way to talk about the relationship
between *the running time of an algorithm* and *the size of its inputs*.

Almost any algorithm is sufficiently efficient when run on small inputs; what we typically need to
worry about is the efficiency of the algorithm when run on very large inputs. As a proxy for "very
large", **asymptotic notation describes the comTo avoid this kind of confusion we will use Big Theta (`θ`) when we are describing something that
is both an upper and a lower bound on the asymptotic worst-case running time. This is called a
tight bound.plexity of an algorithm as the size of its inputs
approaches infinity**.

Consider, for example, the code below.

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
    
    # Nested loops take time x**2
    for i in range(x):
        for j in range(x):
            ans += 1
            ans += 1 # my note: should this be less indented (at the level of first loop)?
    print("Number of additions so far", ans)
    
    return ans

```

If we assume that each line of code takes one unit of time to execute, the running time of this
function can be described as `1000 + x + 2*x^2`. The constant `1000` corresponds to the number of
times the first loop is executed, `x` corresponds to the number of times the second loop is
executed, and  `2*x^2` corresponds to the time spent executing the two statements in the nested for
loop.

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

This shows that for small values of x the constant term dominates (if x is 10, over 80% of the steps
are accounted for by the first loop), but that this changes for large values of x.

* For `x = 1000`, each of the first two loops accounts for about 0.05% of the steps.

* For `x = 1,000,000`, the first loop takes about `0.00000005%` of the total time and the second
  loop about `0.00005%`. 

    - A full `2,000,000,000,000` of the `2,000,001,001,000` steps are in the body of the inner 
      `for` loop.

This means that, *by considering only the inner loop (i.e. the quadratic component), we can get a
meaningful notion of how long this code will take to run on very large inputs*.

Should we care about the fact that this loop takes `2*x^2` steps rather than `x^2` steps? 

If your computer executes roughly 100 million steps per second, evaluating `f` will take about 5.5
hours. If we could reduce the complexity to `x^2` steps, it would take about 2.25 hours. (In either
case, the moral is the same: we should probably look for a more efficient algorithm.) 

[I don't think he actually answers the question "should we care ...". I think there is a meaningful
difference. Sure it's more important to deal with the quadratic and maybe do another algorithm but
this passage is unclear—if he wanted to convey that we shouldn't care, perhaps he should have used
an example that doesn't save/cost 2.25 hours.]

This kind of analysis leads us to use the following:

### Rules of thumb in describing the asymptotic complexity of an algorithm:

* If the running time is the sum of multiple terms, keep the one with the largest growth rate, and
  drop the others

* If the remaining term is a product, drop any constants


<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈***≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
## Big O Notation

Since we are particularly interested in **an upper bound on the asymptotic growth of a function**
(which is often called the *order of growth*), we use a special notation for this upper bound:
"Big O" notation.[^note_1] 

Thus we may say something like "the function f of x belongs to omicron X^2": `f(x) ∈ O(x^2)`. This
statement, the formula `f(x) ∈ O(x^2)`, means that the function `f` grows no faster than the
quadratic polynomial `x^2`, in an asymptotic sense. 

Many computer scientists will abuse Big O notation by making statements like, "the complexity of f
(x) is O(x^2)"; by this they mean that in the worst case `f` will take no more than `O(x^2)` steps
to run.

But the difference between a function "*being in* O(x^2)" and "*being* O(x^2)" is **subtle but
important**. Saying that `f(x) ∈ O(x^2)`—which is the correct terminology—does not preclude the
worst-case running time of `f` from being considerably less than `O(x^2)`.

(To avoid this kind of confusion we will use Big Theta (`θ`) when we are describing something that
is both an upper and a lower bound on the asymptotic worst-case running time. This is called a
tight bound.)

<!-- continue at page 243 -->
<!-- 11.3 Some Important Complexity Classes -->


<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
## References

* Guttag, John, *Introduction to computation and programming using Python: with application to
  computational modeling and understanding data* (Third edition. ISBN 9780262542364)

[^note_1]: 
The O is actually the Greek capital letter Omicron `Ο`, unicode U+039F, and used to evoke **O**rder 
of growth.
