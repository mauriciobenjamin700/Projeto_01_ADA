# Lista de funções relacionadas ao gerenciamento de restaurantes

def add_restaurant(restaurants:list) -> None:
    """
    Função para adicionar um novo restaurante à lista de restaurantes.
    Recebe a lista de restaurantes e adiciona um novo restaurante.
    
    Parâmetros:
        restaurants::list: lista onde os restaraurantes serão armazenados
    return:
        None
    """
    # Solicitando ao usuário as informações do novo restaurante
    print('\nPreencha as informações do restaurante!\n')
    name = input('Nome: ').upper()
    cnpj = input('CNPJ: ')
    address = input('Endereço: ').upper()
    phone = input('Telefone: ')
    time = input('Tempo médio de entrega [Minutos]: ')
    menu = []
    
    # Adicionando o novo restaurante à lista
    restaurants.append([name, cnpj, address, phone, time, menu])
    print("Restaurante adicionado com sucesso!")

def search_restaurant(restaurants:list) -> int:
    """
    Função que busca um restaurante pelo nome ou CNPJ.
    
    Parâmetros:
        restaurants::list: lista de restaurantes
    Retorna:
        id: int (o índice do restaurante na lista ou -1 se não for encontrado.)
    """
    # Opções para o usuário escolher como quer buscar o restaurante
    opc = input('\nDeseja acessar por:\n\t1 - Nome do Restaurante\n\t2 - CNPJ do restaurante\n\nSua escolha: ')
    key = ''
    cont = 0
    id = -1

    # Obtendo a chave de pesquisa (nome ou CNPJ) com base na escolha do usuário
    if opc == '1':
        key = input('Nome do restaurante: ').upper()
    elif opc == '2':
        key = input('CNPJ do restaurante: ')
    
    # Continuando a busca do restaurante, a função retorna o índice do restaurante
    # ou -1 se não encontrá-lo na lista
    for restaurant in restaurants:
        if restaurant[int(opc)-1] == key:
            id = cont
            return id
        cont += 1
    return id
        
def modify_restaurant(restaurants:list) -> None:
    """
    Função para modificar informações de um restaurante existente.
    O usuário pode escolher qual campo deseja alterar.
    
    Parâmetros:
        restaurants::list: lista de restaurantes
    return:
        None
    """
    # Procurando o restaurante a ser modificado
    id = search_restaurant(restaurants)
    
    # Se o restaurante for encontrado
    if id != -1:
        # Solicitando ao usuário qual campo deseja modificar
        opc = input('\nQual campo deseja alterar?\n\t1 - Nome\n\t2 - CNPJ\n\t3 - Endereço\n\t4 - Telefone\n\t5 - Tempo médio de entrega\n\nSua escolha: ')
        
        # Verificando se a opção inserida é um número e está no intervalo correto
        if opc.isnumeric():
            opc = int(opc)
            
            if opc > 0 and opc < 6:
                # Solicitando ao usuário o novo valor para o campo escolhido
                data = input('\nInfome o novo valor para o respectivo campo: ')
                restaurants[id][opc-1] = data
                print("\nValor atualizado com sucesso!")
            else:
                print("\nOpção escolhida é invalida!")
        
        else:
            print("\nOpção Invalida, insira apenas números!")        
    else:
        print("\nRestaurante não encontrado!")

def remove_restaurant(restaurants:list) -> None:
    """
    Função para remover um restaurante da lista.
    Parâmetros:
        restaurants::list: lista de restaurantes
    return:
        None
    """
    # Procurando o restaurante a ser removido
    id = search_restaurant(restaurants)
    
    # Se o restaurante for encontrado, removendo-o da lista
    if id != -1:
        del restaurants[id]
        print("\nRestaurante removido!")
    else:
        print("\nRestaurante não encontrado!")

def show_menu(restaurants:list) -> None:
    """
    Função para exibir o menu de um restaurante.
    Parâmetros:
        restaurants::list: lista de restaurantes
    return:
        None
    """
    # Procurando o restaurante cujo menu será exibido
    id = search_restaurant(restaurants)
    
    # Se o restaurante for encontrado, imprimindo seu menu
    if id != -1:
        for item in restaurants[id][-1]:
            print(item)
            
    else:
        print("\nRestaurante não encontrado!")
    
#################### Menu func ##############

def add_item(restaurants:list) -> None:
    """
    Função para adicionar um novo item ao menu de um restaurante.
    Parâmetros:
        restaurants::list: lista de restaurantes
    
    return:
        None
    """
    # Procurando o restaurante ao qual o item será adicionado
    id = search_restaurant(restaurants)
    
    # Se o restaurante for encontrado
    if id != -1:
        # Solicitando ao usuário as informações do novo item
        print('\nInforme os dados do item: ')
        name = input('Nome: ').upper()
        valor = input('Preço: ')
        
        # Adicionando o novo item ao menu do restaurante
        restaurants[id][-1].append([name, valor])
        print("Item adicionado ao cardápio!")

    else:
        print("\nRestaurante não encontrado!")
        
