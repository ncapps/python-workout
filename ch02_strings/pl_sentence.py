from pig_latin import pig_latin


def pl_sentence(param=None):
    if not param:
        user_input = input("Translate a sentence: ")
    else:
        user_input = param

    output = []
    for word in user_input.split():
        output.append(pig_latin(word))

    return " ".join(output)


print(pl_sentence())
