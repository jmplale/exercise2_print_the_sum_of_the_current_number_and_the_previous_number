# making a range function with for loop
for adding in range(10):
    # making if statement
    if adding == 0:
        current_number = adding
        previous_number = 0
     # making else statment   
    else:
        current_number = adding + previous_number    

    print(f"Current Number {current_number} Previous Number {previous_number} Sum: {current_number + previous_number}")    
