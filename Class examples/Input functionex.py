# an input function allows a user to input data

#example

# Get full name input
full_name = input("Enter your full name: ")

# Split the full name into first and last name
name_parts = full_name.split()

# Check if there's at least a first and last name
if len(name_parts) >= 2:
    first_name = name_parts[0]
    last_name = name_parts[-1]
else:
    print("Please enter both a first and last name.")
    first_name = full_name
    last_name = ""

# Print the first and last name
print(f"First name: {first_name}")
print(f"Last name: {last_name}")





#Dont forget that rfind needs a space between quotes inorder to find last name


fullName = input("Enter a full name:")

n = fullName.rfind(" ")

print("Last name:", fullName[n+1:])
print("First name(s):", fullName[ :n] )