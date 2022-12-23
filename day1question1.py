"""Write a function that takes list of numbers and returns sum of all even numbers from the list with user providing input"""
def sum_evens(numbers):
    even_sum = 0
    for number in numbers:
        if number % 2 == 0:  # check if number is even
            even_sum += number  # add even number to sum
    return even_sum

# Get user input
numbers_str = input("Enter a list of numbers separated by space: ")

# Convert input string to a list of integers
numbers = [int(number) for number in numbers_str.split()]

# Get sum of even numbers
even_sum = sum_evens(numbers)

# Print result
print(f"Sum of even numbers: {even_sum}")
