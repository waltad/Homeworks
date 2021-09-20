def words_ending_in_a(filepath):
    with open(filepath) as f:
        counter = 0
        for line in f:
            words = line.rstrip().split(' ')
            for word in words:
                if word.endswith('A'):
                    counter += 1
    return print(counter)


def first_word_include_in_too(filepath):
    with open(filepath) as f:
        counter = 0
        for line in f:
            words = line.rstrip().split(' ')
            if words[0] in words[1]:
                counter += 1
    return print(counter)


def number_of_anagrams(filepath):
    with open(filepath) as f:
        counter = 0
        for line in f:
            words = line.rstrip().split(' ')
            check = True
            if len(words[0]) == len(words[1]):
                for char in words[0]:
                    if char not in words[1]:
                        check = False
                if check:
                    counter += 1
    return print(counter)


if __name__ == '__main__':
    file_path = 'slowa2.txt'
#    words_ending_in_a(file_path)
#    first_word_include_in_too(file_path)
    number_of_anagrams(file_path)