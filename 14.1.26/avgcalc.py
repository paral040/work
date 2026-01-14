num_count = int(input("How many numbers do you want to average? "))
total = 0
for i in range(num_count):
    num = float(input(f"Enter number {i+1}: "))
    total += num
average = total / num_count if num_count > 0 else 0
print(f"The average is: {average:.2f}")