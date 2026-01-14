def to_celsuis(fahrenheit): return (fahrenheit - 32) * 5.0 / 9.0

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = to_celsuis(fahrenheit)
print(f"{fahrenheit} Fahrenheit is {celsius:.2f} Celsius.")