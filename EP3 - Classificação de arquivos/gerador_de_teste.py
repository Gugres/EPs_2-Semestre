
from random import seed, randrange

# nomes randômicos
n1 = ["Felicia", "Catulo", "Osmund", "Artmio", "Senizio", "Tilenio"]
n2 = ["Cartuxo", "Olambro", "Romulo", "Ambulo", "Atomon", "Virino"]
n3 = ["Sereno", "Soterno", "Moncoes", "Oscaran", "Topovi", "Talento"]
n4 = ["Lasmia", "Mantega", "Casas", "Lorentao", "Melkioz", "Motivio"]
nn = 6

# gera um registro com NOME[0..39], DATAN[40..47] e IDENT[48..55]
# conteúdo randômico baseado em seu NUSP
# pp = '' - gera um registro completo
# pp != '' - gera apenas uma nova datan + ident ou apenas ident
def GeraRegistro(pp):
  global n1, n2, n3, n4, nn
  # nome, datan e ident
  nome = n1[randrange(nn)] + ' ' + n2[randrange(nn)] + ' ' + n3[randrange(nn)] + ' ' + n4[randrange(nn)]
  dia = randrange(28) + 1
  mes = randrange(12) + 1
  ano = randrange(17) + 2000
  datan = f'{dia:02}' + '/' + f'{mes:02}' + '/' + f'{ano:04}'
  ident = f'{randrange(100000000000):011}'
  if pp == '':
    # gera um novo registro completo
    registro = nome + ',' + datan + ',' + ident
    return registro
  elif randrange(2) == 0:
    # preserva o nome e gera datan + ident
    campos = pp.split(',')
    registro = campos[0] + ',' + datan + ',' + ident
    return registro
  else:
    # preserva o nome e datan e gera ident
    campos = pp.split(',')
    registro = campos[0] + ',' + campos[1] + ',' + ident
    return registro

# gera arquivo nomearq com nreg registros
def GeraArquivo(nusp, nomearq, nreg):
  # randomize
  seed(nusp)
  # quantidade de registros - gera 80% do total
  nreg80 = nreg * 80 // 100
  # tabela para guardar registros para repetição
  tab = ['' for k in range(nreg // 20)] # 5% dos registros
  # abre arquivo para gravação
  arq = open(nomearq, "w")
  # grava metade dos registros
  for k in range(nreg80):
    reg = GeraRegistro('')
    arq.write(reg + '\n')
    # guarda 5% dos registros para repetição
    if k % 20 == 0:
      # guarda em tab
      tab[k // 20] = reg
  # grava o resto dos 20% dos registros
  cont = nreg80 + 1
  for k in range(len(tab)):
    # para cada registro em tab gera 4 outros
    for j in range(4):
      reg = GeraRegistro(tab[k])
      arq.write(reg + '\n')
      cont += 1
  # fecha arquivo
  arq.close()

# Entre com seu NUSP - para randomizar
nusp = '11340571'
# Gera arquivo com uma certa quantidade de registros
quant_reg = 100000
GeraArquivo(nusp, "arquivo_de_teste.txt", quant_reg)