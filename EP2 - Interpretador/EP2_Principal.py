# As expressões podem conter:
# a)Constantes inteiras (ex: 132, -45, 123456789, etc.)
# b)Variáveis contendo apenas letras (ex: k, SoMa, contador, QuantaDor, etc.)
# c)Operadores binários e parêntesis: +, -, *, /, **
# d)Operadores unários: + e –
# e)Parêntesis: ()
# f)Atribuição: =
# Subistituir "-" por "_" e "+" por "#" quando forem unários

class _Node:
    '''classe _Node - interna'''

    __slots__ = '_info', '_prox'

    def __init__ (self, info, prox):
        # inicia os campos
        self._info = info
        self._prox = prox


class Pilha:
    ''' implementa uma pilha usando uma Lista Ligada simples. '''

    def __init__ (self):
        ''' cria uma pilha vazia.'''
        self._topo = None # vazia
        self._tamanho = 0 # tamanho da pilha

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
            raise Empty("Pilha Vazia")
        return self._topo._info # topo da pilha

    def pop(self):
        ''' remove e retorna o topo da pilha.
        sinaliza exceção se pilha vazia.'''
        if self.is_empty():
            raise Empty("Pilha Vazia")
        val_topo = self._topo._info
        self._topo = self._topo._prox # pula o primeiro elemento
        self._tamanho -= 1
        return val_topo

    def Imprime(self):
        p = self._topo
        print("Imprimindo a pilha")
        while p is not None:
            print(p._info)
            p = p._prox
            
def main ():

    while True:
        #Colocar o prompt
        #Solicita uma nova expressão do tipo:
        expressao = str(input(">>> "))
        novaPilha = Pilha()
        if Operadores(expressao) != None:
            novaPilha.push(expressao)
            continue
        print (novaPilha.Imprime())
        return
        #Traduzir a notação para pós-fixas

        # Calcular o valor da expressão usando a notação pós-fixas
        # Se o final for "=" atribuição, armazenar o valor. Caso contrario, print

def Operadores(param):
    '''Verifica qual o operador'''
    operadores = ["+","-","*","/","**","(",")","="]
    if param in operadores:
        for i in range (len(operadores)):
            if param == operadores[i]: return i
    return None
    
def TraduzPosFixa():
    '''Recebe uma string "expressao" com ou sem atribuição "="
    e devolve uma lista contendo essa expressão em notação pós-fixas.
    Devolve True se foi realizado com sucesso, ou False caso contrário'''
    pass

def CalcPosFixa():
    '''Recebe uma lista de valores contendo uma expressão em notação pós-fixa e
    calcula o seu valor. Devolve esse valor se o calculo foi feito com sucesso,
    ou False caso contrário'''
    pass

main()

