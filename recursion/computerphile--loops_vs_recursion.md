# Programming Loops vs Recursion - *Computerphile*

Programming loops are great, but there's a point where they aren't enough.  
[Professor Brailsford explains][link_to_original_video]

<!-- Below is a "horizontal rule" made with 100 hyphens `-` -->
----------------------------------------------------------------------------------------------------

## When were `for` loops invented?

There's a lot of interesting stuff both from the point of view of the content but also the
historical context between. Well, "for loops" is what ALGOL called them but prior to that FORTRAN
called them "DO loops"; and prior to that, they existed in *Assembler*.

So, first of all, what's the history and what does it get you when you can do loops, but when do you
run out of steam—even with loops—and you have to use this—shock! horror!—pure-mathematicians 
thing that computer scientists have to learn about: *recursion*.

It was a real culture shock in the 1940s–1950s to find out that what the theoreticians had been
talking about for years—recursive functions in mathematics—actually had massive importance for
computer science.

Back then, it was all Assembler, or a slightly dressed-up thing called a "macro Assembler" where you
can have little routines full of, y'know, packaged Assembler instructions which could be called-up
when needed.

That sort of served people for quite some time. But probably one of the first high-level languages
to introduce loops was good old FORTRAN. (Even though that was published in '65, FORTRAN itself
goes back, I think, for almost ten years before that. It was invented by John Backus and a large
team of people at IBM in the 1950s. It's an excellent language for engineering and scientific
calculations, it is low level.)

## The Nature Of FORTRAN Loops

When you look at the nature of a FORTRAN loop it's almost like doing it in Assembler, but not quite.

They didn't call them "for" loops—they called them "do" loops.

<!-- https://youtu.be/HXNhEYqFo0o?si=VJzF0gIDGDLSojH_&t=127 -->

```

Line Num |     DO 180 I = 1, 10
         |        ~~~
         |        ~~~
         |        ~~~
     180 |        ~~~

```

You package all this up, where you're saying: "repeat the following sequence of instructions"
(which are represented as wavy lines above). Keep doing them until you hit the statement with a
numeric label on it of "180". Then loop back from the statement labelled "180", back up to here
[the top] and increment the loop counter—which you're all familiar with in languages like C. 

It wasn't done, as it would be in C, by saying: "Here's my block of stuff to be repeated it's inside
these curly braces". Here you can see it's a lot more like assembler, a lot more low-level. There's
nothing magic about "180", it could be "72"—it depended on your labelling system. 

Implicitly here [in `DO 180 I = 1, 10`], in a simple thing like this, it starts off with the counter
`I` at `1`, and every time I returned back [to the top] it would reset `I` to be `2`, `3`, `4` and
so on up to and including `10`. It's comforting for those who were coming from assembler into a
higher-level language to see something that was only slightly higher level, in sophistication, than
assembler was.

## How did loops become more "powerful"

How did loops become more "powerful"?

Well, again, even in assembler and even in FORTRAN, there's no reason why you couldn't have a loop
within a loop.

So I might have, outside of all this code, yet another layer of DO. What shall we say:
"`DO 200 J = 1, 20`". 

```

Line Num | DO 200 J = 1, 20
         |     DO 180 I = 1, 10
         |        ~~~
         |        ~~~
         |        ~~~
     180 |        ~~~
         |        
         |        ~~~
         |        ~~~
     200 |        ~~~

```

So, there might be some more statements between 180 and 200, (who knows?), but again, you see, a
numeric label. And we can see what's happening is that for every setting of J, which will start at
1 and go up to 20, for every single one of those J settings the inner loop will be running through
the complete spectrum of settings of I going from 1 to 10. So you will have 200 locations that are
being affected here. Basically going through the rows and columns of a matrix. 

All sorts of calculations in physics, chemistry and particularly engineering just rely on
two-dimensional arrays full of numbers—either integers or scientific numbers with a decimal
point. and so on. Even hard-core assembly programmers had to admit if you were doing heavy
scientific programming it was nice to be a little bit more abstract and to have this sort of
facility available to you.

## How did people realize that this was not enough? How many nested loops would the compiler allow?

