def c_to_f(c): return c * 9/5 + 32
def f_to_c(f): return (f - 32) * 5/9
def c_to_k(c): return c + 273.15

def feels_like(c):
    if c < -20: return "Dangerously cold! Stay inside!"
    elif c < 0: return "Freezing! Wear a heavy coat."
    elif c < 10: return "Very cold. Wrap up warm."
    elif c < 18: return "Cool. Jacket recommended."
    elif c < 25: return "Comfortable and pleasant."
    elif c < 35: return "Warm. Great outdoor weather!"
    else: return "Very hot! Stay hydrated."

print("Temperature Converter")
print("=====================")
while True:
    print("\n1) Celsius to Fahrenheit")
    print("2) Fahrenheit to Celsius")
    print("3) Celsius to Kelvin")
    print("4) Quit")
    choice = input("Choose: ")
    if choice == "1":
        c = float(input("Enter Celsius: "))
        print(f"{c}°C = {c_to_f(c):.1f}°F")
        print(f"Feels like: {feels_like(c)}")
    elif choice == "2":
        f = float(input("Enter Fahrenheit: "))
        c = f_to_c(f)
        print(f"{f}°F = {c:.1f}°C")
        print(f"Feels like: {feels_like(c)}")
    elif choice == "3":
        c = float(input("Enter Celsius: "))
        print(f"{c}°C = {c_to_k(c):.2f}K")
    elif choice == "4":
        break
