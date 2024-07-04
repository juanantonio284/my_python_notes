# Notes on Abstraction 2

* Barbara Liskov and John Guttag, *Abstraction and Specification in Program Development*
  [Second printing, 1987. ISBN 0-262-12112-3 (MIT Press). ISBN 0-07-037996-3 (McGraw-Hill)]

## Decomposition and Abstraction

<!-- section 1.1 -->

The basic paradigm for tackling any large problem is clear—we must "divide and rule". Unfortunately,
merely deciding to follow Machiavelli's dictum still leaves us a long way from solving the problem
at hand. **Exactly *how* we choose to divide a problem is of overriding importance.**

**Our goal in decomposing a program is to create modules that are themselves small programs that
 interact with one another in simple, well-defined ways.** 
 
If we achieve this goal:
 
* different people will be able to work on different modules independently, without needing much
  communication among themselves, and yet the modules will work together

* during program modification and maintenance it will be possible to modify some of the modules
  without affecting all of the others

When we decompose a problem, we factor it into separable subproblems in such a way that

1. each subproblem is at the same level of detail
2. each subproblem can be solved independently
3. the solutions to the subproblems can be combined to solve the original problem

Sorting using *merge sort* is an elegant example of problem solving by decomposition. It breaks the
problem of sorting a list of arbitrary size into the two simpler problems of sorting a list of size
two and merging two sorted lists of arbitrary size.

...

**Large or poorly understood problems are difficult to decompose properly.** The most common problem
is creating individual components that succeed at solving the stated subproblems but, when combined,
are unable to solve the original problem. For example, imagine creating a play by assembling a
group of writers, giving each a list of characters and a general plot outline, and asking each of
them to write a single character's lines. The authors might accomplish their individual tasks
admirably, but it is highly unlikely that their combined efforts will be an admirable play. It
might be artistic, but it would lack any sort of coherence or sense. Individually acceptable
solutions simply cannot be expected to combine properly if the original task has been divided in a
counterproductive way.

**Abstraction is a way to do decomposition productively by changing the level of detail to be
considered. When we abstract from a problem, we agree to ignore certain details in an effort to
convert the original problem to a simpler one.** We might, for example, abstract from the problem
of writing a play to the problem of deciding how many acts it should have, or what its plot will be,
or even the sense (but not the wording) of individual pieces of dialogue. After this has been done,
the original problem (of writing all of the dialogue) remains, but it has been considerably
simplified—perhaps even to the point where it could be turned over to another or even several
others. (Dumas, père, churned out novels in this way.)

The paradigm of abstracting and then decomposing is typical of the program design process:
**Decomposition is used to break software into components that can be combined to solve the original
problem; abstractions assist in making a good choice of components. We alternate between the two
processes until we have reduced the original problem to a set of problems we already know how to
solve.**

## Abstraction

<!-- section 1.2 -->

The process of abstraction can be seen as an application of many-to-one mapping. It allows us to
forget information and consequently to treat things that are different as if they were the same. We
do this in the hope of simplifying our analysis by separating attributes that are relevant from
those that are not. It is crucial to remember, however, that relevance often depends upon context.
In the context of an elementary school classroom we learn to abstract both `(8/3)*3` and `5+3` to
the concept we represent by the numeral `8`. Much later we learn, often under unpleasant
circumstances, that on many computing machines this abstraction can get us into a world of
trouble.

<!-- In this book we are interested in abstraction as it is used in programs in general. The most significant development to date in this area is the development of high-level languages. By dealing directly with the constructs of a high-level language rather than with the many possible sequences of machine instructions into which they can be translated, the programmer achieves a significant simplification. In recent years, however, programmers have become dissatisfied with the level of abstraction generally achieved even in high-level language programs. -->
...

