import os
contagem = 0
x = 1

# Remover o arquivo se existir
if os.path.exists('Lista.txt'):
    os.remove('Lista.txt')

# Perguntar quantas tarefas adicionar
numero_tarefas = int(input('Quantas tarefas você deseja adicionar? '))

# Verificar se o número de tarefas é positivo
if numero_tarefas > 0:
    open('Lista.txt', 'w').close()  # Criar um arquivo vazio
else:
    print('Não existem tarefas negativas ou nulas!')

# Função para adicionar tarefa ao arquivo
def adicionar_tarefa(tarefa):
    with open('Lista.txt', 'a') as lista:
        lista.write(f'{contagem + 1}° -> {tarefa}\n')

# Adicionar tarefas
for i in range(numero_tarefas):
    adicionar_tarefa(input(f'Digite a {i + 1}ª tarefa: ')) 
    contagem = contagem + 1

# Verificar o que o usuário quer 
questionamento = input('O que deseja no momento? ')

ver_tarefas = ['ver tarefas','verificar tarefas', ' olhar status', 'olhar tarefas','ver lista','olhar lista']
concluir_tarefas = ['riscar tarefa','concluir tarefa','marcar tarefa', 'concluida']




if (questionamento.lower() in ['ver tarefas','verificar tarefas', ' olhar status', 'olhar tarefas','ver lista','olhar lista']):
    with open('Lista.txt', 'r') as verificacao:
        for item in verificacao:
            print(item)
else:  
    x = 2
    for frases in concluir_tarefas:
        if questionamento.lower() in frases:
            if x == 2:
                qual_tarefa = input('Qual o numero da tarefa que deseja marcar como conlcuida? ')
                x = x + 1

                with open('Lista_temp.txt','w') as lista_temp:
                    lista_temp.truncate()

                with open('Lista.txt','r+') as conclusao, open('Lista_temp.txt','r+') as lista_temp:
                    linhas = conclusao.readlines()
                    conclusao.seek(0)

                    for linha in linhas:
                        if qual_tarefa in linha:
                            lista_temp.write(f'{linha.strip()} -- CONCLUIDA!\n')
                        else:
                            lista_temp.write(f'{linha}')
                os.replace('Lista_temp.txt','Lista.txt')


        
                            
                            
                           

                            
                    




   
                        
