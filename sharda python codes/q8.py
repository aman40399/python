#A positive integer m can be partitioned as primes if it can be written
#as p + q where p > 0, q > 0 and both p and q are prime numbers.
#Write a Python function primepartition(m) that takes an integer m as
#input and returns True if m can be partitioned as primes and False
#otherwise. (If m is not positive, your function should return False.)
# Input
m = int(input("Enter a positive integer: "))

# Check if m is positive
if m <= 0:
    print("False")
else:
    # Check if m can be partitioned into primes
    partition_exists = False
    for p in range(2, m):
        q = m - p

        # Check if p is prime
        is_p_prime = True
        for i in range(2, int(p**0.5) + 1):
            if p % i == 0:
                is_p_prime = False
                break

        # Check if q is prime
        is_q_prime = True
        for i in range(2, int(q**0.5) + 1):
            if q % i == 0:
                is_q_prime = False
                break

        # If both p and q are prime, set partition_exists to True and break the loop
        if is_p_prime and is_q_prime:
            partition_exists = True
            break

    print(partition_exists)
