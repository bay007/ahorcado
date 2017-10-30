import random


# Se definen las imagenes multilinea que estaran sirviendo para visualizar el estado del juego
IMAGENES_AHORCADO = ['''
    +-------+
            |
            |
            |
            |
            |
            |
            |
   /-----------------\\
  /___________________\\
    ''',
                     '''
    +-------+
    |       |
    O       |
            |
            |
            |
            |
            |
   /-----------------\\
  /___________________\\
    ''',
                     '''
    +-------+
    |       |
   [O       |
            |
            |
            |
            |
            |
   /-----------------\\
  /___________________\\
    ''',
                     '''
    +-------+
    |       |
   [O]      |
            |
            |
            |
            |
            |
   /-----------------\\
  /___________________\\
    ''', '''
    +-------+
    |       |
   [O]      |
    |       |
    |       |
            |
            |
            |
   /-----------------\\
  /___________________\\
  ''',
                     '''
    +-------+
    |       |
   [O]      |
    |\      |
    |       |
            |
            |
            |
   /-----------------\\
  /___________________\\
  ''',
                     '''
    +-------+
    |       |
   [O]      |
   /|\      |
    |       |
            |
            |
            |
   /-----------------\\
  /___________________\\
  ''',
                     '''
    +-------+
    |       |
   [O]      |
   /|\      |
    |       |
     \      |
            |
            |
   /-----------------\\
  /___________________\\
  ''',
                     '''
    +-------+
    |       |
   [O]      |
   /|\      |
    |       |
   / \      |
            |
            |
   /-----------------\\
  /___________________\\
  '''
                     ]

LISTA_PALABRAS_POSIBLES = ("Abrelatas", "Disposicion", "Parlante", "Aire", "Drogas", "PC", "Andrea", "Escuela", "Pelusa", "Andres", "Esfera", "Periferico", "Animal", "Esquina", "Perro", "Antonia", "Eugenia", "Piscinas", "Antonio", "Excel", "Planta", "Argentina", "Fernanda", "Polonia", "atomo", "Francia", "Posavasos", "Belen", "Galleta", "Programa", "Beto", "Guadalupe", "Puerta", "Boton", "Guitarra", "Quimica", "Brasil", "Hoja", "Rectangulo", "Bruselas", "Idea", "Ropa", "Cable", "Juanita", "Silla", "Calculadora", "Juguete", "Sonido", "Carpeta", "Julio",
                           "Spotify", "Cartera", "Suciedad", "Celular", "Loros", "Sustancia", "Cerradura", "Louisiana", "Televidente", "Cesped", "Manantial", "Televisor", "Chile", "Mariano", "Tierra", "Chrome", "Mausoleo", "Tigre", "Circulo", "Mesa", "Tomas", "Ciudad", "Mexico", "Trabajador", "Ciruela", "Molecula", "Trabajo", "Claridad", "Mouse", "Triangulo", "Clavel", "Mueble", "Tulipan", "Competencia", "Nicolas", "Utensilio", "Computadora", "Notas", "Vaso", "Cuerda", "Ventana", "Dinamarca", "Paint", "Vidrio", "Dios", "Pantalla", "Violin", "Diodo", "Paris", "Visita")


def obtener_palabra_al_azar(lista_de_palabras):
    """
    selecciona elemento al azar de una lista o una tupla y regresa una cadena
    """
    palabra_Seleccionada = random.choice(lista_de_palabras)
    return palabra_Seleccionada


def mostrar_tablero(imagenes_ahorcado, palabra_enmascarada, letras_usadas):
    print("".join(palabra_enmascarada))
    print(imagenes_ahorcado)
    print("-".join(letras_usadas))

########################################################################


letras_erroneas = []
letras_usadas = []
palabra_para_usar = obtener_palabra_al_azar(LISTA_PALABRAS_POSIBLES).lower()

palabra_enmascarada = " _" * len(palabra_para_usar)
palabra_enmascarada = list(palabra_enmascarada[1:])
ganador = False

while (len(letras_erroneas) < (len(IMAGENES_AHORCADO) - 1)) and not ganador:
    if len(letras_erroneas) == 0:
        mostrar_tablero(IMAGENES_AHORCADO[0],
                        palabra_enmascarada, letras_usadas)

    letra = input("¿Que letra piensas?: ")

    if letra in letras_usadas:
        print("Esta letra ya fue usada")
    else:

        if letra.lower() in palabra_para_usar:
            indices_de_palabras = []
            for key, letra_palabra_para_usar in enumerate(palabra_para_usar):
                if letra.lower() in letra_palabra_para_usar:
                    indices_de_palabras.append(key)

            for posicion_letra_enmascarada in indices_de_palabras:
                palabra_enmascarada[(
                    posicion_letra_enmascarada * 2)] = letra.lower()
                if ("".join(palabra_enmascarada).replace(' ', "")) == palabra_para_usar:
                    ganador = True
                    break
        else:
            letras_erroneas.append(letra.lower())

        letras_usadas.append(letra)
    mostrar_tablero(IMAGENES_AHORCADO[len(
        letras_erroneas)], palabra_enmascarada, letras_usadas)

print("Tenemos un ganador, con la palabra: {}".format(palabra_para_usar)) if ganador else print(
    "Game OVER, la palabra era: {}".format(palabra_para_usar))
