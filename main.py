import requests

def show_dishes():
    """
    Muestra una lista básica de platos disponibles
    para que el usuario pueda escoger un número.
    """

    print("\nObteniendo lista de platos disponibles...\n")

    url = "https://api-colombia.com/api/v1/TypicalDish"

    response = requests.get(url)

    if response.status_code == 200:

        dishes = response.json()

        print("====== PLATOS DISPONIBLES ======\n")

        # Mostramos algunos platos disponibles
        for dish in dishes[:10]:
            print(f"{dish['id']} -> {dish['name']}")

        print("\n===============================\n")

    else:
        print("No fue posible cargar los platos disponibles.")


def dish_fetch(num):
    print("\nConectando con API Colombia...")
    
    url = f"https://api-colombia.com/api/v1/TypicalDish/{num}"

    print("Buscando información del plato...")

    response = requests.get(url)

    # Verificamos si la petición fue exitosa
    if response.status_code == 200:
        print("¡Plato encontrado correctamente!")

        data = response.json()

        # Retornamos un diccionario organizado
        return {
            "id": data.get("id"),
            "name": data.get("name"),
            "description": data.get("description"),
            "ingredients": data.get("ingredients"),
            "image": data.get("image")
        }

    # Si no se encuentra el plato
    print("No se encontró el plato.")

    return {
        "error": "Plato no encontrado"
    }


def main():
    print("===================================")
    print(" MENÚ DE PLATOS TÍPICOS COLOMBIANOS ")
    print("===================================")

    print("\n¡Bienvenido!")
    print("Aquí podrás explorar platos típicos de Colombia.\n")

    # Mostramos platos disponibles
    show_dishes()

    try:
        num = int(input("Por favor ingresa el número del plato: "))

        print("\nProcesando tu solicitud...")

        dish = dish_fetch(num)

        print("\n========== INFORMACIÓN DEL PLATO ==========\n")

        for key, value in dish.items():
            print(f"{key}: {value}")

        print("\n===========================================")

    except ValueError:
        print("\nEntrada inválida.")
        print("Por favor ingresa únicamente números.")


if __name__ == "__main__":
    main()