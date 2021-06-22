# Sumatoria de cuadrados
# Iteracion
def suma_cuadrados_i(n1, n2):
    suma = 0
    for i in range(n1, n2 + 1):
        suma += i ** 2
    return suma


# Pila
def suma_cuadrados_p(n1, n2):
    if n1 > n2:
        return "Error"
    else:
        return suma_cuadrados_p_aux(n1, n2)


def suma_cuadrados_p_aux(n1, n2):
    if n1 > n2:
        return 0
    else:
        return n1 ** 2 + suma_cuadrados_p_aux(n1 + 1, n2)


# Cola
def suma_cuadrados_c(n1, n2):
    if n1 > n2:
        return "ERROR"
    else:
        return suma_cuadrados_c_aux(n1, n2, 0)


def suma_cuadrados_c_aux(n1, n2, suma):
    if n1 > n2:
        return suma
    else:
        suma += n1 ** 2
        n1 += 1
        return suma_cuadrados_c_aux(n1, n2, suma)


# Ejercicio 4
# Iteracion
def pares_impares(n):
    if not isinstance(n, int):
        return "Error"
    else:
        par = 0
        impar = 0
        while n != 0:
            n, digito = divmod(n, 10)
            if digito % 2 == 0:
                par += 1
            else:
                impar += 1
        return par, impar


# Pila
"""def pares_impares_c(n):
    if not isinstance(n, int):
        return "Error"
    else:
        return pares_impares_c_aux(n, 0, 0)
def pares_impares_c_aux(n, par, impar):
    if n == 0:
        return par, impar
    else:
        n, digito = divmod(n, 10)
        if digito % 2 == 0:
            return (par + 1) + pares_impares_c_aux(n, par, impar)
        else:
            return (impar + 1) + pares_impares_c_aux(n, par, impar)"""


# Cola
def pares_impares_c(n):
    if not isinstance(n, int):
        return "Error"
    else:
        return pares_impares_c_aux(n, 0, 0)


def pares_impares_c_aux(n, p, i):
    if n == 0:
        return p, i
    else:
        n, digito = divmod(n, 10)
        if digito % 2 == 0:
            p += 1
        else:
            i += 1
        return pares_impares_c_aux(n, p, i)


# Ejercicio 5
# Iteracion
def multiplos(n, a, b):
    lista = []
    for i in range(a, b + 1):
        m = n * i
        lista.append(m)
    return lista


# Cola
def multiplos_c(n, a, b):
    return multiplos_c_aux(n, a, b, [])


def multiplos_c_aux(n, a, b, lista):
    if a > b:
        return lista
    else:
        m = a * n
        lista.append(m)
        return multiplos_c_aux(n, a + 1, b, lista)


# Pila
def multiplos_p(n, a, b):
    return multiplos_p_aux(n, a, b)


def multiplos_p_aux(n, a, b):
    if a > b:
        return []
    else:
        m = a * n
        return [m] + multiplos_p_aux(n, a + 1, b)


# Ejercicio 6
# Iteracion
def lista_indices(n, lista):
    contador = 0
    lista_2 = []
    while contador < len(lista):
        i = lista[contador]
        if i == n:
            lista_2.append(contador)
        contador += 1
    return lista_2


# Cola
def lista_indices_c(n, lista):
    return lista_indices_c_aux(n, lista, [], 0)


def lista_indices_c_aux(n, lista, lista2, contador):
    if contador >= len(lista):
        return lista2
    else:
        if lista[contador] == n:
            lista2.append(contador)
        contador += 1
        return lista_indices_c_aux(n, lista, lista2, contador)


# Pila

def lista_indices_p(n, lista):
    return lista_indices_p_aux(n, lista, 0)


def lista_indices_p_aux(n, lista, contador):
    if contador >= len(lista):
        return []
    else:
        i = lista[contador]
        if i == n:
            return [contador] + lista_indices_p_aux(n, lista, contador + 1)
        else:
            return lista_indices_p_aux(n, lista, contador + 1)


