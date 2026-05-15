print("BMI Calculator")
print("==============")
print("BMI helps doctors understand if a person has a healthy weight for their height.")
print("(Always talk to a doctor for real health advice!)")
while True:
    try:
        weight = float(input("\nWeight in kg: "))
        height = float(input("Height in cm: ")) / 100
        if weight <= 0 or height <= 0:
            print("Please enter positive numbers.")
            continue
        bmi = weight / (height ** 2)
        if bmi < 18.5: category = "Underweight"
        elif bmi < 25: category = "Healthy weight"
        elif bmi < 30: category = "Overweight"
        else: category = "Obese"
        print(f"\nYour BMI: {bmi:.1f}")
        print(f"Category: {category}")
        print("Remember: BMI is just one health indicator. Always see a doctor for real advice!")
    except ValueError:
        print("Please enter valid numbers.")
    if input("\nCalculate again? (yes/no): ").lower() != "yes":
        break
