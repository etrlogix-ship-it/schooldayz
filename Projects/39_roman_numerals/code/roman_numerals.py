def to_roman(num):
    val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    syms = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    result = ""
    for i in range(len(val)):
        while num >= val[i]:
            result += syms[i]
            num -= val[i]
    return result

def from_roman(s):
    vals = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    result = 0
    for i in range(len(s)):
        if i+1 < len(s) and vals[s[i]] < vals[s[i+1]]:
            result -= vals[s[i]]
        else:
            result += vals[s[i]]
    return result

print("Roman Numeral Converter")
print("=======================")
while True:
    print("\n1) Number to Roman  2) Roman to Number  3) Quit")
    choice = input("Choose: ")
    if choice == "1":
        try:
            n = int(input("Enter number (1-3999): "))
            if 1 <= n <= 3999:
                print(f"{n} = {to_roman(n)}")
            else:
                print("Number must be 1-3999!")
        except ValueError:
            print("Invalid!")
    elif choice == "2":
        r = input("Enter Roman numeral: ").upper().strip()
        try:
            print(f"{r} = {from_roman(r)}")
        except (KeyError, IndexError):
            print("Invalid Roman numeral!")
    elif choice == "3":
        break
