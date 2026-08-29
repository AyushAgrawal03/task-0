def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            break
    else:
        return True
    return False

print(is_prime(7))   # True
print(is_prime(12))  # False

N = int(input("Enter N: "))

for i in range(2, N + 1):
    if is_prime(i):
        print(i, end=" ")

# The else block associated with a for loop executes ONLY if the loop finishes  all its iterations naturally, without ever hitting a `break` statement. In this function, if a divisor is found, the loop breaks (it's not prime). If the loop finishes without breaking, it means no divisors were found, so the else block runs and returns True (the number is prime).
