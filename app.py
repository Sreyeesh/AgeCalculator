user_age = input("Enter your age: ")
years = int(user_age)
months = years * 12

print(f"Your age, {years}, is equal to {months} months.")

# Calculate the number of seconds in those years
seconds = years * 365.25 * 24 * 60 * 60

print(f"Your age, {years} years, is approximately equal to {int(seconds)} seconds.")