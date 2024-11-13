# Object-Oriented Programming (Basic Concepts)

<!-- [Page 200] -->

**Objects**: Objects are the core things that Python programs manipulate. Every object has a *type*
  that defines the kinds of things that programs can do with that object. (Section 2.2.1)

**The key to object-oriented programming**: think about objects as collections of both data *and*
  the methods that operate on that data


<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈***≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
## 4.5 Methods, Oversimplified
<!-- [Page 109] -->

**Methods are function-like objects**: they can be called with parameters, return values, and have
side effects. For now, **think of methods simply as functions invoked with a peculiar syntax, dot
notation**. With a function we put the first argument inside parentheses following the function
name; with a method, we use dot notation to place that argument before the function name. e.g.
`object.method_name()`
 
<!-- (They do differ from functions in some important ways, which we will discuss in Chapter 10.) -->
<!-- I'm not sure they actually did! -->

Many useful operations on built-in types are methods, and therefore invoked using dot notation. For
example: for a string `s` there is `s.find`. The `find` method can be used to find the index of the
first occurrence of a substring in `s`. So, if `s` were `'abcbc'`, the invocation `s.find
('bc')` would return `1`.

Attempting to treat `find` as a function, e.g. invoking `find(s,'bc')`produces the error message
`NameError: name 'find' is not defined`.

<!-- maybe read this -->
<!-- https://stackoverflow.com/questions/46312470/difference-between-methods-and-attributes-in-python -->

<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈***≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
## Abstract Data Types and Classes
<!-- section 10.1 -->

["Abstract" qualifies the main noun "data type".]

An **abstract data type** is a set of objects and the operations on those objects. Objects and
operations are bound together so that programmers can pass an object from one part of a program to
another, and in doing so provide access not only to the data attributes of the object but also to
operations that make it easy to manipulate that data. Examples of data types are: integers, lists,
floats, strings, and dictionaries.

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

We have been using abstract data types (without calling them that) throughout this book. We have
written programs using integers, lists, floats, strings, and dictionaries without giving any
thought to how these types might be implemented. In Python, we implement data abstractions
using **classes**. 

Each class definition begins with the reserved word `class` followed by the name of the class and
some information about how it relates to other classes.

Consider the following class definition:

```Python

# textbook page 201
# The first class definition seen: "a tiny (and totally useless) class definition"

# There are three attributes associated with this class: __init__, add, and size.
# Each is of type `function`. 

class Toy(object):
    def __init__(self):
        self._elems = []
    
    def add(self, new_elems):
        """new_elems is a list"""
        self._elems += new_elems
    
    def size(self):
        return len(self._elems)

```

The first line indicates that `Toy` is a subclass of `object`. (For now, ignore what it means to be
a subclass.)

A class definition creates an object of type `type` and associates with that class object a set of
objects called **attributes**. In this example, the three attributes associated with the class are
`__init__`, `add`, and `size`. Each is of type `function`. 


```Python

# this asks to print the type of Toy (it is of type "type")
print( type(Toy) ) 
# <class 'type'>

# this asks to print the type of each of the attributes of the class (they are of type "function")
print( type(Toy.__init__), type(Toy.add), type(Toy.size) )
# <class 'function'> <class 'function'> <class 'function'>

```

<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
### `__init__`
<!-- [Page 202] -->

As we will see, Python has a number of special function names that start and end with two
underscores. These are called **special methods** aka *magic methods*.

<!-- A method that is called implicitly by Python to execute a certain operation on a type, such as addition. Such methods have names starting and ending with double underscores. Special methods are documented in Special method names. -->
<!-- https://docs.python.org/3/reference/datamodel.html#object.__init__ -->

The first of these we will look at is `__init__`.

**Whenever a class is instantiated, a call is made to the `__init__` function defined in that
class**.

For example: 

When the line of code `s = Toy()` is executed the interpreter will create a new **instance**
(`s`) of *type* `Toy`. 

```Python

# same as above, for easy reading
class Toy(object):
    def __init__(self):
        self._elems = []
    
    def add(self, new_elems):
        """new_elems is a list"""
        self._elems += new_elems
    
    def size(self):
        return len(self._elems)
 
```

Then `Toy.__init__` is called (with the newly created object `s` as the actual parameter that is
bound to the formal parameter `self`) and it creates the list object `_elems`, which becomes part
of the newly created instance of type `Toy`. The list `_elems` is called a **data attribute** of
the instance of `Toy`. 

