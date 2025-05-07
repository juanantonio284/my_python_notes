# Recursions 1 (Unit 2, Lesson 4) -- Part 2 of code

# SEE MARKDOWN FILE OF THE SAME NAME FOR BETTER FORMATTING AND EXPLANATIONS

## Session 8

### Towers of Hanoi

# The Towers of Hanoi is a game where there are 3 pillars and, on one pillar, there is a stack of 64
# disks of different sizes, with the largest disk at the bottom and the smallest disk at the top.
# The goal of the game is to move the disk stack to another pillar following these rules:

# * Movement: can only move one disk at a time
# * Arrangement: a larger disk can never cover up a small disk

# **Strategy for two disks**:

# * Move the smaller top disk to a spare pillar
# * Move the larger bottom disk to another spare pillar
# * Move the smaller disk to the other spare pillar (on top of the larger disk)

# **Strategy abstracted**:

# * There is a stack of n disks
# * Move a stack of size n-1 to a spare pillar
# * Move a single disk n (the one that was at the bottom of the stack) to another spare pillar
# * Move the stack of size n-1 to the other spare pillar (on top of disk n)

# **Strategy abstracted further**:

# * Three locations denominated as such:
    # - `fr`: the pillar *from* where the stack is moved
    # - `to`: the pillar *to* where the stack is moved
    # - `spare`: the pillar that is empty, *spare*

# * The "movements" are made with words, e.g. "move from a to spare", "move from a to b", "move from
#   spare to b"
    # - this is done with a print statement `print( 'move from ' + str(fr) + ' to ' + str(to) )`
    # - this print statement runs through a function which "loads the coordinates" `fr` and `to`
    # - this function is called `printMove`
    
# * The movements are as follows:
    # -  Move stack of size `n-1` from the `fr` pillar to the `spare` pillar 
    # -  Move the base case `1` (a single disk) to another pillar 
    # -  Move stack of size `n-1` from the spare to the `to` pillar (on top of the single disk) 

# * The movements are elicited by the `Towers` function, which:
    # - organizes the movements
    # - calls the `printMove` function that makes the movements

# * The three necessary movements are organized through these (recursive) calls:
    # - `Towers( n-1, fr, spare, to )`
    # - `Towers( 1, fr, to, spare )`
    # - `Towers( n-1, spare, to, fr )`

# ................................................

### Towers of Hanoi Code

# unit 2, lesson 4, session 8, slide 55
# Towers of Hanoi

# (i)
def printMove(fr, to):
    print( 'move from ' + str(fr) + ' to ' + str(to) )

# (ii)
def Towers( n, fr, to, spare ):
    
    if n == 1: # base case, a stack of size 1
        printMove(fr, to)
    
    else:
        # Towers function is called recursively 3 times below
        
        Towers( n-1, fr, spare, to )
        Towers( 1, fr, to, spare )
        Towers( n-1, spare, to, fr )

# tester .........................................
Towers(4, "a", "b", "spare pillar") # each pillar has been named a, b, and c

# the calls above might be better understood if written as below

#       Towers( n = n-1, fr = fr,    to = spare, spare = to )
#       Towers( n = 1,   fr = fr,    to = to,    spare = spare )
#       Towers( n = n-1, fr = spare, to = to,    spare = fr )

# i.e. this makes it more clear how the PASSED arguments move around for each call, but the expected
# arguments stay the same as when they were defined


# The sample call `Towers(4, "a", "b", "spare pillar")` means:

# 1. When entering the function, following the function definition `Towers( n, fr, to, spare )`:
#  `n = 4`, `fr = "a"`, `to = "b"`, and `spare = "spare pillar"`.

# 2. The values above go in the first type of call `Towers( n-1, fr, spare, to )`. This call means
# that the values passed to the towers function are rearranged as such:

#     * the `n` argument is passed the value n-1: 3
#     * the `fr` argument is passed the original value of `fr`: "a"
#     * the `to` argument is passed the original value of `spare`: "spare pillar"
#     * the `spare` argument is passed the original value of `to`: "b"

# 3. The second type of call `Towers( 1, fr, to, spare )` means that:

#     * the `n` argument is passed the value `1`, which will trigger the `if` clause
#     * the other arguments are passed the original values

# 4. The third type of call `Towers( n-1, spare, to, fr )` means that: 

#     * the `n` argument is passed the value n-1: 3
#     * the `fr` argument is passed the original value of `spare`: "spare pillar"
#     * the `to` argument is passed the original value of `to`: "b"
#     * the `spare` argument is passed the original value of `fr`: "a"

# 5. maybe it would have been better form to write as such:

Towers( n = n-1, fr = fr,    to = spare, spare = to )
Towers( n = 1,   fr = fr,    to = to,    spare = spare )
Towers( n = n-1, fr = spare, to = to,    spare = fr )


# ................................................

### Towers of Hanoi Code (with comments and debugs)

# unit 2, lesson 4, session 8, slide 55
# Towers of Hanoi (with comments and debugs)

