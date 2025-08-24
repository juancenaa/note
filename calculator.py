
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

num1 = int(num1)
num2 = int(num2)

print(f"Sum (+): {num1 + num2}")
print(f"Difference (-): {num1 - num2}")
print(f"Multiplication (*): {num1 * num2}")

if num2 != 0:
    print(f"Division (/): {num1 / num2}")
    print(f"Modulus (%): {num1 % num2}")
    print(f"Integer Division (//): {num1 // num2}")
else:
    print("Division (/): Undefined (cannot divide by zero)")
    print("Modulus (%): Undefined (cannot divide by zero)")
    print("Integer Division (//): Undefined (cannot divide by zero)")


print(f"Power (**): {num1 ** num2}")
