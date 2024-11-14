# This function converts kilometers to miles
def km_to_miles(km):  
    return km * 0.621371

# This function converts miles to kilometers
def miles_to_km(miles):  
    return miles / 0.621371

# This function converts kilograms to pounds
def kg_to_pounds(kg):  
    return kg * 2.20462

# This function converts pounds to kilograms
def pounds_to_kg(pounds):  
    return pounds / 2.20462

# This function converts Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):  
    return (celsius * 9/5) + 32

# This function converts Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):  
    return (fahrenheit - 32) * 5/9



# This dictionary contains all the available conversion types and their corresponding functions.  # A dictionary is used to simplify the proccess
# The keys '1', '2', '3' represent categories (Length, Weight, Temperature), and within each category,
# there are options (e.g., "Kilometers to Miles" or "Miles to Kilometers") mapped to conversion functions.
conversions = {  
    '1': {"name": "Length", "options": {"1": ("Kilometers to Miles", km_to_miles), "2": ("Miles to Kilometers", miles_to_km)}},
    '2': {"name": "Weight", "options": {"1": ("Kilograms to Pounds", kg_to_pounds), "2": ("Pounds to Kilograms", pounds_to_kg)}},
    '3': {"name": "Temperature", "options": {"1": ("Celsius to Fahrenheit", celsius_to_fahrenheit), "2": ("Fahrenheit to Celsius", fahrenheit_to_celsius)}}
}



# This function prompts the user for input and ensures that they provide a valid option from a set of choices.
# It loops until the user inputs a correct value found in 'valid_inputs'.
def get_valid_input(prompt, valid_inputs):  
    while True:
        user_input = input(prompt).strip()
        if user_input in valid_inputs:
            return user_input
        else:
            print(f"Invalid input. Please enter one of {valid_inputs}")



# List to store the history of conversions made by the user
conversion_history = []




# Main function for the unit converter
def unit_converter():  
    while True:
        
        # Step 1: Ask the user to pick a conversion type (Length, Weight, or Temperature)
        print("\nSelect a conversion type:")
        for key, value in conversions.items():
            print(f"{key}. {value['name']}")


        # Get the valid conversion type input (1, 2, or 3)
        conversion_type = get_valid_input("\nEnter your choice (1/2/3): ", conversions.keys())


        # Display the selected conversion type (e.g., "Length")
        print(f"\nYou selected {conversions[conversion_type]['name']}")
        # Get the options for that type (e.g., Kilometers to Miles, Miles to Kilometers)
        options = conversions[conversion_type]['options']


        # Display the options for the selected conversion type
        # Loop through each option and display its name (e.g., "1. Kilometers to Miles")
        for key, (name, _) in options.items():
            print(f"{key}. {name}")


        # Get the valid conversion option (1 or 2)
        conversion_choice = get_valid_input("\nChoose conversion (1/2): ", options.keys())
        # Get the selected conversion name (e.g., "Kilometers to Miles") and the corresponding function (e.g., km_to_miles)
        conversion_name, conversion_func = options[conversion_choice]


        # Step 2: Ask the user to input a value for the conversion and handle non-numeric inputs
        # Loop until a valid numeric input is provided
        while True:  
            try:
                value = float(input(f"\nEnter the value for {conversion_name}: "))
                break  # Break the loop if the input is valid
            except ValueError:  # Handle non-numeric input
                print("Invalid input. Please enter a numeric value.")


        # Step 3: Perform the conversion by calling the appropriate function (e.g., km_to_miles) with the input value
        result = conversion_func(value)
        print(f"\nResult: {value} converted using {conversion_name} is {result:.2f}")


        # Add the conversion result to the history list in a readable format
        conversion_history.append(f"{value} -> {result:.2f} ({conversion_name})")


        # Step 4: Ask the user if they want to perform another conversion
        another = input("\nDo you want to perform another conversion? (yes/no): ").strip().lower()
        if another != 'yes':
            # If the user says no, display the conversion history and end the program
            print("\nConversion History:")
            if conversion_history:
                # If there are previous conversions, print them
                for record in conversion_history:
                    print(f" - {record}")
            else:
                print("No conversions were made.")
            print("\nThank you for using the unit converter. Goodbye!")
            break  # Exit the loop and end the program


# Run the unit converter function to start the program
unit_converter()
