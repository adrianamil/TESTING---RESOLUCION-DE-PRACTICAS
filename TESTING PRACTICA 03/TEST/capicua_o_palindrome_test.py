from capicua_o_palindromo import palindromo_o_capicua

def test_palindromo_o_capicua():
    # Caso 1: Palíndromo con números
    resultado = palindromo_o_capicua(12321)
    assert resultado == True  # 12321 es un capicúa

    # Caso 2: No es palíndromo con números
    resultado = palindromo_o_capicua(12345)
    assert resultado == False  # 12345 no es un capicúa

    # Caso 3: Palíndromo con palabras
    resultado = palindromo_o_capicua("radar")
    assert resultado == True  # "radar" es un palíndromo

    # Caso 4: No es palíndromo con palabras
    resultado = palindromo_o_capicua("hello")
    assert resultado == False  # "hello" no es un palíndromo

    # Caso 5: Número de un solo dígito (siempre palíndromo)
    resultado = palindromo_o_capicua(7)
    assert resultado == True  # Cualquier número de un solo dígito es un palíndromo

    # Caso 6: Palíndromo con palabra en mayúsculas
    resultado = palindromo_o_capicua("AnNa")
    assert resultado == True  # "AnNa" es un palíndromo, sin tener en cuenta mayúsculas/minúsculas

    # Caso 7: Entrada con caracteres especiales
    resultado = palindromo_o_capicua("a@a")
    assert resultado == True  # "a@a" es un palíndromo

    # Caso 8: Entrada con número negativo (debería devolver False, no es un palíndromo por su signo)
    resultado = palindromo_o_capicua(-12321)
    assert resultado == False  # -12321 no es un capicúa

    # Caso 9: Entrada vacía (cadena vacía o 0)
    resultado = palindromo_o_capicua("")
    assert resultado == True  # La cadena vacía es un palíndromo
    resultado = palindromo_o_capicua(0)
    assert resultado == True  # El número 0 es un palíndromo

    # Caso 10: Número capicúa
    resultado = palindromo_o_capicua(12321)
    assert resultado == True  # 12321 es un capicúa

    # Caso 11: Número no capicúa
    resultado = palindromo_o_capicua(12345)
    assert resultado == False  # 12345 no es un capicúa

    # Caso 12: Cadena capicúa
    resultado = palindromo_o_capicua("madam")
    assert resultado == True  # "madam" es un palíndromo (capicúa)

    # Caso 13: Cadena no capicúa
    resultado = palindromo_o_capicua("example")
    assert resultado == False  # "example" no es un palíndromo

    # Caso 14: Número capicúa con un solo dígito
    resultado = palindromo_o_capicua(5)
    assert resultado == True  # El número 5 es un capicúa (un solo dígito)

    # Caso 15: Palabra capicúa con espacios
    resultado = palindromo_o_capicua("a man a plan a canal panama")
    assert resultado == True  # "a man a plan a canal panama" es un capicúa (ignora los espacios)

    # Caso 16: Número con ceros al inicio (por ejemplo, "01210")
    resultado = palindromo_o_capicua("01210")
    assert resultado == True  # "01210" es un capicúa (ignora los ceros a la izquierda)

    # Caso 17: Número con ceros al final (por ejemplo, "1001")
    resultado = palindromo_o_capicua("1001")
    assert resultado == True  # "1001" es un capicúa

    # Caso 18: Palabra con caracteres especiales (con espacio al final)
    resultado = palindromo_o_capicua("racecar ")
    assert resultado == False  # "racecar " no es un capicúa porque tiene un espacio extra al final

    # Caso 19: Número grande que es capicúa
    resultado = palindromo_o_capicua(9876543210123456789)
    assert resultado == True  # 9876543210123456789 es un capicúa

    # Caso 20: Número con letras (entrada inválida)
    resultado = palindromo_o_capicua("123abc321")
    assert resultado == False  # "123abc321" no es ni un palíndromo ni capicúa

# Ejecutar los casos de prueba
test_palindromo_o_capicua()
