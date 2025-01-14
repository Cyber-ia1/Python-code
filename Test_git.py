find_perimeter = lambda a, b: 2 * (a + b)  # This lambda function calculates the perimeter of a rectangle using length (a) and width (b).

print("Welcome to the Rectangle Perimeter Calculator!")  # A simple welcome message for the user.

# Get user inputs
try:
    length = float(input("Enter the length of the rectangle: "))  # Prompts the user to input the length of the rectangle and converts it to a float.
    width = float(input("Enter the width of the rectangle: "))  # Prompts the user to input the width of the rectangle and converts it to a float.

    # Calculate and display the perimeter
    perimeter = find_perimeter(length, width)  # Calls the lambda function defined above with the user-provided length and width to compute the perimeter.
    print(f"The perimeter of the rectangle is: {perimeter}")  # Displays the calculated perimeter with a descriptive message.
except ValueError:
    print("Invalid input. Please enter valid numbers for length and width.")  # Handles cases where the input is not a valid number and informs the user.
