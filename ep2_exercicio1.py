
#QUESTAO 1

def transforma_base(lista_questoes):
    dicio_retorno = {}

    for dicio in lista_questoes:
        nivel = dicio['nivel']
        
        if nivel not in dicio_retorno:

            dicio_retorno[nivel] = [dicio]
        else:
            dicio_retorno[nivel].append(dicio)
    
    return dicio_retorno

# QUESTAO 2
def valida_questao(questao):
    retorno = {}

    #verificar a quantidade de chaves
    qnt_chaves = len(questao.keys())

    if qnt_chaves != 4:
        retorno['outro'] = 'numero_chaves_invalido'
    

    #caso para o titulo inexistente
    if 'titulo' not in questao:
        retorno['titulo'] = 'nao_encontrado'
    
    else:
        #caso titulo existente, porem vazio
        if questao['titulo'].strip() == '':
        
            retorno['titulo'] = 'vazio'

    #verificacao do nivel
    if 'nivel' in questao:
        if questao['nivel'] != 'facil' and questao['nivel'] != 'medio' and questao['nivel'] != 'dificil':
            retorno['nivel'] = 'valor_errado'
        
    else:
        retorno['nivel'] = 'nao_encontrado'
    
    #verificacao de opções
    if 'opcoes' in questao:
        qnt_opcoes = len(questao['opcoes'].keys())

        if qnt_opcoes != 4: 
            retorno['opcoes'] = 'tamanho_invalido'

        #verificando se há 4 respostas
        elif 'A' not in questao['opcoes'] or 'B' not in questao['opcoes'] or 'C' not in questao['opcoes'] or 'D' not in questao['opcoes']:
            retorno['opcoes'] = 'chave_invalida_ou_nao_encontrada'
           

        else:
             #verificando se há resp vazias
            for alternativa, respostas in questao['opcoes'].items():
                if respostas.strip() == '':
                    questao['opcoes'][alternativa] = 'vazia'

                    if 'opcoes' not in retorno:
                        retorno['opcoes'] = {alternativa: questao['opcoes'][alternativa]}
                    
                    else:
                        retorno['opcoes'][alternativa] = questao['opcoes'][alternativa]

    else:
        retorno['opcoes'] = 'nao_encontrado'
    
    #verificando o gabarito
    if 'correta' in questao:
        if questao['correta'] != 'A' and questao['correta'] != 'B' and questao['correta'] != 'C' and questao['correta'] != 'D':
           retorno['correta'] = 'valor_errado'
    
    else:
        retorno['correta'] = 'nao_encontrado'
    
    return retorno

#QUESTAO 3

def valida_questoes(lista_questoes):
    lista_retorno = []
    

    for questao in lista_questoes:
        retorno = {}
        #verificar a quantidade de chaves
        qnt_chaves = len(questao.keys())

        if qnt_chaves != 4:
            retorno['outro'] = 'numero_chaves_invalido'
        

        #caso para o titulo inexistente
        if 'titulo' not in questao:
            retorno['titulo'] = 'nao_encontrado'
        
        else:
            #caso titulo existente, porem vazio
            if questao['titulo'].strip() == '':
            
                retorno['titulo'] = 'vazio'

        #verificacao do nivel
        if 'nivel' in questao:
            if questao['nivel'] != 'facil' and questao['nivel'] != 'medio' and questao['nivel'] != 'dificil':
                retorno['nivel'] = 'valor_errado'
            
        else:
            retorno['nivel'] = 'nao_encontrado'
        
        #verificacao de opções
        if 'opcoes' in questao:
            qnt_opcoes = len(questao['opcoes'].keys())

            if qnt_opcoes != 4: 
                retorno['opcoes'] = 'tamanho_invalido'

            #verificando se há 4 respostas
            elif 'A' not in questao['opcoes'] or 'B' not in questao['opcoes'] or 'C' not in questao['opcoes'] or 'D' not in questao['opcoes']:
                retorno['opcoes'] = 'chave_invalida_ou_nao_encontrada'
            

            else:
                #verificando se há resp vazias
                for alternativa, respostas in questao['opcoes'].items():
                    if respostas.strip() == '':
                        questao['opcoes'][alternativa] = 'vazia'

                        if 'opcoes' not in retorno:
                            retorno['opcoes'] = {alternativa: questao['opcoes'][alternativa]}
                        
                        else:
                            retorno['opcoes'][alternativa] = questao['opcoes'][alternativa]

        else:
            retorno['opcoes'] = 'nao_encontrado'
        
        #verificando o gabarito
        if 'correta' in questao:
            if questao['correta'] != 'A' and questao['correta'] != 'B' and questao['correta'] != 'C' and questao['correta'] != 'D':
                retorno['correta'] = 'valor_errado'
        
        else:
            retorno['correta'] = 'nao_encontrado'
        
        lista_retorno.append(retorno)
    
    return lista_retorno