One approach to dealing with [the problem of achieving the desired level of abstraction] lies in the
invention of "very-high-level languages", built around some fixed set of relatively general data
structures and a powerful set of primitives that can be used to manipulate them. For example,
suppose a language provided `is-in` and `index_of` as primitive operations on arrays.
[These functions could serve to determine if an element is in an array, and the index of that
element in the array.]

The flaw in this approach is that it presumes that the designer of the programming language will
build into the language most of the abstractions that users of the language will want. Such
foresight is not given to many; and even if it were, a language containing so many built-in
abstractions might well be so unwieldy as to be unusable. A preferable alternative is to design
into the language mechanisms that allow programmers to construct their own abstractions as they
need them. The most common such mechanism is the use of procedures. 

**By separating procedure definition and invocation, a programming language makes two important
methods of abstraction possible**:

* abstraction by parameterization
* abstraction by specification

### Abstraction by Parameterization

<!-- section 1.2.1 -->

**Abstraction by parameterization** allows us, through the introduction of parameters, to represent
  a potentially infinite set of different computations with a single program text that is an
  abstraction of all of them. 

Consider first the program text `x * x + y * y`. This describes a computation that adds the square
of the value stored in a particular variable `x` to the square of the value stored in another
particular variable `y`. 

Consider, on the other hand, the **lambda expression** `λx, y: int.(x * x + y * y)`. This describes
the set of computations that square the value stored in *some* integer variable (which we
shall *temporarily* refer to as `x`) and add to it the square of the value stored in *some other*
integer variable (*temporarily* called `y`). 

In such a lambda expression we refer to `x` and `y` as the **formal parameters** and `x*x` + `y*y`
as the body of the expression. **We invoke a computation by binding the formal parameters to
arguments and then evaluating the body**. For example,

`λx, y: int.(x * x + y * y) (w, z)` is identical in meaning to `w * w + z * z`

In more familiar notation, we might denote the above lambda expression by

```
squares = proc (x, y: int) returns (int)
    return (x * x + y * y)
    end
```

and the binding of actual to formal parameters and evaluation of the body by the procedure call
`squares(w, z)`.

Abstraction by parameterization is an important means of achieving generality in programs. A *sort
routine* that works on *any* array of integers is much more generally useful than one that works
only on a *particular* array of integers. By further abstraction we might define a *sort
abstraction* that works on arrays of reals as well as arrays of integers, or even one that works on
arraylike structures in general.

Abstraction by parameterization is an extremely powerful mechanism, but it is not a sufficiently
powerful mechanism to describe conveniently and fully the abstraction that the careful use of
procedures can provide.

### Abstraction by Specification

<!-- section 1.2.2 -->

**Abstraction by specification** allows us to abstract *from* the computation described by the body
  of a procedure *to* the end that procedure was designed to accomplish. [Read: from a to b, from
  construction to purpose.] To do this, we **associate with each procedure a specification of its
  intended effect, then we can consider the meaning of a procedure call to be based on this
  specification rather than on the procedure's body**.

We are making use of abstraction by specification whenever we associate with a procedure a comment
that is sufficiently informative as to allow others to use that procedure without looking at its
body. A good way to write such comments is to use pairs of assertions. 

* The **requires assertion** specifies something that is required to be true in order to carry out
  the procedure. [The pre-condition of a procedure specifies something that is assumed to be true
  on entry to the procedure.] In practice what is most often asserted is a set of conditions
  sufficient to ensure the proper operation of the procedure; and it is often simply the vacuous
  assertion "true".

* The **effects assertion** (or post-condition) specifies something that is supposed to be true at
  the completion of any invocation of the procedure for which the pre-condition was satisfied.

Consider, for example, the `sqrt` procedure in figure 1.3.

```

Figure 1.3 The sqrt procedure.

sqrt = proc (coef: real) returns (real)
    % requires coef > 0
    % effects returns an approximation to the square root of coef
        ans: real = coef/2.0;
        i: int := 1
    while i < 7 do
        ans := ans — ((ans * ans — coef)/(2.0 * ans))
        i := i + 1
        end
    return (ans)
end sqrt

```

