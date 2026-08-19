def contiene_suma(A:list, n:int) -> bool:
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] + A[j] == n:
                return True
    return False

def contiene_suma2(A: list, n: int) -> bool:
    vistos = set()

    for x in A:
        complemento = n - x

        if complemento in vistos:
            return True

        vistos.add(x)

    return False

if __name__ == "__main__":
    # prueba con algoritmo 1
    lista1 = [1, 2, 3, 4, 5]
    print(lista1)
    print(contiene_suma(lista1, 9))  # True
    print(contiene_suma(lista1, 10)) # False
    
    # prueba con algoritmo 2
    print(contiene_suma2(lista1, 9))  # True
    print(contiene_suma2(lista1, 10)) # False