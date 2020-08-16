def wordcount(filename):
    counts = {
        'characters': 0,
        'words': 0,
        'lines': 0,
        'unique_words': 0
    }
    unique_words = set()

    with open(filename, 'r') as f:
        for line in f:
            counts['lines'] += 1
            counts['characters'] += len(line)

            if not line.startswith(('\n')):
                counts['words'] += len(line.split())
                unique_words.update(line.split())

    counts['unique_words'] = len(unique_words)
    return counts


for key, value in wordcount('ch05_files/wcfile.txt').items():
    print(f'{key}: {value}')
