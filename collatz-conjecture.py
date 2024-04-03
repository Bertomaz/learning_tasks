starting_point_ok = False
continue_sequence = True


while starting_point_ok == False:

    starting_point = input("Please enter a positive Integer:")

    if starting_point.isdigit():
        starting_point = int(starting_point)
    
    if type(starting_point) == int and starting_point > 0:
        starting_point_ok = True
    else:
        print("it must be a positive Integer !")

current_point = starting_point

while continue_sequence == True:
    print(current_point)

    if (current_point % 2) == 0:
        current_point = current_point // 2
    else:
        current_point = 3 * current_point + 1

    if current_point == 4 or current_point == 2 or current_point == 1 :
        continue_sequence = False
        print(current_point)
    else:
        pass
