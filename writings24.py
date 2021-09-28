from math import sqrt


def prime_numbers(filepath):
    with open(filepath) as f:
        amount_prime_numbers = 0
        for line in f:
            counter = 0
            factor = 2
            check = True
            for char in line.strip():
                counter += ord(char)
            while factor <= sqrt(counter) and check:
                if counter % factor == 0:
                    check = False
                factor += 1
            if check:
                amount_prime_numbers += 1
        return print(f'The number of primes is {amount_prime_numbers}')


def rising_inscriptions(filepath):
    with open(filepath) as f:
        for line in f:
            check = True
            line = line.strip()
            for i in range(len(line)-1):
                if ord(line[i+1]) < ord(line[i]):
                    check = False
            if check:
                print(line)


def repeated_inscriptions(filepath):
    with open(filepath) as f:
        writings = []
        repeated_writings = []
        for line in f:
            line = line.strip()
            if line not in writings:
                writings.append(line)
            else:
                if line not in repeated_writings:
                    repeated_writings.append(line)
        return print(repeated_writings)


if __name__ == '__main__':
    file_path = 'napis.txt'
    # prime_numbers(file_path)
    # rising_inscriptions(file_path)
    repeated_inscriptions(file_path)
