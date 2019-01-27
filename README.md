# trapped_knight

An examination of the "Trapped Knight" problem, as discussed in the Numberphile video "The Trapped Knight - Numberphile".

Based on a comment by user "Smt Smt": "What happens if you mark 2084 as already visited before you start the game? Will it still get trapped somewhere else?"

It appears that other users responding to that Numberphile comment have independently written code which does the same as this code does. This codebase was originally developed independently but, once I discovered the detailed discussion below Smt Smt's comment, I was able to improve my code's efficiency considerably and also add some analysis of n-traps.

Interestingly, the sequence is non-monotonic but appears to be increasing on average. It would be interesting to look at the distribution of knight-stops probabilistically (what is the probability that the knight will stop at step n, or at value k, etc.)
 
There is a very interesting discussion in the YouTube comments section about "double traps", "triple traps", etc - I had trouble implementing the code recursively and this appears to be why (the idea of an n-trap is that, when your knight is trapped in a position, that position is an n-trap if you have to recurse n positions before you have another position you can go to).
