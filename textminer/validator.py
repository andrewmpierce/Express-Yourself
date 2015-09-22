import re

#location_regex = re.compile(r"\s*(.+), ([A-Z]{2})\s*$")

def binary(x):
    return re.match(r'[01]', x)

def binary_even(x):
    return re.match(r'^[01]+0$', x)


def hex(x):
    return re.match(r'[A-Fa-f0-9]{3}', x)

def word(x):
    return re.match(r'[A-Za-z0-9-]{4}', x)
