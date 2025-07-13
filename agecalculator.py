from datetime import datetime

def calculate_age(birth_date_str):
    try:
        birth_date = datetime.strptime(birth_date_str, "%d-%m-%Y")
        today = datetime.today()

        years = today.year - birth_date.year
        months = today.month - birth_date.month
        days = today.day - birth_date.day

        if days < 0:
            months -= 1
            days += 30

        if months < 0:
            years -= 1
            months += 12

        print(f"\n🎉 Your Age is: {years} years, {months} months, {days} days.")
    except ValueError:
        print("❌ Invalid date format. Please use DD-MM-YYYY.")

def main():
    print("📅 Welcome to the Age Calculator!")
    dob_input = input("Enter your date of birth (DD-MM-YYYY): ")
    calculate_age(dob_input)

main()
