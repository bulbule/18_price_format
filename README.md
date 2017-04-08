# Price Formatter

The script in `format_price.py` outputs a price in a readable way (see examples below). Note that if the price has decimals than it is rounded up by two orders. The `tests.py` merely checks that everything works properly.

# Usage
The tests can be run as:
```#!bash
$ python tests.py
```
For the `format_price.py` indicate a value in the command line that you want to format:
```#!bash
$ python format_price.py 12340.0001000
12 340
$ python format_price.py 12a
N/A
$ python format_price.py 10101.101
10 101.1
$ python format_price.py 10101.198
10 101.2
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
