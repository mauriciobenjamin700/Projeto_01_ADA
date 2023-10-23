restaurants = []
# [[nome, cnpj,endereço, telefone, tempo de entrega, [[arroz, 10], [pão, 2], [coca, 10]] ] ]

from func import *


opc = ''
id = ''

while opc != '0':
    
    opc = interface()
    #caso usuário escolha a opção 1 do menu
    if opc == '-1':
        # se for zero para o loop
        print("\nOpção invalida!\n")
    
    elif opc == '11':
        add_restaurant(restaurants)
        
    elif opc == '12':
        modify_restaurant(restaurants)
        
    elif opc == '13':
        remove_restaurant(restaurants)
        
    elif opc == '21':
        add_item(restaurants)
        
    elif opc == '22':
        id = search_restaurant(restaurants)
        
        edit_item(restaurants, id)
        
    elif opc == '23':
        id = search_restaurant(restaurants)
        remove_item(restaurants, id)
    
    elif opc == '31':
        show_list_restaurant(restaurants)
        
    elif opc == '32':
        show_describ_all_restaurant(restaurants)
         
        
print("\nSistema encerrado!")