# (i)
# this function just prints what the recommended move is, e.g. "move from a to b"
def printMove( fr, to ):
    print( 'move from ' + str(fr) + ' to ' + str(to) )

# (ii)
def Towers( n, fr, to, spare ):

    if n == 1: # base case, a stack of size 1
        print( "n:", n, "Inside the first if in the function (base case)" ) #debug .....
        printMove( fr, to )
    
    else:
        # Towers function is called recursively 3 times below
                
        print( "Call 1: Towers( n-1, fr, spare, to )", "| n =", n )              #debug .....        
        print( "\twill re-call the function and start more calls at n-1:", n-1 ) #debug .....
        Towers( n-1, fr, spare, to )

        # this call triggers the base case directly, regardless of value of n
        print( "Call 2: Towers( 1, fr, to, spare )", "| n =", n )                #debug .....
        print( "go directly to Base Case" )                                      #debug .....
        Towers( 1, fr, to, spare ) # n = 1 is the base case
        
        print( "Call 3: Towers( n-1, spare, to, fr )", "| n =", n )              #debug .....
        print( "\twill re-call the function and start more calls at n-1:", n-1 ) #debug .....
        Towers( n-1, spare, to, fr )

        print( "--------------------" )        #debug .....
        print( "--------------------" )        #debug .....    
        print( "End of calls at n =", n )      #debug .....
        print( "--------------------" )        #debug .....
        print( "--------------------" )        #debug .....
    
    print( "\tEnd of 'Towers' function")       #debug .....
    print( "\n" )                              #debug .....        
    
# tester .........................................
Towers(4, "a", "b", "spare pillar") # each pillar has been named a, b, and c


# ***...............................................................................................
## Session 8 Exercises 

# ................................................

### gcdIter and gcdRecur


# unit 2, lesson 4, exercise which follows L4_S8--1_hanoi.md

# 21. Exercise: gcd iter
# an iterative function to find the greatest common divisor

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    testValue = min(a, b)

    # Keep looping until testValue divides both a & b evenly
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1

    return testValue


# unit 2, lesson 4, exercise which follows L4_S8--1_hanoi.md

# 22. Exercise: gcd recur
# a recursive function to find the greatest common divisor

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Base case is when b = 0
    if b == 0:
        return a

    # Recursive case
    return gcdRecur(b, a % b)


# * The order matters—e.g. `gcdRecur(0,1)` is not the same as `gcdRecur(1,0)`.

#     - But you don't need to do separate code to account for this. Just test if `b == 0`.

#     - If it's not (and `a == 0` as in the case `gcdRecur(0,1)`), the function will enter the
#       recursive step and compute `0 % 1 = 0` and put that in the `b` position. Then in the next
#       iteration, the `if` will trigger and return `a` (which was 0).

#     - note that the test is if `b == 0` because you don't want to try to calculate `a%0`, as it is
#       undefined (division by 0)


#### gcdRecur (with comments and debugs)


# unit 2, lesson 4, exercise which follows L4_S8--1_hanoi.md

# 22. Exercise: gcd recur (with comments and debugs)
# a recursive function to find the greatest common divisor

def gcdRecur(a, b):
    
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    print("a:", a)                           #debug.....
    print("b:", b)                           #debug.....
    
    # Base case is when b = 0
    # here, a is returned directly because you don't want to try to calculate `a%0`, as it is
    # undefined (division by 0)      
    if b == 0:
        
        print("---------")                   #debug..... 
        print("---------")                   #debug..... 
        print("inside if: b == 0, return a") #debug.....
        
        return a

    # Recursive case
    print("Recursion will go ahead. New value that will pass to b = a%b =", a%b)    #debug..... 
    print("---------")                                                              #debug.....
    return gcdRecur(b, a % b)

# testers ........................................

gcdRecur(0,1)

gcdRecur(1,0)

gcdRecur(1071,462)

gcdRecur(462,1071)


# ***...............................................................................................
## Session 9

# unit 2, lesson 4, session 9, slide 70

# first fibonacci code

def fib(x):
    """assumes x an int >= 0
    returns Fibonacci of x
    """
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)


# ***...............................................................................................
## Session 10 - Recursion on Non-numerics

# ................................................

### original

# unit 2, lesson 4, session 10, slide 75

# recursion on non-numerics
# check if a string of characters is a palindrome

def isPalindrome(s):
    
    def toChars(s): # (i) ..........
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans 

    def isPal(s): # (ii) ..........
        if len(s) <= 1:
            return True 
        else:
            return s[0] == s[-1] and isPal( s[1:-1] )
    
    return isPal( toChars(s) ) 
    
# ................................................

### commented and explained

# unit 2, lesson 4, session 10, slide 75 
# (commented and explained)

# recursion on non-numerics
# check if a string of characters is a palindrome

# The isPalindrome function contains (i) the toChars function and (ii) the isPal function.

# (i) The toChars function changes uppercase to lowercase and strips out all the spaces and
# punctuation, returns "ans". In the code below, there seems to be no point to it as "ans" is not
# used again (maybe ans should have been passed to isPal).

# (ii) The isPal function checks if s is a palindrome 