Note 1: The list is created using the notation `[]`, which is simply an abbreviation for `list
()`.  
Note 2: `_elems` seems to be just a name (likely some type of convention); it doesn't seem to
be a reserved word in Python.

### SOS

A class should not be confused with instances of that class, just as an object of type *list* should
not be confused with the list *type*.

```Python

# textbook page 203
t1 = Toy()
t2 = Toy()

print( type( t1 ) ) # <class '__main__.Toy'>

print( type( t1.add ) ) # <class 'method'>
print( type(Toy.add) ) # <class 'function'> 
# Notice that `t1.add` is of type method, whereas `Toy.add` is of type function. 
# Because t1.add is a method, we can invoke it using dot notation.

print( t1 is t2 ) #False (this is a test for object identity)

```

————————————
<!-- ≈≈≈≈≈≈ 12 character line (EM Rule —) ≈≈≈≈ -->

**Attributes** can be associated either with a class itself or with instances of a class:

* Class attributes are defined in a class definition; for example `Toy.size` is an attribute of the
  class `Toy`. When the class is instantiated by the statement `t = Toy()`, for example; instance
  attributes, such as `t.size`, are created.

    - `t.size` is initially bound to the `size` function defined in the class `Toy`, but that
      binding can be changed during the course of a computation. For example, you could
      (but definitely should not!) change the binding by executing `t.size = 3`.

* When data attributes are associated with a class, we call them *class variables*. When they are
  associated with an instance, we call them *instance variables*. 
  
    - For example, `_elems` is an instance variable because for each instance of class `Toy`,
      `_elems` is bound to a different list. [So far, we haven't seen a class variable. We will use
      one in Figure 10-4.] 

Now, consider the code

```Python

t1 = Toy()
t2 = Toy()

t1.add([3, 4]) # adds the integers 3 and 4 to the _elems instance variable in t1
t2.add([4]) # adds the integers 4 to the _elems instance variable in t2

print( t1.size() + t2.size() ) # adds the length of the list in t1 to the length of the list in t2
#         2      +     1

```

Since each instance of `Toy` is a different object, each instance of type Toy will have a different
`_elems` attribute. Therefore, the code prints 3.

<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->

### Keyword `self` (first parameter of a method)
<!-- [Page 204] -->

At first blush, something appears to be inconsistent in this code. It looks as if each method is
being called with one argument too few. For example, add has two formal parameters, but we appear
to be calling it with only one actual parameter. This is an artifact of using dot notation to
invoke a method associated with an instance of a class. The object associated with the expression
preceding the dot is implicitly passed as the first parameter to the method. Throughout this book,
we follow the convention of using `self` as the name of the formal parameter to which this actual
parameter is bound. Python programmers observe this convention almost universally, and we strongly
suggest that you use it as well.

