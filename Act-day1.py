from datetime import datetime

score = float(input("Enter your grade (0-100): "))


if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"


print(f"Your letter grade is: {grade} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
