

if True:
    earplugs_in_stock = 10
    goggles_in_stock = 8
    gloves_in_stock = 6
    continue_dispensing = True
    stock = [earplugs_in_stock,goggles_in_stock,gloves_in_stock]
    while continue_dispensing:
        print("there are ", stock[0], " earplugs, ", stock[1], " goggles and ", stock[2], " gloves in stock")
        try_input = True
        while try_input:
            user_input = input("please enter what you would like to get dispensed: ")
            if user_input == "gloves" or user_input == "goggles" or user_input == "earplugs" or user_input == "stop":
                try_input = False
            else:
                print("please enter gloves, goggles or earplugs or stop if you want to stop")
        if user_input == "gloves":
            stock[2] = stock[2] - 2
        elif user_input == "goggles":
            stock[1] = stock[1] - 1
        elif user_input == "earplugs":
            stock[0] = stock[0] - 2
        elif user_input == "stop":
            continue_disensing = False
            
        for i in range(0, len(stock)):
            if stock[i] == 0:
                continue_dispensing = False

        if continue_dispensing == True:
            try_continue = True
            while try_continue:
                input_continue = input("do you want to dispense something else ? Y/N")
                if input_continue == "N" or input_continue == "n":
                    continue_dispensing = False
                    try_continue = False
                elif input_continue == "Y" or input_continue == "y":
                    try_continue = False
                else:
                    print("something went wrong :(, please try again ->")

                
    print("there are ", stock[0], " earplugs, ", stock[1], " goggles and ", stock[2], " gloves in stock")
    
        
