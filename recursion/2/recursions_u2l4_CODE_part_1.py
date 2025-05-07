# Recursions 1 (Unit 2, Lesson 4) -- Part 1 of code

# SEE MARKDOWN FILE OF THE SAME NAME FOR BETTER FORMATTING AND EXPLANATIONS

# From the MITx course **Introduction to Computer Science and Programming Using Python
# (6.00.1x)** `Unit 2: Simple Programs, Lesson 4: Functions`

# This file contains all (or most) of the material regarding **recursions** presented in the
# course.

# The basis of this material is *copied and pasted* from class slides and transcripts, but I have
# arranged, re-arranged, explained, re-explained, commented, and changed comments to make it easier
# to understand. In other words, the contents of these files are either *very different* to the
# original class material or *essentially the same and don't provide anything new*, depending on
# how you want to look at it. Simply put: these are simply my personal notes and they are arranged
# and edited in a way that is convenient for me; no claims are made and no guarantees are given.

# Note: the course is organized in `units` that contain `lessons` that contain videos and exercises.
# I refer to the videos as "`sessions`" (as in *class sessions*) and give them their own numbering. 
# (The website numbers everything sequentially, but that doesn't make clear that the exercises are
# related to the video.)

# ***...............................................................................................
## Session 6

# unit 2, lesson 4, session 6, slide 41

# Multiplication (iterative solution)

#    a*b = a + a + ... + a [a is repeated b times]

def mult_iter(a, b):

    result = 0 # initialize variable

    while b > 0: # iteration (there are b additions to do)
        result += a # current value of computation, a running sum
        b -= 1 # current value of iteration variable
    
    return result


# unit 2, lesson 4, session 6, slide 42

# Multiplication (recursive solution)

#    a*b = a + a + ... + a [a is repeated b times]
#        = a + (a * b-1)

def mult(a, b):

    # base case
    if b == 1:
        return a

    # recursive step
    else:
        return a + mult(a, b-1)


# unit 2, lesson 4, session 6, slide 44

# Factorial

def fact(n):
    
    # base case
    if n == 1:
        return 1
    
    # recursive step
    else:
        return n * fact(n-1)


# unit 2, lesson 4, session 6, slide 46, panel 1

# Factorial (iterative solution)

def factorial_iter(n):

    prod = 1
    
    for i in range(1,n+1):
        prod *= i

    return prod


# unit 2, lesson 4, session 6, slide 46, panel 2
# same as slide 44

# Factorial (recursive solution)

def factorial(n):
    
    # base case
    if n == 1:
        return 1

    # recursive step
    else:
        return n * factorial(n-1)


# ................................................

### Session 6 exercises 

#### iterPower and recurPower


# unit 2, lesson 4, exercise which follows L4_S6--1_iteration_vs_recursion.md
# 17. Exercise: iterPower
# given answer

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    result = 1
    while exp > 0:
        result = base * result
        exp = exp - 1
    return result


# unit 2, lesson 4, exercise which follows L4_S6--1_iteration_vs_recursion.md
# 17. Exercise: iterPower
# another answer

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''    
    for i in range(exp):
        result = base * result


# unit 2, lesson 4, exercise which follows L4_S6--1_iteration_vs_recursion.md
# 18. Exercise: recurPower

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    
    returns: int or float, base^exp
    '''
    # base case
    if exp == 0:
        return 1
    # recursive step
    else:
        return base * recurPower(base, exp-1)


# ***...............................................................................................
## Session 7

# ................................................

### Mathematical Induction

# [Slide 49]

# To prove a statement indexed on integers is true for all values of n:

# 1. Prove it is true when n is smallest value (e.g. n = 0 or n = 1)

# 2. Then prove that if it is true for an arbitrary value of n, one can show that it must be true
# for n+1

# ................................................

### Example: Using Induction To Prove A Statement Is True

# [Slide 50]

# Prove that the following statement holds for all `n >= 0`:  
# `0 + 1 + 2 + 3 + … + n = ( n(n+1) ) / 2`

#### Proof

# 1. Prove it is true when n is smallest value (e.g. n = 0 or n = 1)

    # * If n = 0, then the left-hand side of the equation is 0 and the RHS is also `0*1/2 = 0`, so #   the first requirement for an induction is true

# 2. Then prove that if it is true for an arbitrary value of n, one can show that it must be true
# for n+1

    # * Assume true for some k, then you need to show that 
    # `0 + 1 + 2 + … + k + (k+1) = ((k+1)(k+2))/2`
        
        # - LHS reduces to `k(k+1)/2 + (k+1)` by the assumption that this property holds for problem
          # of size k
        
            # - This becomes, by algebra, `( (k+1)(k+2) )/2`

# **Having proved 1. and 2. the expression thus holds for all n >= 0 [QED]**


# ................................................

### Relevance of mathematical induction to code

# [Slide 51, Original title: "RELEVANCE TO CODE?"]

# * Same logic applies


# unit 2, lesson 4, session 6, slide 42

# Multiplication (recursive solution)

#    a*b = a + a + ... + a [a is repeated b times]
#        = a + (a * b-1)

def mult(a, b):

    # base case
    if b == 1:
        return a

    # recursive step
    else:
        return a + mult(a, b-1)


# * Base case, we can show that `mult` must return correct answer

# * For recursive case, we can assume that `mult` correctly returns an answer for problems of size
#   smaller than b, then by the addition step, it must also return a correct answer for problem of
#   size b

# * Thus, by induction, code correctly returns answer


