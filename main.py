restaurants = []
menus = []
from func import *


opc = ''

while opc != '0' :
    
    opc = interface()
    #caso usuário escolha a opção 1 do menu
    if opc == '-1':
        # se for zero para o loop
        print("\nOpção invalida!\n")
    
    elif opc == '11':
        add_restaurant(restaurants)
        
    elif opc == '12':
        print("Editar restaurante")
        
    elif opc == '13':
        remove_restaurant(restaurants)
        
    elif opc == '21':
        add_item(restaurants)
        
    elif opc == '22':
        print("Editar item do cardápio")
        
    elif opc == '23':
        print("Remover item do cardápio")
    
    elif opc == '31':
        show_list_restaurant(restaurants)
        
    elif opc == '32':
        show_describ_all_restaurant(restaurants)
        
    
        
print("\nSistema encerrado!")