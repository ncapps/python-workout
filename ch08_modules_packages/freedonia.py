from decimal import Decimal

RATES = {
    'chico': Decimal('0.50'),
    'groucho': Decimal('0.70'),
    'harpo': Decimal('0.50'),
    'zeppo': Decimal('0.40')
}


class HourTooLowError(Exception):
    pass


class HourTooHighError(Exception):
    pass


def time_percentage(hour):
    return hour / Decimal('24.0')


def calculate_tax(amount, province, hour):
    if hour < 0:
        raise HourTooLowError(f'Hour of {hour} is < 0')

    if hour >= 24:
        raise HourTooHighError(f'Hour of {hour} is >= 24')
    
    return float(amount * RATES.get(province.lower(), 0) * time_percentage(hour))
