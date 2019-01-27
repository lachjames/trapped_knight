# trapped_knight

An examination of the "Trapped Knight" problem, as discussed in the Numberphile video "The Trapped Knight - Numberphile".

Based on a comment by user "Smt Smt": "What happens if you mark 2084 as already visited before you start the game? Will it still get trapped somewhere else?"

It appears that other users responding to that Numberphile comment have independently written code which does the same as this code does, but this code was developed independently.

It's not the most efficient code, but it demonstrates some interesting properties of the sequence:
 - It's not monotonic
 - It appears to increase (on average) though
 - I'll analyse the sequence further over time
 
There is a very interesting discussion in the YouTube comments section about "double traps", "triple traps", etc - I had trouble implementing the code recursively and this appears to be why (the idea of an n-trap is that, when your knight is trapped in a position, that position is an n-trap if you have to recurse n positions before you have another position you can go to).
