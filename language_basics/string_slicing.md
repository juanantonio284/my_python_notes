# Slicing

## TLDR

A slice is an object usually containing a portion of a sequence. 

```Python

s = 'Python is Fun!'

s[1:5] # 'ytho'

s[:5] # 'Pytho'

s[1:] # 'ython is Fun!'

s[:] # 'Python is Fun!'

s[1:12:2] # 'yhni u'

s[1:12:3] # 'yoiF'

s[::2] # 'Pto sFn'
# this is the full string s (from index 0 through 13), with a step size of 2 (every other character)

```

## Definitions

A slice is an object usually containing a portion of a sequence. 

Slice objects can be generated when extended indexing syntax is used—e.g. 
`variable_name [start:stop:step]` or `variable_name[start:stop, i]`. This extended syntax (bracket 
or subscript notation) uses objects of the [slice class][] internally.

```

class slice(stop)
class slice(start, stop, step=None)

```

Return a slice object representing the set of indices specified by `range(start, stop, step)`. `stop
argument` must be passed; the `start` and `step` arguments default to `None`.

slice objects have read-only data attributes `start`, `stop`, and `step` which merely return the
argument values (or their default). They have no other explicit functionality; however, they are
used by NumPy and other third-party packages.

See [itertools.islice()][] for an alternate version that returns an iterator.

## Discussion

Slicing is used to extract substrings of arbitrary length. 

If s is a string, the expression `s[start:end]` denotes the substring of s that starts at index
`start` and ends at index `end-1`. For example, `'abc'[1:3]` evaluates to `'bc'`. 

Why does it end at index `end-1` rather than `end`? So that expressions such as `'abc'[0:len
('abc')]` have the value you might expect. 

If the value before the colon is omitted, it defaults to 0. If the value after the colon is omitted,
it defaults to the length of the string. Consequently, the expression `'abc'[:]` is semantically
equivalent to the more verbose `'abc'[0:len('abc')]`. 

It is also possible to supply a third argument to select a non-contiguous slice of a string. For
example, the value of the expression `'123456789'[0:8:2]` is the string `'1357'`.


<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->

## References

* Guttag, John, *Introduction to computation and programming using Python: with application to
  computational modeling and understanding data* (Third edition. ISBN 9780262542364)
* https://docs.python.org/3/glossary.html#term-slice
* https://docs.python.org/3/library/functions.html#slice
* https://docs.python.org/3/library/itertools.html#itertools.islice

[slice class]: https://docs.python.org/3/library/functions.html#slice
[itertools.islice()]: https://docs.python.org/3/library/itertools.html#itertools.islice
