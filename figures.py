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
            while a % b != 0:
                gcd = a % b
                a = b
                b = gcd



if __name__ == '__main__':
    file_path = 'liczby.txt'
    numbers_in_ascending_order(file_path)