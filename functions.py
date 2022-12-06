import random

def sorteia_questao (D,N):
    Q = random.choice(D[N])
    return (Q)


def sorteia_questao_inedita(dict, nivel, lista):
    while True:
        questao = sorteia_questao(dict, nivel)
        if questao not in lista:
            lista.append(questao)
            break
    
    return questao

def transforma_base(lista):
    dicionario = {}
    lista_facil = []
    lista_medio = []
    lista_dificil = []
    for e in lista:
        if e['nivel'] =='facil':
            lista_facil.append(e)
            dicionario['facil'] = lista_facil
        elif e['nivel'] == 'medio':
            lista_medio.append(e)
            dicionario['medio'] = lista_medio
        else:
            lista_dificil.append(e)
            dicionario['dificil'] = lista_dificil
    return dicionario


def valida_questao(questao):
    saidas = {}
    saidas_opcoes = {}
    dificuldade = ['facil', 'medio' , 'dificil']
    respostas = ['A', 'B', 'C', 'D']

    if 'titulo' not in questao.keys():
        saidas['titulo'] = 'nao_encontrado'
    else:
        if questao['titulo'].strip() == '':
            saidas['titulo'] = 'vazio'     

    if 'nivel' not in questao.keys():
        saidas['nivel'] = 'nao_encontrado'
    else:
        if questao['nivel'] not in dificuldade:
            saidas['nivel'] = 'valor_errado'
    
    if 'opcoes' not in questao.keys():
        saidas['opcoes'] = 'nao_encontrado'
    else:
        if len(questao['opcoes'].keys()) != 4:
            saidas['opcoes'] = 'tamanho_invalido'
        else:
            for l, e in questao['opcoes'].items():
                if l in respostas:
                    if e.strip() == '':
                        saidas_opcoes[l] = 'vazia'
                        saidas['opcoes'] = saidas_opcoes 
                else:
                    saidas['opcoes'] = 'chave_invalida_ou_nao_encontrada'

                
    if 'correta' not in questao.keys():
        saidas['correta'] = 'nao_encontrado'
    else:
        if questao['correta'] not in respostas:
            saidas['correta'] = 'valor_errado'
    if len(questao.keys()) != 4:
        saidas['outro'] = 'numero_chaves_invalido'

    return saidas 


def valida_questoes(lista):
    retorno = {}
    lista_final = []
    num = 0
    for i in lista:
        num += 1
        retorno[num] = valida_questao(i)
        lista_final.append(retorno[num])
        
    return lista_final


def questao_para_texto (D,ID):
    return ("----------------------------------------"
    '\n'
    "QUESTAO {0}"
    '\n'
    '\n'
    "{1}"
    '\n'
    '\n'
    "RESPOSTAS:"
    '\n'
    "A: {2}"
    '\n'
    "B: {3}"
    '\n'
    "C: {4}"
    '\n'
    "D: {5}"
    '\n'
    ).format(ID,D["titulo"],D["opcoes"]["A"],D["opcoes"]["B"],D["opcoes"]["C"],D["opcoes"]["D"])


def gera_ajuda(x):
    incorreto = []
    correto = x['correta']
    opc = x['opcoes']
    for i in opc.keys():
        if i != correto:
            incorreto.append(i)
    num = random.randint(1, 2)
    if num == 1:
        ajuda = random.choice(incorreto)
        return 'DICA:\nOpções certamente erradas: {0}'.format(opc[ajuda])
    if num == 2:
        ajuda = random.choice(incorreto)
        incorreto.remove(ajuda)
        ajuda2 = random.choice(incorreto)
        return 'DICA:\nOpções certamente erradas: {0} e {1}'.format(opc[ajuda], opc[ajuda2])