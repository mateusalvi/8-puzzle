import time

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
    tempoDeInicio = time.time()
    totalExpandidos = 0

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
            print("Tempo de execução BFS:", (time.time() - tempoDeInicio), "segundos") 
            print("Nodos expandidos:", totalExpandidos)
            caminho = encontraCaminho(estadoAtual)
            print("Custo até a solução:", len(caminho))
            print("")
            return caminho
        if estadoAtual.estado not in explorados:
            explorados.add(estadoAtual.estado)
            expandidos = expande(estadoAtual)
            totalExpandidos = totalExpandidos + len(expandidos)
            fronteira.extend(expandidos)
    
def dfs(estado):
    tempoDeInicio = time.time()
    totalExpandidos = 0
    
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
        totalExpandidos = totalExpandidos + len(listab)

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
            print("Tempo de execução DFS:", (time.time() - tempoDeInicio), "segundos") 
            print("Nodos expandidos:", totalExpandidos)
            caminho = encontraCaminho(nodev)
            print("Custo até a solução:", len(caminho))
            print("")
            return caminho
            
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

def distHamming(nodo):
    estado = nodo.estado
    distancia = 0
    for a, b in zip(estado, meta):
        if a != b:
            distancia += 1

    distancia = distancia + nodo.custo
    listd = []
    listd.append(distancia)
    listd.append(nodo)
    return listd

def astar_hamming(estado):
    tempoDeInicio = time.time()
    totalExpandidos = 0

    if not testaInsolução(estado):
        return None

    if estado == meta:
        return []
    else:
        pass   
    
    sexp = set()
    listab = [] 
    nodev = Nodo(estado,None,None,0)
    sexp.add(nodev.estado)
    flag = 0

    fronteira = []

    while flag == 0:

        listab = expande(nodev)
        totalExpandidos = totalExpandidos + len(listab)

        k=0
        m=0
        
        for k in range(len(listab)):    
            if not(listab[k].estado in sexp):
                fronteira.append(distHamming(listab[k]))    
        
        aux = []
        t = 0
        aux = fronteira[0]
        for m in range(len(fronteira)):
            if(fronteira[m][0] < aux[0]):
                aux = fronteira[m]
                t = m   

        nodevl = []
        nodevl = fronteira.pop(t)
        nodev = nodevl[1]
      
        sexp.add(nodev.estado)

        s = 0
        if(nodev.estado == meta):
            s = len(encontraCaminho(nodev))
            print("Tempo de execução Manhattan:", (time.time() - tempoDeInicio), "segundos") 
            print("Nodos expandidos:", totalExpandidos)
            caminho = encontraCaminho(nodev)
            print("Custo até a solução:", len(caminho))
            print("")
            return caminho  

def mah(nodo):

    k=0
    i=0
    j=0
    
    lin1 = []
    lin2 = []
    lin3 = []

    strn = nodo.estado

    for i in range(9):
        if(i<3):
            lin1.append(strn[i])
        else:
            if(i<6):
                lin2.append(strn[i])
            else:
                lin3.append(strn[i])            
        i = i + 1
    
    dist=0
    for j in range(3):
        if(lin1[j] == "1"):
            dist = dist + abs(j - 0) + abs(0 - 0)
        if(lin1[j] == "2"):
            dist = dist + abs(j - 1) + abs(0 - 0)
        if(lin1[j] == "3"):
            dist = dist + abs(j - 2) + abs(0 - 0)
        if(lin1[j] == "4"):
            dist = dist + abs(j - 0) + abs(0 - 1)
        if(lin1[j] == "5"):
            dist = dist + abs(j - 1) + abs(0 - 1)
        if(lin1[j] == "6"):
            dist = dist + abs(j - 2) + abs(0 - 1)
        if(lin1[j] == "7"):
            dist = dist + abs(j - 0) + abs(0 - 2)
        if(lin1[j] == "8"):
            dist = dist + abs(j - 1) + abs(0 - 2)
        if(lin1[j] == "_"):
            dist = dist + abs(j - 2) + abs(0 - 2)

    j=0
    for j in range(3):
        if(lin2[j] == "1"):
            dist = dist + abs(j - 0) + abs(1 - 0)
        if(lin2[j] == "2"):
            dist = dist + abs(j - 1) + abs(1 - 0)
        if(lin2[j] == "3"):
            dist = dist + abs(j - 2) + abs(1 - 0)
        if(lin2[j] == "4"):
            dist = dist + abs(j - 0) + abs(1 - 1)
        if(lin2[j] == "5"):
            dist = dist + abs(j - 1) + abs(1 - 1)
        if(lin2[j] == "6"):
            dist = dist + abs(j - 2) + abs(1 - 1)
        if(lin2[j] == "7"):
            dist = dist + abs(j - 0) + abs(1 - 2)
        if(lin2[j] == "8"):
            dist = dist + abs(j - 1) + abs(1 - 2)
        if(lin2[j] == "_"):
            dist = dist + abs(j - 2) + abs(1 - 2)

    j=0
    for j in range(3):
        if(lin3[j] == "1"):
            dist = dist + abs(j - 0) + abs(2 - 0)
        if(lin3[j] == "2"):
            dist = dist + abs(j - 1) + abs(2 - 0)
        if(lin3[j] == "3"):
            dist = dist + abs(j - 2) + abs(2 - 0)
        if(lin3[j] == "4"):
            dist = dist + abs(j - 0) + abs(2 - 1)
        if(lin3[j] == "5"):
            dist = dist + abs(j - 1) + abs(2 - 1)
        if(lin3[j] == "6"):
            dist = dist + abs(j - 2) + abs(2 - 1)
        if(lin3[j] == "7"):
            dist = dist + abs(j - 0) + abs(2 - 2)
        if(lin3[j] == "8"):
            dist = dist + abs(j - 1) + abs(2 - 2)
        if(lin3[j] == "_"):
            dist = dist + abs(j - 2) + abs(2 - 2)

    dist = dist + nodo.custo
    listdm = []
    listdm.append(dist)
    listdm.append(nodo)
    return listdm
    
def astar_manhattan(estado):
    if not testaInsolução(estado):
        return None

    if estado == meta:
        return []
    else:
        pass   
    
    tempoDeInicio = time.time()
    totalExpandidos = 0
    sexp = set()
    listab = []
    nodev = Nodo(estado,None,None,0)
    sexp.add(nodev.estado)
    flag = 0

    fronteira = []

    while flag == 0:

        listab = expande(nodev)
        totalExpandidos = totalExpandidos + len(listab)

        k=0
        m=0
        
        for k in range(len(listab)):    
            if not(listab[k].estado in sexp):
                fronteira.append(mah(listab[k]))    
                        
        aux = []
        t = 0
        aux = fronteira[0]
        for m in range(len(fronteira)):
            if(fronteira[m][0] < aux[0]):
                aux = fronteira[m]
                t = m   

        nodevl = []
        nodevl = fronteira.pop(t)
        nodev = nodevl[1]
      
        sexp.add(nodev.estado)

        s = 0
        if(nodev.estado == meta):
            s = len(encontraCaminho(nodev))
            s = len(encontraCaminho(nodev))
            print("Tempo de execução Hamming:", (time.time() - tempoDeInicio), "segundos") 
            print("Nodos expandidos:", totalExpandidos)
            caminho = encontraCaminho(nodev)
            print("Custo até a solução:", len(caminho))
            print("")
            return caminho 

def encontraCaminho(nodoMeta):
    caminho = []

    while nodoMeta.pai is not None:
        caminho.append(nodoMeta.acao)
        nodoMeta = nodoMeta.pai
    caminho.reverse()

    return caminho