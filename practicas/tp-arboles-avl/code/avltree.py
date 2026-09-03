class AVLTree:
    def __init__(self):
        self.root = None

class AVLNode:
    def __init__(self):
        self.parent = None
        self.leftNode = None
        self.rightNode = None
        self.key = None
        self.value = None
        self.bf = None


def search(B: AVLTree, element) -> int:
    if B.root is None:
        return None
    return searchR(B.root, element)

def searchR(current: AVLNode, element) -> int:
    if current is None:
        return None
    if current.value == element:
        return current.key
    found = searchR(current.leftNode, element)
    if found is not None:
        return found
    return searchR(current.rightNode, element)


def rotateLeft(Tree, avlnode):
    # la nueva raíz del subárbol será el hijo derecho
    new_root = avlnode.rightNode
    avlnode.rightNode = new_root.leftNode
    
    if new_root.leftNode is not None:
        new_root.leftNode.parent = avlnode
        
    new_root.parent = avlnode.parent
    
    # si el nodo a rotar era la raíz del árbol
    if avlnode.parent is None:
        Tree.root = new_root
    elif avlnode == avlnode.parent.leftNode:
        avlnode.parent.leftNode = new_root
    else:
        avlnode.parent.rightNode = new_root
        
    new_root.leftNode = avlnode
    avlnode.parent = new_root
    
    return new_root

def rotateRight(Tree, avlnode):
    # la nueva raíz del subárbol será el hijo izquierdo
    new_root = avlnode.leftNode
    avlnode.leftNode = new_root.rightNode
    
    if new_root.rightNode is not None:
        new_root.rightNode.parent = avlnode
        
    new_root.parent = avlnode.parent
    
    # si el nodo a rotar era la raíz del árbol
    if avlnode.parent is None:
        Tree.root = new_root
    elif avlnode == avlnode.parent.rightNode:
        avlnode.parent.rightNode = new_root
    else:
        avlnode.parent.leftNode = new_root
        
    new_root.rightNode = avlnode
    avlnode.parent = new_root
    
    return new_root


def calculateBalance(Tree):
    if Tree.root is not None:
        calculateHeight(Tree.root)
        
    return Tree

def calculateHeight(node):
    if node is None:
        return 0
    
    hl = calculateHeight(node.leftNode)
    hr = calculateHeight(node.rightNode)
    
    node.bf = hl - hr
    
    return 1 + max(hl, hr)


def reBalance(Tree):
    calculateBalance(Tree)
    
    if Tree.root is not None:
        rebalanceNodeR(Tree, Tree.root)
        
    return Tree

def rebalanceNodeR(Tree, node):
    if node is None:
        return
        
    rebalanceNodeR(Tree, node.leftNode)
    rebalanceNodeR(Tree, node.rightNode)
    
    if node.bf > 1: 
        # caso izquierda-derecha: rotación doble
        if node.leftNode and node.leftNode.bf < 0:
            rotateLeft(Tree, node.leftNode)
        # caso izquierda-izquierda
        new_root = rotateRight(Tree, node)
        # solo recalculamos el subárbol rotado, el resto no cambió
        calculateHeight(new_root)
        
    elif node.bf < -1: 
        # caso derecha-izquierda: rotación doble
        if node.rightNode and node.rightNode.bf > 0:
            rotateRight(Tree, node.rightNode)
        # caso derecha-derecha
        new_root = rotateLeft(Tree, node)

        calculateHeight(new_root)


def insert(B: AVLTree, element, key: int) -> int:
    newNode = AVLNode()
    newNode.key = key
    newNode.value = element

    if B.root is None:
        B.root = newNode
        return newNode.key
    else:
        inserted_key = insertR(B, newNode, B.root)
        
        reBalance(B)
        return inserted_key

def insertR(B: AVLTree, newNode: AVLNode, current: AVLNode) -> int:
    if newNode.key < current.key:
        if current.leftNode is None:
            current.leftNode = newNode
            newNode.parent = current
            return newNode.key
        else:
            return insertR(B, newNode, current.leftNode)
            
    elif newNode.key > current.key:
        if current.rightNode is None:
            current.rightNode = newNode
            newNode.parent = current
            return newNode.key
        else:
            return insertR(B, newNode, current.rightNode)
            
    else:
        current.value = newNode.value
        return current.key


