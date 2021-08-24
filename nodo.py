import numpy

class Nodo:
    def __init__(self, estado, pai, acao, custo):
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """


def sucessor(estado):
    estadoLista = list(estado)
    indexDoEspaco = encontraEspacoVazio(estadoLista) #encontra onde está o espaço vazio, poupando de fazer isso para cada movimento possível
    sucessores = (moverEsquerda(estadoLista, indexDoEspaco), moverDireita(estadoLista, indexDoEspaco), moverAcima(estadoLista, indexDoEspaco), moverAbaixo(estadoLista, indexDoEspaco))
    print(sucessores)
    
    """
    Recebe um estado (string) e retorna uma lista de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    # substituir a linha abaixo pelo seu codigo

#encontraEspacoVazio retorna o index do espaço vazio em um estado já transformado para lista

def encontraEspacoVazio(estadoLista):
    indexDoEspaco = estadoLista.index("_")
    return indexDoEspaco

def moverEsquerda(estadoLista, indexDoEspaco):
    novaEstadoLista = estadoLista[:]
    if indexDoEspaco in (0,3,6):                                            #checa se pode se mover para esquerda
        return None
    else:
        novaEstadoLista[indexDoEspaco] = novaEstadoLista[indexDoEspaco-1]   #substitui o espaco pelo novo numero que entra no seu lugar
        novaEstadoLista[indexDoEspaco-1] = "_"
        
        estadoPalavra = ''.join(novaEstadoLista)                            #transforma a lista de volta em palavra para usar na tupla de retorno
        novoEstado =  ("esquerda", estadoPalavra)                           #cria tupla de retorno
        
        return novoEstado

def moverDireita(estadoLista, indexDoEspaco):
    novaEstadoLista = estadoLista[:]
    if indexDoEspaco in (2,5,8):
        return None
    else:
        novaEstadoLista[indexDoEspaco] = novaEstadoLista[indexDoEspaco+1]
        novaEstadoLista[indexDoEspaco+1] = "_"
        
        estadoPalavra = ''.join(novaEstadoLista)
        novoEstado =  ("direita", estadoPalavra)
        
        return novoEstado

def moverAbaixo(estadoLista, indexDoEspaco):
    novaEstadoLista = estadoLista[:]
    if indexDoEspaco in (6,7,8):
        return None
    else:
        novaEstadoLista[indexDoEspaco] = novaEstadoLista[indexDoEspaco+3]
        novaEstadoLista[indexDoEspaco+3] = "_"
        
        estadoPalavra = ''.join(novaEstadoLista)
        novoEstado =  ("abaixo", estadoPalavra)
        
        return novoEstado

def moverAcima(estadoLista, indexDoEspaco):
    novaEstadoLista = estadoLista[:]
    if indexDoEspaco in (0,1,2):
        return None
    else:
        novaEstadoLista[indexDoEspaco] = novaEstadoLista[indexDoEspaco-3]
        novaEstadoLista[indexDoEspaco-3] = "_"
        
        estadoPalavra = ''.join(novaEstadoLista)
        novoEstado =  ("acima", estadoPalavra)

        return novoEstado

def expande(nodo):
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um iterable de nodos.
    Cada nodo do iterable é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


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
