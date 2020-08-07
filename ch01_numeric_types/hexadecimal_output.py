def hex_output():
    decnum = 0
    user_input = input("Enter a hex number to convert: ")
    for power, digit in enumerate(reversed(user_input)):
        decnum += int(digit, base=16) * (16 ** power)
    print(decnum)


hex_output()
