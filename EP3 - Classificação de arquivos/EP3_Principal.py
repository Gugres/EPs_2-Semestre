# Desafio - Classificar um arquivo pelos critérios: Nome -> Identificação -> Data
import gerador_de_teste

def main():
  '''função principal'''

  # Entre com seu NUSP - para randomizar
  nusp = '11340571'
  # Gera arquivo com uma certa quantidade de registros
  quant_reg = '100'
  gerador_de_teste.GeraArquivo(nusp, "arquivo_de_teste.txt", quant_reg)
  arq_origem = "arquivo_de_teste.txt"
  arq_destino = "arquivo_de_teste_ordenado.txt"

  # if tipoDeTeste == "avaliar":
  #   arq_origem = str(input("Entre com o nome do arquivo de origem: "))
  #   arq_destino = str(input("Entre com o nome do arquivo de destino: "))

  print("")
  TAB = GeradorDaTabela(arq_origem)
  for k in range(len(TAB)):
    print (k, end=" ")
    print(TAB[k])
  print("")

def GeradorDaTabela(nome_arq):
  try:
    arq = open(nome_arq, "r")
  except:
    return False
  TAB = []
  for l in arq:
    linha = l[:len(l) - 1]
    TAB.append(linha)
  arq.close()
  return TAB

def ClassQuickRecursivo(TAB):
  '''Método QuickRecursivo para ordenação de tabela'''
  pass

def ClassQuickNaoRecursivo(TAB):
  '''Método Quick normal para ordenação de tabela'''
  pass

def classMetodoSort(TAB):
  '''Utiliza o método "sort()" para ordenar a tabela'''
  pass

if __name__ == "__main__":
  main()