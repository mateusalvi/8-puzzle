import nodo

def main(): 
    raiz = nodo.Nodo        #cria um novo nodo
    
    raiz.estado = raizInput()
    nodo.sucessor(raiz.estado)


#raizInput faz uma checagem para o tamanho da string de entrada, sem checar se é semanticamente válida
#depois podemos generalizar melhor essa função
def raizInput():
    entradaCorreta = False
    while entradaCorreta == False:
        entrada = None
        print("Entre com o nodo inicial, por exemplo 1_3452867, com exatamente 9 caracteres")
        entrada = input()
        if (len(entrada) != 9):
            print("Entrada de tamanho incorreto.")
        else:
            entradaCorreta = True
            return entrada


if __name__ == "__main__":
    main()