

# pedra papel e tesoura

import random

score_user = 0
score_maqui = 0

while True:
    lista_maquina =  ['pedra', 'papel', 'tesoura']
    escolha_maqui  =  random.choice(lista_maquina)
    escolha_usuario = input('Escolha: pedra, papel ou tesoura >> ')

    if escolha_maqui == escolha_usuario:
        
        print('Empate')
        print('MAQUINA ESCOLHEU: ', escolha_maqui)
        print('Pontos da máquina: ', score_maqui)
        print('O USUARIO ESCOLHEU: ', escolha_usuario)
        print('Pontos so usuario(a) ', score_user)
        
    elif escolha_maqui == 'pedra' and  escolha_usuario == 'tesoura':    
        print('A maquina ganhou *.*')
        score_maqui =  score_maqui + 1 
        print('MAQUINA ESCOLHEU: ', escolha_maqui)
        print('Pontos da máquina: ', score_maqui)
        print('O USUARIO ESCOLHEU: ', escolha_usuario)
        print('Pontos so usuario(a) ',score_user)

    elif escolha_maqui == 'tesoura' and  escolha_usuario == 'papel':    
        print('A maquina ganhou *.*')
        score_maqui =  score_maqui + 1 
        print('MAQUINA ESCOLHEU: ', escolha_maqui)
        print('Pontos da máquina: ', score_maqui)
        print('O USUARIO ESCOLHEU: ', escolha_usuario)
        print('Pontos so usuario(a) ', score_user)

    elif escolha_maqui == 'papel' and  escolha_usuario == 'pedra':    
        print('A maquina ganhou *.*')
        score_maqui =  score_maqui + 1 
        print('MAQUINA ESCOLHEU: ', escolha_maqui)
        print('Pontos da máquina: ', score_maqui)
        print('O USUARIO ESCOLHEU: ', escolha_usuario)
        print('Pontos so usuario(a) ', score_user)
        
# usuario        
        
    elif escolha_maqui == 'tesoura' and  escolha_usuario == 'pedra':    
        print('O usuário ganhou *.*')
        score_user =  score_user + 1 
        print('MAQUINA ESCOLHEU: ', escolha_maqui)
        print('Pontos da máquina: ', score_maqui)
        print('O USUARIO ESCOLHEU: ', escolha_usuario)
        print('Pontos so usuario(a) ',score_user)

    elif escolha_maqui == 'papel' and  escolha_usuario == 'tesoura':    
        print('O usuário ganhou *.*')
        score_user =  score_user + 1 
        print('MAQUINA ESCOLHEU: ', escolha_maqui)
        print('Pontos da máquina: ', score_maqui)
        print('O USUARIO ESCOLHEU: ', escolha_usuario)
        print('Pontos so usuario(a) ', score_user)

    elif escolha_maqui == 'pedra' and  escolha_usuario == 'papel':    
        print('O usuário ganhou *.*')
        score_user =  score_user + 1 
        print('MAQUINA ESCOLHEU: ', escolha_maqui)
        print('Pontos da máquina: ', score_maqui)
        print('O USUARIO ESCOLHEU: ', escolha_usuario)
        print('Pontos so usuario(a) ', score_user)        
        
        
    else:
        print('DIGITE ALGO VALIDO')
  
        
