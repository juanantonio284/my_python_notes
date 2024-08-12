# Unit 6, Lesson 11, Session 3, Slide 41

# Take a list and generate subset lists from it

def genSubsets(L):

    res = [] # this is created and re-filled everytime the function runs
    print( "function start" )                         #debug .....
    print( "\t", "function called with list:", L )    #debug .....
        
    # Base case of the recursion: when L is empty
    if len(L) == 0:
        print( "\t", "base case, ending function" )   #debug .....        
        return [[]]  # Return list of empty list

                     # Remember that we always get to the base case at some point and this is where
                     # the function ends. In this example, we end the function by 
                     # returning the empty set.

    # Recursion
    print( "\t", "\t", "re-calling function with list:", L[ :-1] )       #debug .....
    smaller = genSubsets( L[ :-1] )  # this calls the function with a list that does not include 
                                     # the last element and assigns the end result (the return) of 
                                     # the function to "smaller". 
                                     # "smaller" is thus a list of lists.
                                     
    # The rest of the program
    print( "--------------------" )                                       #debug .....
    print( "After recursive call to function" )                           #debug .....       
    print( "\t", "this corresponds to function called with list:", L )    #debug .....         
    extra = L[-1: ]  # extra is a list that contains just the last element of the list that was 
                     # passed as an argument to this call of the function 
                     # (every call, the list passed gets less big)
    new = [] # this is created and re-filled everytime the function runs 
             # it is where the "new" subsets discovered in this call will be put
    
    print( "\t", "extra:", extra )                            #debug .....
    
    print( "\t", "smaller (from last call):", smaller )       #debug .....
    
    # the "smaller" used at this point is the smaller that comes from the previous function call
    # since "smaller" is a list of lists, "small" is a list (don't treat it as some other type)
    for small in smaller:
        print( "\t", "--------" )             #debug .....
        print( "\t", "inside loop" )          #debug .....
        print( "\t", "\t", "small:", small )  #debug .....
        print( "\t", "\t", "new:", new )      #debug .....
        
        new.append(small+extra)
        print( "\t", "\t", "append (small+extra) to new:", new )                      #debug .....
        print( "\t", "\t", "end of function, return smaller+new:", smaller+new )      #debug .....

    return smaller+new  # take the "smaller" which came from the last call and add the new 
                        # sets discovered in this call


# ..................................................................................................
# sample usage -------------------------------------------------------------------------------------

sample_list = [1,2]
genSubsets(sample_list)
