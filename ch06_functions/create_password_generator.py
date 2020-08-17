import random


def create_password_generator(valid_chars):
    def create_password_by(length):
        return ''.join([random.choice(valid_chars) for _ in range(length)])
    return create_password_by


alpha_password = create_password_generator('abcdef')
symbol_password = create_password_generator('!@#$%')

print(alpha_password(5))
print(alpha_password(10))
print(symbol_password(5))
print(symbol_password(10))
