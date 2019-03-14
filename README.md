# Meta-PI #

> A Raspberry PI calculating the first $\pi\times 10^6$ digits of $\pi$.

Meta-PI is a raspberry *pi* that is using an iterative algorithm to solve for
the first $3141592$ digits of *pi*. Every $500$ iterations it dumps a file
``pi.txt`` and pushes to this repository.

This is by no means an efficient way of doing this. Every $500$ iterations, it
restarts from the beginning because I was lazy and didn't want to figure out how
to push from the python script itself. So it might be very very slow.
