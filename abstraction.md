# Notes on Abstraction

> We all know that the only mental tool by means of which a very finite piece of reasoning can cover
  a myriad cases is called "abstraction"; as a result the effective exploitation of his powers of
  abstraction must be regarded as one of the most vital activities of a competent programmer. In
  this connection it might be worth-while to point out that the purpose of abstracting is not to be
  vague, but to create a new semantic level in which one can be absolutely precise. 
>
> ... I tend to the assumption —up till now not disproved by experience— that by suitable
  application of our powers of abstraction, the intellectual effort needed to conceive or to
  understand a program need not grow more than proportional to program length. 

— Edsger W. Dijkstra [*The Humble Programmer (ACM Turing Lecture 1972 EWD340)*][]

[*The Humble Programmer (ACM Turing Lecture 1972 EWD340)*]: https://www.cs.utexas.edu/~EWD/transcriptions/EWD03xx/EWD340.html

## Function Definitions

<!-- section 4.1.1 -->

In Python each function definition is of the form

```Python

def function_name (list of formal parameters):
    body of function

# example:
def maxVal(x, y):
  if x > y:
    return x
  else:
    return y

```

`def` is a **reserved word** that tells Python that a function is about to be defined. 

`function_name` ("maxVal" in the example) is simply a name that is used to refer to the function.

The list of **formal parameters** of the function is the sequence of names within the parentheses
following the function name (x,y in the example).

When the function is used, the formal parameters are bound—as in an assignment statement—to
the **actual parameters** (aka **arguments**) of the **function invocation**
(aka **function call**). 
For example, the invocation `maxVal(3, 4)` binds `x` to `3`, and `y` to `4`.

Parameters provide something called **lambda abstraction**, allowing programmers to write code that
manipulates not specific objects, but instead whatever objects the caller of the function chooses
to use as actual parameters. (The name "lambda abstraction" is derived from mathematics developed
by Alonzo Church in the 1930s and 1940s.)

## Specifications

<!-- section 4.2 -->

Functions are a way of creating computational elements that we can think of as primitives. Just as
we have the built-in functions max and abs, we would like to have the equivalent of a built-in
function for finding roots and for many other complex operations. Functions facilitate this by
providing decomposition and abstraction.

**Decomposition** creates structure. It allows us to break a program into parts that are reasonably
self-contained, and that may be reused in different settings.

**Abstraction** hides detail. It allows us to use a piece of code as if it were a black box—that is,
something whose interior details we cannot see, don't need to see, and shouldn't even want to see.
The essence of abstraction is preserving information that is relevant in a given context, and
forgetting information that is irrelevant in that context. The key to using abstraction
effectively in programming is finding a notion of relevance that is appropriate for both the
builder of an abstraction and the potential clients of the abstraction. That is the true art of
programming.

## Classes and Object-Oriented Programming

<!-- Chapter 10 -->

**Objects** are the core things that Python programs manipulate. Every object has a **type** that
defines the kinds of things that programs can do with that object. We have relied upon built-in
types such as `float` and `str` and the methods associated with those types. 

We have already looked at a mechanism that allows programmers to define new functions; we now look
at a mechanism that allows programmers to define new types.

### Abstract Data Types and Classes

<!-- section 10.1 -->

An **abstract data type** ["abstract" qualifies the main noun "data type"] is a set of objects and
the operations on those objects. Examples of data types are: integers, lists, floats, strings, and
dictionaries

(Objects and operations are bound together so that programmers can pass an object from one part of a
program to another, and in doing so provide access not only to the data attributes of the object
but also to operations that make it easy to manipulate that data.)

The specifications of those operations define an **interface** between the abstract data type and
the rest of the program. The interface defines the behavior of the operations—what they do, but not
how they do it. The interface thus provides an **abstraction barrier** that isolates the rest of
the program from the data structures, algorithms, and code involved in providing a realization of
the type abstraction.

Abstraction suppresses detail. The key is to suppress the appropriate details; this is where data
abstraction hits the mark. We can create domain-specific types that provide a convenient
abstraction. Ideally, these types capture concepts that will be relevant over the lifetime of a
program. **If we start the programming process by devising types that will be relevant months and
even decades later, we have a great leg up in maintaining that software**.

<!-- continue at bottom of page 201 -->

## References

* Guttag, John, *Introduction to computation and programming using Python: with application to
  understanding data* (Second edition. ISBN 9780262529624)
   
* Guttag, John, *Introduction to computation and programming using Python: with application to
  computational modeling and understanding data* (Third edition. ISBN 9780262542364)

* Edsger W. Dijkstra, *The Humble Programmer* (ACM Turing Lecture 1972 EWD340)