# Ejercicio 7
# Iteracion
def tipo_matriz(matriz, n):
    lista_grande = []
    if n == 1:
        for fila, i in enumerate(matriz):
            lista = []
            columna = fila
            for columna_comparar, j in enumerate(i):
                if columna_comparar >= columna:
                    lista.append(j)
                else:
                    lista.append(0)
            lista_grande.append(lista)
    elif n == 2:
        for fila, i in enumerate(matriz):
            lista = []
            columna = fila
            for columna_comparar, j in enumerate(i):
                if columna_comparar <= columna:
                    lista.append(j)
    else:
        for fila, i in enumerate(matriz):
            lista = []
            columna = fila
            for columna_comparar, j in enumerate(i):
                if columna_comparar == columna:
                    lista.append(j)

    return lista_grande


# Cola
def tipo_matriz_c(matriz, n):
    return tipo_matriz_c_aux(matriz, n, [], [], 0, 0)


def tipo_matriz_c_aux(matriz, n, lista_grande, lista, fila, columna):
    if n == 1:
        if columna >= fila:
            lista.append(matriz[fila][columna])
            columna += 1
        else:
            lista.append(0)
            columna += 1
        if len(lista) == len(matriz[fila]):
            columna = 0
            fila += 1
            lista_grande.append(lista)
            lista = []
        if len(lista_grande) == len(matriz):
            return lista_grande
        return tipo_matriz_c_aux(matriz, n, lista_grande, lista, fila, columna)
    elif n == 2:
        if columna <= fila:
            lista.append(matriz[fila][columna])
            columna += 1
        else:
            lista.append(0)
            columna += 1
        if len(lista) == len(matriz[fila]):
            columna = 0
            fila += 1
            lista_grande.append(lista)
            lista = []
        if len(lista_grande) == len(matriz):
            return lista_grande
        return tipo_matriz_c_aux(matriz, n, lista_grande, lista, fila, columna)
    else:
        if columna == fila:
            lista.append(matriz[fila][columna])
            columna += 1
        else:
            lista.append(0)
            columna += 1
        if len(lista) == len(matriz[fila]):
            columna = 0
            fila += 1
            lista_grande.append(lista)
            lista = []
        if len(lista_grande) == len(matriz):
            return lista_grande
        return tipo_matriz_c_aux(matriz, n, lista_grande, lista, fila, columna)


def tipo_matriz_p(matriz, n):
    return tipo_matriz_p_aux(matriz, n, 0, 0)


def tipo_matriz_p_aux(matriz, n, columna, fila):
    if n == 1:
        if fila == len(matriz):
            return []
        else:
            if columna >= len(matriz[fila]):
                columna = 0
                return tipo_matriz_p_aux(matriz, n, columna, fila + 1)
            else:
                if columna >= fila:
                    return [matriz[fila][columna]] + tipo_matriz_p_aux(matriz, n, columna + 1, fila)
                else:
                    return [0] + tipo_matriz_p_aux(matriz, n, columna + 1, fila)
    elif n == 2:
        if fila == len(matriz):
            return []
        else:
            if columna >= len(matriz[fila]):
                columna = 0
                return tipo_matriz_p_aux(matriz, n, columna, fila + 1)
            else:
                if columna <= fila:
                    return [matriz[fila][columna]] + tipo_matriz_p_aux(matriz, n, columna + 1, fila)
                else:
                    return [0] + tipo_matriz_p_aux(matriz, n, columna + 1, fila)
    else:
        if fila == len(matriz):
            return []
        else:
            if columna >= len(matriz[fila]):
                columna = 0
                return tipo_matriz_p_aux(matriz, n, columna, fila + 1)
            else:
                if columna == fila:
                    return [matriz[fila][columna]] + tipo_matriz_p_aux(matriz, n, columna + 1, fila)
                else:
                    return [0] + tipo_matriz_p_aux(matriz, n, columna + 1, fila)


# Ejercicio 8
# Iteracion
def notas(lista):
    nueva_lista = []
    for i in lista:
        elemento = i
        contador = 0
        for j in lista:
            if i == j:
                contador += 1
        tupla = (i, contador)
        if tupla not in nueva_lista:
            nueva_lista.append(tupla)
    return nueva_lista


def notas_c(lista):
    return notas_c_aux(lista, 0, 0, 0, [])


def notas_c_aux(lista, contador, contador2, contador_elementos, nueva_lista):
    if contador2 >= len(lista):
        return nueva_lista
    else:
        elemento = lista[contador2]
        if contador >= len(lista):
            tupla = elemento, contador_elementos
            contador = 0
            contador2 += 1
            contador_elementos = 0
            if tupla not in nueva_lista:
                nueva_lista.append(tupla)
            return notas_c_aux(lista, contador, contador2, contador_elementos, nueva_lista)
        else:
            if elemento == lista[contador]:
                contador_elementos += 1
                contador += 1
                return notas_c_aux(lista, contador, contador2, contador_elementos, nueva_lista)
            else:
                contador += 1
                return notas_c_aux(lista, contador, contador2, contador_elementos, nueva_lista)


# Pila
def notas_p(lista):
    return notas_p_aux(lista, 0, 0, 0)


def notas_p_aux(lista, contador, contador2, contador_elementos):
    if contador2 >= len(lista):
        return []
    else:
        elemento = lista[contador2]
        if contador >= len(lista):
            for i in range(contador_elementos):
                lista.remove(elemento)
            tupla = elemento, contador_elementos
            contador = 0
            contador_elementos = 0
            contador2 = 0
            return [tupla] + notas_p_aux(lista, contador, contador2, contador_elementos)
        else:
            if elemento == lista[contador]:
                contador_elementos += 1
                contador += 1
                return notas_p_aux(lista, contador, contador2, contador_elementos)
            else:
                contador += 1
                return notas_p_aux(lista, contador, contador2, contador_elementos)


# Ejercicio 9
# Iteracion
def extiende(lista):
    contador = 0
    nueva_lista = []
    while contador < len(lista):
        n = lista[contador][1]
        while n > 0:
            nueva_lista.append(lista[contador][0])
            n -= 1
        contador += 1
    return nueva_lista


# Cola
def extiende_c(lista):
    n = lista[0][1]
    return extiende_c_aux(lista, 0, n, [])

def extiende_c_aux(lista, contador, n_comparar, nueva_lista):
    if contador >= len(lista):
        return nueva_lista
    else:
        if n_comparar > 0:
            nueva_lista.append(lista[contador][0])
            n_comparar -= 1
            return extiende_c_aux(lista, contador, n_comparar, nueva_lista)
        else:
            contador += 1
            if contador < len(lista):
                n_comparar = lista[contador][1]
            return extiende_c_aux(lista, contador, n_comparar, nueva_lista)

#Pila
def extiende_p(lista):
    n = lista[0][1]
    return extiende_p_aux(lista, 0, n)

def extiende_p_aux(lista, contador, n):
    if contador >= len(lista):
        return []
    else:
        if n > 0:
            n -= 1
            return [lista[contador][0]] + extiende_p_aux(lista, contador, n)
        else:
            contador += 1
            if contador < len(lista):
                n = lista[contador][1]
            return extiende_p_aux(lista, contador, n)

#Ejercicio 10
#Iteracion

def matriz_unitaria(n):
    contador = 0
    nueva_lista = []
    while contador < n:
        lista = []
        contador2 = 0
        while contador2 < n:
            if contador == contador2:
                lista.append(1)
            else:
                lista.append(0)
            contador2 += 1
        nueva_lista.append(lista)
        contador += 1
    return nueva_lista

#Cola
def matriz_unitaria_c(n):
    return matriz_unitaria_c_aux(n, 0, 0, [], [])
def matriz_unitaria_c_aux(n, contador, contador2, nueva_lista, lista):
    if contador >= n:
        return nueva_lista
    else:
        if contador2 >= n:
            contador += 1
            nueva_lista.append(lista)
            lista = []
            contador2 = 0
            return matriz_unitaria_c_aux(n, contador, contador2, nueva_lista, lista)
        else:
            if contador == contador2:
                lista.append(1)
                contador2 += 1
                return matriz_unitaria_c_aux(n, contador, contador2, nueva_lista, lista)
            else:
                lista.append(0)
                contador2 += 1
                return matriz_unitaria_c_aux(n, contador, contador2, nueva_lista, lista)

#Pila
def matriz_unitaria_p(n):
    return matriz_unitaria_p_aux(n, 0, 0, [])

def matriz_unitaria_p_aux(n, contador, contador2, lista):
    if contador >= n:
        return []
    else:
        if contador2 >= n:
            contador += 1
            contador2 = 0
            return [lista] + matriz_unitaria_p_aux(n, contador, contador2, lista)
        else:
            if contador == contador2:
                if len(lista) >= n:
                    lista = []
                lista.append(1)
                contador2 += 1
                return matriz_unitaria_p_aux(n, contador, contador2, lista)
            else:
                if len(lista) >= n:
                    lista = []
                lista.append(0)
                contador2 += 1
                return matriz_unitaria_p_aux(n, contador, contador2, lista)


#Ejercicio 12
def extrae_diagonal(matriz, n):
    if n >= 0:
        lista = []
        contador = 0
        while n < len(matriz[0]):
            elemento = matriz[contador][n]
            lista.append(elemento)
            contador += 1
            n += 1
        return lista
    else:
        n = abs(n)
        contador = 0
        lista = []
        while n < len(matriz):
            elemento = matriz[n][contador]
            lista.append(elemento)
            n += 1
            contador += 1
        return lista

#Cola
def extrae_diagonal_c(matriz, n):
    return extrae_diagonal_c_aux(matriz, n, 0, [])

def extrae_diagonal_c_aux(matriz, n, contador, lista):
    if n >= 0:
        if n >= len(matriz[0]):
            return lista
        else:
            elemento = matriz[contador][n]
            lista.append(elemento)
            n += 1
            contador += 1
            return extrae_diagonal_c_aux(matriz, n, contador, lista)
    else:
        n = abs(n)
        if n >= len(matriz):
            return lista
        else:
            elemento = matriz[n][contador]
            lista.append(elemento)
            n += 1
            contador += 1
            return extrae_diagonal_c_aux(matriz, n * -1, contador, lista)

#Pila
def extrae_diagonal_p(matriz, n):
    return extrae_diagonal_p_aux(matriz, n, 0)

def extrae_diagonal_p_aux(matriz, n, contador):
    if n >= 0:
        if n >= len(matriz[0]):
            return []
        else:
            elemento = matriz[contador][n]
            n += 1
            contador += 1
            return [elemento] +  extrae_diagonal_p_aux(matriz, n, contador)
    else:
        n = abs(n)
        if n >= len(matriz):
            return []
        else:
            elemento = matriz[n][contador]
            n += 1
            contador += 1
            return [elemento] + extrae_diagonal_p_aux(matriz, n * -1, contador)

#Ejercicio 14
#Iteracion
def compactar(lista):
    contador = 0
    lista_nueva = []
    while contador < len(lista):
        elemento = lista[contador]
        contador2 = contador
        aparicion = 0
        while contador2 < len(lista):
            if elemento == lista[contador2]:
                aparicion += 1
                contador2 += 1
            else:
                break
        tupla = elemento, aparicion
        lista_nueva.append(tupla)
        contador += aparicion
    return lista_nueva

#Pila
def compactar_p(lista):
    return compactar_p_aux(lista, 0)

def compactar_p_aux(lista, contador):
    if contador >= len(lista):
        return []
    else:
        contador2 = contador
        elemento = lista[contador]
        aparicion = compactar_p_aux_tupla(lista, contador, contador2, elemento, 0)
        contador += aparicion[-1]
        tupla = elemento, aparicion[-1]
        return [tupla] + compactar_p_aux(lista, contador)

def compactar_p_aux_tupla(lista, contador, contador2, elemento, aparicion):
    if contador2 >= len(lista):
        return []
    else:
        if elemento == lista[contador2]:
            aparicion += 1
            contador2 += 1
            return [aparicion] + compactar_p_aux_tupla(lista, contador, contador2, elemento, aparicion)
        else:
             return [aparicion]


#Ejercicio 16
"""def lista_principal(lista):
    elemento = lista[0]
    contador = 0
    return lista_principal_aux(lista, elemento, contador, [])

def lista_principal_aux(lista, elemento, contador, lista_prueba):
    if len(lista_prueba) > 0 and contador >= len(lista_prueba):
        contador -= len(lista_prueba) - 1
        elemento = lista[contador]
        return lista_principal_aux(lista,elemento, contador, [])
    if isinstance(elemento, int):
        contador += 1
        if len(lista_prueba) > 0:
            try:
                elemento = lista_prueba[contador]
            except:
                pass
        else:
            try:
                elemento = lista[contador]
            except:
                pass
        return [elemento] + lista_principal_aux(lista, elemento, contador)
    else:
        lista_prueba = elemento
        contador = 0
        elemento = lista_prueba[contador]
        return lista_principal_aux(lista, elemento, contador, lista_prueba)
"""


