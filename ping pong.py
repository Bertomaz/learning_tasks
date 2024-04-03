continue_match = True

while continue_match == True :
    user_input = ""
    user_input = input("please put in your next move:")
    user_want_to_continue = ""
    existing_input = False

    if user_input == "ping":
        print("pong")
    elif user_input == "pong":
        print("ping")
    elif user_input == "":
        pass
    else:
        print("That is not Ping-Pong")

    while existing_input == False:
        user_want_to_continue = input("Do you Want to stop ?")
        if user_want_to_continue == "stop":
            existing_input = True
            continue_match = False
        elif user_want_to_continue == "":
            existing_input = True
        else:
            print("please answer with stop if you want to stop")
