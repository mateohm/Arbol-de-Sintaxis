import sys
from collections import defaultdict

class Node:
    def __init__(self, symbol):
        self.symbol = symbol
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def pretty(self, level=0):
        print("  " * level + self.symbol)
        for child in self.children:
            child.pretty(level + 1)


def leer_gramatica(nombre_archivo):
    reglas = defaultdict(list)
    with open(nombre_archivo, "r") as f:
        for linea in f:
            if "->" in linea:
                izq, der = linea.strip().split("->")
                izq = izq.strip()
                producciones = [p.strip().split() for p in der.split("|")]
                reglas[izq].extend(producciones)
    return reglas

def eliminar_recursion_izquierda(reglas):
    nuevas_reglas = defaultdict(list)
    for nt in list(reglas.keys()):
        alpha = []
        beta = []
        for prod in reglas[nt]:
            if prod[0] == nt:  
                alpha.append(prod[1:])
            else:
                beta.append(prod)
        if alpha:
            ntp = nt + "'"
            for b in beta:
                nuevas_reglas[nt].append(b + [ntp])
            for a in alpha:
                nuevas_reglas[ntp].append(a + [ntp])
            nuevas_reglas[ntp].append(["ε"])
        else:
            nuevas_reglas[nt].extend(reglas[nt])
    return nuevas_reglas

def compute_first(reglas):
    first = defaultdict(set)

    def first_of(symbol):
        if not symbol in reglas:  # terminal
            return {symbol}
        for prod in reglas[symbol]:
            for sym in prod:
                f = first_of(sym)
                first[symbol] |= (f - {"ε"})
                if "ε" not in f:
                    break
            else:
                first[symbol].add("ε")
        return first[symbol]

    for nt in reglas:
        first_of(nt)
    return first

def compute_follow(reglas, first, start):
    follow = defaultdict(set)
    follow[start].add("$")

    changed = True
    while changed:
        changed = False
        for nt in reglas:
            for prod in reglas[nt]:
                for i, sym in enumerate(prod):
                    if sym in reglas:  # no terminal
                        trailer = set()
                        for s in prod[i+1:]:
                            f = first[s] if s in reglas else {s}
                            follow[sym] |= (f - {"ε"})
                            if "ε" in f:
                                continue
                            else:
                                break
                        else:
                            if follow[nt] - follow[sym]:
                                follow[sym] |= follow[nt]
                                changed = True
    return follow

def construir_tabla(reglas, first, follow):
    tabla = defaultdict(dict)
    for nt in reglas:
        for prod in reglas[nt]:
            f = set()
            for sym in prod:
                f |= (first[sym] if sym in reglas else {sym})
                if "ε" not in f:
                    break
            else:
                f.add("ε")

            for t in (f - {"ε"}):
                tabla[nt][t] = prod
            if "ε" in f:
                for t in follow[nt]:
                    tabla[nt][t] = prod
    return tabla

def clasificar_token(token):
    if token.isdigit():  
        return "num"
    return token

def parse(tokens, start, tabla):
    stack = [start]
    root = Node(start)
    node_stack = [root]

    i = 0
    while stack:
        top = stack.pop()
        current_node = node_stack.pop()

        if top not in tabla:  # terminal
            if top == "ε":
                current_node.add_child(Node("ε"))
            elif i < len(tokens) and tokens[i] == top:
                current_node.add_child(Node(tokens[i]))
                i += 1
            else:
                raise Exception(f"Error: se esperaba {top}, se encontró {tokens[i] if i < len(tokens) else 'EOF'}")
        else:  # no terminal
            lookahead = tokens[i] if i < len(tokens) else "$"
            if lookahead in tabla[top]:
                prod = tabla[top][lookahead]
                for sym in reversed(prod):
                    stack.append(sym)
                    child = Node(sym)
                    current_node.children.insert(0, child)
                    node_stack.append(child)
            else:
                raise Exception(f"No regla para {top} con lookahead {lookahead}")
    return root

if __name__ == "__main__":
    reglas = leer_gramatica("gra.txt")
    start = list(reglas.keys())[0]

    reglas = eliminar_recursion_izquierda(reglas)
    first = compute_first(reglas)
    follow = compute_follow(reglas, first, start)
    tabla = construir_tabla(reglas, first, follow)

    cadena = input("Ingrese la cadena: ")
    tokens = [clasificar_token(tok) for tok in cadena.split()] + ["$"]

    try:
        arbol = parse(tokens, start, tabla)
        print("Cadena aceptada \nÁrbol de sintaxis:")
        arbol.pretty()
    except Exception as e:
        print("Cadena rechazada:", e)