Now you might say: "Well, what came along to spoil the party then?" or "How did people realize that
this was wonderful but not quite enough?" The compiler of course has got to be tolerant and has got
to be capable of compiling nested DO loops correctly but how deep would it let you nest them?

Well, I'm guessing, I would suspect that the early FORTRAN compilers probably wouldn't allow you to
go more than about 10 deep, maximum. And I think you and I Sean have just been looking up what are
the current limits in C?  I seem to remember the earliest gcc was something like 32. But I think we
looked up this ... some C++ nowadays allows you to do nested loops 256 deep! And, of course, there
are multi-dimensional problems that might actually need that.

It doesn't take much knowledge of higher maths to realize if you've got a loop within a loop the
outer loop goes around n times; the inner loop is going around n times, you are then coping with an
n-squared problem. If you put the third loop inside the other two you're coping with a cubic,
three-dimensional, problem. So what we're saying is all these multi-dimensional,
polynomial-going-on-exponential, problems that come up quite naturally, you can cope with them in
nested for-loops so long as they don't need to be more than power-32, or power-256, or whatever it
is.

And you think, well, that should be enough for anybody! There's these multi-dimensional problems you
can just do them by nesting for loops and surely [a depth of] 256 is enough for anybody? What
kind of problem wouldn't it be enough for? 

**What kind of problem is not ideally solved with nested loops?**

Well, a lot of theoretical computer scientists of my knowledge amused me greatly when—those of
them that will own up to this—back in the 60s. People started going to lectures from
mathematicians, theoreticians, people concerned with "Godel Computability" and so on. And of
course those sort of people were very familiar indeed, at a mathematical level, with Ackermann's
function. Now, as you know—you and I—we've [done that one][most_difficult_program].

So what made it so difficult? Well, you write down Ackermann's function and it very clearly ends up
with routines calling themselves recursively in a very very complicated way. Now I think your
average sort of engineer would be happy to say that there's this thing called "*factorial*" which
is 5 times 4 times 3 times 2 times 1, or whatever. And you could do that in a loop as well as doing
this fancy recursion thing, but a lot of theoreticians admitted to me they saw a Ackermann's
function and said: "I could try that out in FORTRAN!". 

Now what they perhaps didn't realize—but it became famous by 1960—is: FORTRAN is wonderful, but
original FORTRAN did not do user-level recursion You could write a thing called "ACK". You could
actually get it to call itself in FORTRAN. But you might have been expecting that every time it
called itself it would lay out a data area for each recursive call, they're called 
["stack frames"][reverse_polish_notation_and_stack]. You [expect to] get lots of stack frames, one 
on top of another and as you come back through the recursion they're deleted and thrown away and you
climb back into your main program. 

But FORTRAN doesn't do that: it sets aside one stack frame. You keep calling yourself recursively it
just tramples in its muddy gumboots over all your data area and you end up with total garbage. It
no more gives you values of the Ackermann function than fly to the moon!

And people said: "I then realized **the importance of having user-level recursion, in programming
languages, to cope with those really hard problems that fell outside nested for-loops**".

ALGOL was famous in that its routines could call themselves recursively and could get the right
answer and, for limited low-order values of Ackermann's function—very slow, very slow indeed—
it would come out with the right answer.

## Applications

> Sean Riley: Is there any need to think of an example of a problem, or program, because Ackermann
  feels to me like it's the test-bed. You know, when you're testing out a motor-car you might take
  it on the track and see how fast it can go. But in day-to-day life that car might only get half
  that speed. What's the real-world kind of equivalent [of something that might need to use
  recursion]? Is there such a thing?

[Something that might need to use recursion] of that complexity? Not many things.  I mean, yes, it's
true that Ackermann, as you know, was David Hilbert's research student. And the challenge was on to
find something that was so innately recursive that—remember it was "*generally recursive*", they
called it, as opposed to "*primitive recursive*". And simple things like factorial and indeed
Fibonacci, are primitive recursive. So I think you're right that you really are just making the
point that eventually there are things that will kill you. 

**What kind of programs *need* recursion? Compilers**

