# Lista que armazena os restaurantes.
restaurants = []
# Estrutura da lista: [[nome, cnpj, endereço, telefone, tempo de entrega, [[produto1, preço1], [produto2, preço2], ...]]]

# Importando todas as funções do módulo func.
from func import *

# Inicializando variáveis.
opc = '' # Opção selecionada pelo usuário.
id = '' # ID do restaurante.

# Loop principal do programa.
while opc != '0':
    
    # Solicita a interface do menu ao usuário.
    opc = interface()

    # Verifica a opção escolhida pelo usuário.
    if opc == '-1':
        # Mostra mensagem de opção inválida se o usuário inserir uma opção não reconhecida.
        print('\nOpção invalida!\n')
    
    # Caso o usuário escolha adicionar um restaurante.
    elif opc == '11':
        add_restaurant(restaurants)

    # Caso o usuário escolha modificar um restaurante.    
    elif opc == '12':
        modify_restaurant(restaurants)

    # Caso o usuário escolha remover um restaurante.    
    elif opc == '13':
        remove_restaurant(restaurants)

    # Caso o usuário escolha adicionar um item ao cardápio.    
    elif opc == '21':
        add_item(restaurants)

    # Caso o usuário escolha editar um item do cardápio.    
    elif opc == '22':
        # Busca o ID do restaurante selecionado.
        id = search_restaurant(restaurants)

        # Edita o item do cardápio do restaurante selecionado.
        edit_item(restaurants, id)

    # Caso o usuário escolha remover um item do cardápio.    
    elif opc == '23':
        # Busca o ID do restaurante selecionado.
        id = search_restaurant(restaurants)

        # Remove o item do cardápio do restaurante selecionado.
        remove_item(restaurants, id)
    
    # Caso o usuário escolha exibir a lista de restaurantes.
    elif opc == '31':
        show_list_restaurant(restaurants)

    # Caso o usuário escolha exibir detalhes de todos os restaurantes.    
    elif opc == '32':
        show_describ_all_restaurant(restaurants)

# Mensagem exibida ao encerrar o sistema.         
print('\nSistema encerrado!')