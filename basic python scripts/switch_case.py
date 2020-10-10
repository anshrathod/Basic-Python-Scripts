# Switcher for implementing switch case options
def get_number(ID):
    # Prepare Cases
    switcher = {
        1: "One",
        2: "Two",  
        3: "Three",
    }

    """Return first Matched argument Value 
       if no match then returns No Match case statement."""
    return switcher.get(ID, "No Match Case")

# Get input from the user
NUMBER = int(input("Enter a Number between 1 and 3: "))

# Print the output
print(get_number(NUMBER))
