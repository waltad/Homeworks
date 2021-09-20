import string


def message(file_path: str) -> str:
    with open(file_path, 'r') as f:
        counter = 1
        sentence = ''
        for line in f:
            if counter % 40 == 0:
                sentence += line[9]
            counter += 1
        return sentence


def counter_other_letters(file_path: str) -> str:
    with open(file_path, 'r') as f:
        max_number_letters = 0
        for line in f:
            n = len(line.strip())
            letters_set = []
            for i in range(0, n):
                if line[i] not in letters_set:
                    letters_set.append(line[i])
            number_letters = len(letters_set)
            if number_letters > max_number_letters:
                max_number_letters = number_letters
                longest_words = line.strip()
        return f'{longest_words} {max_number_letters}'


def words_to_ten_distance_letters(file_path: str):
    with open(file_path) as f:
        alphabet = string.ascii_uppercase
        for line in f:
            n = len(line.strip())
            check = True
            for i in range(0, n - 1):
                if abs(alphabet.index(line[i]) - alphabet.index(line[i+1])) > 10:
                    check = False
            if check == True:
                    print(line.strip())


if __name__ == '__main__':
    filepath = 'sygnaly.txt'
    filepath2 = 'przyklad.txt'

    text = message(filepath)
    print(text)

    word = counter_other_letters(filepath2)
    print(word)

    words_to_ten_distance_letters(filepath2)
