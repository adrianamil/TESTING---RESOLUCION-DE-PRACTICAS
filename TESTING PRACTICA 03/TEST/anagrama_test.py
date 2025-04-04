from anagrama import verificar_anagrama

def test_verificar_anagrama():
    # Caso 1: Anagramas con palabras simples
    resultado = verificar_anagrama("amor", "roma")
    assert resultado == True  # "amor" y "roma" son anagramas

    # Caso 2: No es anagrama con palabras simples
    resultado = verificar_anagrama("hello", "bye")
    assert resultado == False  # "hello" y "bye" no son anagramas

    # Caso 3: Anagrama con palabras de diferente longitud
    resultado = verificar_anagrama("amor", "amores")
    assert resultado == False  # "amor" y "amores" no son anagramas (diferente longitud)

    # Caso 4: Anagrama con palabras en mayúsculas
    resultado = verificar_anagrama("Listen", "Silent")
    assert resultado == True  # "Listen" y "Silent" son anagramas, ignorando mayúsculas/minúsculas

    # Caso 5: Anagrama con espacios
    resultado = verificar_anagrama("el amor", "Roma le")
    assert resultado == True  # "el amor" y "Roma le" son anagramas, ignorando espacios

    # Caso 6: No es anagrama con palabras con letras repetidas
    resultado = verificar_anagrama("hello", "heelllo")
    assert resultado == False  # "hello" y "heelllo" no son anagramas (diferente cantidad de letras)

    # Caso 7: Anagrama con palabras en minúsculas
    resultado = verificar_anagrama("triangle", "integral")
    assert resultado == True  # "triangle" y "integral" son anagramas

    # Caso 8: Anagrama con palabras cortas
    resultado = verificar_anagrama("aba", "aab")
    assert resultado == True  # "aba" y "aab" son anagramas

    # Caso 9: No es anagrama con palabras completamente diferentes
    resultado = verificar_anagrama("world", "earth")
    assert resultado == False  # "world" y "earth" no son anagramas

    # Caso 10: Anagrama con una sola letra
    resultado = verificar_anagrama("a", "a")
    assert resultado == True  # "a" y "a" son anagramas

    # Caso 11: Anagrama con diferentes letras
    resultado = verificar_anagrama("pot", "top")
    assert resultado == True  # "pot" y "top" son anagramas

    # Caso 12: No es anagrama con palabras que tienen letras repetidas pero no coinciden
    resultado = verificar_anagrama("apple", "ppale")
    assert resultado == False  # "apple" y "ppale" no son anagramas

    # Caso 13: Anagrama con letras en orden invertido
    resultado = verificar_anagrama("hello", "olleh")
    assert resultado == True  # "hello" y "olleh" son anagramas

    # Caso 14: No es anagrama con caracteres diferentes
    resultado = verificar_anagrama("abcd", "abef")
    assert resultado == False  # "abcd" y "abef" no son anagramas

    # Caso 15: Anagrama con palabras con diferentes letras pero mismas frecuencias
    resultado = verificar_anagrama("aabb", "bbaa")
    assert resultado == True  # "aabb" y "bbaa" son anagramas

    # Caso 16: Anagrama con números como letras
    resultado = verificar_anagrama("123", "231")
    assert resultado == True  # "123" y "231" son anagramas

    # Caso 17: No es anagrama con palabra vacía y palabra con letras
    resultado = verificar_anagrama("", "a")
    assert resultado == False  # "" y "a" no son anagramas

    # Caso 18: No es anagrama con palabra con espacio y palabra vacía
    resultado = verificar_anagrama(" ", "")
    assert resultado == False  # " " y "" no son anagramas

    # Caso 19: No es anagrama con palabra vacía y otra con letras
    resultado = verificar_anagrama("", "abc")
    assert resultado == False  # "" y "abc" no son anagramas

    # Caso 20: Anagrama con palabras que contienen caracteres especiales
    resultado = verificar_anagrama("a@b#", "#b@a")
    assert resultado == True  # "a@b#" y "#b@a" son anagramas

# Ejecutar los casos de prueba
test_verificar_anagrama()
