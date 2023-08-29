def create_list():
    """
    Creates a list of invoice numbers based on user input.
    
    Returns:
    invoice_list (list): List of entered invoice numbers.
    """
    invoice_list = []
    while True:
        user_input = input("Enter the Receipt # or (type 'exit' to quit):")
        if user_input.lower() == "exit":
            break
        invoice_list.append(user_input)
    return invoice_list

if __name__ == "__main__":
    # Call the create_list function to gather invoice numbers from the user
    my_list = create_list()
    print("Created List:", my_list)