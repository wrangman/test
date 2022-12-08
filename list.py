numbers = input("Enter a list of numbers, separated by spaces: ")

# Convert the input string into a list of numbers
numbers = numbers.split()
numbers = [int(x) for x in numbers]

# Calculate the sum of the numbers in the list
total = sum(numbers)

# Print the result to the screen
print("The sum of the numbers is:", total)