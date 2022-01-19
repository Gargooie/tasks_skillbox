import re


def calculator(R, W):
    y, x = (R, W)
    red = "R"
    white = "W"
    if R > W:
        red, white = white, red
        x, y = y, x

    a_range = red * y

    # цикл с добавлением чередования через 2
    for _ in range(x):
        match = re.search(rf"{red}{red}", a_range)
        if match is not None:
            matched = match.start() + 1
            a_range = a_range[:matched] + white + a_range[matched:]
            x -= 1
    # проверка на выполняемое условие
    match = re.search(rf"{red}{red}", a_range)
    if match is not None and x <= 0:
        print("Нет решения")
        print(a_range)
        print(y)
        return

    # добавление в начало и конец
    if x > 0:
        a_range = white + a_range
        x -= 1
    else:
        print(a_range)
        print(x)
        return

    if x > 0:
        a_range = a_range + white
        x -= 1
    else:
        print(a_range)
        print(x)
        return

    # цикл с добавлением чередования через 1
    for _ in range(x):
        match = re.search(rf"{red}{white}{red}", a_range)
        if match is not None:
            # print(match.start())
            matched = match.start() + 1
            a_range = a_range[:matched] + white + a_range[matched:]
            x -= 1
    if x == 0:
        print(a_range)
    else:
        print("Нет решения")


red = int(input("Кол-во красных: "))
white = int(input("Кол-во белых: "))

calculator(red, white)
