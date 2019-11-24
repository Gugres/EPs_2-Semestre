# Desafio - Classificar um arquivo pelos critérios: Nome -> Identificação -> Data
import gerador_de_teste
import time

class Empty (Exception):
  pass

class _Node:
  '''classe _Node'''
  __slots__ = '_info', '_prox'

  def __init__(self, info, prox):
    # inicia os campos
    self._info = info
    self._prox = prox

class PilhaLista:
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
  '''função principal'''

  while True:
    print ("\nSe deseja sair, digite 'exit()'")
    nome_arq_origem = input(str("Entre com o nome do arquivo de origem: "))
    if nome_arq_origem == 'exit()': return
    nome_arq_destino = input(str("Entre com o nome do arquivo de destino: "))
    try:
      arq_destino = open(nome_arq_destino, 'w')
    except:
      print("Erro na leitura do arquivo de destino")
      continue

    # Ordenação por QuickSorte recursivo
    TABOrdenadaRecursiva = GeradorDaTabela(nome_arq_origem)
    time1 = time.time()
    ClassQuickRecursivo(TABOrdenadaRecursiva, 0, len(TABOrdenadaRecursiva) - 1)
    time2 = time.time()
    if VerificaçãoDaResposta(TABOrdenadaRecursiva):
      print("\nTabela ordenada pelo metodo QuickSort Recursivo")
      tempoTotal = time2 - time1
      print("Tempo gasto: ", tempoTotal)

    # Ordenação por QuickSorte Não Recursivo
    TABOrdenadaNormal = GeradorDaTabela(nome_arq_origem)
    time1 = time.time()
    ClassQuickNaoRecursivo(TABOrdenadaNormal, 0, len(TABOrdenadaRecursiva) - 1)
    time2 = time.time()
    if VerificaçãoDaResposta(TABOrdenadaNormal):
      print("Tabela ordenada pelo metodo QuickSort Nao Recursivo")
      tempoTotal = time2 - time1
      print("Tempo gasto: ", tempoTotal)

    # Ordenação por Sort()
    TABOrdenadaSort = GeradorDaTabela(nome_arq_origem)
    time1 = time.time()
    classMetodoSort(TABOrdenadaSort)
    time2 = time.time()
    if VerificaçãoDaResposta(TABOrdenadaSort):
      print("Tabela ordenada pelo metodo 'sort()' do Python")
      tempoTotal = time2 - time1
      print("Tempo gasto: ", tempoTotal)

    if ComparaRespostas(TABOrdenadaRecursiva, TABOrdenadaNormal, TABOrdenadaSort):
      print ("\nRespostas iguais")
    else: print ("\nRespostas diferentes")

    # Salvar no arquivo secundário
    for linha in TABOrdenadaSort:
      linha[1], linha[2] = time.strftime("%d/%m/%Y", linha[2]), linha[1]
      arq_destino.write(','.join(linha) + '\n')

    arq_destino.close()

def GeradorDaTabela(nome_arq_origem):
  try:
    arq = open(nome_arq_origem, "r")
  except:
    print("Erro na leitura do arquivo de origem")
  TAB = []
  for l in arq:
    linha = l[:len(l) - 1]
    linha = linha.split(',')
    linha[2], linha[1] = time.strptime(linha[1], '%d/%m/%Y'), linha[2]
    TAB.append(linha)
  arq.close()
  return TAB

def ClassQuickRecursivo(TAB, inicio, fim):
  '''Método QuickRecursivo para ordenação de tabela'''
  # Se a lista tem mais de um elemento, ela será
  # particionada e as duas partições serão classificadas
  # pelo mesmo método Quick Sort
  if inicio < fim:
    k = particiona(TAB, inicio, fim)
    ClassQuickRecursivo(TAB, inicio, k - 1)
    ClassQuickRecursivo(TAB, k + 1, fim)

def ClassQuickNaoRecursivo(TAB, inicio, fim):
  '''Método Quick normal para ordenação de tabela'''
  # Cria a pilha de sub-listas e inicia com lista completa
  Pilha = PilhaLista()
  Pilha.push((0, len(TAB) - 1))
  # Repete até que a pilha de sub-listas esteja vazia
  while not Pilha.is_empty():
    inicio, fim = Pilha.pop()
    # Só particiona se há mais de 1 elemento
    if fim - inicio > 0:
      k = particiona(TAB, inicio, fim)
      # Empilhe as sub-listas resultantes
      Pilha.push((inicio, k - 1))
      Pilha.push((k + 1, fim))

def classMetodoSort(TAB):
  '''Utiliza o método "sort()" para ordenar a tabela'''
  TAB = TAB.sort()

def particiona(lista, inicio, fim):
  i, j = inicio, fim
  pivo = lista[fim]
  while True:
    # aumentado i
    while i < j and lista[i] <= pivo: i = i + 1
    if i < j: lista[i], lista[j] = pivo, lista[i]
    else: break
    # diminuindo j
    while i < j and lista[j] >= pivo: j = j - 1
    if i < j: lista[i], lista[j] = lista[j], pivo
    else: break
  return i

def ComparaRespostas(resp1, resp2, resp3):
  for k in range(len(resp1)):
    for j in range(len(resp1[0])):
      if resp1[k][j] != resp2[k][j]:
        return False
      if resp1[k][j] != resp3[k][j]:
        return False
      if resp2[90][0] != resp3[90][0]:
        return False
  return True

def VerificaçãoDaResposta(param):
  for k in range(len(param) - 1):
    if param[k] > param[k + 1]: return False
  return True

if __name__ == "__main__":
  main()