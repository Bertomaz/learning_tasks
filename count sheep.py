
input_txt = input("which word should i repeat? ")
repeat = True
länge = len(input_txt)
anfangsindex = 0
while repeat:
    print(input_txt[anfangsindex:länge])
    if anfangsindex == länge:
        repeat = False
    anfangsindex = anfangsindex + 1
