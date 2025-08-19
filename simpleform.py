# Simple Form

# take input
name = input("Enter your Name:")
age = int(input("Enter your Age:"))
height = float(input("Enter your Height (in feet):"))
country = input("Enter your Country:")

# process
name_upper = name.upper()
nickname = (name[:2] + name[-2:]).upper()
country_upper = country.upper()
height_rounded = round(height, 2)

# output
print(f"\nHello {name_upper}")
print(f"You are {age} years old.")
print(f"Your height is {height_rounded:.2f} feet.")
print(f"You are from {country_upper}.")
print(f"Your nickname is {nickname}")