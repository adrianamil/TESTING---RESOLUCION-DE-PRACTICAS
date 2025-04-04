def verificar_anagrama(palabra1: str, palabra2: str) -> bool:
    # Eliminar espacios y convertir a minúsculas para comparar correctamente
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()

    # Verificar si ambas palabras tienen el mismo número de caracteres
    if len(palabra1) != len(palabra2):
        return False

    # Comparar las palabras ordenadas
    return sorted(palabra1) == sorted(palabra2)
