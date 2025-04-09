# Paleta de colores para imprimir texto en consola con formato
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
RESET = "\033[0m"

import re

# ------------------------ FUNCIONES PRINCIPALES ------------------------

def descifrar(texto, desplazamiento):
    """
    Descifra un texto cifrado por sustitución tipo César (rotación).
    Aplica un desplazamiento circular a las letras, respetando mayúsculas y minúsculas.
    """
    resultado = ""
    for letra in texto:
        if letra.isalpha():  # Solo se descifran letras
            base = ord('A') if letra.isupper() else ord('a')
            nueva_letra = chr((ord(letra) - base + desplazamiento) % 26 + base)
            resultado += nueva_letra
        else:
            resultado += letra  # Mantiene caracteres especiales y espacios
    return resultado

def evaluar(descifrado, intento, umbral):
    """
    Evalúa si el texto descifrado es legible, usando patrones entre vocales y consonantes.
    Devuelve True si es legible, False si no lo es.
    """
    evaluacion = ""
    vocales = ["a", "e", "i", "o", "u"]
    consonantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ñ",
                   "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

    # Codifica el texto usando "1" para vocales, "2" para consonantes, "3" para otros
    for letra in descifrado.lower():
        if letra in vocales:
            evaluacion += "1"
        elif letra in consonantes:
            evaluacion += "2"
        elif not letra.isalpha():  # detecta símbolos como '3'
            evaluacion += "3"


    # Busca patrones comunes en palabras naturales (como 12, 21, 121...)
    patrones_validos = re.findall(r'(12|21|121|212)', evaluacion)
    cantidad_patrones = len(patrones_validos)

    # Calcula el total de combinaciones posibles
    total_posibles = max(len(evaluacion) - 1, 1)

    # Porcentaje de patrones válidos encontrados
    porcentaje = cantidad_patrones / total_posibles

    # Si es suficientemente alto, se considera legible
    if porcentaje >= umbral:
        print(AMARILLO + "\n\n[+] El texto descifrado es: " + RESET + VERDE + descifrado + RESET)
        print(AMARILLO + "[+] Se consiguió a los: " + RESET + VERDE + str(intento) + RESET + AMARILLO + " intentos.\n\n" + RESET)
        return True
    else:
        return False

def Cripto(entrada, umbral):
    for intento in range(1, 27):  # De 1 a 26
        resultado = descifrar(entrada, intento)
        if evaluar(resultado, intento, umbral):
            return
    print(ROJO + "[!] No se encontró una coincidencia probable tras 26 intentos." + RESET)

# ------------------------ INTERFAZ PRINCIPAL ------------------------

def main():
    # Título artístico
    print(VERDE + r"""
            _____                  _        _           _    _  _   
           / ____|                | |      | |         | |  | || |  
          | |     _ __ _   _ _ __ | |_ ___ | |     __ _| |__| || |_ 
          | |    | '__| | | | '_ \| __/ _ \| |    / _` | '_ \__   _|
          | |____| |  | |_| | |_) | || (_) | |___| (_| | |_) | | |  
           \_____|_|   \__, | .__/ \__\___/|______\__,_|_.__/  |_|  
                        __/ | |                                     
                       |___/|_|                                   
    """ + RESET)

    while True:
        print(AMARILLO + "Elige una opción de acuerdo a lo que quieras hacer:" + RESET)
        print(AMARILLO + "[+] " + RESET + "1. Descifrar clave de cifrado por sustitución (rotación)")

        menu = input(AMARILLO + "Ingresa la opción: " + RESET)
        if menu == "1":
            texto = input(AMARILLO + "Ingresa el texto cifrado: " + RESET)
            while True:
                try:
                    umbral = float(input(AMARILLO + "Nivel de exactitud (recomendado 0.45): " + RESET))
                    if 0 <= umbral <= 1:
                       break
                    else:
                       print(ROJO + "[!] Ingresa un valor entre 0.0 y 1.0" + RESET)
                except ValueError:
                   print(ROJO + "[!] Valor inválido, escribe un número como 0.45" + RESET)
            Cripto(texto, umbral)
            break
                           
        elif menu == "2":
            print(ROJO + "[!] Función aún no implementada" + RESET)
            break
        else:
            print("\n" + ROJO + "[!] Opción no válida. Intenta nuevamente." + RESET + "\n")

# Ejecutar el programa
if __name__ == "__main__":
    main()
