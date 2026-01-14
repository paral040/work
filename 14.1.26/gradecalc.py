def get_grade(mark):
    if mark >= 90:
        return "9"
    elif mark >= 80:
        return "8"
    elif mark >= 70:
        return "7"
    else:
        return "Below 7"

mark = int(input("Enter your mark (0-100): "))
if 0 <= mark <= 100:
    grade = get_grade(mark)
    print(f"Your grade is: {grade}")
else:
    print("Invalid mark. Please enter a value between 0 and 100.")
