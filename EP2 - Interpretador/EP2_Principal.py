'''Desafio - Construir um Shell Mode do Python, utilizando um ADT de uma pilha e notação polonesa'''

# As expressões podem conter:
# a)Constantes inteiras (ex: 132, -45, 123456789, etc.)
# b)Variáveis contendo apenas letras (ex: k, SoMa, contador, QuantaDor, etc.)
# c)Operadores binários e parêntesis: +, -, *, /, **
# d)Operadores unários: + e –
# e)Parêntesis: ()
# f)Atribuição: =
# Subistituir "-" por "_" e "+" por "#" quando forem unários

class Empty (Exception):
  pass

class _Node:
  '''classe _Node'''
  __slots__ = '_info', '_prox'

  def __init__(self, info, prox):
    # inicia os campos
    self._info = info
    self._prox = prox

class Pilha:
  ''' implementa uma pilha usando uma Lista Ligada simples. '''
  __slots__ = '_topo', '_tamanho'

  def __init__(self):
    ''' cria uma pilha vazia.'''
    self._topo = None  # vazia
    self._tamanho = 0  # tamanho da pilha

  def __len__(self):
    return self._tamanho

  def is_empty(self):
    ''' retorna True se pilha vazia'''
    return self._tamanho == 0

  def push(self, e):
    ''' adiciona elemento ao topo da pilha.'''
    novo = _Node(e, self._topo)
    self._topo = novo
    self._tamanho += 1

  def top(self):
    ''' retorna sem remover o topo da pilha.
    sinaliza exceção se pilha vazia.'''
    if self.is_empty():
        return None
    return self._topo._info  # topo da pilha

  def pop(self):
    ''' remove e retorna o topo da pilha.
    sinaliza exceção se pilha vazia.'''
    if self.is_empty():
        raise Empty("Pilha vazia")
    val_topo = self._topo._info
    self._topo = self._topo._prox  # pula o primeiro elemento
    self._tamanho -= 1
    return val_topo

  def Imprime(self):
    p = self._topo
    while p is not None:
        print(p._info)
        p = p._prox

def main():
  '''Função principal'''
  while True:
    # Colocar o prompt
    # Solicita uma nova expressão do tipo:
    expressao = str(input(">>> "))
    if expressao == "0": return

    # Cria uma nova param, separando operadores de operandos
    novaExpressao = NovaExpressao(expressao)
    # Transforma em uma lista
    novaExpressao = novaExpressao.split()

    # Verifica a lista, para ver se a expressao esta escrita corretamente
    # Verifica se os parentesis estão em pares e se os operadores estão entre numeros
    # novaExpressao = Verificacao(novaExpressao)
    # if novaExpressao == None:
    #   continue

    # Traduzir a notação para pós-fixas
    expressaoPosFixa = TraduzPosFixa(novaExpressao)
    if expressaoPosFixa == False:
      print ("Erro na tradução da expressão para a Pós Fixa")
    print(expressaoPosFixa)

    # Cria um dicionario para armazenar variaveis
    variaveis = {}

    # Calcular o valor da expressão usando a notação pós-fixas
    # Se o final for "=" atribuição, armazenar o valor. Caso contrario, print
    resultadoFinal, variaveis = CalcPosFixa(expressaoPosFixa, variaveis)
    print (resultadoFinal)
    print (variaveis)

# def Verificacao(param):
#   try:
#     # Cria uma pilha para verificar os parentesis
#     pilhaVerificacao = Pilha()
#     for i in range (len(param)):
#       if param[i] == "(":
#         pilhaVerificacao.push(param[i])
#         continue
#       if param[i] == ")":
#         pilhaVerificacao.pop()
#         continue
#       if Operadores(param[i]) != None:
#         if Operadores(param[i+1]) != None:
#           if Operadores(param[i+1]) != 8 and Operadores(param[i+1]) != 9:
#             raise ("Error")
#     if len(pilhaVerificacao) != 0:
#       raise ("Error")
#     # Se a expressao esta consistente, retorna o proprio parametro
#     return param
#   except:
#     print ("Expressão inconsistente nos parentesis, ou ordem de operadores incorreta")
#     # Se inconsistente, retorna None
#     return None

def Operadores(param):
  '''Verifica qual o operador'''
  operadores = ["=", "+", "-", "*", "/", "**", "(", ")"]
  if param in operadores:
      for i in range(len(operadores)):
          if param == operadores[i]:
              return i
  return None

def ConverteOperador(param):
  '''Converte os operadores unarios de + e -'''
  if Operadores(param) == 1:
    return "#"
  if Operadores(param) == 2:
    return "_"

