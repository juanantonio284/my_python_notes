# my_python_notes
Introductory CSCI notes for the Python programming language

Most of the material in this repository is taken from the MITx course 
**Introduction to Computer Science and Programming Using Python (6.00.1x)**

The basis of this material is *copied and pasted* from class slides and transcripts, but I have
arranged, re-arranged, explained, re-explained, commented, and changed comments to make it easier
to understand. In other words, the contents of these files are either *very different* to the
original class material or *essentially the same and don't provide anything new*, depending on how
you want to look at it. Simply put: these are simply my personal notes and they are arranged and
edited in a way that is convenient for me; no claims are made and no guarantees are given.

If you want the complete course material this is not a good place to look. By a standard of "having
all the notes to help me can pass the class" this repo would be disorganized, incomplete in some
ways, and too expansive in other ways.

Note: the course is organized in `units` that contain `lessons` that contain videos and exercises. I
refer to the videos as "`sessions`" (as in *class sessions*) and give them their own numbering.
(The website numbers everything sequentially, but that doesn't make clear that the exercises are
related to the video.)

## Contents

* `oop_basic_concepts.md`: basic concepts of Object-Oriented Programming (e.g. methods, classes)

### recursions

* `basic_examples_recursion.md`

* `recursions_unit_2_lesson_4.md` contains all (or most) of the material regarding recursions
  presented in the course. [I find recursions interesting and wanted to have all the material in
  one place.]

  - `recursions_u2l4_CODE_part_1.py` (and `...part 2`) have the same code as the markdown but are
    ready to use in python

* `genSubsets_explanation.md` contains a recursion to generate subsets from a list. This was seen in
  one of the latter lessons of the course and presented mostly to talk about complexity of the
  code (exponential running time as size of the input gets larger). The explanation in this page is
  much more detailed than anything that was given. There is a `.py` file with the code ready for
  running.

### abstraction

I found the following quote by Edsger Dijkstra fascinating: 

> " ... the effective exploitation of his powers of abstraction must be regarded as one of the most
    vital activities of a competent programmer. In this connection it might be worth-while to
    point out that the purpose of abstracting is not to be vague, but to create a new semantic
    level in which one can be absolutely precise."

so I dug into the subject a little more, starting with notes from the class. 

* `abstraction.md`: introductory notes, with a more practical sense, on function definitions and the
  basic concepts of decomposition and abstraction

* `abstraction_2.md`: more theoretical notes from an old book by Barbara Liskov and John Guttag in
  which they talk about the need for decomposition and abstraction and show its application in the
  CLU language (a precursor to many modern programming languages)

* `abstraction_3_procedural.md`: deeper into the theory seen in file 2

### complexity

* `1_asymp_notation.md`: a description of how asymptotic notation works and what "Big O" and "Big
  Theta" notations represent
  
* `2_merge_sort.md`: a description of how the *merge sort* algorithm works and an analysis of its
  complexity
