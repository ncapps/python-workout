def ubbi_dubbi(param=None):
    if not param:
        user_input = "Translate to ubbi dubbi: "
    else:
        user_input = param

    output = []
    for letter in user_input:
        if letter in "aeiou":
            output.append(f"ub{letter}")
        else:
            output.append(letter)
    
    return "".join(output)

print(ubbi_dubbi("soap"))
