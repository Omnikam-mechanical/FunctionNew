###1Write a Python function that takes a list of numbers s input and 
# returns sum of all even numbers in the list
def sum_of_even_numbers(numbers):
    # Use a list comprehension to filter even numbers and sum them
    return sum(num for num in numbers if num % 2 == 0)

# Example usage
numbers = [47, 11, 42, 13]
result = sum_of_even_numbers(numbers)
print(result)  # Output will be 42 (since only 42 is even)

##2 Create a Python function that accepts a 
# string and returns the reverse of that string.
def reverse_string(input_string):
    # Return the reversed string using slicing
    return input_string[::-1]

# Example usage
result = reverse_string("Hello World")
print(result)  # Output will be "dlroW olleH"


##3Implement a Python function that takes a list of integers and returns a new list 
# containing the squares of each number
def square_numbers(numbers):
    # Use a list comprehension to square each number in the list
    return [num ** 2 for num in numbers]

# Example usage
numbers = [2, 3, 4, 5]
result = square_numbers(numbers)
print(result)  # Output will be [4, 9, 16, 25]

##4Write a Python function that checks if 
# a given number is prime or not from 1 to 200
def is_prime(number):
    # Handle edge cases
    if number < 2:
        return False
    # Check divisibility for numbers from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Example usage to check prime numbers between 1 and 200
for num in range(1, 201):
    if is_prime(num):
        print(f"{num} is a prime number.")

##5Create an iterator class in Python that generates the Fibonacci sequence up to a specified number of terms 
class FibonacciIterator:
    def __init__(self, num_terms):
        self.num_terms = num_terms  # Total number of Fibonacci terms to generate
        self.current_term = 0  # Current term index
        self.a, self.b = 0, 1  # Starting values for Fibonacci sequence

    def __iter__(self):
        return self  # Returns the iterator object itself

    def __next__(self):
        if self.current_term >= self.num_terms:
            raise StopIteration  # Stop the iteration when the limit is reached
        
        # Handle the first two terms separately
        if self.current_term == 0:
            self.current_term += 1
            return self.a  # Return 0 for the first term
        elif self.current_term == 1:
            self.current_term += 1
            return self.b  # Return 1 for the second term

        # Generate subsequent terms
        next_value = self.a + self.b  # Calculate next Fibonacci number
        self.a, self.b = self.b, next_value  # Update a and b
        self.current_term += 1  # Increment the term counter
        return next_value  # Return the next Fibonacci number

# Example usage
fib_iterator = FibonacciIterator(10)  # Create an iterator for the first 10 Fibonacci numbers
for num in fib_iterator:
    print(num)

##6Write a generator function in Python that yields the powers of 2 up to a given exponen
def powers_of_two(max_exponent):
    """Generator function that yields powers of 2 up to the specified exponent."""
    for exponent in range(max_exponent + 1):  # Include the max_exponent
        yield 2 ** exponent  # Yield 2 raised to the current exponent

# Example usage
max_exp = 10  # Specify the maximum exponent
for power in powers_of_two(max_exp):
    print(power)

##7mplement a generator function that reads a file line by line and yields each line as a string
def read_file_line_by_line(file_path):
    """Generator function that reads a file line by line."""
    try:
        with open(file_path, 'r') as file:  # Open the file in read mode
            for line in file:  # Iterate over each line in the file
                yield line.strip()  # Yield the line after stripping leading/trailing whitespace
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError:
        print(f"Error: An IOError occurred while reading the file '{file_path}'.")

# Example usage
file_path = 'example.txt'  # Specify the path to your file
for line in read_file_line_by_line(file_path):
    print(line)

##8Use a lambda function in Python to sort a list of tuples based on the second element of each tuple.
# Sample list of tuples
tuples_list = [(1, 'banana'), (2, 'apple'), (3, 'cherry'), (4, 'date')]

# Using sorted() to create a new sorted list
sorted_list = sorted(tuples_list, key=lambda x: x[1])

# Output the sorted list
print("Sorted list (new list):", sorted_list)

# If you want to sort the original list in place
tuples_list.sort(key=lambda x: x[1])

# Output the original list after sorting
print("Original list after sort:", tuples_list)


##9Write a Python program that uses `map() to convert a list of temperatures from Celsius to Fahrenheit
# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# List of temperatures in Celsius
celsius_temps = [0, 20, 37, 100]

# Using map() to convert Celsius to Fahrenheit
fahrenheit_temps = list(map(celsius_to_fahrenheit, celsius_temps))

# Output the results
print("Celsius temperatures:", celsius_temps)
print("Fahrenheit temperatures:", fahrenheit_temps)


##10 Create a Python program that uses `filter() to remove all the vowels from a given string.
def remove_vowels(input_string):
    # Define a function to check if a character is a vowel
    def is_not_vowel(char):
        return char.lower() not in 'aeiou'

    # Use filter() to apply the is_not_vowel function to each character in the string
    filtered_chars = filter(is_not_vowel, input_string)

    # Join the filtered characters back into a string
    return ''.join(filtered_chars)

# Example usage
input_string = "Hello, World!"
result = remove_vowels(input_string)
print("Original string:", input_string)
print("String without vowels:", result)