I think the question in the middle is: "Is there something out there—pieces of program you need to
write—where non-trivial recursion, in a sense, is needed but not quite to the horrendous degree
that Ackermann did. And the answer is: "Yes, compilers is where it hit people". 

Because although early FORTRAN did not provide user-level recursion, for you and me, nevertheless
John Backus and his team implemented it in the middle 1950s I think at IBM. And Backus wrote
articles afterwards basically saying: "We didn't know enough about recursion and even though we
didn't provide it for the users of our language, boy did we need it in the compiler! And we ended
up inventing it in all but name".

The syntactic structures of what is legal, in a language, even at the level just of arithmetic
statements can be quite recursive. Because you end up with brackets within brackets within brackets
all with a multiplier outside. And which order do you do the brackets in? And, you know, how how
many levels of bracket nesting can you have. And if you don't get things sorted out correctly then
you'll get the wrong answer.

But once again the problem could be that your users would come up to you and present you with a
problem just designed to test out your compiler, and whether it was robust enough to be able to
cope with a high degree of nesting even just in arithmetic statements. So by 1960 in ALGOL, yeah,
the there were enough users, at the user level, who could see that a modicum of recursion, perhaps
more complicated than factorial but not quite up to full Ackermann capabilities would be very nice
indeed to have within your language.

<!-- [Video ends here, there is a preview of the next video] -->

## Extra Bits

[Loops, Ackermann, & Recursion][loops_ackermann_recursion]  

Well, in the end 32 won't be enough, 128 won't be enough, 256 won't be enough; for high orders of
Ackermann function, it will blow those apart eventually. 
So the only way to do it, generally, is via a recursion mechanism where—as I said—it's all done
in data areas called [stack frames][reverse_polish_notation_and_stack]. You can make the things go
arbitrarily deep just by calling recursively.

So what's the problem then? 
The problem then is you'll eventually run out of memory.
(For those who now want to go off and watch the most difficult program to compute ...)
Steve Bagley, and I had set it off and we waited patiently three weeks.
And Steve had given it a gigabyte of memory and, if we waited another three months, it would've just
blown up and run out of memory, even then. 

But—I think I pointed out also—the bigger problem was that the precision of the arithmetic was
gonna do us down. I mean there were we with a 64-bit machine. What we needed to get the answer
right was a thing where the lengths of integers weren't 64 bits but two to the power of 64 bits
(which is something like twenty thousand decimal places).

Again referring back to that original video, I had a lot of really interesting mail from various
people who said to me: 
"OK you said that this is an innately recursive problem and it just had to have general recursion
 capabilities. Well, I want to tell you that I have implemented it in C and I have never called my
 Ack routine recursively once! Not once have I called it recursively; so it can't be that the
 problem, in general, requires recursion."

So I then said: "Well, then let me take a look at what you've done to implement it." And what
they've done was unbelievable sophisticated mechanisms, using "malloc", the memory allocator. And,
basically, these very talented people were simulating a stack. They were given themselves stack
frames, keeping them all adding up, keeping track of them, and so on. But it was basically: they
weren't giving it the name recursion, but that's exactly what was happening. [Sean Riley asks: Is
that manual recursion?] It was manual, cleverly-implemented, recursion and—yeah, I mean—even
they admitted they would run out of resources eventually. "But I haven't called myself
recursively" [Is what they would say]. No, but you've done everything that a recursion would do.
You have to, to get the problem to work out alright.

## Related videos

[The Most Difficult Program to Compute?][most_difficult_program]  
[What on Earth is Recursion?][what_on_earth_is_recursion]  
[Reverse Polish Notation & the Stack][reverse_polish_notation_and_stack]  

[link_to_original_video]: https://www.youtube.com/watch?v=HXNhEYqFo0o
[most_difficult_program]: https://www.youtube.com/watch?v=i7sm9dzFtEI
[what_on_earth_is_recursion]: https://www.youtube.com/watch?v=Mv9NEXX1VHc
[reverse_polish_notation_and_stack]: https://www.youtube.com/watch?v=7ha78yWRDlE
[loops_ackermann_recursion]: https://www.youtube.com/watch?v=DVG5G1V8Zx0
