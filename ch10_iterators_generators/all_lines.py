import os

def all_lines(path):
    for filename in os.listdir(path):
        full_filename = os.path.join(path, filename)
        try:
            for line in open(full_filename):
                yield line.strip()
        except OSError:
            pass


for line in all_lines('ch10_iterators_generators/testdir'):
    print(line)