def delete(B: AVLTree, key: int) -> int:
    if B.root is None:
        return None
    
    deleted_key = deleteR(B, B.root, key)
    
    if deleted_key is not None:
        reBalance(B)
        
    return deleted_key

def deleteR(B: AVLTree, current: AVLNode, key: int):
    if current is None: 
        return None
    
    if current.key == key:
        # nodo hoja o con un solo hijo
        if current.leftNode is None or current.rightNode is None:
            if current.leftNode is not None:
                hijito = current.leftNode
            else: 
                hijito = current.rightNode
            
            # nodo a borrar es la raíz
            if current.parent is None: 
                B.root = hijito
                if hijito is not None: 
                    hijito.parent = None
            else: 
                if current.parent.leftNode == current:
                    current.parent.leftNode = hijito
                else: 
                    current.parent.rightNode = hijito
                    
                if hijito is not None:
                    hijito.parent = current.parent

            return key

        # nodo con dos hijos
        else:
            hijito2 = min_nodo(current.rightNode)
            
            current.key = hijito2.key
            current.value = hijito2.value
            
            deleteR(B, current.rightNode, hijito2.key)
        
        return key

    elif key < current.key:
        return deleteR(B, current.leftNode, key)
    else: 
        return deleteR(B, current.rightNode, key)

def min_nodo(node: AVLNode) -> AVLNode:
    while node.leftNode is not None:
        node = node.leftNode
    return node


"""
Ejercicio 7: Une dos árboles AVL (A y B) usando un nodo x como puente.
Condición: Todo A < x < Todo B.
Complejidad: O(log m + log n)
"""

def height(node: AVLNode) -> int:
    if node is None:
        return 0
    
    if node.bf is not None and node.bf >= 0:
        return 1 + height(node.leftNode)
    else:
        return 1 + height(node.rightNode)

def unir_avl(treeA: AVLTree, treeB: AVLTree, x_key: int, x_value) -> AVLTree:
    hA = height(treeA.root)
    hB = height(treeB.root)
    
    x_node = AVLNode()
    x_node.key = x_key
    x_node.value = x_value
    
    new_tree = AVLTree()
    
    if abs(hA - hB) <= 1:
        x_node.leftNode = treeA.root
        if treeA.root: 
            treeA.root.parent = x_node
            
        x_node.rightNode = treeB.root
        if treeB.root: 
            treeB.root.parent = x_node
            
        new_tree.root = x_node
        
    elif hA > hB + 1:
        current = treeA.root
        current_h = hA
        
        # bajamos por la derecha de A hasta que la altura sea compatible con B
        while current is not None and current_h > hB + 1:
            # si el bf > 0 (izq más alta), la altura de la derecha es h-2. Sino, h-1.
            if current.bf is not None and current.bf > 0:
                current_h -= 2
            else:
                current_h -= 1
            current = current.rightNode
            
        # current es el nodo de enganche (c), p es su padre
        p = current.parent
        
        # enganchamos x_node
        x_node.leftNode = current
        if current: current.parent = x_node
        
        x_node.rightNode = treeB.root
        if treeB.root: treeB.root.parent = x_node
        
        x_node.parent = p
        if p is not None:
            p.rightNode = x_node
            
        new_tree.root = treeA.root
        
    else:
        current = treeB.root
        current_h = hB
        
        # bajamos por la izquierda de B
        while current is not None and current_h > hA + 1:
            if current.bf is not None and current.bf < 0:
                current_h -= 2
            else:
                current_h -= 1
            current = current.leftNode
            
        p = current.parent
        
        x_node.rightNode = current
        if current: current.parent = x_node
        
        x_node.leftNode = treeA.root
        if treeA.root: treeA.root.parent = x_node
        
        x_node.parent = p
        if p is not None:
            p.leftNode = x_node
            
        new_tree.root = treeB.root

    reBalance(new_tree)
    
    return new_tree


def print_tree(B: AVLTree):
    if getattr(B, 'root', None) is None:
        print("El árbol está vacío.")
    else:
        print("--- Estructura del Árbol AVL ---")
        _print_tree_R(B.root, 0)
        print("--------------------------------")