#QUESTAO 4
import random
def sorteia_questao(questoes, nivel):

    #criando uma lista com o nivel pedido
    lista_questoes_por_dificuldade = []

    for dificuldade, lista_questao in questoes.items():
        for questao in lista_questao:
            if dificuldade == nivel:

                lista_questoes_por_dificuldade.append(questao)

    #sorteando um indice da lista
    indice_sorteado= random.randint(0, len(lista_questoes_por_dificuldade)-1)
    questao_sorteada = lista_questoes_por_dificuldade[indice_sorteado]

    return questao_sorteada

#QUESTÃO 5
import random as rd
def sorteia_questao_inedita(questoes,nivel,sorteadas):
    novas_sorteadas = sorteadas   # Faz uma cópia da lista 'sorteadas'
    lista_nivel = []
    # Percorre as questões do nível especificado (nivel) no dicionário 'questoes'
    for dif, questao in questoes.items():
        if dif == nivel:
            for elemento in questao:
                lista_nivel.append(elemento) # Adiciona as questões do nível à lista 'lista_nivel'
    sorteada = rd.choice(lista_nivel)  # Escolhe aleatoriamente uma questão do nível da lista 'lista_nivel'
    if sorteada not in novas_sorteadas:  # Verifica se a questão sorteada não está na lista de questões já sorteadas
        novas_sorteadas.append(sorteada)  # Se não estiver, adiciona a questão sorteada à lista de questões sorteadas
    return sorteada # Retorna a questão sorteada (ou None se todas as questões já foram sorteadas anteriormente)

#Questao 6
questao = {
  "titulo": 'Qual o resultado da operação 57 + 32?',
  "nivel": "facil",
  "opcoes": {
    "A": "-19",
    "B": "85",
    "C": "89",
    "D": "99"
  },
  "correta": "D"
}
id = 17
def questao_para_texto(questao, id):
    # Montar a string formatada da questão
    final = f"----------------------------------------\nQUESTAO {id}\n\n{questao['titulo']}\n\nRESPOSTAS:\n"
    
    # Obter a lista de opções e a opção correta
    opcoes = questao['opcoes']
    # Adicionar as opções formatadas à string
    for letra, opcao in opcoes.items():
        final += f"{letra}: {opcao}\n"
    # Retornar a string formatada
    return final

print(questao_para_texto(questao,id))

#Questao 7
import random as rd
questao = {
  "titulo": "Qual destes parques não se localiza em São Paulo?!",
  "nivel": "facil",
  "opcoes": {
    "A": "Ibirapuera",
    "B": "Parque do Carmo",
    "C": "Parque Villa Lobos",
    "D": "Morro da Urca"
  },
  "correta": "D"
}
import random as rd

def gera_ajuda(questao):
    l = []
    opcoes = questao['opcoes']

    # Percorre todas as opções do dicionário 'opcoes'
    for k, v in opcoes.items():
        if k != questao['correta']:
            l.append(v)  # Adiciona as opções erradas à lista 'l'

    qtd = rd.randint(1, 2)  # Gera um número aleatório entre 1 e 2

    if qtd == 1:
        x = rd.choice(l)  # Escolhe aleatoriamente uma opção errada da lista 'l'
        return f"DICA:\nOpções certamente erradas: {x}"
    elif qtd == 2:
        x = rd.choice(l)  # Escolhe aleatoriamente uma opção errada da lista 'l'
        l.remove(x)  # Remove a opção escolhida para não ser selecionada novamente
        y = rd.choice(l)  # Escolhe outra opção errada da lista 'l'
        return f"DICA:\nOpções certamente erradas: {x} | {y}"

def junta_game(questoes):
  dinheiro_inicial = 1000
  nome_jogador = input('Informe seu nome:')

  jogando = True

  while jogando == True:
    print('O jogo já vai começar! Lá vem a primeira questão!')                           
                                                                                
    print('Vamos começar com questões do nível {nivel}!') 

