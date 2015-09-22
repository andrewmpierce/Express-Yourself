import re
import textminer.validator as v

def words(x):
    if v.words(x):
        return x.split(' ')
    else:
        return None

def phone_number(x):
    if v.phone_number(x):
        number = re.sub(r'[^0-9]', '', x)
        ret = {'area_code': number[0:3], 'number': number[3:6]+'-'+number[6:10]}
        #print(ret)
        return ret
    else:
        return None