# * first it checks if the string s is of length 1 or less (one letter or blank); if it is, it is a
#   palindrome and returns True. This is the line that exits isPal and thus ends the recursion.

# * if s is longer than one letter, it checks if the first s[0] and last element s[-1] are the same
#   s[0] == s[-1] and returns a True/False
#   - if it's True, the isPal function is called again (this is the recursion) with the argument 
#     s[1:-1] i.e. a slice of the string s that starts at the second character and ends at the -1
#     character In other words, the new string passed is a shorter string than the one before with 
#     the first and second letters of the one before removed.

def isPalindrome(s):
    
    def toChars(s): # (i) ..........
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans # Why is this even here? (It's not used and not returned.)

    def isPal(s): # (ii) ..........
        
        # Notice that there is one test to prove if it's true, one test to prove if it's false
        
        if len(s) <= 1:
            return True # THIS is the line that will end the recursion if S is a palindrome
        else:
            return s[0] == s[-1] and isPal( s[1:-1] )
            # THIS is the line that will end the recursion if S is not a palindrome
            # It returns a True/False and, if true,
            # calls the isPal function again with a slice containing the 1st and 2nd letters of s
            # removed. (In the last call, the slice passed is blank "" and the if statement above  
            # returns true and thus exits at the if clause.)
    
    return isPal( toChars(s) ) # THIS is the line that actually gets things going. 
                               # So far, we've only defined functions

# tester .....
isPalindrome("ABba")
isPalindrome("ABcd")

# ................................................

### with explanatory debugs


# unit 2, lesson 4, session 10, slide 75
# (with comments and debugs)

# recursion on non-numerics
# check if a string of characters is a palindrome

def isPalindrome(s):
    
    print( "\n" )                                 #debug....
    print( "Start of isPalindrome function")      #debug....
    print( "\t", "start of function definitions") #debug....
    
    def toChars(s): # (i) ..........
        s = s.lower()
    
        print( "-----------" )            #debug....
        print( "inside toChars function") #debug....
        print( "s:", s )                  #debug....
        
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
            print( "ans:", ans )          #debug.... (inside for loop)
        
        return ans # Why is this even here? (It's not used and not returned.)

    def isPal(s): # (ii) ..........
        
        # Notice that there is one test to prove if it's true, one test to prove if it's false
        
        print( "-----------" )            #debug....
        print( "inside isPal function")   #debug....
        
        if len(s) <= 1:
            print( "    inside if") # debug
            return True # THIS is the line that will eventually end the recursion
        else:
            
            print( "    inside else")                                  #debug .....
            print( "\t", "s[0]:", s[0] )                               #debug .....
            print( "\t", "s[-1]:", s[-1] )                             #debug .....
            print( "\t", "s[0] == s[-1]:", s[0] == s[-1] )             #debug .....
            print( "\t", "the new value passed to isPal is:", s[1:-1]) #debug .....
            
            return s[0] == s[-1] and isPal( s[1:-1] )
            # THIS is the line that will end the recursion if S is not a palindrome
            # It returns a True/False and, if true,
            # calls the isPal function again with a slice containing the 1st and 2nd letters of s
            # removed. (In the last call, the slice passed is blank "" and the if statement above  
            # returns true and thus exits at the if clause.)
                
    print( "\t", "end of function definitions, the next line starts the calls.") # debug....
    
    return isPal( toChars(s) ) # THIS is the line that actually gets things going. 
                               # So far, we've only defined functions

# tester .....
isPalindrome("ABba")
isPalindrome("ABcd")

# ***...............................................................................................
## Session 10 Exercises 

# ................................................

### isIn


# unit 2, lesson 4, exercise which follows L4_S10--1_recursion_non_num.md

# 25. Exercise: is in
# a function that checks if a character is inside an alphabetized string

def isIn(char, aStr):

   '''
   char: a single character
   aStr: an alphabetized string
   
   returns: True if char is in aStr; False otherwise
   '''

   # Base case: If aStr is empty
   if aStr == '':
      return False # character was not found

   # Base case: if aStr is of length 1
   if len(aStr) == 1:
      return aStr == char # a simple test for equality is needed

   # ...........................................................................
   # Base case: see if character in the middle of aStr equals test character 
   midIndex = len(aStr) // 2 # floor division, a division that rounds down to nearest integer.
   midChar = aStr[midIndex]
   if char == midChar:
      return True # character found
   
   # Recursive Case 1
   # If the test character is smaller than the middle character, 
   # recursively search on the first half of aStr
   elif char < midChar: # python can compare characters according to alphabetic position
      return isIn( char, aStr[ :midIndex ] )

   # Recursive Case 2
   # Else, if the test character is larger than the middle character, 
   # recursively search on the latter half of aStr
   else:
      return isIn( char, aStr[ midIndex+1: ] )
      
# ***................................................................................................
# Note:

# * There are three base cases (empty, length == 1, middle character = desired character)
# * It is the base cases that really do the test, the recursives (elif, else) just select the lower 
#   or upper part
#    -  `elif` to select the lower part of the string
#    -  `else` for the upper part of the string

