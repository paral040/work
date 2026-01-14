def divide(a, b):
    return a / b

numerator = float(input("Enter the numerator: "))
divisor = float(input("Enter the divisor: "))

while divisor == 0:
    print("Error: Divisor cannot be zero.")
    divisor = float(input("Enter a non-zero divisor: "))

result = divide(numerator, divisor)
print(f"The result of {numerator} divided by {divisor} is {result}.")