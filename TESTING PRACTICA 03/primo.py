def esPrim(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

numero = int(input("Ingresa un numero: "))

if esPrim(numero):
    print(f"{numero} es primo.")
else:
    print(f"{numero} no es primo.")
