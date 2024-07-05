# Procedural Abstraction

<!-- chapter 3 -->

In this chapter we discuss the most familiar kind of abstraction used in programming, the procedural
abstraction, or procedure for short. Anyone who has introduced a subroutine to provide a function
that can be used in other programs has used procedural abstraction. Procedures combine the methods
of abstraction by parameterization and specification in a way that allows us to abstract a single
operation or event, such as computing the `gcd` of two integers or sorting an array.

A procedure provides a transformation from input arguments to output arguments. More precisely, it
is a mapping from a set of input arguments to a set of output results, with possible modifications
of the inputs. The set of inputs or outputs or both might be empty. For example, `gcd` has two
inputs and one output, and it does not modify its inputs. By contrast, `remove_dupls` has one input
and no output, and it does modify its input.

We begin with the benefits of abstraction and, in particular, of abstraction by specification. Next
we discuss specifications and why they are needed. Then we discuss how to specify and implement
procedures, and we conclude with some general remarks about their design.

## The Benefits of Abstraction

<!-- section 3.1 -->

Abstraction by specification provides a method for achieving a program
structure with two advantageous properties: *locality* and 

**Locality** means that the implementation of one abstraction can be read or written without our
needing to examine the implementation of any other abstraction. To write a program that uses an
abstraction, a programmer need understand only its behavior, not the details of its
implementation.

<!-- Locality is beneficial both when a program is being written and later when someone wants to understand it or reason about its behavior. Because of locality, different abstractions that make up a program can be implemented by people working independently. One person can implement an abstraction that uses another abstraction being implemented by someone else. As long as both people agree on what the used abstraction is, they can work independently and still produce programs that work together properly. Also ... -->

**Modifiability**: abstraction by specification helps to bound the effects of program modification
and maintenance. If the implementation of an abstraction changes but its specification does not, the
rest of the program will not be affected by the change. Of course, if the number of abstractions
that must be reimplemented is large, making a modification will still be a lot of work. 

<!-- As will be discussed later, the workload can be reduced by identifying potential modifications while designing the program and then trying to limit their effects to a small number of abstractions. For example, if the effects of machine dependencies can be limited to just a few modules, the result will be software that can be transported readily to another machine. -->

Modifiability leads to a sensible method of tuning performance. Programmers are notoriously bad at
predicting where time will actually be spent in a complex system, probably because it is difficult
to anticipate where bottlenecks will arise. Since it is unwise to invest effort in inventing
structures that avoid nonexistent bottlenecks, a better method is to start with a simple set of
abstractions, run the system to discover where the bottlenecks are, and then reimplement the
abstractions that are bottlenecks.

## Specifications of Procedural Abstractions

<!-- section 3.3 -->

**The specification of a procedure consists of a header and a description of effects**. 

* The header gives the name of the procedure and the number, order, and types of its inputs and
  outputs

* Names must be given for the inputs and may be given for the outputs

For example, the header for `remove_dupls` is `remove_dupls = proc (a: array[int])`; the header of
`sqrt` is `sqrt = proc (x: real) returns (rt: real)`.

**The information in the header is just syntactic; it describes the "form" of the procedure**. It is
similar to a description of the "form" of a mathematical function, as in `f: integer —► integer`. 

The meaning (what the procedure or the function does) is not captured in the header, but in the
semantic part of the specification. (The behavior of the procedure is described in English,
possibly extended with convenient mathematical notation.) This description makes use of the names
of the inputs and outputs.

Figure 3.2 shows a template of a procedure specification. **The semantic part of a specification
consists of three parts: the requires, modifies, and effects clauses**. These clauses should appear
in the order shown, although the `requires` and `modifies` clauses are optional.

### Specification template for procedural abstractions.

```

Figure 3.2 Specification template for procedural abstractions.

pname = proc (...) returns (...)
    requires % this clause states any constraints on use
    modifies % this clause identifies all modified inputs
    effects % this clause defines the behavior

```

## Implementing Procedures

<!-- section 3.4 -->

The implementation of a procedure should produce the behavior defined by its specification. In
particular:

* it should modify only those inputs that appear in the `modifies` clause

* for all inputs that satisfy the `requires` clause, it should produce the outputs in accordance
  with the `effects` clause

Every programming language includes some mechanism for implementing procedural abstractions. 
<!-- (In CLU, these abstractions are implemented by means of CLU procedures, or procs for short.) -->

<!-- Figure 3.4 shows two CLU procs that implement search; one uses linear search, while the other uses binary search. These two implementations differ in many details. -->
<!-- For example, for all but very small arrays, binary search is faster than linear search.  -->
<!-- Moreover, if x appears in a more than once, the two procs may return different indexes.  -->
<!-- Finally, if x is contained in a but a is not sorted, the proc using binary search may return high (a) +1 when the other proc finds x or vice versa (consider a = [1: 1, 7, 6, 4, 9] and x = 7, for example). -->
<!-- Nevertheless, both procs are correct realizations of the search abstraction since both provide behavior that is consistent with the specification. -->

