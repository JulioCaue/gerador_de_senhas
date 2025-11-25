import random
import string
import os
import json
from cryptography.fernet import Fernet

os.system('cls')  # Execute 'cls' command for Windows

#cria chave caso não haja, e a mostra para o usuario
if not os.path.exists('chave.key'):
    chave = Fernet.generate_key()
    with open('chave.key','wb') as chave_arquivo: 
        chave_arquivo.write(chave)
else:
    with open('chave.key','rb') as chave_arquivo:
        chave=chave_arquivo.read()

Senhas_gravadas={}

if os.path.exists('Senhas_gravadas.json'):
    with open('Senhas_gravadas.json', 'r') as arquivo:
        Senhas_gravadas=json.load(arquivo)


lista_final=[]
segurança=Fernet(chave)

#gera uma senha forte aleatoria de 12 caracteres
def gerar_senha():
    contagem=0
    while contagem!=12:
        numero=random.randint(1,3)

        if numero==1:
            caractere_1=random.choice(string.ascii_letters)
            lista_final.append(caractere_1)
            contagem=contagem+1
        elif numero ==2:
            caractere_2=random.choice(string.digits)
            lista_final.append(caractere_2)
            contagem=contagem+1
        else:
            caractere_3=random.choice(string.punctuation)
            if caractere_3 not in (';',':','~','{','}','>','<'):
                lista_final.append(caractere_3)
                contagem=contagem+1

while True:
    escolha_menu=input('Gerenciador de senhas\n\n1. Adiciona uma senha ao gerenciador\n2. Mostra senha nescessaria\n3. Sair\nEscolha uma opção: ')
    try:
        escolha_menu=int(escolha_menu)
    except:
        print('Escolha uma das opções.')

    try:
        if 0<int(escolha_menu)<=3:
            if escolha_menu==1:
                gerar_senha()
                #pede nome do serviço e retira virgulas da senha
                serviço=input('digite o nome do serviço que usara a senha: ')
                senha=''.join(lista_final)

                #transforma a senha em bytes e depois de volta em uma string
                senha=senha.encode('utf-8')
                senha=segurança.encrypt(senha)
                senha=senha.decode('utf-8')
                nova_senha=(serviço,senha)
                Senhas_gravadas[serviço]=senha


                #coloca tudo no json
                with open('Senhas_gravadas.json', 'w') as arquivo:
                    json.dump(Senhas_gravadas,arquivo,indent=4)

                #volta a lista ao estado inicial (vazio)
                lista_final=[]


            elif escolha_menu==2:
                os.system('cls')
                serviço_selecionado=input('Digite o nome do serviço: ')
                if serviço_selecionado in Senhas_gravadas:
                    resultado=Senhas_gravadas[f'{serviço_selecionado}']
                    print(f'Sua senha para {serviço_selecionado} é: {segurança.decrypt(resultado).decode()}')
                else:
                    print('Senha não exite.')
            else:
                break
        else:
            os.system('cls')
            print ('escolha uma opção do menu.')
    except:
        os.system('cls')
        print('escolha uma opção do menu.')