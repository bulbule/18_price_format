import argparse


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
    number = float('{:.2f}'.format(number))
    if (number).is_integer():
        return int(number)
    else:
        return number


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('price', help='a price to format')
    args = parser.parse_args()
    print(format_price(args.price))