[summary below from  
https://stackoverflow.com/questions/2709821/what-is-the-purpose-of-the-self-parameter-why-is-it-needed ]

Python decided to do methods in a way that makes (the instance to which the method belongs) be
passed automatically, but not received automatically: the first parameter of any method is the
instance the method is called on. That makes methods entirely the same as functions and leaves the
actual name to use up to you (keep in mind that 'self' is the name used by convention, and people
will generally frown at you when you use something else.). 

The reason you need to use `self` is because Python does not use special syntax to refer to instance
attributes. `self` is not special to the code, it's just another object.

[Python could have done something else to distinguish normal names from attributes but it didn't.
Python's all for making things explicit, making it obvious what's what; and although it doesn't do
it always, it does do it for instance attributes. That's why assigning to an instance attribute
needs to know what instance to assign to, and that's why it needs `self`.]

<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
### Example of a class definition
<!-- [Page 205] -->

Let's look at a more interesting example. Figure 10-1 contains a class definition that provides a
straightforward implementation of a set-of-integers abstraction called `Int_set`. (Given that Python 
has a built-in type `set`, this implementation is both unnecessary and unnecessarily complicated. 
However, it is pedagogically useful.)

Notice that the docstring (the comment enclosed in `"""`) at the top of the class definition 
describes the abstraction provided by the class, not information about how the class is implemented. 
The docstring contains information for programmers who might want to use the abstraction.

In contrast, the comments below the docstring contain information about the implementation. That
information is aimed at programmers who might want to modify the implementation or build subclasses 
(see Section 10.2) of the class.

```Python

# textbook page 205
# Figure 10-1

class Int_set(object):

    """An Int_set is a set of integers"""
    
    # Information about the implementation (not the abstraction):
    #   * Value of a set is represented by a list of ints, self._vals.
    #   * Each int in a set occurs in self._vals exactly once.

    def __init__(self):
        """Create an empty set of integers"""
        self._vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if e not in self._vals:
            self._vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self._vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self._vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def get_members(self):
        """Returns a list containing the elements of self._
           Nothing can be assumed about the order of the elements"""
        return self._vals[:]
    
    def union(self, other):
        """other is an Int_set
           mutates self so that it contains exactly the elemnts in self
           plus the elements in other."""

    def __str__(self):
        """Returns a string representation of self"""
        if self._vals == []:
            return '{}'
        self._vals.sort()
        result = ''
        for e in self._vals:
            result = result + str(e) + ','
        return f'{{{result[:-1]}}}'

```

As we have seen, methods associated with an instance of a class can be invoked using dot notation. 

For example, the code below creates a new instance, `s`, of `Int_set`; then inserts the integer `3`
into that instance; and then prints `True`.

```Python

s = Int_set()
s.insert(3)
print(s.member(3))

```

<!-- continues at page 206 -->
<!-- talks about data abstraction, maybe good to put in other notes -->

<!-- Data abstraction achieves representation-independence. Think of the implementation of an abstract
type as having several components:

* Implementations of the methods of the type

* Data structures that together encode values of the type

* Conventions about how the implementations of the methods are to use the data structures; a key
  convention is captured by the representation invariant

The **representation invariant** defines which values of the data attributes correspond to valid representations of class instances. The representation invariant for Int_set is that vals contains no duplicates. The implementation of __init__ is responsible for establishing the invariant (which holds for the empty list), and the other methods are responsible for maintaining that invariant. That is why insert appends e only if it is not already in self.vals.

The implementation of remove exploits the assumption that the representation invariant is satisfied when remove is entered. It calls list.remove only once, since the representation invariant guarantees that there is at most one occurrence of e in self.vals.
 -->

<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
### `__STR__`
<!-- bottom of page 206 -->

`__str__`, is another one of those *special methods* with `__`. The `__str__` method of a class is
invoked when a program converts an instance of that class to a `string` by calling str. Therefore,
when the print command is used, the `__str__` function associated with the object to be printed is
invoked. 

For example:

```Python

s = Int_set()
s.insert(3)
s.insert(4)

print( str(s) ) # {3,4}

print( 'The value of s is', s ) # The value of s is {3,4}
# (If no __str__ method were defined, executing print(s) would cause something like
# <__main__.Int_set object at 0x1663510> to be printed.)

```

### 10.1.1 Magic Methods and Hashable Types
<!-- page 207 -->

One of the design goals for Python was to allow programmers to use classes to define new types that
are as easy to use as the built-in types of Python. Using magic methods to provide class-specific
definitions of built-in functions such as `str` and `len` plays an important role in achieving this
goal. Magic methods can also be used to provide class-specific definitions for infix operators such
as `==` and `+`.

The names of the methods available for infix operators are:

| **operator** |   **method**   |
|:------------:|:--------------:|
|      `+`     |    `__add__`   |
|      `-`     |   `__sub__ `   |
|              |                |
|      `*`     |    `__mul__`   |
|     `**`     |    `__pow__`   |
|              |                |
|      `/`     |  `__truediv__` |
|     `//`     | `__floordiv__` |
|      `%`     |    `__mod__`   |
|              |                |
|      `&`     |    `__and__`   |
|      `|`     |    `__or__`    |
|      `∧`     |    `__xor__`   |
|              |                |
|     `<<`     |  `__lshift__`  |
|     `>>`     |  `__rshsift__` |
|              |                |
|      `<`     |    `__lt__`    |
|      `>`     |    `__gt__`    |
|     `==`     |    `__eq__`    |
|     `<=`     |    `__le__`    |
|     `!=`     |    `__ne__`    |
|     `>=`     |    `__ge__`    |

## References

* Guttag, John, *Introduction to computation and programming using Python: with application to
  understanding data* (Second edition. ISBN 9780262529624)
   
* Guttag, John, *Introduction to computation and programming using Python: with application to
  computational modeling and understanding data* (Third edition. ISBN 9780262542364)
