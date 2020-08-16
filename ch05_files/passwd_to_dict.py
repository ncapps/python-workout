def passwd_to_dict(filename):
    users = {}
    with open(filename, 'r') as f:
        for line in f:
            # Ignores comment and blank lines
            if not line.startswith(('#', '\n')):
                user_info = line.split(':')
                users[user_info[0]] = user_info[2]
    return users

print(passwd_to_dict('./fakefile.txt'))