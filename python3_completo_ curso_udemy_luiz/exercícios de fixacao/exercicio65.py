nome = 'Geice'
i = 0
asterisco = '*'
new_name = ''
while i < len(nome):
    
    print(asterisco + nome[i] + asterisco)
    i += 1

#for
for letter in nome:
    all_letters = f'*{letter}'
    new_name += all_letters

print(new_name)



