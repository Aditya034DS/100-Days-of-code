#Tip Calculator

print("Welcome to the tip calculator.")

# get the base bill without tip
a = float(input("What was the total bill? $"))

# get the percentage
b = int(input("What precentage tip would you like to give? 10, 12, or 15? "))

# get the number of people
c = int(input("How many people to split the bill? "))

# add the tip to the base bill
d = b/100*a
a = a+d

# calculate the split bill and round to 2 decimal places
a = round(a/c,2)

# Print the bill message.
print(f"Each person should pay: ${a}")
