def start_game(): 
    print("Bienvenido a la aventura.")
    print("Estás en un bosque oscuro.")
    persona = input("¿Cuál camino eliges? Hay uno a la izquierda y otro a la derecha: ")

    if persona.lower() == "izquierda":
        level_one()
    elif persona.lower() == "derecha":
        print("Caminas por el camino de la derecha y caes en un agujero. ¡Fin del juego!")
    else:
        print("Opción no válida. Intenta de nuevo.")
        start_game()

def level_one():
    print("Caminas por el camino de la izquierda y encuentras un río.")
    persona = input("¿Intentas cruzar nadando o buscas un puente? (Nadar/Puente): ")

    if persona.lower() == "nadar":
        print("La corriente es demasiado fuerte y te arrastra. ¡Fin del juego!")
    elif persona.lower() == "puente":
        level_two()
    else:
        print("Opción no válida. Intenta de nuevo.")
        level_one()

def level_two():
    print("Cruzas el puente y ves un castillo misterioso.")
    persona = input("¿Entras o sigues caminando? (Entrar/Seguir): ")

    if persona.lower() == "entrar":
        level_three()
    elif persona.lower() == "seguir":
        print("Te pierdes en el bosque y nunca encuentras salida. ¡Fin del juego!")
    else:
        print("Opción no válida. Intenta de nuevo.")
        level_two()

def level_three():
    print("Dentro del castillo encuentras un cofre del tesoro.")
    persona = input("¿Abrir o dejar? (Abrir/Dejar): ")

    if persona.lower() == "abrir":
        print("¡Felicidades, encontraste el One Piece! ¡Ganaste el juego!")
    elif persona.lower() == "dejar":
        print("Te fuiste con las manos vacías. ¡Fin del juego!")
    else:
        print("Opción no válida. Intenta de nuevo.")
        level_three()

# Iniciar el juego
start_game()
