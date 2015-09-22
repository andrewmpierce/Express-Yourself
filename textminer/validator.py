import re

#location_regex = re.compile(r"\s*(.+), ([A-Z]{2})\s*$")

def binary(x):
    return re.match(r'[01]', x)

def binary_even(x):
    return re.match(r'^[01]+0$', x)
