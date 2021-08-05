def echo(name: str):
    print('hola ', name)


def test(numero: int):
    if numero < 0:
        print('true')
    elif numero > 10:
        print('superior')
    else:
        print('false')


def test2():
    coleccion = [2, 4, 6, 8, 10]
    for element in coleccion:
        print(element)


def test3(number: int):
    while number < 10:
        print(number)
        number += 1


if __name__ == '__main__':
    echo('World!')
    test2()
    test3(4)
    test(11)
