from decimal import Decimal, getcontext
import time

print("Pi Calculator")
print("=============")
try:
    digits = int(input("How many decimal places of Pi? (1-500): "))
    digits = max(1, min(500, digits))
except ValueError:
    digits = 50

getcontext().prec = digits + 10
print(f"\nCalculating Pi to {digits} decimal places...")
start = time.time()

# Chudnovsky algorithm (simplified)
C = 426880 * Decimal(10005).sqrt()
K = Decimal(6)
M = Decimal(1)
X = Decimal(1)
L = Decimal(13591409)
S = Decimal(13591409)

for i in range(1, digits // 14 + 2):
    M = M * (K**3 - 16*K) / (i**3)
    L += 545140134
    X *= -262537412640768000
    S += M * L / X
    K += 12

pi = C / S
pi_str = str(pi)[:digits + 2]
elapsed = time.time() - start

print(f"Pi = {pi_str}")
print(f"\nCalculated in {elapsed:.4f} seconds")
print(f"Fun fact: Pi has been calculated to over 100 trillion digits!")
