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

questoes = {
  "facil": [
    {
      "titulo": "Qual o resultado da operação 57 + 32?",
      "nivel": "facil",
      "opcoes": {
        "A": "-19",
        "B": "85",
        "C": "89",
        "D": "99"
      },
      "correta": "C"
    },
    {
      "titulo": "Qual destes parques não se localiza em São Paulo?!",
      "nivel": "facil",
      "opcoes": {
        "A": "Ibirapuera",
        "B": "Parque do Carmo",
        "C": "Parque Villa Lobos",
        "D": "Morro da Urca"
      },
      "correta": "D"
    },
    {
      "titulo": "Qual destas não é uma linguagem de programação?",
      "nivel": "facil",
      "opcoes": {
        "A": "Miratdes",
        "B": "Python",
        "C": "Lua",
        "D": "C++"
      },
      "correta": "A"
    },
    {
      "titulo": "Dentre os listados, qual destes esportes é menos praticado no Brasil?",
      "nivel": "facil",
      "opcoes": {
        "A": "Natação",
        "B": "Vôlei",
        "C": "Ski Cross Country",
        "D": "Natação"
      },
      "correta": "C"
    }
  ],
  "medio": [
    {
      "titulo": "Qual destes números é primo?",
      "nivel": "medio",
      "opcoes": {
        "A": "259",
        "B": "85",
        "C": "49",
        "D": "19"
      },
      "correta": "D"
    },
    {
      "titulo": "Na Conjectura de _______, escolhendo-se um número natural inicial n, onde n > 0, os seguintes critérios serão obedecidos: Se n for par o seu sucessor será a metade e se n for ímpar o seu sucessor será o triplo mais um, gerando então um novo número. Qual o nome da conjectura?",
      "nivel": "medio",
      "opcoes": {
        "A": "Collatz",
        "B": "Goldbach",
        "C": "Poincaré",
        "D": "Hodge"
      },
      "correta": "A"
    },
    {
      "titulo": "Qual a segunda pessoa mais seguida no Instagram?",
      "nivel": "medio",
      "opcoes": {
        "A": "Cristiano Ronaldo",
        "B": "Dwayne Johnson",
        "C": "Kim Kardashian",
        "D": "Kylie Jenner"
      },
      "correta": "D"
    }
  ],
  "dificil": [
    {
      "titulo": "A reprodução dos seres vivos é um processo biológico através do qual os organismos geram descendência. Qual desta não é uma forma de reprodução assexuada?",
      "nivel": "dificil",
      "opcoes": {
        "A": "Autogamia",
        "B": "Esporulação",
        "C": "Partenogênese",
        "D": "Divisão binária"
      },
      "correta": "A"
    },
    {
      "titulo": "Qual o resultado da operação 5 + 2 * 3 ^ 2, onde ^ representa potenciação?",
      "nivel": "dificil",
      "opcoes": {
        "A": "441",
        "B": "86",
        "C": "Nenhuma das outras respostas",
        "D": "23"
      },
      "correta": "D"
    }
  ]
}

nivel = 'facil'

print(sorteia_questao(questoes, nivel))