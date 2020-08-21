def menu(**kwargs):
    while True:
        func = input('Enter function name: ').lower()
        if func in kwargs:
            break
        print(f'{func} is not a valid function name.')

    return kwargs[func]()
