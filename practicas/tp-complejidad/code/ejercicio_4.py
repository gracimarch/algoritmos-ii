def reordenar(A):
    if not A:
        return []
        
    n = len(A)
    medio = (n - 1) // 2
    pivote = A[medio]

    A_sin_pivote = A[:medio] + A[medio+1:]

    menores = [x for x in A_sin_pivote if x < pivote]
    otros = [x for x in A_sin_pivote if x >= pivote]

    mitad = len(menores) // 2

    menores_izquierda = menores[:mitad]
    menores_derecha = menores[mitad:]

    cantidad_izquierda = medio
    faltan = cantidad_izquierda - len(menores_izquierda)

    izquierda = menores_izquierda + otros[:faltan]
    derecha = menores_derecha + otros[faltan:]

    return izquierda + [pivote] + derecha

if __name__ == "__main__":
    A = [10, 1, 7, 6, 5, 8, 9, 4, 3, 2]
    
    print("Lista original:  ", A)
    print("Lista reordenada:", reordenar(A))