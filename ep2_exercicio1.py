def transforma_base(lista_questoes):
    dicio_retorno = {}

    for dicio in lista_questoes:
        nivel = dicio['nivel']
        
        if nivel not in dicio_retorno:

            dicio_retorno[nivel] = [dicio]
        else:
            dicio_retorno[nivel].append(dicio)
    
    return dicio_retorno

print(transforma_base([
  {
    'titulo': 'Qual o resultado da operação 57 + 32?',
    'nivel': 'facil',
    'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
    'correta': 'C'
  },
  {
    'titulo': 'Qual a capital do Brasil?',
    'nivel': 'facil',
    'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
    'correta': 'A'
  },
  {
    'titulo': 'Quem é considerada a primeira pessoa programadora do mundo?!',
    'nivel': 'medio',
    'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
    'correta': 'C'
  }
]))