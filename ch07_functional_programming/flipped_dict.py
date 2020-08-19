D = {'a': 1, 'b': 2, 'c': 3}


def flipped_dict(d):
    return {value: key
            for key, value in d.items()}


print(flipped_dict(D))