def OrganizaPrioridade(param, pilha, expressao):
  '''Organiza os operadores na pilha e na expressao, de acordo com suas prioridades'''
  if param == "#" or param == "_":
    pilha.push(param)
    return (pilha, expressao)
  if 1 <= Operadores(param) <= 2:
    while pilha.top() != None:
      if Operadores(pilha.top()) == 6:
        break
      if pilha.top() == "#" or pilha.top() =="_":
        expressao.append(pilha.pop())
        continue
      if 1 <= Operadores(pilha.top()) <= 2 or Operadores(pilha.top()) > Operadores(param):
        expressao.append(pilha.pop())
      break
    pilha.push(param)
  if 3 <= Operadores(param) <= 4:
    while pilha.top() != None:
      if Operadores(pilha.top()) == 6:
        break
      if pilha.top() == "#" or pilha.top() =="_":
        expressao.append(pilha.pop())
        continue
      if 3 <= Operadores(pilha.top()) <= 4 or Operadores(pilha.top()) > Operadores(param):
        expressao.append(pilha.pop())
      break
    pilha.push(param)
  if param == "**":
    while pilha.top() != None:
      if Operadores(pilha.top()) == 6:
        break
      if pilha.top() == "#" or pilha.top() == "_":
        expressao.append(pilha.pop())
      break
    pilha.push(param)
  if param == "=":
    while pilha.top() != None:
      if Operadores(pilha.top()) == 6:
        break
      if pilha.top() == "#" or pilha.top() =="_":
        expressao.append(pilha.pop())
        continue
      if Operadores(pilha.top()) >= Operadores(param):
        expressao.append(pilha.pop())
      break
    pilha.push(param)
  return (pilha, expressao)

def CalculaOperadoresBinarios(operador, elemento1, elemento2):
  if Operadores(operador) == 0:
    return elemento1
  if Operadores(operador) == 1:
    return (elemento1 + elemento2)
  if Operadores(operador) == 2:
    return (elemento2 - elemento1)
  if Operadores(operador) == 3:
    return (elemento1 * elemento2)
  if Operadores(operador) == 4:
    return (elemento2 / elemento1)
  if Operadores(operador) == 5:
    return (elemento2 ** elemento1)

def NovaExpressao(param):
  '''Separa os operandos dos operadores na string, independentemente de terem
  espaços entre eles ou não'''
  novaExpressao = ""
  for i in range (len(param)):
    if param[i] == "*" and param[i+1] == "*":
      novaExpressao = novaExpressao + " " + param[i]
      continue
    if param[i] == "*" and param[i-1] == "*":
      novaExpressao = novaExpressao + param[i] + " "
      continue
    elif Operadores(param[i]) != None:
      novaExpressao = novaExpressao + " " + param[i] + " "
      continue
    else:
      novaExpressao += param[i]
      continue
  return novaExpressao

def TraduzPosFixa(param):
  '''Recebe uma string "param" com ou sem atribuição "="
  e devolve uma lista contendo essa expressão em notação pós-fixas.
  Devolve True se foi realizado com sucesso, ou False caso contrário'''
  expressaoPosFixa = []
  # Cria uma pilha para montar a expressao Pos-Fixa
  pilhaPosFixa = Pilha()
  try:
    for k in range (len(param)):
      # Se operando, adiciona na lista expressaoPosFixa
      if Operadores(param[k]) == None: expressaoPosFixa.append(param[k])
      # Se operador, tratamos quando é abre parentesis, operador comum, ou fecha parentesis
      if Operadores(param[k]) != None:
        if Operadores(param[k]) == 6:
          pilhaPosFixa.push(param[k])
        if 0 <= Operadores(param[k]) <= 5:
          if 1 <= Operadores(param[k]) <= 2:
            # Caso seja + ou - unarios, converte em "+" -> "#" e "-" -> "_"
            if (Operadores(param[k-1]) != None):
              if Operadores(param[k-1]) != 7:
                param[k] = ConverteOperador(param[k])
          if pilhaPosFixa.top() != None:
            pilhaPosFixa, expressaoPosFixa = OrganizaPrioridade(param[k], pilhaPosFixa, expressaoPosFixa)
            continue
          pilhaPosFixa.push(param[k])
        if Operadores(param[k]) == 7:
          while pilhaPosFixa.top() != None and Operadores(pilhaPosFixa.top()) != 6:
            expressaoPosFixa.append(pilhaPosFixa.pop())
          pilhaPosFixa.pop()
    while pilhaPosFixa.top() != None:
      expressaoPosFixa.append(pilhaPosFixa.pop())
    return expressaoPosFixa
  except:
    return False

def CalcPosFixa(param1, param2):
  '''Recebe uma lista de valores contendo uma expressão em notação pós-fixa e
  calcula o seu valor. Devolve esse valor se o calculo foi feito com sucesso,
  ou False caso contrário'''
  pilhaCalcPosFixa = Pilha()
  for k in range (len(param1)):
    if Operadores(param1[k]) == None: pilhaCalcPosFixa.push(param1[k])
    if param1[k] == "#" or param1[k] == "_":
      topoDaPilha = float(pilhaCalcPosFixa.pop())
      if param1[k] == "#":
        topoDaPilha = 0 + topoDaPilha
      if param1[k] == "_":
        topoDaPilha = 0 - topoDaPilha
      pilhaCalcPosFixa.push(topoDaPilha)
    if param1[k] == "=" and (len(param1) - 1) == k:
      elemento1 = float(pilhaCalcPosFixa.pop())
      elemento2 = pilhaCalcPosFixa.pop()
      param2[str(elemento2)] = elemento1
      topoDaPilha = CalculaOperadoresBinarios(param1[k], elemento1, elemento2)
      pilhaCalcPosFixa.push(topoDaPilha)
      continue
    if Operadores(param1[k]) != None:
      elemento1 = float(pilhaCalcPosFixa.pop())
      elemento2 = float(pilhaCalcPosFixa.pop())
      topoDaPilha = CalculaOperadoresBinarios(param1[k], elemento1, elemento2)
      pilhaCalcPosFixa.push(topoDaPilha)
  return (pilhaCalcPosFixa.pop(), param2)

main()
