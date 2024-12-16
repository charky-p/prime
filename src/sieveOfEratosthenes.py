import time
import matplotlib.pyplot as plt

# Sieve of Eratosthenes
def sieve_of_eratosthenes(x):
  sieve = [True] * (x + 1)
  sieve[0], sieve[1] = False, False

  # Mark non primes
  for p in range(2, int(x ** 0.5) + 1):
    if sieve[p]:
      for i in range(p ** 2, x + 1, p):
        sieve[i] = False

  return sieve

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
  
  # Precompute primes
  sieve = sieve_of_eratosthenes(1700)
  
  while 1 > 0:
    if sieve[i] and check_mersenne_prime(i):
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
times = [p[0] for p in primes]
largest_primes = [p[1] for p in primes]
original_primes = [p[2] for p in primes]
print([p[2] for p in primes]) 

# Plot the graph
plt.plot(times, original_primes, marker='o')
plt.title('Largest Prime With Lucas-Lehmer Test Without Composite p')
plt.xlabel('Time (seconds)')
plt.ylabel('Largest Prime p (not 2^p - 1)')
plt.grid(True)
plt.show()