
def get_rainfall():
    rainfall_by_city = {}

    while True:
        city_input = input('Enter city: ').strip()
        if not city_input:
            break

        try:
            rainfall_input = int(input('Enter rainfall: '))
        except ValueError:
            print('Enter a valid integer')
            continue

        rainfall_by_city[city_input] = rainfall_by_city.get(
            city_input, 0) + rainfall_input

    for city, rainfall in rainfall_by_city.items():
        print(f'{city}: {rainfall}')


get_rainfall()
