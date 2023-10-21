"""
print("SISTEMA DE GESTÃO DE RESTAURANTES")

opcao_escolhida = None # variável global que será usada nas funções
lista_restaurantes = []


def tela_incial():  # funcao para a tela inicial do programa
        
        sinal = 0

        print(("""
        1 - Gestão de restaurantes
        2 - Gestão de cardápio
        3 - Visualizar informações (Restaurantes e cardápios)
        4 - Encerrar programa
        """))
        
        opcao_escolhida = int(input("Digite a opção desejada: "))
        
        if opcao_escolhida == 1: # compara a opção escolhida e seleciona a respectiva função
            sinal = gestao_restaurantes()
        
        elif opcao_escolhida == 2:
            gestao_cardapios()
        
        elif opcao_escolhida == 3:
            apresentacao_de_informacoes()

        elif opcao_escolhida == 4:  # opcao 4 encerra o programa
            condicao = False
            print("Encerrando programa")
            return condicao # retorna a condição False para sair do loop e encerrar o programa


def gestao_restaurantes_1(): 
    """Função menu de gerenciamento dos restaurantes"""
    
    sinal = 0
    while True:
        print(("""
        1 - Adicionar restaurante
        2 - Editar restaurante
        3 - Remover restaurante
        4 - Voltar para a tela inicial
        """))
        
        opcao()
            
        if opcao_escolhida == 1: # cada opçao escolhida encaminha para a respectiva funcao a ser criada
                sinal = 11
                #print("Adicionar restaurante") 
                #adicionar_restaurante()

        elif opcao_escolhida == 2:
                sinal = 12
                print("Editar restaurante")
            
        elif opcao_escolhida == 3:
                sinal = 13
                print("Remover restaurante")

        elif opcao_escolhida == 4:  # opcao 4 volta para tela inicial
                condicao = False
                sinal = 14
                print("Voltando para tela inicial")
                return condicao
        
        return sinal

def gestao_cardapios_1():
    while True:
        print(("""
        1 - Adicionar item ao cardápio
        2 - Editar item do cardápio
        3 - Remover item do cardápio
        4 - Voltar para a tela inicial
        """))
        
        opcao()
            
        if opcao_escolhida == 1: # cada opçao escolhida encaminha para a respectiva funcao a ser criada
                print("Adicionar item ao cardápio") 
            
        elif opcao_escolhida == 2:
                print("Editar item do cardápio")
            
        elif opcao_escolhida == 3:
                print("Remover item do cardápio")

        elif opcao_escolhida == 4:  # opcao 4 encerra o programa
                condicao = False
                print("Voltando para tela inicial")
                return condicao

def apresentacao_de_informacoes():
    while True:
        print(("""
        1 - Exibir lista de restaurantes
        2 - Voltar para a tela inicial
        """))
        
        opcao()
            
        if opcao_escolhida == 1: # cada opçao escolhida encaminha para a respectiva funcao a ser criada
                print("Exibir lista de restaurantes") 
                exibir_restaurantes()

        elif opcao_escolhida == 2:
                condicao = False
                print("Voltando para tela inicial")
                return condicao
"""        
def adicionar_restaurante():
        lista_restaurantes = []
        nome = input("Digite o nome do restaurante: ")
        lista_restaurantes.append(nome)
        telefone = input("Digite o telefone do restaurante: ")
        lista_restaurantes.append(telefone)
        print(lista_restaurantes)
        
        return lista_restaurantes

def exibir_restaurantes():
        print("Lista de restaurantes")


# aqui começamos a executar o programa 

tela_incial() # executa a tela inicial

