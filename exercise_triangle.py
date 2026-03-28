def triangle():
    """
    Ejercicio 8 - Validar Triángulo

    Leer tres números que representan los lados de un triángulo mediante input().
    Verificar si pueden formar un triángulo válido e imprimir el resultado.
    Un triángulo es válido si la suma de dos lados cualesquiera es estrictamente mayor
    que el tercer lado (desigualdad triangular). Si la suma es igual, forman una línea
    recta, no un triángulo.

    Ejemplo:
        Para las entradas "3", "4" y "5", la salida esperada es:
        Los lados forman un triangulo valido

        Para las entradas "1", "2" y "5", la salida esperada es:
        Los lados no forman un triangulo valido
    """
    pass
    numero1 = int(input())
    numero2 = int(input())
    numero3 = int(input())
    lado1 = numero1 + numero2
    lado2 = numero2 + numero3
    lado3 = numero3 + numero1
    if lado1 > numero3 and lado2 > numero1 and lado3 > numero2:
        print("Los lados forman un triangulo valido")
    else:
        print("Los lados no forman un triangulo valido")

