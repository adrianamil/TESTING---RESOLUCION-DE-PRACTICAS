def palindromo_o_capicua(dato: int | str) -> bool:
    # si es entero
    if type(dato) == int:
        dato = str(dato)  # convertir de entero a cadena 

    elif type(dato) == str:
        pass
    else:
        return False  # si no es ni int ni str
    
    # Convertimos a minúsculas para asegurar que no haya distinción entre mayúsculas y minúsculas
    dato = dato.lower()

    # Verificar si es palíndromo
    if dato == dato[::-1]:
        return True  # Es palíndromo o capicúa
    
    return False  # No es palíndromo ni capicúa

