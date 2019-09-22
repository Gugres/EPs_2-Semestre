# from ep1_modulos import Sudoku
import ep1_modulos
import time

contGlobal = 0
 
def main():
    '''Função principal que pergunta qual o jogo que o usuário deseja subir para o programa'''

    # Etapa de criação de um novo jogo
    global contGlobal
    global contMatrizesErradas
    print ("\n**** Programa para solução de Sudoku ****")
    print ("\nVoce deseja:\n1 - Importar arquivos localmente \n2 - Ler os arquivos da internet")
    try:
        tipoDeArquivo = int(input("\nEntre com a opcão: "))
        while tipoDeArquivo < 1 or tipoDeArquivo > 2:
            print ("Opcão digitada não existe ")
            tipoDeArquivo = int(input("\nEntre com uma nova opcão: "))
    except:
        print ("Erro na escolha da opção de leitura de arquivos")
    while True:
        contGlobal = 0
        contMatrizesErradas = 0
        try:    
            if tipoDeArquivo == 1:
                print ("\nDigite 0 se quiser sair")
                nomeArq = str(input("Entre com o nome do arquivo( <nome_arquivo> . <tipo_de_arquivo> ): "))
                if nomeArq == "0":
                    return
                tempo1 = time.time()
                # Intancia de um novo jogo de Sudoku, utilizando o Leitor de Matriz
                novoJogo = ep1_modulos.Sudoku(ep1_modulos.LeiaMatrizLocal(nomeArq))
            
            if tipoDeArquivo == 2:    
                print ("\nDigite 0 se quiser sair")
                number = int(input("Entre com o numero do sudoku que deseja testar (entre 1 e 15): "))
                while number < 0 or number > 15:
                    print("\nNumero digitado não existe")
                    number = int(input("Entre com outro numero de sudoku que deseja testar (entre 1 e 15): "))    
                if number == 0:
                    return
                nomeArq = "sudoku" + str(number)
                tempo1 = time.time()
                # Instancia um novo jogo de Sudoku, utilizando o Leitor de Matriz Remota
                novoJogo = ep1_modulos.Sudoku(ep1_modulos.LeiaMatrizRemota(nomeArq))
        except:
            print ("Erro na preparação do novoJogo")
            continue

        # Verificação dos elementos do novo jogo
        if not ep1_modulos.TestaMatrizLida(novoJogo):
            tempo2 = time.time()
            tempo_decorrido = tempo2 - tempo1
            print ("**** Matriz Inconsistente")
            print (" - Tempo decorrido = ", tempo_decorrido, " segundos")
            continue

        # Imprime a matriz principal
        print ("\n**** Matriz inicial ****\n")
        ep1_modulos.ImprimaMatriz(novoJogo.matriz)
        # Resolvendo o Sudoku
        contGlobal, contMatrizesErradas = ep1_modulos.ResolvendoSudoku(novoJogo, contGlobal, contMatrizesErradas)
        if contGlobal == 0:
            tempo2 = time.time()
            tempo_decorrido = tempo2 - tempo1
            print("\n**** Matriz Incompleta e Consistente")
            print ("**** - Tempo decorrido = ", tempo_decorrido, " segundos")
            print ("**** - ", contGlobal, " soluções para a matriz")
            continue
        tempo2 = time.time()
        tempo_decorrido = tempo2 - tempo1 
        print("**** Matriz Completa e Consistente")
        print ("**** - Tempo decorrido = ", tempo_decorrido, " segundos")
        print ("**** - ", contGlobal, " soluções para a matriz")
        print ("**** - ", contMatrizesErradas, " matrizes erradas")

main()


