# trapped_knight

An examination of the "Trapped Knight" problem, as discussed in the Numberphile video "The Trapped Knight - Numberphile", found at https://www.youtube.com/watch?v=RGQe8waGJ4w.

Based on a comment by user "Smt Smt": "What happens if you mark 2084 as already visited before you start the game? Will it still get trapped somewhere else?" - https://www.youtube.com/watch?v=RGQe8waGJ4w&lc=UgxnOQujJFUbGTf13Tp4AaABAg

It appears that other users responding to that Numberphile comment have written code which does the same sort of thing as this code does. By looking at this discussion I was able to improve my code's efficiency considerably and also add some analysis of n-traps.

Interestingly, the sequence is non-monotonic but appears to be increasing on average. It would be interesting to look at the distribution of knight-stops probabilistically (what is the probability that the knight will stop at step n, or at value k, etc.)
 
There is a very interesting discussion in the YouTube comments section about "double traps", "triple traps", etc - I had trouble implementing the code recursively and this appears to be why (the idea of an n-trap is that, when your knight is trapped in a position, that position is an n-trap if you have to recurse n positions before you have another position you can go to).

Some questions that arise from the sequence:
 - At any step k, is it guaranteed that we won't stop below some value f(k)?
 - For some positive integer p, do p-traps become more or less common as we get further into the sequence?
 - What is the probability of the knight becoming trapped at some step i, or some value x of the spiral?
 - I found 1-traps, 2-traps, 3-traps, 4-traps, and 5-traps; are traps of any size possible? User Shirou97 found an 8-trap at step 754,165,534 - https://www.youtube.com/watch?v=RGQe8waGJ4w&lc=UgxnOQujJFUbGTf13Tp4AaABAg.8qVECW_mhGl8qWHlI1xgjd)
 - As asked by Gareth Ma (https://www.youtube.com/watch?v=RGQe8waGJ4w&lc=UgxnOQujJFUbGTf13Tp4AaABAg.8qVECW_mhGl8qXLofMDB-R), what would happen if, rather than marking the positions of the stops as visited, we instead _start the sequence_ from those points? User SBGif has analysed this in some detail (https://www.youtube.com/watch?v=RGQe8waGJ4w&lc=UgxnOQujJFUbGTf13Tp4AaABAg.8qVECW_mhGl8qZrgDGvqQQ and other comments in that chain).

Similar/interesting results were found in the comments section by the following users (with sincere apologies if I missed anyone - if I did miss you, please know that it was not intentional):
 - Harrison Harris
 - dLichti
 - Darryl4779
 - Shirou97
 - John Merritt
 - SBGif
