def numbers_in_ascending_order(filepath):
    with open(filepath) as f:
        counter = 0
        for line in f:
            numbers = line.rstrip().split(' ')
            if int(numbers[0]) < int(numbers[1]) < int(numbers[2]):
                counter += 1
                # print(numbers[0], numbers[1], numbers[2])
        return print(f'In the {counter} lines, the numbers are in ascending order.')


def greatest_common_divisor(filepath):
    with open(filepath) as f:
        counter = 0
        for line in f:
            numbers = line.rstrip().split(' ')
            numbers = [int(i) for i in numbers]
            numbers.sort()
            a, b, c = numbers[2], numbers[1], numbers[0]
            if a % b == 0:
                gcd = b
            else:
                while a % b != 0:
                    gcd = a % b
                    a = b
                    b = gcd
            if c % gcd != 0:
                d = gcd
                while c % d != 0:
                    gcd = c % d
                    c = d
                    d = gcd
            counter += gcd
        return print(f'Sum of the greatest common divisors is: {counter}')


def sum_of_digits_in_the_row(filepath):
    with open(filepath) as f:
        counter_sum_35 = 0
        counter_sum_max = 0
        sum_digits_max = 0
        for line in f:
            digits = line.strip().replace(' ', '')
            sum_digits = 0
            for digit in range(len(digits)):
                sum_digits += int(digits[digit])
            if sum_digits == 35:
                counter_sum_35 += 1
            if sum_digits > sum_digits_max:
                sum_digits_max = sum_digits
    with open(filepath) as f:
        for line in f:
            digits = line.strip().replace(' ', '')
            sum_digits = 0
            for digit in range(len(digits)):
                sum_digits += int(digits[digit])
            if sum_digits == sum_digits_max:
                counter_sum_max += 1
        return print(f'Number of lines for which the sum of the digits of all three written numbers is equal 35: '
                     f'{counter_sum_35}\nThe greatest sum of digits in the row: {sum_digits_max} the number of rows '
                     f'where the sum of the digits is equal to the highest value: {counter_sum_max}')


if __name__ == '__main__':
    file_path = 'liczby.txt'
    # file_path2 = 'liczby2.txt'
    # file_path3 = 'liczby3.txt'
    numbers_in_ascending_order(file_path)
    greatest_common_divisor(file_path)
    sum_of_digits_in_the_row(file_path)