def search_item(restaurants: list, id: int) -> int:
    """
    Função para pesquisar um item no menu de um restaurante específico.
    
    Parâmetros:
        restaurants::list: Lista de todos os restaurantes.
        id:int: Índice do restaurante em que se deseja buscar o item.
    
    return: 
        idx::int: índice do item encontrado ou -1 se não encontrar.
    """
    cont = 0  # Inicializando um contador.
    idx = -1  # Inicializando o índice de retorno com -1 (item não encontrado).
    
    # Verifica se o ID fornecido é válido
    if id != -1:
        # Solicita ao usuário o nome do produto que deseja buscar
        name = input('\nNome do produto: ').upper()
        
        # Procura o produto no menu do restaurante especificado
        for item in restaurants[id][-1]:
            if item[0] == name:
                idx = cont  # Atribui o valor do contador ao índice de retorno
                return idx
            cont += 1  # Incrementa o contador
         
    return idx

def edit_item(restaurants: list, id: int) -> None:
    """
    Função para editar informações de um item em um restaurante específico.
    
    Parâmetros:
        restaurants::list: lista de restaurantes
        id::int: identificação do restaurante, sendo ela a posição que o mesmo se encontra na lista
    
    return:
        None
    """
    # Procura o índice do item que será editado
    idx = search_item(restaurants, id)
    
    # Se o item for encontrado
    if idx != -1:
        # Solicita ao usuário qual campo do item deseja alterar
        opc = input('\nQual campo deseja alterar?\n\t1 - Nome\n\t2 - Preço\n\nSua escolha: ')
        
        # Verifica se a entrada é numérica e se está no intervalo correto
        if opc.isnumeric():
            opc = int(opc)
            if opc > 0  and opc < 3:
                # Solicita ao usuário o novo valor para o campo escolhido
                data = input('\nInfome o novo valor para o respectivo campo: ')
                # Atualiza o valor do campo escolhido no item
                restaurants[id][-1][idx][opc-1] = data
            else:
                print("\nOpção escolhida é invalida")
        else:
            print("\nInforme um valor númerico!")
                
    else:
        print("\nRestaurante não encontrado!")
        
def remove_item(restaurants: list, id: int) -> None:
    """
    Função para remover um item do menu de um restaurante específico.
    
    Parâmetros:
        restaurants::list: lista de restaurantes
        id::int: indice do item que se deseja remover
    
    return:
        None
    
    """
    # Procura o índice do item que será removido
    idx = search_item(restaurants, id)
    
    # Se o item for encontrado, remove-o da lista
    if idx != -1:
        del restaurants[id][-1][idx]
        
    else:
        print("\nRestaurante não encontrado!")

################## show info ################

def show_restaurant(restaurant:list) -> None:
    """
    Exibe os dados de um restaurante.
    
    Parâmetros:
        restaurants::list: lista de restaurantes
        
    return:
        None
    
    """

    print(f'\n\tNome: {restaurant[0]}\n\tCNPJ: {restaurant[1]}\n\tEndereço: {restaurant[2]}\n\tTelefone: {restaurant[3]}\n\tTempo médio para um entrega: {restaurant[4]}')


def show_list_restaurants(restaurants:list):
    """
    Exibe uma lista de restaurantes cadastrados.
    
    Parâmetros:
        restaurants::list: lista de restaurantes
        
    return:
        None
    
    """
    if len(restaurants) > 0:
        # Imprime o cabeçalho para a lista de restaurantes cadastrados.
        print('\nRestaurantes Cadastrados: ')
        
        # Percorre cada restaurante na lista fornecida.
        for restaurant in restaurants:
            # Imprime os detalhes do restaurante de forma formatada.
            show_restaurant(restaurant)
    
    else:
        print("\nNão há restaurantes cadastrados no sistema")
        
def show_describ_all_restaurants(restaurants: list) -> None:
    """
    Exibe uma descrição detalhada de cada restaurante cadastrado, incluindo os itens do menu.
    
    Parâmetros:
        restaurants::list: lista de restaurantes
        
    return:
        None
    """
    if len(restaurants) > 0:
        # Imprime o cabeçalho para a lista de restaurantes cadastrados.
        print('\nRestaurantes Cadastrados: ')
        
        # Percorre cada restaurante na lista fornecida.
        for restaurant in restaurants:
            # Imprime os detalhes do restaurante de forma formatada.
            show_restaurant(restaurant)
            
            # Verifica se o restaurante possui itens no menu.
            if len(restaurant[-1])>0:
                # Imprime o cabeçalho para a lista de produtos disponíveis do restaurante.
                print('Produtos Disponiveis: ')
                
                # Percorre cada item no menu do restaurante.
                for item in restaurant[-1]:
                    # Imprime os detalhes do item de forma formatada.
                    print(f'\n\t| {item[0]} | R${item[1]},00 |')
            else:
                print("\nNão há itens disponiveis no cardapio ainda!")
    else:
        print("\nNão há restaurantes cadastrados no sistema")

