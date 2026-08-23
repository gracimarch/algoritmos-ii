def ordenar(elementos: list) -> list:
	"""Ordena una lista usando Merge Sort.

	Al quedar ordenada, el elemento central queda en la posición
	len(elementos) // 2: a su izquierda quedan la mitad de los elementos
	menores que él y a su derecha queda la otra mitad.

	Merge Sort divide la lista en dos mitades, ordena cada una recursivamente
	y luego las fusiona comparando sus primeros elementos. Su complejidad es
	O(n log n), con O(n) de memoria auxiliar.
	"""
	if len(elementos) <= 1:
		return elementos.copy()

	mitad = len(elementos) // 2
	izquierda = ordenar(elementos[:mitad])
	derecha = ordenar(elementos[mitad:])

	resultado: list = []
	i = j = 0
	while i < len(izquierda) and j < len(derecha):
		if izquierda[i] <= derecha[j]:
			resultado.append(izquierda[i])
			i += 1
		else:
			resultado.append(derecha[j])
			j += 1

	resultado.extend(izquierda[i:])
	resultado.extend(derecha[j:])
	return resultado


if __name__ == "__main__":
	lista_ordenada = ordenar([7, 2, 9, 1, 5, 3, 8])
	print(lista_ordenada)
	print("Elemento del medio:", lista_ordenada[len(lista_ordenada) // 2])
