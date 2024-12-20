import time
import numpy as np
import matplotlib.pyplot as plt

def check_prime(x):
  for i in range(2, x):
    if x % i == 0:
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

# Plot results
times = np.array([p[0] for p in primes])
largest_primes = np.array([p[1] for p in primes])

# Plot the graph
plt.plot(times, largest_primes, marker='o')
plt.title('Largest Prime With Trial Division')
plt.xlabel('Time (seconds)')
plt.ylabel('Largest Prime')
plt.grid(True)
plt.show()