def low_time(restaurants:list) -> int:
    """
    Função responsavel por análisar todos os restaurantes disponiveis na plataforma e
    retornar o restaurante com o menor tempo de entrega.
    função retorna -1 caso não encontre.
    
    Parâmetros:
        restaurants::list: Lista contendo todos os restaurantes cadastrados na plataforma.
        
    Retorna:
        id::int: identificação da posição que o restaurante adequada se encontra caso existir
    """
    
    id = -1
    
    if len(restaurants) == 0:
        print("\nNão há restaurantes cadastrados na plataforma")
        
    elif len(restaurants) == 1:
        id+=1
    
    else:
        
        maior = int(restaurants[0][4])
    
        for restaurant in restaurants:
            id+=1
        
            if int(restaurant[4]) > maior:
                maior = int(restaurant[4])
        
    return id
################ user interface #######

# Função principal da interface do programa
def interface() -> int:
    """
    Função responsavel por interagir com o usuário e descobrir o que ele deseja fazer.
    A mesma aciona outros submenus para mostrar opções para o usuário
    
    Parâmetros:
        None
    Retorna:
        opc::int: identificação da operação que será realizada
    """  
    # Exibe as opções da tela inicial
    print(('''
                            INICIO
    |-------------------------------------------------------|
    | 1 - Gestão de restaurantes                            |
    | 2 - Gestão de cardápio                                |
    | 3 - Visualizar informações (Restaurantes e cardápios) |
    | 0 - Encerrar programa                                 |
    |------------------------------------------------------ |
    '''))

    # Solicita que o usuário insira a opção desejada
    opc = input('\nOpção desejada: ')

    # Verifica qual a opção escolhida pelo usuário e redireciona para a função correspondente
    if opc == '1':
        opc = gestao_restaurantes() 
    elif opc == '2':
        opc = gestao_cardapios()
    elif opc == '3':
        opc = apresentacao_de_informacoes()
    elif opc == '0':
        opc = '0'
    else:
        opc = '-1'
        
    return opc

# Função que exibe o menu de gerenciamento dos restaurantes
def gestao_restaurantes() -> int:
    """
    Função responsavel por interagir com o usuário e descobrir o que ele deseja fazer.

    Parâmetros:
        None
    Retorna:
        opc::int: identificação da operação que será realizada
    """  
    print(('''
                    GESTAO DE RESTAURANTES
    |-------------------------------------------------------|
    | 1 - Adicionar restaurante                             |
    | 2 - Editar restaurante                                |
    | 3 - Remover restaurante                               |
    | 4 - Voltar para a tela inicial                        |
    |------------------------------------------------------ |
    '''))
     
    opc = input('\nOpção desejada: ')

    # Redireciona o usuário com base na sua escolha
    if opc == '1':
        opc =  '11'
    elif opc == '2':
        opc =  '12'
    elif opc == '3':
        opc = '13'
    elif opc == '4':
        opc = '4'
    else:
        opc = '-1'
        
    return opc
    
# Função que exibe o menu de gerenciamento do cardápio
def gestao_cardapios() -> int:   
    """
    Função responsavel por interagir com o usuário e descobrir o que ele deseja fazer.

    Parâmetros:
        None
    Retorna:
        opc::int: identificação da operação que será realizada
    """ 
    print(('''
                        GESTAO DE CARDAPIO
    |-------------------------------------------------------|
    | 1 - Adicionar item ao cardápio                        |
    | 2 - Editar item do cardápio                           |
    | 3 - Remover item do cardápio                          |
    | 4 - Voltar para a tela inicial                        |
    |------------------------------------------------------ |
    '''))
    
    
    opc = input('\nOpção desejada: ')

    # Redireciona o usuário com base na sua escolha
    if opc == '1':
        opc = '21'
    elif opc == '2':
        opc = '22'
    elif opc == '3':
        opc = '23'
    elif opc == '4':
        opc = '4'
    else:
        opc = '-1'
        
    return opc

# Função que exibe as opções para visualização de informações dos restaurantes
def apresentacao_de_informacoes() -> int:
    """
    Função responsavel por interagir com o usuário e descobrir o que ele deseja fazer.

    Parâmetros:
        None
    Retorna:
        opc::int: identificação da operação que será realizada
    """
    print(('''
                    VISUALIZAR INFORMACOES
    |-------------------------------------------------------|
    | 1 - Exibir lista de restaurantes                      |
    | 2 - Exibir detalhadamente cada restaurante            |
    | 3 - Exibir restaurante com o menor tempo de entrega   |
    | 4 - Voltar para a tela inicial                        |
    |------------------------------------------------------ |
    '''))
    
    opc = input('\nOpção desejada: ')

    # Redireciona o usuário com base na sua escolha
    if opc == '1':
        opc = '31'
    elif opc == '2':
        opc = '32'
    elif opc == '3':
        opc = '33'
    elif opc == '4':
        opc = '4'
            
    return opc

