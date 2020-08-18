def join_number(num_range):
    return ','.join(str(number)
                    for number in range(num_range))


print(join_number(15))
