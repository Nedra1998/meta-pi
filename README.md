# Meta-PI #

> A Raspberry PI calculating the first $\pi\times 10^6$ digits of $\pi$ through
> $\pi\times 10^5$ iterations.

Meta-PI is a raspberry *pi* that is using an iterative algorithm to solve for
the first $3141592$ digits of *pi*, by doing the iteration $314159$ times.
Every $500$ iterations it dumps a file ``pi.txt`` and pushes to this
repository.

This is by no means an efficient way of doing this. Every $500$ iterations, it
restarts from the beginning because I was lazy and didn't want to figure out how
to push from the python script itself. So it might be very very slow.

Also each iteration can accuratly compute $~14$ digits of pi in my
initial testing, so this actually calculates the first $~4398226$ digits, but
that is not nearly as poetic.
