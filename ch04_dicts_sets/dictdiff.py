D1 = {'a': 1, 'b': 2, 'c': 3}
D2 = {'a': 1, 'b': 2, 'c': 4}
D3 = {'a': 1, 'b': 2, 'd': 3}
D4 = {'a': 1, 'b': 2, 'c': 4}
D5 = {'a': 1, 'b': 2, 'd': 4}


def dictdiff(first, second):
    output = {}
    all_keys = first.keys() | second.keys()
    
    for key in all_keys:
        if first.get(key) != second.get(key):
            output[key] = [first.get(key), second.get(key)]

    return output


print(dictdiff(D1, D1))
print(dictdiff(D1, D2))
print(dictdiff(D3, D4))
print(dictdiff(D1, D5))
