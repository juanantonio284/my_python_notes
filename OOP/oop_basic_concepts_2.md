# Object-Oriented Programming (Basic Concepts, Part 2)

See full text [here][book_link]; consider contributing to the author.

[book_link]: https://greenteapress.com/thinkpython2/html/thinkpython2019.html

<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈***≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
## Inheritance

The language feature most often associated with object-oriented programming is inheritance.
**Inheritance is the ability to define a new class that is a modified version of an existing class.**

If we want to define a new object to represent a playing card, it is obvious what the attributes
should be: rank and suit. It is less obvious what type the attributes should be. One possibility is
to use strings like '`Spade`' and `Queen` for suits and ranks. A problem with this implementation
is that it would not be easy to compare cards to see which has a higher rank or suit. An
alternative is to use integers to encode the ranks and suits—i.e. to define a mapping between
numbers and suits, or between numbers and ranks.

```

Suits and the corresponding integer codes

 Suit     Code
Spades      3
Hearts      2
Diamonds    1
Clubs       0 

```

```

Ranks and the corresponding integer codes

 Rank Code
   2   2
   3   3
   .   .
   .   .
   .   .
 Jack 11
Queen 12
 King 13

And we can use either 1 or 14 to represent an Ace, depending on whether we want it to be considered
lower or higher than the other ranks.

```

To represent these encodings, we will use two lists of strings, one with the names of
the suits and the other with the names of the ranks.

Here’s a definition for a class that represents a playing card, with these lists of strings as class
variables (these are variables defined inside a class definition, but not inside a method):

```Python

class Card:
"""Represents a standard playing card."""
suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
              'Jack', 'Queen', 'King', 'Ace']

# The first element of rank_names is None because there is no card with rank zero. By including None
# as a place keeper, we get a list with the nice property that the index 2 maps to the string '2',
# and so on.

```

Class variables are associated with the class, rather than an instance of the class, so we can
access them like this: 

```Python

Card.suit_names 
# ['Clubs', 'Diamonds', 'Hearts', 'Spades']

Card.suit_names[0]
# 'Clubs'

Card.rank_names[11]
# 'Jack'

```


<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈***≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
## Attributes associated to `Card` 

Here’s an `__init__` method for the `Card` class—it takes suit and rank as parameters and assigns
them to attributes with the same names:

```Python

%%add_method_to Card

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

```

This allows:

```Python
# create a Card object
queen = Card(1, 12)
```

When the line `queen = Card(1, 12)` is executed, the interpreter will create a new **instance**
(`queen`) of *type* `Card`. 

Whenever a class is instantiated, a call is made to the `__init__` function defined in that class;
so `Card.__init__` is called (with the newly created object `queen` as the actual parameter that is
bound to the formal parameter `self`) and the instance attributes `suit` and `rank` are created.

```Python

# use the new instance to access the attributes:
queen.suit, queen.rank
# (1, 12)

# It is also legal to use the instance to access the class variables:
queen.suit_names
# ['Clubs', 'Diamonds', 'Hearts', 'Spades']
# But if you use the class, it is clearer that they are class variables, not attributes.

```


<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈***≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
## Printing Cards

Here’s a `__str__` method for `Card` objects:

```Python

%%add_method_to Card
    def __str__(self):
        rank_name = Card.rank_names[self.rank]
        suit_name = Card.suit_names[self.suit]
        return f'{rank_name} of {suit_name}'

```

When we print a `Card`, Python calls the `__str__` method to get a human-readable representation of
the card:

```Python
print(queen)
# Queen of Diamonds
```

The following is a diagram of the `Card` class object (its type is `type`)

```
            Type        List

Card --> suit_names --> ['Clubs', 'Diamonds', 'Hearts', 'Spades']

     --> rank_names --> [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                         'Jack', 'Queen', 'King', 'Ace']
```

The following is a diagram of a `Card` instance (`queen` is an instance of `Card`, so its type is
`Card`)


```
          Card
          
queen --> suit --> 1
          rank --> 11
```

Every `Card` instance has its own `suit` and `rank` attributes, but there is only one `Card` class
object, and only one copy of the class variables `suit_names` and `rank_names`.


<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈***≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
## Comparing Cards

### Test 1

Suppose we create a second Card object with the same suit and rank:

```Python
queen2 = Card(1, 12)
print(queen2)
# Queen of Diamonds
```

If we use the `==` operator to compare them, it checks whether `queen` and `queen2` refer to the
same object:

```Python
queen == queen2
# False
```

They don’t, so it returns `False`. We can change this behavior by defining a special method called
`__eq__`. `__eq__` takes two `Card` objects as parameters and returns `True` if they have the same
suit and rank, even if they are not the same object (i.e. it checks whether they are equivalent,
even if they are not identical).

```Python
%%add_method_to Card
    
    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank
```

```Python
queen == queen2
# True
```

<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
### Test 2

As a second test, let’s create a card with the same suit and a different rank:

```Python
six = Card(1, 6)
print(six)
# 6 of Diamonds
```

```Python
queen != queen2
# False

queen != six
# True
```

If we use the `!=` operator, Python invokes a special method called `__ne__`, if it exists.
Otherwise, it invokes `__eq__` and inverts the result (e.g. if `__eq__` returns `True`, the result
of the `!=` operator is `False`).

<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
### Test 3

Now suppose we want to compare two cards to see which is bigger. If we use one of the relational
operators, we get a `TypeError`:

```Python
queen < queen2
# TypeError: '<' not supported between instances of 'Card' and 'Card'
```

To change the behavior of the `<` operator, we can define a special method called `__lt__`, which is
short for "less than". For the sake of this example, let’s assume that suit is more important than
rank.

```
Suits and the corresponding integer codes

 Suit     Code
Spades      3
Hearts      2
Diamonds    1
Clubs       0 
```

Spades outrank all Hearts, which outrank all Diamonds, and so on. If two cards have the same suit,
the one with the higher rank wins.

<!-- Continue at page 254 -->

```Python



```

```Python



```

```Python



```

```Python



```



```Python



```

```Python



```

```Python



```

```Python



```


```Python



```

```Python



```

```Python



```

```Python



```