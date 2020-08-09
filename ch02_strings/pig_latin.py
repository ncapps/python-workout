def pig_latin():
    user_input = input("Translate a word to pig latin: ")

    if user_input[0] in "aeiou":
        return f"{user_input}way"
    
    return f"{user_input[1:]}{user_input[0]}ay"


print(pig_latin())
