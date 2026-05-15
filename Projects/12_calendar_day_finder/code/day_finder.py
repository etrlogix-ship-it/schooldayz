from datetime import date, datetime
import calendar

print("📅 Birthday Day Finder!")
print("=======================\n")

while True:
    try:
        year = int(input("Enter year (e.g. 2010): "))
        month = int(input("Enter month (1-12): "))
        day = int(input("Enter day (1-31): "))
        d = date(year, month, day)

        day_name = calendar.day_name[d.weekday()]
        month_name = calendar.month_name[month]
        today = date.today()
        age_days = (today - d).days

        print(f"\n🎂 {day} {month_name} {year} was a {day_name}!")
        if age_days > 0:
            years = age_days // 365
            print(f"📆 That was {age_days} days ago ({years} years)")
        elif age_days == 0:
            print("🎉 That's today!")
        else:
            print(f"🔮 That's {-age_days} days in the future!")

        print(f"\nFun fact: You can use calendar.monthcalendar({year}, {month}) to see the full month!")

    except ValueError as e:
        print(f"Invalid date: {e}. Please try again.")

    if input("\nCheck another date? (yes/no): ").lower() != "yes":
        break
