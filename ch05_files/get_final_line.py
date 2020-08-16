def get_final_line(filename):
    final_line = ''
    with open(filename, 'r') as f:
        for current_line in f:
            final_line = current_line
        return final_line


print(get_final_line('./fakefile.txt'))
