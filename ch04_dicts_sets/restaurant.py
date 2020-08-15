MENU = {
    'sandwich': 10,
    'tea': 7
}


def restaurant(menu):
    total_cost = 0
    while True:
        user_order = input('Enter your order: ').strip()

        if not user_order:
            break

        if user_order in menu.keys():
            total_cost += menu[user_order]
            print(
                f'{user_order} costs {menu[user_order]}, total is {total_cost}')
        else:
            print(f'Sorry, we are fresh out of {user_order}')

    print(f'Your total is {total_cost}')


restaurant(MENU)
