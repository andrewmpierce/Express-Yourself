import re

#location_regex = re.compile(r"\s*(.+), ([A-Z]{2})\s*$")

def binary(x):
    return re.match(r'[01]', x)

def binary_even(x):
    return re.match(r'^[01]+0$', x)


def hex(x):
    return re.match(r'[A-Fa-f0-9]+$', x)


def word(x):
    return re.match(r'^[0-9a-zA-Z-]*[a-zA-Z]$', x)


def words(x, count=None):
    split_x = re.split(' ', x)
    if count:
        if count != len(split_x):
            return False
        else:
            pass
    if None in [word(x) for x in split_x]:
        return False
    else:
        return True


def phone_number(x):
    return re.match(r'\(?[0-9]{3}\)?[-. ]?[0-9]{3}[-. ]?[0-9]{4}$', x)


def money(x):
    return re.match(r'^\$[0-9]{1,3}([,]?[0-9]{3})*([.][0-9]{2})?$', x)


def zipcode(x):
    return re.match(r'^[0-9]{5}(-[0-9]{4})?$', x)


def date(x):
    return re.match(r'^[0-9]{1,4}[/|-][0-9]{1,4}[/|-]?[0-9]{1,4}$', x)
