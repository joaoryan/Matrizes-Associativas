# Criando uma matriz associativa com chave sendo nome do aluno e o valor e a matricula
# Adicionando varios alunos
school = {'Zezinho': 5512, 'Mariazinho': 929, 'Joao': 239}
# Adicionando apenas um aluno
school['Marcelo'] = 523
print(school)

# Retornar apenas a matricula de um aluno
print(school['Joao'])

#Deletando um aluno
del school['Zezinho']
print(school)

# Criando uma lista e a ordenando
list(school)
print(sorted(school))

# Fazendo condicional 
if 'Joao' in school:
    print('Aluno existente')

if 'Joao' not in school:
    print('Aluno inexistente')
else:
    print('Aluno existente')