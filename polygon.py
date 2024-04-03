from math import sin, tan, degrees, radians
number_corners_ok = False
side_length_ok = False


while number_corners_ok == False:
    number_corners = input("Please enter the Number of corners:")
    if number_corners.isdigit():
        number_corners = int(number_corners)
        
    if type(number_corners) == int and number_corners >= 3:
        number_corners_ok = True
    else:
        print("Please enter a whole number greater than 3")

while side_length_ok == False:
    side_length = input("Please enter the length of the Sides in mm:")
    if side_length.replace('.','',1).isdigit() == True:
        side_length = float(side_length)
        side_length_ok = True
    else:
        print("The Input must be a real Number")

print(number_corners, type(number_corners))
print(side_length, type(side_length))


number_sides = number_corners
center_angle = 1 / number_sides * 360
corner_angle = (number_sides - 2) / number_sides * 180
outer_radius = side_length / (2* sin(radians(180)/number_sides))
inner_radius = side_length / (2 * tan(radians(180)/number_sides))

print("the Center angle is", center_angle,"degrees")
print("the Corner Angle is" , corner_angle, "degrees")
print("the outer Radius is", outer_radius, "mm")
print("the inner Radius is", inner_radius, "mm")
