def flatten(lists):
    return [number
            for numbers in lists
            for number in numbers]


print(flatten([[1, 2], [3, 4]]))
