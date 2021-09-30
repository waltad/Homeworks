import datetime


class NoFoodException(Exception):  # błąd oznaczający brak zapasów karmy dla żubrów
    pass


def amount_hay_and_acorn(start, end, wisents, project=True):  # start - pierwszy dzień karmienia żubrów,
    # end - ostatni dzień karmienia żubrów, wisents - liczba żubrów, project - czy wyświetlić dane?
    hay = 100000  # początkowa ilość siana
    acorn = 5000  # początkowa ilość żołędzi
    amount_delivery_hay = 0  # ilość dni, w których odbyły się dostawy siana
    amount_delivery_acorn = 0  # ilość dni, w których odbyły się dostawy żołędzi
    hay_feeding_days = 0  # ilość dni karmienia sianem
    acorn_feeding_days = 0  # ilość dni karmienia żołędziami
    first_day_feeding_acorns = None  # pierwszy dzień, w którym zaczęto karmić żołedziami
    table = []
    width = 46
    date = start  # aktualna data

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
        if date.strftime('%d-%m-%Y') == '31-12-2012' or date.strftime('%d-%m-%Y') == '31-01-2013' or \
                date.strftime('%d-%m-%Y') == '28-02-2013':
            table.append([date, hay, acorn])
        date += datetime.timedelta(days=1)
    if project:
        print(f'Amount delivery hay: {amount_delivery_hay}, amount delivery acorn: {amount_delivery_acorn}. \n'
                f'Hay feeding days: {hay_feeding_days}, acorn feeding days: {acorn_feeding_days}. \n'
                f'The first day of feeding with acorns: {first_day_feeding_acorns.strftime("%d %B %Y")} \n')
        print('-' * width)
        print(f"| {'Data':{10}} | Zapasy siana | Zapasy żołędzi |")
        print('*' * width)
        print(
            f"| {table[0][0].strftime('%d-%m-%Y')} | {(table[0][1] / 1000):{8}} ton | {(table[0][2] / 1000):{10}} ton |")
        print(
            f"| {table[0][0].strftime('%d-%m-%Y')} | {(table[1][1] / 1000):{8}} ton | {(table[1][2] / 1000):{10}} ton |")
        print(
            f"| {table[2][0].strftime('%d-%m-%Y')} | {(table[2][1] / 1000):{8}} ton | {(table[2][2] / 1000):{10}} ton |")
        print('-' * width)


def maximum_number_of_bison(start, end, wisents=1):  # fukcja wyznaczająca maksymalną liczbę żubów, którą da się wyżywić
    check = True
    while check:
        try:
            amount_hay_and_acorn(start, end, wisents, project=False)
        except NoFoodException:
            print(f'The maximum number of bison is {wisents - 1}')
            check = False
        wisents += 1


if __name__ == '__main__':
    start_time = datetime.datetime(2012, 12, 1)
    end_time = datetime.datetime(2013, 2, 28)
    bison = 90
    amount_hay_and_acorn(start_time, end_time, bison)
    maximum_number_of_bison(start_time, end_time)
