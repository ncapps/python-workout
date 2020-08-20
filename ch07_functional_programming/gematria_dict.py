import string


def gematria_dict():
    return {letter: index
            for index, letter in enumerate(string.ascii_lowercase, 1)
            }

GEMATRIA = gematria_dict()

def gematria_for(word):
    return sum(GEMATRIA.get(char, 0)
               for char in word)


def gematria_equal_words(word, filename):
    score = gematria_for(word)
    with open(filename, 'r') as f:
        return {one_word.strip()
                for one_word in f
                if score == gematria_for(one_word.lower())}


# print(gematria_dict())
# print(gematria_for('cat'))
print(gematria_equal_words('cat', 'ch07_functional_programming/words.txt'))
