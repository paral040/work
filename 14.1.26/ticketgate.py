age = int(input("Enter your age:\n"))

if age >= 18:
    print("Adult ticket")
elif age < 18 and age >= 0:
    print("Child Ticket")
else:
    print("Invalid")