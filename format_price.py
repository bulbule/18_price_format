import argparse
from decimal import *


def format_price(price):
    not_available = 'N/A'
    try:
        if not isinstance(price, bool):
            price = float(price)
        else:
            return not_available
    except (ValueError, TypeError):
        return not_available
    if not price:
        return not_available
    if (price).is_integer():
        price = int(price)
    else:
        price = round_float_number_to_two_decimals(price)
    return "{:,}".format(price).replace(',', ' ')


def round_float_number_to_two_decimals(number):
    getcontext().prec = 30
    return float(
        Decimal(
            '{}'.format(number)).quantize(
            Decimal('.01'),
            rounding=ROUND_UP))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('price', help='a price to format')
    args = parser.args_parse()
    print(format_price(args.price))
