import time
import math as m

def check_prime(x):
  for i in range(2, m.floor(m.sqrt(x))):
    if x % i == 0:
      return False
  
  return True

def prime_finder(start_time):
  largest_prime = 2
  i = 2
  while 1 > 0:
    if check_prime(i):
      largest_prime = i
    
    if time.time() - start_time >= 1:
      return largest_prime

    i += 1

start_time = time.time()
print(prime_finder(start_time), time.time() - start_time)

