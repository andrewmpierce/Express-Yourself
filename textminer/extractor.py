import re


def phone_numbers(x):
    #x = re.split(r'\s', x)
    x = re.findall(r'\(?[0-9]{3}\)?[-. ]?[0-9]{3}[-. ]?[0-9]{4}', x)
    return x
    #numbers = re.match(r'\(?[0-9]{3}\)?[-. ]?[0-9]{3}[-. ]?[0-9]{4}', x)
    # for word in x:
    #     if re.match(r'\(?[0-9]{3}\)?[-. ]?[0-9]{3}[-. ]?[0-9]{4}', word):
    #         nums.append(word)
    # print(nums)