Because a specification is provided [in the two % commented lines after the definition], we can
ignore the body of the procedure. We thus take the meaning of the procedure call `y := sqrt(x)` to
be "`If x is greater than 0 when the procedure is invoked, then after the execution of the
procedure, y is an approximation to the square root of x`".

Notice that the "`requires`" and "`effects`" assertions permit us to say nothing about the value of
`y` unless `x` is greater than `0`.

**In using a specification to reason about the meaning of a procedure call, we follow two distinct
  rules**:

1. After the execution of the procedure we can assume that the postcondition holds.

2. We can assume only those properties that can be inferred from the post-condition.

The two rules mirror the **two benefits of abstraction by specification**. 

**The first** asserts that users of the procedure need not bother looking at the body of the
procedure in order to use it. They are thus spared the effort of first understanding the details of
the computations described by the body and then abstracting from these details to discover that the
procedure really does compute an approximation to the square root of its argument. For complicated
procedures, or even simple ones using unfamiliar algorithms, this is a nontrivial benefit.

**The second** rule makes it clear that we are indeed abstracting from the procedure body, that is,
forgetting some supposedly irrelevant information. This insistence on forgetting information is what
distinguishes abstraction. 
<!-- Trouble visualizing this. Are they saying that, for example: -->
<!-- If the post-condition is met (if something is true at the completion of the procedure), you can 
    infer something about how the procedure was called -->

### Kinds of Abstractions

<!-- section 1.2.3 -->

Abstraction by parameterization and by specification are powerful methods for program construction.
They enable us to define three different kinds of abstractions: **procedural abstraction**, **data
abstraction**, and **iteration abstraction**.(In general, each of these will incorporate both
abstraction by parameterization and abstraction by specification within it.)

**Procedural abstractions** are abstractions that are operationlike. Procedural abstraction allows
us to extend the virtual machine defined by a programming language by adding a new operation. This
kind of extension is most useful when we are dealing with problems that are conveniently
decomposable into independent functional units. Often, however, it is more fruitful to think of
adding new kinds of data objects to the virtual machine. For example, `sqrt` is like an operation:
It abstracts a single event or task. (Note that `sqrt` incorporates both abstraction by
parameterization and abstraction by specification.)

A **data abstraction** (or data type) consists of a set of objects and a set of operations
characterizing the behavior of the objects. The behavior of the data objects is expressed most
naturally in terms of a set of operations that are meaningful for those objects. This set includes
operations to create objects, to obtain information from them, and possibly to modify them. For
example, `push` and `pop` are among the meaningful operations for stacks, while integers need the
usual arithmetic operations.

An **Iteration abstraction** is used to avoid having to say more than is relevant about the flow of
control in a loop. A typical iteration abstraction might allow us to iterate over all the elements
of a *multi_set* (see below) without constraining the order in which the elements are to be
processed.

### Example

<!-- page 9, bottom -->

As an example, consider *multi_sets*. ['set' refers to an operation that sets, 'multi' refers to
these operations occurring more than once.] 

*Multi_sets* operations include `empty`, `insert`, `delete`, `number_of`, and `size`. 

<!-- properly define runtime environment? -->

The operations might be implemented within the runtime environment of the programming language by
calls to various procedures. Programmers using *multi_sets*, however, need not worry about how
these procedures are implemented. To them empty, insert, delete, number_of, and size are
abstractions define by such statements as 
`"The size of the multi_set insert(s, e) is equal to size (s) + 1."`, and 
`"For all e, the number_of times e occurs in the multi_set empty( ) is 0."`.

The key thing to notice is that each of these statements deals with more than one operation. **We do
not present independent definitions of each operation, but rather define them by showing how they
relate to one another. The emphasis on the relationships among operations is what makes a data
abstraction something more than just a set of procedures.** The importance of this distinction is
discussed throughout this book.
