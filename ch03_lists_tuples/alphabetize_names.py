from operator import itemgetter

PEOPLE = [
    {'first': 'Minney', 'last': 'Mouse', 'email': 'minney@disney.com'},
    {'first': 'Donald', 'last': 'Duck', 'email': 'donald@disney.com'},
    {'first': 'Mickey', 'last': 'Mouse', 'email': 'mickey@disney.com'}
]


def alphabetize_names(items):
    return sorted(items, key=itemgetter('last', 'first'))

print(alphabetize_names(PEOPLE))
