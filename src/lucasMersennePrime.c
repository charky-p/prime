#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
#include <math.h>
#include <string.h>
#include <gmp.h>

// MAX_TIME, 1 second = 1000
#define MAX_TIME 180000
#define SIEVE_AMT 100000

static bool *sieveOfEratosthenes(int x);
bool checkMersennePrime(int p);
int *primeFinder(int start_time, int *numPrimes);

int main() {  
  time_t start_time = clock();
  int numPrimes = 0;
  int *primes = primeFinder(start_time, &numPrimes);

  for (int i = 0; i < numPrimes; i++) {
    printf("%d\n", primes[i]);
  }

  free(primes);
  return 0;
}

bool *sieveOfEratosthenes(int x) {
  bool *sieve = malloc(sizeof(bool) * (x + 1));
  if (sieve == NULL) {
    printf("Memory allocation failed for sieve\n");
    return NULL;
  }

  memset(sieve, true, (x + 1) * sizeof(bool));
  sieve[0] = false;
  sieve[1] = false;

  // Mark non primes
  int limit = (int) sqrt(x);
  for (int p = 2; p <= limit; p++) {
    if (sieve[p] == true) {
      for (int i = p * p; i <= x; i += p) {
        sieve[i] = false;
      }
    }
  }

  return sieve;
}

bool checkMersennePrime(int p) {
  mpz_t m_p;
  mpz_init(m_p);
  mpz_ui_pow_ui(m_p, 2, p); // m_p = 2^p
  mpz_sub_ui(m_p, m_p, 1);  // m_p = 2^p - 1

  mpz_t s_n;
  mpz_init(s_n);
  mpz_set_ui(s_n, 4);
  for (int i = 0; i < p - 2; i++) {
    mpz_mul(s_n, s_n, s_n);
    mpz_sub_ui(s_n, s_n, 2);
    mpz_mod(s_n, s_n, m_p);
  }

  bool result = mpz_cmp_ui(s_n, 0) == 0;
  mpz_clear(m_p);
  mpz_clear(s_n);
  return result;
}

int *primeFinder(int start_time, int *numPrimes) {
  int *primes = malloc(sizeof(int) * 100);
  if (primes == NULL) {
    printf("Memory allocation failed for primes\n");
    return NULL;
  }

  // Precompute primes
  bool *sieve = sieveOfEratosthenes(SIEVE_AMT);
  if (sieve == NULL) {
    free(primes);
    return NULL;
  }
  printf("Finished computing Sieve\n");

  int i = 3;
  while (1) {
    if (sieve[i] && checkMersennePrime(i)) {
      primes[*numPrimes] = i;
      (*numPrimes)++;
    }

    if (clock() - start_time >= MAX_TIME) {
      free(sieve);
      return primes;
    }

    i++;
  }
}