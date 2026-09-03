from linkedlist import LinkedList, add, print_list
from myqueue import Queue, enqueue, dequeue
from mystack import Stack, push, pop

class BinaryTree:
    def __init__(self):
        self.root = None

class BinaryTreeNode:
    def __init__(self):
        self.key = None
        self.value = None
        self.leftNode = None
        self.rightNode = None
        self.parent = None

def search(B: BinaryTree, element) -> int:
    if B.root is None:
        return None
    return _searchR(B.root, element)

def _searchR(current: BinaryTreeNode, element) -> int:
    if current is None:
        return None
    if current.value == element:
        return current.key
    found = _searchR(current.leftNode, element)
    if found is not None:
        return found
    return _searchR(current.rightNode, element)


def insert(B:BinaryTree, element, key:int)-> int:
    newNode = BinaryTreeNode()
    newNode.key = key
    newNode.value = element

    if B.root is None:
        B.root = newNode
        return newNode.key
    else:
        return insertR(newNode, B.root)


def insertR(newNode: BinaryTreeNode, current: BinaryTreeNode)-> int:
    if newNode.key > current.key:
        if current.rightNode == None:
            current.rightNode = newNode
            newNode.parent = current
            return newNode.key
        else:
            return insertR(newNode, current.rightNode)
    else:
        if current.leftNode == None:
            current.leftNode = newNode
            newNode.parent = current
            return newNode.key
        else:
            return insertR(newNode, current.leftNode)


def obtenerNodo(current: BinaryTreeNode, key: int) -> BinaryTreeNode:
    if current.key == key:
        return current
    
    elif key < current.key:
        return obtenerNodo(current.leftNode, key) 
    else: 
        return obtenerNodo(current.rightNode, key) 

    
def delete(B: BinaryTree, element) -> int:
    if B.root is None:
        return None
    
    key = search(B, element)
    
    if key is None:
        return None
    
    node = obtenerNodo(B.root, key)
    
    if B.root.key == key:
        print("DESCABEZANDO EL ÁRBOL")
        if B.root.rightNode and B.root.leftNode:  
            newRoot = min_nodo(B.root.rightNode)
            newRoot.parent.rightNode = None
            newRoot.leftNode = B.root.leftNode
            newRoot.rightNode = B.root.rightNode
            B.root = newRoot
    
    # Hojita
    elif node.leftNode is None and node.rightNode is None:
        if node == B.root:
            B.root = None
        elif node.parent.leftNode == node:
            node.parent.leftNode = None
        else:
            node.parent.rightNode = None
    
    # 1 nodito hijito o nada
    elif node.leftNode is None or node.rightNode is None:
        hijito = node.leftNode if node.leftNode else node.rightNode
        if node == B.root:
            B.root = hijito
            hijito.parent = None
        else:
            hijito.parent = node.parent
            if node.parent.leftNode == node: node.parent.leftNode = hijito
            else: node.parent.rightNode = hijito

    # 2 noditos hijitos
    else:         
        newNode = mayorMenores(node.leftNode)
        node.key, node.value = newNode.key, newNode.value
        # eliminar el nodo predecesor (newNode) del árbol
        if newNode.parent.rightNode == newNode:
            newNode.parent.rightNode = newNode.leftNode
        else:
            newNode.parent.leftNode = newNode.leftNode
        if newNode.leftNode is not None:
            newNode.leftNode.parent = newNode.parent
    
    return key

def mayorMenores(current: BinaryTreeNode)-> BinaryTreeNode:
    if current.rightNode is None:
        return current
    else:
        return mayorMenores(current.rightNode)
    

def deleteKey(B: BinaryTree, key: int) -> int:
    if B.root is None:
        return None
    
    return deleteKeyR(B, B.root, key)

def deleteKeyR(B: BinaryTree, current: BinaryTreeNode, key: int):
    if current == None: 
        return None
    
    if current.key == key:
        
        if current.leftNode == None or current.rightNode == None:

            if current.leftNode != None:
                hijito = current.leftNode
            else: 
                hijito = current.rightNode
            
            if current.parent == None: 
                B.root = hijito

                if hijito != None: 
                    hijito.parent = None
                    
            else: 

                if current.parent.leftNode == current:
                    current.parent.leftNode = hijito

                else: 
                    current.parent.rightNode = hijito

                if hijito is not None:
                   hijito.parent = current.parent

            return key

        else: 
            hijito2 = min_nodo(current.rightNode)
            current.key = hijito2.key
            deleteKeyR(B, hijito2, hijito2.key)
        
        return key

    elif key < current.key:
        return deleteKeyR(B, current.leftNode, key)
    
    else: 
        return deleteKeyR(B, current.rightNode, key)

def min_nodo(node: BinaryTreeNode) -> BinaryTreeNode:
    while node.leftNode != None:
        node = node.leftNode
    return node


def access(B: BinaryTree, key: int):
    if B.root is None:
        return None

    return accessR(B.root, key)

def accessR(current: BinaryTreeNode, key: int):
    if current is None:
        return None
    
    if current.key == key:
        return current.value
    
    if key < current.key:
        return accessR(current.leftNode, key)
    
    else: 
        return accessR(current.rightNode, key)


def update(B: BinaryTree, element, key: int) -> int:
    if B.root is None:
        return None

    return updateR(B.root, element, key)

def updateR(current, element, key: int) -> int:
     
    if current.key == key:
        current.value = element
        return key
    
    elif key < current.key:
        return updateR(current.leftNode, element, key)
    
    else: 
        return updateR(current.rightNode, element, key)


