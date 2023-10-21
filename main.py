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
        print("Adicionar restaurante")
        
    elif opc == '12':
        print("Editar restaurante")
        
    elif opc == '13':
        print("Remover restaurante")
        
    elif opc == '21':
        print("Adicionar item ao cardápio")
        
    elif opc == '22':
        print("Editar item do cardápio")
        
    elif opc == '23':
        print("Remover item do cardápio")
    
    elif opc == '31':
        print("Exibir lista de restaurantes")
        
    
        
print("\nSistema encerrado!")