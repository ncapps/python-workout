def pig_latin(word=None):
    if not word:
        return word

    if word[0] in "aeiou":
        return f"{word}way"

    return f"{word[1:]}{word[0]}ay"


def plfile(filename):
    with open(filename, 'r') as f:
        return ' '.join(pig_latin(word)
                         for line in f
                         for word in line.split())


print(plfile('ch07_functional_programming/test_file.txt'))