def _print_tree_R(current: AVLNode, level: int):
    if current is not None:
        _print_tree_R(current.rightNode, level + 1)
        
        espaciado = "              " * level
        # Solo imprimimos la clave y el Factor de Balanceo (bf)
        print(f"{espaciado}-> {current.key} (bf: {current.bf})")
        
        _print_tree_R(current.leftNode, level + 1)


if __name__ == '__main__':
    print("=== PRUEBA 1: INSERCIONES Y ROTACIONES ===")
    tree1 = AVLTree()
    
    # Insertamos de forma secuencial para forzar rotaciones
    insert(tree1, "A", 10)
    insert(tree1, "B", 20)
    insert(tree1, "C", 30) # Rotación Izquierda (RR)
    insert(tree1, "D", 40)
    insert(tree1, "E", 50) # Rotación Izquierda
    insert(tree1, "F", 25) # Rotación Doble (Derecha-Izquierda)

    calculateBalance(tree1) # Aseguramos calcular el balance final
    print_tree(tree1)

    # 2. PRUEBA DE ELIMINACIÓN
    print("\n=== PRUEBA 2: ELIMINACIÓN ===")
    print("Eliminando las keys 40 y 50...")

    delete(tree1, 40)
    delete(tree1, 50)
    
    calculateBalance(tree1)
    print_tree(tree1)

    # 3. PRUEBA CON TU CONJUNTO DE DATOS
    print("\n=== PRUEBA 3: CONJUNTO DE DATOS COMPLETO ===")
    tree2 = AVLTree()
    
    insert(tree2, "A", 8)
    insert(tree2, "B", 4)
    insert(tree2, "C", 12)
    insert(tree2, "D", 2)
    insert(tree2, "E", 6)
    insert(tree2, "F", 10)
    insert(tree2, "G", 14)
    insert(tree2, "H", 1)
    insert(tree2, "I", 3)
    insert(tree2, "J", 5)
    insert(tree2, "K", 7)
    insert(tree2, "L", 9)
    insert(tree2, "M", 11)
    insert(tree2, "N", 13)
    insert(tree2, "O", 15)

    calculateBalance(tree2)
    print_tree(tree2)

    # 4. PRUEBA EJERCICIO 7: UNIÓN DE DOS AVL
    print("\n=== PRUEBA 4: UNIÓN DE DOS AVL (Ejercicio 7) ===")

    # A tiene keys 1..5, B tiene keys 10..14, x = 7
    # Condición: todo a ∈ A < 7 < todo b ∈ B ✓
    treeA = AVLTree()
    for k in [3, 1, 5, 2, 4]:
        insert(treeA, str(k), k)

    treeB = AVLTree()
    for k in [12, 10, 14, 11, 13]:
        insert(treeB, str(k), k)

    x_key = 7

    print("Árbol A (keys 1-5):")
    print_tree(treeA)
    print(f"Árbol B (keys 10-14):")
    print_tree(treeB)
    print(f"Key x = {x_key}  (condicion: max(A) < x < min(B) => 5 < 7 < 10)")

    merged = unir_avl(treeA, treeB, x_key, str(x_key))

    print("\nÁrbol resultado (A + x + B):")
    print_tree(merged)

    # Verificar propiedad AVL: todos los bf deben ser -1, 0 o 1
    def _checkAVL(node):
        if node is None:
            return True
        if node.bf not in (-1, 0, 1):
            print(f"  [X] Nodo {node.key} tiene bf={node.bf} (invalido)")
            return False
        return _checkAVL(node.leftNode) and _checkAVL(node.rightNode)

    calculateBalance(merged)
    es_valido = _checkAVL(merged.root)
    print(f"Propiedad AVL cumplida? {'[OK]' if es_valido else '[FALLO]'}")

    # Verificar que todos los nodos estan presentes
    keys_esperadas = list(range(1, 6)) + [x_key] + list(range(10, 15))
    faltantes = [k for k in keys_esperadas if search(merged, str(k)) is None]
    print(f"Todos los keys presentes? {'[OK]' if not faltantes else f'[FALLO] Faltan: {faltantes}'}")

    # Verificar orden BST: in-order debe dar los keys en orden creciente
    keys_inorder = []
    def _inorder(node):
        if node is None:
            return
        _inorder(node.leftNode)
        keys_inorder.append(node.key)
        _inorder(node.rightNode)
    _inorder(merged.root)
    en_orden = keys_inorder == sorted(keys_inorder)
    print(f"Orden BST correcto?     {'[OK]' if en_orden else '[FALLO]'}")

    # ----------------------------------------------------------------
    # PRUEBA 5: A mucho mas alto que B
    # El algoritmo debe bajar por la derecha de A para encontrar el
    # punto de enganche, ya que B es bastante mas chico.
    # A: keys 1-15 (altura 4), B: keys 100-102 (altura 2), x = 50
    # ----------------------------------------------------------------
    print("\n=== PRUEBA 5: A >> B (A alto 4, B bajo 2) ===")

    treeA2 = AVLTree()
    for k in [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]:
        insert(treeA2, str(k), k)

    treeB2 = AVLTree()
    for k in [101, 100, 102]:   # B de altura 2
        insert(treeB2, str(k), k)

    x_key2 = 50  # 15 < 50 < 100

    hA2 = height(treeA2.root)
    hB2 = height(treeB2.root)
    print(f"Altura de A = {hA2}, Altura de B = {hB2}  =>  el algoritmo baja por la derecha de A")
    print("Arbol A (keys 1-15):")
    print_tree(treeA2)
    print("Arbol B (keys 100-102):")
    print_tree(treeB2)

    merged2 = unir_avl(treeA2, treeB2, x_key2, str(x_key2))

    print(f"\nArbol resultado (A + {x_key2} + B):")
    print_tree(merged2)

    keys_inorder2 = []
    def _inorder2(node):
        if node is None: return
        _inorder2(node.leftNode)
        keys_inorder2.append(node.key)
        _inorder2(node.rightNode)
    _inorder2(merged2.root)

    calculateBalance(merged2)
    print(f"Propiedad AVL cumplida? {'[OK]' if _checkAVL(merged2.root) else '[FALLO]'}")
    print(f"Todos los keys presentes? {'[OK]' if len(keys_inorder2) == 19 else '[FALLO]'}")
    print(f"Orden BST correcto?     {'[OK]' if keys_inorder2 == sorted(keys_inorder2) else '[FALLO]'}")

    # ----------------------------------------------------------------
    # PRUEBA 6: B mucho mas alto que A
    # El algoritmo debe bajar por la izquierda de B.
    # A: keys 1-3 (altura 2), B: keys 101-115 (altura 4), x = 50
    # ----------------------------------------------------------------
    print("\n=== PRUEBA 6: B >> A (B alto 4, A bajo 2) ===")

    treeA3 = AVLTree()
    for k in [2, 1, 3]:   # A de altura 2
        insert(treeA3, str(k), k)

    treeB3 = AVLTree()
    for k in [108, 104, 112, 102, 106, 110, 114, 101, 103, 105, 107, 109, 111, 113, 115]:
        insert(treeB3, str(k), k)

    x_key3 = 50  # 3 < 50 < 101

    hA3 = height(treeA3.root)
    hB3 = height(treeB3.root)
    print(f"Altura de A = {hA3}, Altura de B = {hB3}  =>  el algoritmo baja por la izquierda de B")
    print("Arbol A (keys 1-3):")
    print_tree(treeA3)
    print("Arbol B (keys 101-115):")
    print_tree(treeB3)

    merged3 = unir_avl(treeA3, treeB3, x_key3, str(x_key3))

    print(f"\nArbol resultado (A + {x_key3} + B):")
    print_tree(merged3)

    keys_inorder3 = []
    def _inorder3(node):
        if node is None: return
        _inorder3(node.leftNode)
        keys_inorder3.append(node.key)
        _inorder3(node.rightNode)
    _inorder3(merged3.root)

    calculateBalance(merged3)
    print(f"Propiedad AVL cumplida? {'[OK]' if _checkAVL(merged3.root) else '[FALLO]'}")
    print(f"Todos los keys presentes? {'[OK]' if len(keys_inorder3) == 19 else '[FALLO]'}")
    print(f"Orden BST correcto?     {'[OK]' if keys_inorder3 == sorted(keys_inorder3) else '[FALLO]'}")