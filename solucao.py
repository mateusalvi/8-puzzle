import numpy
import operator
import sys

EnableDebugNodo = False
meta = "12345678_"

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

def getEstado(self):
    return self.estado

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
        novoEstado =  ('esquerda', estadoPalavra)                           #cria tupla de retorno
        
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

#Recebe um nodo (objeto da classe Nodo) e retorna uma lista de nodos (possíveis jogadas).
#Cada nodo da lista contém um estado sucessor do nó recebido.
def expande(__nodo):
    __sucessores = sucessor(__nodo.estado)
    __filhos = []

    for sublist in __sucessores: 
        #subList = __sucessores[i] #cria uma sublista com a tupla atual
        __acao = sublist[0] #list(map(operator.itemgetter(0), subList))
        __estado = sublist[1]
        __custo = __nodo.custo + 1
        nodoFilho = Nodo(__estado, __nodo, __acao, __custo)
        __filhos.append(nodoFilho)
        nodoFilho = None

    #####DEBUG#####
    if EnableDebugNodo:
        print("NODOS FILHOS DE " + __nodo.estado + ":")
        print(__filhos)
        print(" ")
        print("Conteúdos do primeiro filho:")
        print("Estado:", __filhos[0].estado, "  Pai:", __filhos[0].pai, "  Ação:", __filhos[0].acao, "  Custo total:", __filhos[0].custo)
        print(" ")
    ###############

    return __filhos

def bfs(estado):
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    if not testaInsolução(estado):
        return None

    if estado == meta:
        return []
    else:
        pass    

    explorados = set()
    fronteira = []
    fronteira.append(Nodo(estado, None, None, 1))

    while len(fronteira) > 0:
        if not fronteira: 
            return "Erro no BFS: lista vazia."
        estadoAtual = fronteira[0]
        fronteira.pop(0)
        if estadoAtual.estado == meta: 
            return encontraCaminho(estadoAtual)
        if estadoAtual.estado not in explorados:
            explorados.add(estadoAtual.estado)
            fronteira.extend(expande(estadoAtual))
    
def dfs(estado):
    if testaInsolução(estado):
        pass
    else:
        return None

    if estado == meta:
        return []
    else:
        pass

    pilha = []
    sexp = set()
    lpath = []
    listab = []
    nodev = Nodo(estado,None,None,0)
    sexp.add(nodev.estado)
    flag = 0

    while flag == 0:
        listab = expande(nodev)

        k=0
        m=0

        for k in range(len(listab)):
            if not(listab[k].estado in sexp):
                pilha.append(listab[k])
        
        nodev = pilha.pop()
        sexp.add(nodev.estado)
        lpath.append(nodev.acao)

        if(nodev.estado == meta):
            flag = 1
            return encontraCaminho(nodev)
            
# Calcula a distancia de hamming
def distHamming(nodo):
    estado = nodo.estado
    distancia = 0
    for a, b in zip(estado, meta):
        if a != b:
            distancia += 1
    return (distancia, nodo)

def astar_hamming(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    explorados = set()
    fronteira = []
    auxList = []
    fronteira.append(Nodo(estado, None, None, 1))

    if not fronteira: 
            return "Erro no BFS: lista vazia."

    while len(fronteira) > 0:
        estadoAtual = fronteira[0]
        fronteira.pop(0)
        if estadoAtual.estado == meta: 
            #return encontraCaminho(estadoAtual)
            print("achou")
            return
        if estadoAtual.estado not in explorados:
            explorados.add(estadoAtual.estado)
            nodos_expandidos = expande(estadoAtual)
            for filho in nodos_expandidos:
                auxList.append(distHamming(filho))
            auxList.sort(reverse=True)
            while auxList:
                fronteira.extend(auxList.pop()[1])

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

#Testa se o estado passado tem solução pelo princípio da paridade
def testaInsolução(estado):
    estadoLista = list(estado)
    estadoLista.remove('_')
    paridade = 0

    k = 0
    for k in range(len(estadoLista)):
        m = k + 1
        while m < len(estadoLista):
            if estadoLista[m] < estadoLista[k]:
                paridade = paridade + 1
            m = m + 1

    if (paridade % 2) == 0:
        return True
    else:
        print("O estado inicial passado não tem solução")
        return False
        
def encontraCaminho(nodoMeta):
    caminho = []

    while nodoMeta.pai is not None:
        caminho.append(nodoMeta.acao)
        nodoMeta = nodoMeta.pai
    caminho.reverse()

    return caminho