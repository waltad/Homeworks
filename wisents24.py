import datetime


def amount_hay_and_acorn(start, end):
    hay = 100000
    acorn = 5000
    wisents = 90
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
            acorn -= 20 * wisents
            acorn_feeding_days += 1
            if first_day_feeding_acorns is None:
                first_day_feeding_acorns = date
        if date.strftime('%a') == 'Fri':
            hay += 15000
            amount_delivery_acorn += 1
        if date.strftime('%a') == 'Tue':
            acorn += 4000
            amount_delivery_hay += 1
        date += datetime.timedelta(days=1)
    return print(f'Amount delivery hay: {amount_delivery_hay}, amount delivery acorn: {amount_delivery_acorn}. \n'
                 f'Hay feeding days: {hay_feeding_days}, acorn feeding days: {acorn_feeding_days}. \n'
                 f'The first day of feeding with acorns: {first_day_feeding_acorns.strftime("%x")}.')


if __name__ == '__main__':
    start_time = datetime.datetime(2012, 12, 1)
    end_time = datetime.datetime(2013, 2, 28)
    amount_hay_and_acorn(start_time, end_time)
