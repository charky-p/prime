import time
import math as m
import numpy as np
import matplotlib.pyplot as plt

def check_prime(x):
  # Checking known primes
  known_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
  for prime in known_primes:
    if x % prime == 0:
      return False
    
  # Skipping 6 steps to avoid multiples of 2 and 3
  for i in range(30, m.floor(m.sqrt(x)) + 1, 6):
    if x % i == 0 or x % (i + 2) == 0:
      return False
  
  return True

def prime_finder(start_time, max_time):
  primes = []
  largest_prime = 2
  i = 2
  while 1 > 0:
    if check_prime(i):
      largest_prime = i
      primes.append((time.time() - start_time, largest_prime))
    
    if time.time() - start_time >= max_time:
      return primes

    i += 1

max_time = 1
start_time = time.time()
primes = prime_finder(start_time, max_time)
print(primes[-1])

# Plot results
times = np.array([p[0] for p in primes])
largest_primes = np.array([p[1] for p in primes])

# Plot the graph
plt.plot(times, largest_primes, marker='o')
plt.title('Largest Prime With Efficient Trial Divison')
plt.xlabel('Time (seconds)')
plt.ylabel('Largest Prime')
plt.grid(True)
plt.show()