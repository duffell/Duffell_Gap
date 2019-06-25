# Duffell_Gap

A 1D Model for the Shape of Planet-Induced Gaps in Protoplanetary Disks

Anyone is free to use and distribute!  MIT license, so you can even mix it into proprietary code for any purpose you like.

The code is really straightforward, it's just intended as a bit of base code to show you how the model works.

If you do use this, I only ask that you cite me.  In particular, cite the paper that references it, Duffell (2019).

To compile the C code, all you have to do is

gcc gap.c

Then run with

./a.out

The result is loaded to "output.dat".

Disk and planet parameters are currently hard-coded, you'll have to modify the code yourself if you want to fix that.

I cannot forsee any way this could possibly fail, but life is full of surprises.


The python code is just a starter because I know most people prefer to use python and think I'm crazy for writing anything in C.  Eventually I'll try to incorporate this bit of python code into something larger that can do curve-fitting, but that's off in the future.


