def func(operator, left_input, right_input):
    left_int = 0
    right_int = 0

    # Make sure the users input is a number so that python doesn't print an error
    try:
        int(left_input)
        int(right_input)
    except ValueError:
        print("Something wasn't typed correctly! Make sure you're typing numbers.")
    else:
        left_int = int(left_input)
        right_int = int(right_input)
        
        # Ugly, repetitive code
        if operator == "+":
            print((left_int + right_int))
        if operator == "-":
            print((left_int - right_int))
        if operator == "/":
            print((left_int / right_int))
        if operator == "*":
            print((left_int * right_int))
