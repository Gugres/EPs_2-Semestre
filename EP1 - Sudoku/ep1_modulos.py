import urllib.request
 
class Sudoku:
    def __init__(self, param):
        self.matriz = []
        for i in range(len(param)):
            self.matriz.append([])
            for j in range(len(param[i])):
                self.matriz[i].append(param[i][j])

    def TestaElementoLinha(self, i, j):
        '''Retorna False se o elemento esta repetido na linha'''
        elementoTestado = self.matriz[i][j]
        for k in range(9):
            if k == j:
                continue
            if self.matriz[i][k] == elementoTestado:
                return False
        return True

    def TestaElementoColuna(self, i, j):
        '''Retorna False se o elemento esta repetido na coluna'''
        elementoTestado = self.matriz[i][j]
        for k in range(9):
            if k == i:
                continue
            if self.matriz[k][j] == elementoTestado:
                return False
        return True

    def TestaElementoQuadrado(self, i, j):
        '''Retorna False se o elemento esta repetido no quadrado'''
        elementoTestado = self.matriz[i][j]
        count1 = 3*(i//3)
        count2 = 3*(j//3)
        for k in range(count1, count1 + 3):
            for c in range(count2, count2 + 3):
                if k == i and c == j:
                    continue
                if self.matriz[k][c] == elementoTestado:
                    return False
        return True

    def ProcuraElementoLinha(self, linha, number):
        '''Procura dígito d na linha L da matriz (0 ≤ d ≤ 8). Devolve -1
        se não encontrou ou índice da coluna onde foi encontrado'''
        for j in range(9):
            if self.matriz[linha][j] == number:
                return j
        return -1

    def ProcuraElementoColuna(self, coluna, number):
        '''Procura dígito d na coluna C da matriz (0 ≤ d ≤ 8). Devolve
        -1 se não encontrou ou índice da linha onde foi encontrado'''
        for i in range(9):
            if self.matriz[i][coluna] == number:
                return i
        return -1

    def ProcuraElementoQuadrado(self, linha, coluna, number):
        '''Procura o dígito d no quadrado interno onde está o elemento Mat[L][C] (1 ≤ d ≤ 9). 
        Devolve a dupla (k1, k2) se d está na posição Mat[k1][k2] ou (-1, -1) caso contrário'''
        count1 = 3*(linha//3)
        count2 = 3*(coluna//3)
        for i in range(count1, count1 + 3):
            for j in range(count2, count2 + 3):
                if self.matriz[i][j] == number:
                    return (i, j)
        return (-1, -1)

def LeiaMatrizLocal(NomeArquivo):
    
    # retorna a matriz lida se ok ou uma lista vazia senão
    # abrir o arquivo para leitura
    try:
        arq = open(NomeArquivo, "r")
    except:
        # retorna lista vazia se deu erro
        return False 
        # inicia matriz SudoKu a ser lida
    mat = [9 * [0] for k in range(9)]
    # ler cada uma das linhas do arquivo
    i = 0
    for linha in arq:
        v = linha.split()
        # verifica se tem 9 elementos e se são todos entre '1' e '9'
        try:
            if len(v) != 9:
                raise ("Error")
            # transforma de texto para int
            for j in range(len(v)):
                if int(v[j]) < 0 or int(v[j]) > 9:
                    raise ("Error")
                mat[i][j] = int(v[j])
            i += 1
        except:
            print("\nErro na verificação das linhas do arquivo")
            print ("Erro nas linha: ", i, " e coluna: ", j)

    # fecha arquivo e retorna matriz lida e consistida
    arq.close()
    return mat

def LeiaMatrizRemota(NomeArquivo):
    '''Importa o arquivo e converte em uma lista'''

    # retorna True se conseguiu ler o arquivo e False caso contrário
    # abrir o arquivo para leitura
    try:
        urlarq = "http://www.ime.usp.br/~mms/mac1222s2019/" + NomeArquivo
        arq = urllib.request.urlopen(urlarq)
    except:
        return []  # retorna lista vazia se der erro

    # inicia matriz SudoKu a ser lida
    mat = [9 * [0] for k in range(9)]
    # ler todo o arquivo e separar em linhas
    arqtotal = arq.read()
    linhas = arqtotal.splitlines()
    # tratar cada uma das linhas do arquivo
    i = 0
    for linha in linhas:
        v = linha.split()
        # verifica se tem 9 elementos e se são todos entre '1' e '9'
        try:
            if len(v) != 9:
                raise ("Error")
            # transforma de texto para int
            for j in range(len(v)):
                if int(v[j]) < 0 or int(v[j]) > 9:
                    raise ("Error")
                mat[i][j] = int(v[j])
            i += 1
        except:
            print("\nErro na verificação das linhas do arquivo")
            print ("Erro nas linha: ", i, " e coluna: ", j)

    # fecha arquivo e retorna matriz lida e consistida
    arq.close()
    return mat

def TestaMatrizLida(param):
    '''Devolve True se a matriz lida Mat está com as casas já preenchidas com os
    valores corretos. Não há repetições na linha, na coluna ou no quadrado interno'''
    try:
        for i in range(9):
            for j in range(9):
                if param.matriz[i][j] != 0:
                    if not param.TestaElementoLinha(i, j):
                        raise ("Erro")
                    if not param.TestaElementoColuna(i, j):
                        raise ("Erro")
                    if not param.TestaElementoQuadrado(i, j):
                        raise ("Erro")
        return True
    except:
        print("\nErro na etapa de: TestaMatrizLida")
        return False

def TestaMatrizPreenchida(param):
    '''Devolve True se a matriz Mat está preenchida corretamente. False caso contrário'''
    try:
        for i in range(9):
            for j in range(9):
                if param.matriz[i][j] != 0:
                    if not param.TestaElementoLinha(i, j):
                        raise ("Erro")
                    if not param.TestaElementoColuna(i, j):
                        raise ("Erro")
                    if not param.TestaElementoQuadrado(i, j):
                        raise ("Erro")
        return True
    except:
        print ("\nErro na etapa de: TestaMatrizPreenchida")
        return False

def ImprimaMatriz(param):
    '''Imprime a matrix Sudoku Mat[0..8][0..8]'''
    for i in range(9):
        for j in range(10):
            if j == 9:
                print ("")
                continue
            print (param[i][j], end = " ")    

def ResolvendoSudoku(param, contGlobal, contMatrizesErradas, linha=0, coluna=0):
    '''Função principal que preenche a matriz Sudoku, verificando se chegou ao final
    de uma solução e retrocedendo sempre que necessário'''
    verificador = 0
    for i in range(linha, len(param.matriz)):
        if verificador == 1:
            break
        for j in range(len(param.matriz)):
            if param.matriz[i][j] == 0:
                novaLinha, novaColuna = i, j
                verificador = 1
                break

    if verificador == 0:
        if not TestaMatrizPreenchida(param):
            contMatrizesErradas += 1
            return
        contGlobal += 1
        # Imprima Matriz
        print("\n**** Matriz completa ****\n")
        ImprimaMatriz(param.matriz)
        print("")
        return (contGlobal, contMatrizesErradas)

    for k in range(1, 10):
        if param.ProcuraElementoLinha(novaLinha, k) == -1:
            if param.ProcuraElementoColuna(novaColuna, k) == -1:
                if param.ProcuraElementoQuadrado(novaLinha, novaColuna, k) == (-1, -1):
                    param.matriz[novaLinha][novaColuna] = k
                    ResolvendoSudoku(param, contGlobal, contMatrizesErradas, novaLinha, novaColuna)
        
        param.matriz[novaLinha][novaColuna] = 0
    
    return (contGlobal, contMatrizesErradas) 