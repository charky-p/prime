# Prime
This is a small challenge of finding the largest prime number possible in under a second of runtime.
The final file is src/lucasMersennePrime.c. I wrote more on my blog [here].

## Usage

To compile and run the program in `src`, use the following command:
```bash
$ gcc -o lucasMersennePrime lucasMersennePrime.c -I/mingw64/include -L/mingw64/lib -lgmp
$ ./lucasMersennePrime.exe
```

## Rules
- The 1 second includes the extra time to calculate the time during runtime, but does not count the time after the result has been found.
- Any computations rely within those found during the runtime of the program, this means we cannot start with a known big prime, however it does not need to store any previous primes, only the largest prime, and it can use the first 10 known primes (2,3,5,7,11,13,17,19,23,29). To avoid external factors affecting the computation, the program can be run multiple times, and only the largest prime found will be counted. The computations must also only occur on the same machine and no parallelism or threads are allowed.
- The prime number must be exact to the digit, and not an estimate, and it must also verify that it is a prime
