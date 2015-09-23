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


def money(x):
    if v.money(x):
        money = re.sub(r'[^\$0-9.]', '', x)
        if '.' in money:
            return {'currency': money[0], 'amount': float(money[1:])}
        else:
            new_money = money+'.0'
            return {'currency': new_money[0], 'amount':float(new_money[1:])}
    else:
        return None


def zipcode(x):
    if v.zipcode(x):
        x = re.sub(r'[^0-9]', '', x)
        if len(x) == 5:
            return {'zip':x, 'plus4': None}
        else:
            return {'zip':x[:5], 'plus4': x[5:]}
    else:
        return None


def date(x):
    if v.date(x):
        x = re.sub(r'[/-]', ' ', x)
        x = x.split()
        for data in x:
            if len(data) == 4:
                year = int(data)
                x.remove(data)
        month = re.sub(r'[0]', '', x[0])
        day = re.sub(r'[0]', '', x[1])
        return {'month': int(month), 'day': int(day), 'year': year}
    else:
        None
