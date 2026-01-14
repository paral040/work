start_num = int(input("Enter the Start number: "))
end_num = int(input("Enter the End number: "))

for num in range(start_num, end_num + 1):
    if num % 2 == 0:
        print(num)