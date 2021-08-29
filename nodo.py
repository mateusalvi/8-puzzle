import numpy
import operator

EnableDebugNodo = True

class Nodo:
    def __init__(self, estado, pai, acao, custo, filhos):
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = 1
        self.filhos = filhos
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """


#Recebe um estado (string) e retorna uma lista de tuplas (ação,estado atingido)
#para cada ação possível no estado recebido.
#Tanto a ação quanto o estado atingido são strings também.
def sucessor(estado):
    estadoLista = list(estado) #altera o estado de string para lista, pois strings devem ser imutáveis em python
    indexDoEspaco = encontraEspacoVazio(estadoLista) #encontra onde está o espaço vazio e retorna o índice dele, poupando de fazer isso para cada movimento possível
    __sucessores = [moverEsquerda(estadoLista, indexDoEspaco), moverDireita(estadoLista, indexDoEspaco), moverAcima(estadoLista, indexDoEspaco), moverAbaixo(estadoLista, indexDoEspaco)]
    __sucessores = list(filter(None, __sucessores)) #remove os Nones da lista (movimentos inválidos)
    
    ####DEBUG#####
    if EnableDebugNodo: 
        print(" ")
        print("Sucessores de " + estado + ":")
        print(__sucessores)
        print(" ")
    ##############

    return __sucessores

#encontraEspacoVazio retorna o index do espaço vazio em um estado já transformado para lista
def encontraEspacoVazio(estadoLista):
    indexDoEspaco = estadoLista.index("_")
    return indexDoEspaco

#As funções à baixo recebem um estado do jogo e tentan mover o espaço vazio para o sentido correspondente
#se possivel, retorna uma lista com o movimento usado e o novo estado atingido
def moverEsquerda(estadoLista, indexDoEspaco):
    novaEstadoLista = estadoLista[:]
    if indexDoEspaco in (0,3,6):                                            #checa se pode se mover para esquerda
        return None
    else:
        novaEstadoLista[indexDoEspaco] = novaEstadoLista[indexDoEspaco-1]   #substitui o espaco pelo novo numero que entra no seu lugar
        novaEstadoLista[indexDoEspaco-1] = "_"
        
        estadoPalavra = "".join(novaEstadoLista)                            #transforma a lista de volta em palavra para usar na tupla de retorno
        novoEstado =  ['esquerda', estadoPalavra]                           #cria tupla de retorno
        
        return novoEstado

def moverDireita(estadoLista, indexDoEspaco):
    novaEstadoLista = estadoLista[:]
    if indexDoEspaco in (2,5,8):
        return None
    else:
        novaEstadoLista[indexDoEspaco] = novaEstadoLista[indexDoEspaco+1]
        novaEstadoLista[indexDoEspaco+1] = "_"
        
        estadoPalavra = ''.join(novaEstadoLista)
        novoEstado =  ["direita", estadoPalavra]
        
        return novoEstado

def moverAbaixo(estadoLista, indexDoEspaco):
    novaEstadoLista = estadoLista[:]
    if indexDoEspaco in (6,7,8):
        return None
    else:
        novaEstadoLista[indexDoEspaco] = novaEstadoLista[indexDoEspaco+3]
        novaEstadoLista[indexDoEspaco+3] = "_"
        
        estadoPalavra = ''.join(novaEstadoLista)
        novoEstado =  ["abaixo", estadoPalavra]
        
        return novoEstado

def moverAcima(estadoLista, indexDoEspaco):
    novaEstadoLista = estadoLista[:]
    if indexDoEspaco in (0,1,2):
        return None
    else:
        novaEstadoLista[indexDoEspaco] = novaEstadoLista[indexDoEspaco-3]
        novaEstadoLista[indexDoEspaco-3] = "_"
        
        estadoPalavra = ''.join(novaEstadoLista)
        novoEstado =  ["acima", estadoPalavra]

        return novoEstado

#Recebe um nodo (objeto da classe Nodo) e retorna uma lista de nodos (possíveis jogadas).
#Cada nodo da lista contém um estado sucessor do nó recebido.
def expande(__nodo):
    __sucessores = sucessor(__nodo.estado)
    __filhos = []

    for sublist in __sucessores: 
        #subList = __sucessores[i] #cria uma sublista com a tupla atual
        __acao = sublist[0] #list(map(operator.itemgetter(0), subList))
        __estado = sublist[1]
        __pai = __nodo.estado
        nodoFilho = Nodo(__estado, __pai, __acao, 1, None)
        __filhos.append(nodoFilho)
        nodoFilho = None
          
    __nodo.filhos = __filhos

    #####DEBUG#####
    if EnableDebugNodo:
        print("NODOS FILHOS DE " + __nodo.estado + ":")
        print(__nodo.filhos)
        print(" ")
        print("Conteúdos do primeiro filho:")
        print("Estado:", __nodo.filhos[0].estado, "  Pai:", __nodo.filhos[0].pai, "  Ação:", __nodo.filhos[0].acao)
        print(" ")
    ###############

def bfs(estado):
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

def dfs(estado):
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

def astar_hamming(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError
