# Excepciones

while True:
    try:
        numero = int(input("Digite un número:"))
        print(f"La suma es: {numero+10}")

    except: # Se ejecuta cuando el usuario no digita bien
        print("Ha ocurrido un error")

    else: # Se ejecuta solo cuando el except no se ejecuta
        print("Programa finalizado correctamente")
        break

    finally:  # Se ejecutará siempre
        print("Iteración finalizada")

# Carolina EM