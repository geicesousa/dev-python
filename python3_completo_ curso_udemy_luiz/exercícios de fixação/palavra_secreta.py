# usuário deve acertar a palavra
# ele vai digitar letra por letra
# a letra está na palavra? exiba a letra
# a letra não está, exibe * 
# só pode digitar um letra

# refact: alterar para uma lista e aplicar um random para selecionar uma aleatória

print('\nBem-vindo ao jogo! \nSerá que você consegue acertar a palavra?!?\n\t**********')

palavra_secreta = 'performace'

letras_acertadas = '' 
contador = 0

while True:

    letra_digitada = input('Digite uma letra: ').lower()

    if letra_digitada == '':
        print('Você precisa digitar uma letra') 
        continue

    if len(letra_digitada) > 1:
        print('Você deve digitar apenas uma letra') 
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
        contador +=1

    palavra_sendo_formada = ''
    for letra in palavra_secreta:    
        if letra in letras_acertadas:
            palavra_sendo_formada += letra
        else:
            palavra_sendo_formada += '*'
    
    print(palavra_sendo_formada)

    if palavra_sendo_formada == palavra_secreta:
        break

print(f'Você acertou a palavra {palavra_secreta.upper()} em {contador} tentativas.')
        