import random
import string

## Funciones para generar contraseñas
generate_password = lambda longi: ''.join(random.choices(string.ascii_letters + string.digits, k=longi))
generate_special_password = lambda longi: ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=longi))

## Historial de contraseñas
password_history = []

while(True):
    print("\n ¡Bienvenido al mejor generador de contraseñas!\n")
    print("1. Generar contraseña")
    print("2. Ver historial de contraseñas")
    print("3. Salir \n")

    option = input("Escribe tu opción: ").strip()

    if option == "1":
        longi = int(input("\nEscribe la cantidad de dígitos: "))

        caracters = input("¿Deseas incluir caracteres especiales? (Si/No): ").strip().capitalize()

        if caracters == "No":
            password = generate_password(longi)
        elif caracters == "Si":
            password = generate_special_password(longi)
        else:
            print("Opción no válida, por favor escribe 'Si' o 'No'.")
            continue

        password_history.append(password)  # Guardar en historial
        print(f"\n🔑 Tu nueva contraseña es: {password}")

    elif option == "2":
        if password_history:
            print("\n📜 Historial de contraseñas generadas:")
            for i, passw in enumerate(password_history):
                print(f"{i + 1}. {passw}")
        else:
            print("\n No has generado ninguna contraseña aún.")

    elif option == "3":
        print("\n ¡Vuelve pronto!")
        break 

    else:
        print("\n❌ Opción inválida, intenta de nuevo.")


