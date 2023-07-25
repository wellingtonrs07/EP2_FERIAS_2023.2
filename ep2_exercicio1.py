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
    novas_sorteadas = sorteadas
    lista_nivel = []
    for dif, questao in questoes.items():
        if dif == nivel:
            for elemento in questao:
                lista_nivel.append(elemento)
    sorteada = rd.choice(lista_nivel)
    if sorteada not in novas_sorteadas:
        novas_sorteadas.append(sorteada)
    return sorteada

#Questao 6
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
id = 5
def questao_para_texto(questao, id):

