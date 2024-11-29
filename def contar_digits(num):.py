def contar_digits(num):
    """Retorna la quantitat de dígits d'un número."""
    return len(str(num))

def main():
    # Demanar un número a l'usuari
    while True:
        numero = int(input("Introdueix un número (1 - 900000): "))
        if 1 <= numero <= 900000:
            break
        else:
            print("Error: El número ha de ser entre 1 i 900000.")

    # Comptar els dígits
    quantitat_digits = contar_digits(numero)

    # Mostrar el resultat
    print(f"El número {numero} té {quantitat_digits} dígits.")

# Executar el programa
if __name__ == "__main__":
    main()