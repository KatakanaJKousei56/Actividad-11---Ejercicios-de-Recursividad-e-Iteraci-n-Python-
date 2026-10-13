# ----------------------------------------------------
# Actividad 11 - Ejercicios de Recursividad e Iteración
# Nombre: Josué Jarib Moreno Chandomí
# Asignatura: Estructura de Datos (3er Semestre - LSC)
# ----------------------------------------------------

# Solución Recursiva
def suma_recursiva(n):
    if n <= 9:
        return n  # Caso base
    else:
        return suma_recursiva(n // 10) + (n % 10)  # Llamada recursiva


# Solución Iterativa
def suma_iterativa(n):
    suma = 0
    while n > 9:
        suma += n % 10
        n //= 10
    return suma + n


def main():
    print("=== ACTIVIDAD 11: SUMA DE DIGITOS (RECURSIVIDAD E ITERACION) ===")
    cantidad_numeros = int(input("Cuantos numeros desea ingresar?: "))

    if cantidad_numeros <= 0:
        print("Cantidad no valida.")
        return

    for i in range(cantidad_numeros):
        print("\n----------------------------------------")
        numero = int(input(f"Ingrese el numero [{i + 1} de {cantidad_numeros}]: "))

        if numero < 0:
            numero = abs(numero)  # Convertimos a positivo

        res_recursivo = suma_recursiva(numero)
        res_iterativo = suma_iterativa(numero)

        print(f"-> Resultado (Recursivo): {res_recursivo}")
        print(f"-> Resultado (Iterativo): {res_iterativo}")

    print("\n¡Proceso completado con exito!")


if __name__ == "__main__":
    main()
