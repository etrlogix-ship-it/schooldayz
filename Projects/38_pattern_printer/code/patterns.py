def triangle(n, char="*"):
    for i in range(1, n+1):
        print(char * i)

def diamond(n, char="*"):
    for i in range(1, n+1):
        print(" "*(n-i) + char*(2*i-1))
    for i in range(n-1, 0, -1):
        print(" "*(n-i) + char*(2*i-1))

def checkerboard(rows, cols):
    for r in range(rows):
        for c in range(cols):
            print("## " if (r+c)%2==0 else "   ", end="")
        print()

def spiral_nums(n):
    for i in range(1, n+1):
        print(" ".join(str(j) for j in range(i, i+n)))

print("Pattern Printer!")
print("================")
while True:
    print("\n1) Triangle  2) Diamond  3) Checkerboard  4) Number staircase  5) Quit")
    choice = input("Choose: ")
    try:
        if choice == "1":
            n = int(input("Size (1-20): "))
            char = input("Character (Enter for *): ") or "*"
            triangle(min(n,20), char[0])
        elif choice == "2":
            n = int(input("Size (1-15): "))
            diamond(min(n,15))
        elif choice == "3":
            r = int(input("Rows (1-15): "))
            c = int(input("Cols (1-20): "))
            checkerboard(min(r,15), min(c,20))
        elif choice == "4":
            n = int(input("Size (1-10): "))
            spiral_nums(min(n,10))
        elif choice == "5":
            break
    except ValueError:
        print("Enter a valid number!")
