def sum_numbers(num_string):
    return sum([int(number)
                for number in num_string.split()
                if number.isdigit()])


print(sum_numbers('10 abc 20 de44 30 55fg 40'))
