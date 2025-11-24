import random
import string
import os

lista_final=[]
contagem=0

if os.path.exists('Senhas_gravadas.json'):
    with open('Senhas_gravadas.json', 'r') as arquivo:
        for linha in arquivo:
            lista_final.append(linha.strip())

while contagem!=10:
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
        if caractere_3 !=(';',':','~','{','}'):
            lista_final.append(caractere_3)
            contagem=contagem+1


serviço=input('digite o nome do serviço que usara a senha: ')
senha=''.join(lista_final)
with open ('Senhas_gravadas.json', 'w') as arquivo:
    arquivo.write(f'Service: {serviço}\nPassword: {senha}\n')