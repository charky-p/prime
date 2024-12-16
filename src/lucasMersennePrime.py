import time
import numpy as np
import matplotlib.pyplot as plt

# Lucas-Lehmer Primality Test
def check_mersenne_prime(p):
  m_p = 2 ** p - 1
  s_n = 4
  for _ in range(p - 2):
    s_n = (s_n ** 2 - 2) % m_p
  
  return s_n == 0

def prime_finder(start_time, max_time):
  primes = []
  largest_prime = 2
  i = 2
  while 1 > 0:
    if check_mersenne_prime(i):
      largest_prime = 2 ** i - 1
      primes.append((time.time() - start_time, largest_prime, i))
    
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
plt.title('Largest Prime With Lucas-Lehmer Test')
plt.xlabel('Time (seconds)')
plt.ylabel('Largest Prime')
plt.grid(True)
plt.show()

# Logarithmic Version
plt.plot(times, largest_primes, marker='o')
plt.title('Largest Prime With Lucas-Lehmer Test (Logarithmic)')
plt.xlabel('Time (seconds)')
plt.ylabel('Largest Prime')
plt.yscale('log')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()