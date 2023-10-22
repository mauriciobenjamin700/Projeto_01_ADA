##################### Restaurant func ###############
def add_restaurant(restaurants:list):
    print("\nPreencha as informações do restaurante!\n")
    name = input("Nome: ")
    cnpj = input("CNPJ: ")
    address = input("Endereço: ")
    phone = input("Telefone: ")
    time = input("Tempo médio de entrega: ")
    menu = []
    
    restaurants.append([name,cnpj,address,phone, time,menu])

def search_restaurant(restaurants:list):
    opc = input("\nDeseja acessar por:\n\t1 - Nome do Restaurante\n\t2 - CNPJ do restaurante\n\nSua escolha: ")
    key = ''
    id = -1
    if opc == '1':
        key = input("Nome do restaurante: ")
    elif opc == '2':
        key = input("CNPJ do restaurante: ")
    
    for restaurant in restaurants:
        id += 1
        if restaurant[int(opc)-1] == key:
            break
        
    return id
            
        
def modify_restaurant():
    pass

def remove_restaurant(restaurants):
    id = search_restaurant(restaurants)
    
    if id != -1:
        del restaurants[id]
        

def show_menu(restaurants):
    id = search_restaurant(restaurants)
    
    if id != -1:
        for iten in restaurants[id][-1]:
            print(iten)
    
#################### Menu func ##############

def add_item(restaurants):
    id = search_restaurant(restaurants)

    
    if id != -1:
        print("\nInforme os dados do item:")
        name = input("Nome: ")
        valor = input("Preço: ")
        
        restaurants[id][-1].append([name, valor])


def edit_item():
    pass

def remove_item():
    pass

################## show info ################

def show_list_restaurant(restaurants:list):
    print("\nRestaurantes Cadastrados: ")
    for restaurant in restaurants:
        print(f"\n\tNome: {restaurant[0]}\n\tCNPJ: {restaurant[1]}\n\tEndereço: {restaurant[2]}\n\tTelefone: {restaurant[3]}\n\tTempo médio para um entrega: {restaurant[4]}")

def show_describ_all_restaurant(restaurants:list):
    print("\nRestaurantes Cadastrados: ")
    for restaurant in restaurants:
        print(f"\n\tNome: {restaurant[0]}\n\tCNPJ: {restaurant[1]}\n\tEndereço: {restaurant[2]}\n\tTelefone: {restaurant[3]}\n\tTempo médio para um entrega: {restaurant[4]}\n")
        if len(restaurant[-1])>0:
            print("Produtos Disponiveis: ")
            for item in restaurant[-1]:
                print(f"\n\t{item[0]} custando R$ {item[1]} ")

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
    2 - Exibir detalhadamente cada restaurante
    3 - Voltar para a tela inicial
    """))
    
    opc = input("\nOpção desejada: ")
        
    if opc == '1': # cada opçao escolhida encaminha para a respectiva funcao a ser criada
            opc = '31'
    elif opc == '2': # cada opçao escolhida encaminha para a respectiva funcao a ser criada
            opc = '32'

    elif opc == '3':
            opc = '4'
            
    return opc