In the example procedures we have followed some conventions to enhance program readability.

* First, we have used the same names for the formals as were used in the specification. This
  convention makes it easier to relate an implementation of an abstraction to the specification
* Following the header, we have included a comment explaining the algorithm in use
* Finally, we have adopted formatting conventions to make the code easy to read

As an example, consider sorting an array. One possible method is *merge sort*, which reduces the
problem to that of merging two arrays that have already been sorted. We begin by dividing the array
in half, then sort each half and merge the results:

Figure 3.5 shows the specifications of `sort` and the two subsidiary abstractions. Note that `sort`
does not modify its input array and that both `merge` and `merge_sort` are partial. 

```

Figure 3.5 Specification for merge sort.

% sort the first half of the array
% sort the second half of the array
% merge the two sorted halves

sort = proc (a: array[int]) returns (b: array[int])
    effects Returns a new array, with the same bounds as a, and containing the elements of a 
            arranged in ascending order.

merge_sort = proc (a: array[int], low, high: int) returns (array[int])
    requires low(a) < low < high < high{a).

    effects Returns a new array with the same low bound as a and containing elements 
            a[low], ... , a[high] arranged in ascending order.

merge = proc (a, b: array [int]) returns (array [int])
    requires a and b are sorted in ascending order.
    
    effects Returns a new array with the same low bound as a and containing the elements of a and b 
            arranged in ascending order.

```

To carry out these steps we use two subsidiary procedures: `merge`, to do the merging, and
`merge_sort`, to carry out the sorting of a subpart of the array. `merge_sort` itself will carry
out the same three steps on the subpart of the array, giving a recursive algorithm.

Figure 3.6 shows CLU[^CLU] procs that implement the abstractions.

[^CLU]: CLU is a programming language created at MIT by Barbara Liskov and her students starting in
1973. While it did not find extensive use, it introduced many features that are used widely now,
and is seen as a step in the development of object-oriented programming. 

<!-- page 65 -->

```

Figure 3.6 An implementation of merge sort.

ai = array [int]

sort = proc (a: ai) returns (ai)
    % sort using merge sort
    if ai$empty(a) then
        % create empty array with low bound low(a)
        return (ai$create(ai$low(a)))
        end
    return (merge_sort(a, ai$low(a), ai$high(a)))
    end sort

merge_sort = proc (a: ai, low, high: int) returns (ai)
    if low < high
        then % sort the two halves of a and merge the result
            mid: int := (low + high)/2
            return (merge(merge_sort(a, low, mid),
                merge_sort(a, mid + 1, high)))
    else % a is already sorted, but we must return new array
    b: ai := ai$create(low)
    ai$addh(b, a[low])
    return (b)
    end
    end merge _sort
    
merge = proc (a, b: ai) returns (ai)
    a_low: int := ai$low(a)
    b_low: int := ai$low(b)
    a_high: int := ai$high(a)
    b_high: int := ai$high(b)
    c: ai := ai$create(a_low) % start off with low bound a_low
    % merge a and b
    while a_low <= a_high cor b_low <= b_high do
        if a_low > a_high cor (b_low <= b_high cand b[b_low] < a[a_low])
            then % move element from b, either because all elements of a have
                % been moved, or because the next element of b is less than the
                % next element of a
                ai$addh(c, b[b_low])
                b_low := b_low + 1
            else % move element from a
                ai$addh(c, a[a_low])
                a_low := a_low + 1
            end
        end % while
    return (c)
    end merge

```


<!-- what's below might be beyond the scope of interest for now -->

<!-- ## More General Procedures -->

<!-- section 3.5 -->

<!-- The `sort` procedure discussed previously will work for any array of integers. If it applied to other kinds of arrays, such as arrays of characters, strings, or reals, it would be more generally useful. We can achieve this extra generality, which comes from carrying abstraction by parameterization further than we have done so far, by using data types as parameters. Types are clearly useful as parameters. Evidence for this is the fact that many built-in data types, such as arrays, records, and procedures, are parameterized by types. It is true in general that whatever is useful at the level of a programming language is probably also useful for its users, and there is no doubt that type parameters fall into this category. -->

<!-- When types are used as parameters, some parameter values may not be meaningful. For example, arrays can be sorted only if the elements belong to a type that is totally ordered. Constraints on type parameters take the form of requiring the parameter type to have certain operations that must behave in certain ways. The specification of an abstraction must state such constraints in the requires clause. -->
