import random
import time

#criador de senha
n=random.randint(0,9)
alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','x','z']
caracteresEspeciais=['!','@','#','$','%','&',]
BancoDeSenhas=[]

print('Bem-vindo!')
while True:
    senhaCriada=[]
   
    continuar=str


    print('Escolha como a senha que você deseja criar deve ser composta:')

    print('Opção 1: SENHA NÚMERICA')
    print('Opção 2: SENHA ALFA-NUMERICA')
    print('Opção 3: SENHA ALFA-NUMERICA C/ CARACTERES ESPECIAIS')

    escolhaS=int(input('=>')) 
#usuário digita a opção que ele escolher: 01, 02 ou 03. 

    while escolhaS != 1 and escolhaS!= 2 and escolhaS!= 3:
        print("ERROR.c: 1312052119 _ 114418145") 
        print('por favor, escolha apenas as opções disponiveis:')
        escolhaS=int(input('1, 2 ou 3? => '))

#Se o usuário digita uma opção diferente de: 1,2 ou 3, o programa não o deixará prosseguir!.

    tamanho=int(input('Qual o tamanho você quer que tenha a senha?: '))
    while tamanho <4:
        print('Error.C: Tamanho invalido!')
        tamanho=int(input('DIGITE UM NOVO TAMANHO: '))

    if escolhaS == 1:
        for c in range (0,tamanho):
            n=random.randint(0,9)
            senhaCriada.append(n)
        print('Aguarde, gerando senha...')
        time.sleep(2)
        print(f'Senha Numerica criada com sucesso. A senha é: {senhaCriada}')
        BancoDeSenhas.append(senhaCriada[:])
        senhaCriada.clear()

        criarnova=input('Criar outra senha: [S/N]').upper()
        

    elif escolhaS == 2:
        if tamanho%2!=0:
            senhaCriada.append(random.choice(alfabeto))
        for c in range (0,tamanho//2):
            n=random.randint(0,9)
            senhaCriada.append(n)
            senhaCriada.append(random.choice(alfabeto).title())
        print('Aguarde, gerando senha...')
        time.sleep(2)
        print(f'Senha Alfa-Numerica criada com sucesso. A senha é: {senhaCriada}')
        BancoDeSenhas.append(senhaCriada[:])
        senhaCriada.clear()
        
        criarnova=input('Criar outra senha: [S/N]').upper()

    elif escolhaS == 3:
        
        for c in range (0,tamanho//2):
            n=random.randint(0,9)
            senhaCriada.append(n)
            senhaCriada.append(random.choice(caracteresEspeciais))
            senhaCriada.append((random.choice(alfabeto)))
        len(senhaCriada)
        while len(senhaCriada)> tamanho:
            senhaCriada.pop()
        print('Aguarde, gerando senha...')
        time.sleep(2)
        print(f'Senha Alfa-Numerica com caracteres especiais criada com sucesso. A senha é: {senhaCriada}')
        BancoDeSenhas.append(senhaCriada[:])
        senhaCriada.clear()
        
    criarnova=input('Criar outra senha: [S/N]').upper()

    while criarnova != "S" and criarnova!= "N":
        print("ERROR.c: 1312052119 _ 114418145") 
        criarnova=input('Criar outra senha: [S/N]').upper()

    if criarnova== "N":
        break
print('FIM!!')
print(f'o banco de senhas criado está a seguir:\n')
for senha in BancoDeSenhas:
    print(senha)