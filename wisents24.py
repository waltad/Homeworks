import datetime


class NoFoodException(Exception):
    pass


def amount_hay_and_acorn(start, end, wisents, project=True):
    hay = 100000
    acorn = 5000
    amount_delivery_hay = 0
    amount_delivery_acorn = 0
    hay_feeding_days = 0
    acorn_feeding_days = 0
    first_day_feeding_acorns = None
    date = start

    while date <= end:
        if hay >= 50000:
            hay -= 40 * wisents
            hay_feeding_days += 1
        else:
            if acorn - (20 * wisents) >= 0:
                acorn -= 20 * wisents
                acorn_feeding_days += 1
                if first_day_feeding_acorns is None:
                    first_day_feeding_acorns = date
            else:
                if hay - (40 * wisents) >= 0:
                    hay -= 40 * wisents
                else:
                    raise NoFoodException(f'There is not enough food for {wisents} bison')
        if date.strftime('%a') == 'Fri':
            hay += 15000
            amount_delivery_acorn += 1
        if date.strftime('%a') == 'Tue':
            acorn += 4000
            amount_delivery_hay += 1
        date += datetime.timedelta(days=1)
    if project:
        return print(f'Amount delivery hay: {amount_delivery_hay}, amount delivery acorn: {amount_delivery_acorn}. \n'
                     f'Hay feeding days: {hay_feeding_days}, acorn feeding days: {acorn_feeding_days}. \n'
                     f'The first day of feeding with acorns: {first_day_feeding_acorns.strftime("%d")}'
                     f' {first_day_feeding_acorns.strftime("%B")} {first_day_feeding_acorns.strftime("%Y")}.')


def maximum_number_of_bison(start, end, wisents):
    check = True
    while check:
        try:
            amount_hay_and_acorn(start, end, wisents, project=False)
        except NoFoodException:
            print(f'The maximum number of bison is {wisents-1}')
            check = False
        wisents += 1



if __name__ == '__main__':
    start_time = datetime.datetime(2012, 12, 1)
    end_time = datetime.datetime(2013, 2, 28)
    bison = 90
    amount_hay_and_acorn(start_time, end_time, bison)
    maximum_number_of_bison(start_time, end_time, bison)