def traverseInOrder(B: BinaryTree) -> LinkedList:
    if B.root is None:
        return None
    
    result_list = LinkedList()
    _traverse_recursive(B.root, result_list)
    return result_list

def _traverse_recursive(node: BinaryTreeNode, L: LinkedList):
    if node is not None:
        _traverse_recursive(node.rightNode, L)
        
        add(L, node.value)
        
        _traverse_recursive(node.leftNode, L)


def traverseInPostOrder(B:BinaryTree)-> LinkedList|None:
    if B.root:
        recorrido = LinkedList()
        listaPost(B.root, recorrido)
        return recorrido
    else:
        return None
    
def listaPost(current:BinaryTreeNode, lista:LinkedList):
    if current:
        add(lista, current.value) 
        listaPost(current.rightNode,lista)
        listaPost(current.leftNode,lista)


def traverseInPreOrder(B:BinaryTree)-> LinkedList|None:
    if B.root:
        recorrido = LinkedList()
        listaPre(B.root, recorrido)
        return recorrido
    else:
        return None
    
def listaPre(current:BinaryTreeNode, lista:LinkedList):
    if current:
        listaPre(current.rightNode,lista)
        listaPre(current.leftNode,lista)
        add(lista, current.value)


def traverseBreadthFirst(B: BinaryTree) -> LinkedList|None:
    if B.root:
        queue = Queue()
        stack = Stack()
        recorrido = LinkedList()
        enqueue(queue, B.root)
        while queue.head is not None:
            current = dequeue(queue)
            push(stack, current.value)
            if current.leftNode:
                enqueue(queue, current.leftNode)
            if current.rightNode:
                enqueue(queue, current.rightNode)
        recorrido = LinkedList()
        while stack.head is not None:
            add(recorrido, pop(stack))
        return recorrido
    else:
        return None

def print_inorder(root):
    if root:
        print_inorder(root.leftNode)
        print(root.value)
        print_inorder(root.rightNode)


def print_tree(tree: BinaryTree):
    print("--- Estructura del Árbol ---")
    if tree.root is None:
        print("El árbol está vacío.")
    else:
        _print_recursive(tree.root, 0)
    print("----------------------------")

def _print_recursive(node: BinaryTreeNode, level: int):
    if node is not None:
        # 1. Procesar primero el lado derecho (se verá arriba)
        _print_recursive(node.rightNode, level + 1)
        
        # 2. Imprimir el nodo actual con sangría según su nivel
        # Multiplicamos el nivel por 8 espacios para dar aire visual
        indent = "        " * level 
        print(f"{indent}--> [{node.key}: {node.value}]")
        
        # 3. Procesar el lado izquierdo (se verá abajo)
        _print_recursive(node.leftNode, level + 1)


if __name__ == '__main__':
    # nodos
    A = BinaryTreeNode(); A.key = 8;  A.value = "A"
    B = BinaryTreeNode(); B.key = 4;  B.value = "B"
    C = BinaryTreeNode(); C.key = 12; C.value = "C"
    D = BinaryTreeNode(); D.key = 2;  D.value = "D"
    E = BinaryTreeNode(); E.key = 6;  E.value = "E"
    F = BinaryTreeNode(); F.key = 10; F.value = "F"
    G = BinaryTreeNode(); G.key = 14; G.value = "G"
    H = BinaryTreeNode(); H.key = 1;  H.value = "H"
    I = BinaryTreeNode(); I.key = 3;  I.value = "I"
    J = BinaryTreeNode(); J.key = 5;  J.value = "J"
    K = BinaryTreeNode(); K.key = 7;  K.value = "K"
    L = BinaryTreeNode(); L.key = 9;  L.value = "L"
    M = BinaryTreeNode(); M.key = 11; M.value = "M"
    N = BinaryTreeNode(); N.key = 13; N.value = "N"
    O = BinaryTreeNode(); O.key = 15; O.value = "O"

    # conexiones

    A.leftNode = B; B.parent = A
    A.rightNode = C; C.parent = A

    B.leftNode = D; D.parent = B
    B.rightNode = E; E.parent = B

    C.leftNode = F; F.parent = C
    C.rightNode = G; G.parent = C

    D.leftNode = H; H.parent = D
    D.rightNode = I; I.parent = D

    E.leftNode = J; J.parent = E
    E.rightNode = K; K.parent = E

    F.leftNode = L; L.parent = F
    F.rightNode = M; M.parent = F

    G.leftNode = N; N.parent = G
    G.rightNode = O; O.parent = G

    # árbol
    tree = BinaryTree()
    tree.root = A

    print_tree(tree)

    print("Recorrido InOrder:")
    print_list(traverseInOrder(tree))

    print("Recorrido PreOrder:")
    print_list(traverseInPreOrder(tree))

    print("Recorrido PostOrder:")
    print_list(traverseInPostOrder(tree))

    print("Recorrido Breadth First:")
    print_list(traverseBreadthFirst(tree))

    # deleteKey(tree, 15)
    # print("Borrar una hoja")
    # print_tree(tree)

    # deleteKey(tree, 9)
    # print("Borramos una hoja")
    # print_tree(tree)
        
    # deleteKey(tree, 10)
    # print("Borramos un padre con un hijo derecho")
    # print_tree(tree)

    # deleteKey(tree, 6)
    # print("Borramos un padre con dos hijos")
    # print_tree(tree)

    # print("Borramos un padre con un hijo zurdo")
    # deleteKey(tree, 14)
    # print_tree(tree)

    # deleteKey(tree, 8)
    # print("Borramos la raíz")
    # print_tree(tree)

    