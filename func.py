##################### Restaurant func ###############
def add_restaurant():
    pass

def modify_restaurant():
    pass

def remove_restaurant():
    pass

def show_menu(restaurant):
    pass
    
#################### Menu func ##############

def add_item():
    pass

def edit_item():
    pass

def remove_item():
    pass

################## show info ################

def show_list_restaurant():
    pass

def show_describ_all_restaurant():
    pass

################ user interface #######



#0
def interface():  # funcao para a tela inicial do programa
    
    print(("""
    1 - Gestão de restaurantes
    2 - Gestão de cardápio
    3 - Visualizar informações (Restaurantes e cardápios)
    0 - Encerrar programa
    """))

    opc = input("\nOpção desejada: ") # chama a função de múltipla escolha

    if opc == '1': # compara a opção escolhida e seleciona a respectiva função
        opc = gestao_restaurantes() 

    elif opc == '2':
        opc = gestao_cardapios()

    elif opc == '3':
        opc = apresentacao_de_informacoes()

    elif opc == '0':  # opcao 4 encerra o programa, sempre que for voltar , recebe 4, se for encerrar recebe 0
        opc = '0'
        
    else:
        opc = '-1'
        
    return opc

#1
def gestao_restaurantes(): 
    """Função menu de gerenciamento dos restaurantes"""
    print(("""
    1 - Adicionar restaurante
    2 - Editar restaurante
    3 - Remover restaurante
    4 - Voltar para a tela inicial
    """))
    
    opc = input("\nOpção desejada: ")
        
    if opc == '1': # cada opçao escolhida encaminha para a respectiva funcao a ser criada
            opc =  '11'

    elif opc == '2':
            opc =  '12'
        
    elif opc == '3':
            opc = '13'

    elif opc == '4':  # opcao 4 volta pro menu incial
            opc = '4'
    else:
        opc = '-1'
        
    return opc
    
#2
def gestao_cardapios():
    
    print(("""
    1 - Adicionar item ao cardápio
    2 - Editar item do cardápio
    3 - Remover item do cardápio
    4 - Voltar para a tela inicial
    """))
    
    opc = input("\nOpção desejada: ")
        
    if opc == '1': # cada opçao escolhida encaminha para a respectiva funcao a ser criada
            opc = '21'
        
    elif opc == '2':
            opc = '22'
        
    elif opc == '3':
            opc = '23'

    elif opc == '4':  # opcao 4 voltar a primeira tela
        opc = '4'
    
    else:
        opc = '-1'
        
    return opc

#3
def apresentacao_de_informacoes():

    print(("""
    1 - Exibir lista de restaurantes
    2 - Voltar para a tela inicial
    """))
    
    opc = input("\nOpção desejada: ")
        
    if opc == '1': # cada opçao escolhida encaminha para a respectiva funcao a ser criada
            opc = '31'

    elif opc == '2':
            opc = '4'
            
    return opc
