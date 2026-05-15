import math

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def get_factors(n):
    return [i for i in range(1, n+1) if n % i == 0]

def is_perfect(n):
    return n > 1 and sum(get_factors(n)[:-1]) == n

def is_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

print("🔢 Number Facts Machine!")
print("========================\n")

while True:
    try:
        n = int(input("Enter a number (1–10000): "))
        if not 1 <= n <= 10000:
            print("Please enter a number between 1 and 10000.")
            continue
    except ValueError:
        print("That's not a valid number!")
        continue

    print(f"\n📊 Facts about {n}:")
    print(f"  • It is {'even' if n % 2 == 0 else 'odd'}")
    print(f"  • It {'IS' if is_prime(n) else 'is NOT'} a prime number")
    print(f"  • It {'IS' if math.isqrt(n)**2 == n else 'is NOT'} a perfect square")
    print(f"  • It {'IS' if is_fibonacci(n) else 'is NOT'} a Fibonacci number")
    print(f"  • It {'IS' if is_perfect(n) else 'is NOT'} a perfect number")
    factors = get_factors(n)
    print(f"  • Factors: {factors}")
    print(f"  • Sum of digits: {sum(int(d) for d in str(n))}")
    print(f"  • In binary: {bin(n)}")
    print(f"  • Square root: {math.sqrt(n):.4f}")
    print()

    if input("Try another number? (yes/no): ").lower() != "yes":
        break

print("Thanks for exploring numbers! 🔢")
