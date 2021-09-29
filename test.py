class CustomException(Exception):
    def __init__(self):
        message = "Dzielnik nie może być równy zeru"
        super().__init__(message)


a = 3
b = [1, 0, 2]
for elem in b:
    if elem == 0:
        raise CustomException()
    wynik = a / elem
    print(f"Wynik to: {wynik}")