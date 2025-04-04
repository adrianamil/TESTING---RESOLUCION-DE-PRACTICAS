from primo import esPrimo

def test_es_primo():
    # Caso de prueba 1: Verificar si 1 es primo.
    resultado = esPrimo(1)
    assert resultado == False

    # Caso de prueba 2: Verificar si 2 es primo.
    resultado = esPrimo(2)
    assert resultado == True

    # Caso de prueba 3: Verificar si 3 es primo.
    resultado = esPrimo(3)
    assert resultado == True

    # Caso de prueba 4: Verificar si 4 es primo.
    resultado = esPrimo(4)
    assert resultado == False

    # Caso de prueba 5: Verificar si 5 es primo.
    resultado = esPrimo(5)
    assert resultado == True

    # Caso de prueba 6: Verificar si 9 es primo.
    resultado = esPrimo(9)
    assert resultado == False

    # Caso de prueba 7: Verificar si 11 es primo.
    resultado = esPrimo(11)
    assert resultado == True

    # Caso de prueba 8: Verificar si 15 es primo.
    resultado = esPrimo(15)
    assert resultado == False

    # Caso de prueba 9: Verificar si 17 es primo.
    resultado = esPrimo(17)
    assert resultado == True

    # Caso de prueba 10: Verificar si 18 es primo.
    resultado = esPrimo(18)
    assert resultado == False

    # Caso de prueba 11: Verificar si 19 es primo.
    resultado = esPrimo(19)
    assert resultado == True

    # Caso de prueba 12: Verificar si 21 es primo.
    resultado = esPrimo(21)
    assert resultado == False

    # Caso de prueba 13: Verificar si 23 es primo.
    resultado = esPrimo(23)
    assert resultado == True

    # Caso de prueba 14: Verificar si 25 es primo.
    resultado = esPrimo(25)
    assert resultado == False

    # Caso de prueba 15: Verificar si 29 es primo.
    resultado = esPrimo(29)
    assert resultado == True

    # Caso de prueba 16: Verificar si 31 es primo.
    resultado = esPrimo(31)
    assert resultado == True

    # Caso de prueba 17: Verificar si 35 es primo.
    resultado = esPrimo(35)
    assert resultado == False

    # Caso de prueba 18: Verificar si 37 es primo.
    resultado = esPrimo(37)
    assert resultado == True

    # Caso de prueba 19: Verificar si 50 es primo.
    resultado = esPrimo(50)
    assert resultado == False

    # Caso de prueba 20: Verificar si 53 es primo.
    resultado = esPrimo(53)
    assert resultado == True


test_es_primo()
