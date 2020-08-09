def pig_latin(param=None):
    if not param:
        user_input = input("Translate a word to pig latin: ")
    else:
        user_input = param

    if user_input[0] in "aeiou":
        return f"{user_input}way"
    
    return f"{user_input[1:]}{user_input[0]}ay"


print(pig_latin())
