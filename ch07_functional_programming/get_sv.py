def get_sv(filename):
    vowels = {'a', 'e', 'i', 'o', 'u'}

    with open(filename, 'r') as f:
        return {one_word.strip()
                for one_word in f
                if vowels < set(one_word.lower())}


for word in get_sv('ch07_functional_programming/one_word.txt'):
    print(word)
