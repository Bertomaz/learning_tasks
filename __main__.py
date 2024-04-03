current_number = 10

while current_number >= 0:
    if current_number > 6:
        print(current_number)
    elif current_number == 6:
        print(current_number, "Starting Engine")
    elif current_number == 5:
        print(current_number)
    elif current_number < 5 and current_number > 0:
        print(current_number, "and counting")
    else:
        print(current_number, "Liftoff")
    current_number = current_number - 1
