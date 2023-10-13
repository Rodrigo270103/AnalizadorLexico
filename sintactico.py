import pandas as pd
import main


class node_stack:

  def __init__(self, symbol, lexeme):
    global count
    self.symbol = symbol
    self.lexeme = lexeme
    self.id = count + 1  #identificar tokens
    count += 1


class node_tree:

  def __init__(self, id, symbol, lexeme):
    self.id = id
    self.symbol = symbol
    self.lexeme = lexeme
    self.children = []
    self.father = None


tabla = pd.read_csv("gramatica.csv", index_col=0)
count = 0
stack = []

# init stack
symbol_E = node_stack('K', None)
symbol_dollar = node_stack('$', None)
stack.append(symbol_dollar)
stack.append(symbol_E)

# init tree
root = node_tree(symbol_E.id, symbol_E.symbol, symbol_E.lexeme)

input = main.lexico()


def analyze_step():
  while len(stack) > 0:
    if stack[-1].symbol == input[0]["symbol"]:
      input.pop(0)
      stack.pop()
    else:
      production = tabla.loc[stack[-1].symbol, input[0]["symbol"]]
      print(production)
      if pd.isna(production):
        print("error")
        break

      if production != "e":
        stack.pop()
        for simbolo in reversed(production.split()):
          node_ST = node_stack(simbolo, None)
          stack.append(node_ST)
      else:
        stack.pop()


# Ejecución del análisis hasta que la pila esté vacía o se produzca un error
analyze_step()

if len(stack) == 0 and len(input) == 0:
  print("Análisis sintáctico completado con éxito.")
elif len(stack) == 0:
  print("Error: Entrada adicional no consumida.")
else:
  print("Error: Símbolos no emparejados en la pila.")

# crear los hijo X y T de E
#node_X_tree = node_tree(node_X.id, node_X.symbol, node_X.lexeme)
#node_T_tree = node_tree(node_T.id, node_T.symbol, node_T.lexeme)
#node_father = buscar_node(node_p.id)
#node_father.children.append(node_X_tree)
#node_father.children.append(node_T_tree)
#node_X_tree.father = node_father
#node_T_tree.father = node_father
