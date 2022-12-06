#import
from functions import *
from lib_questoes import *
import sys
import time

questoes_ja_sorteadas = []
lista_premios = [0,1000,5000,10000,30000,50000,100000,300000,500000,1000000]
dinheiro = 0 
pulos = 3
ajudas = 2
id_questao = 1
acertos = 0
nivel = 0
participacao = True 
base = transforma_base(quest)

#Funcao pega no projeto deep sea adventure, para colocar slow entre os prints
def print_slow(str): 
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02) 

valido = valida_questoes(quest)
for questao in valido:
    if len(questao) != 0:
        print('ERRO: Base de questões tem erros')
        exit()

nome = input('Antes de começar fale seu nome: ')
print()
print_slow('\nBEM-VINDO JOGO DE PERGUNTAS E RESPOSTAS {0}'.format(nome.upper()))
print()
print_slow('\n-----------------\nREGRAS\n-----------------\n')
print()
print('Cada pergunta tem quatro alternativas: "A" , "B" , "C" , "D"\nVocê também tem direito a 2 "AJUDAS" , "PULAR" 3 vezes e "PARAR" de jogar')
print()
input('Aperte ENTER para continuar: ')
print()
print_slow('\nAgora que você conhece as regras:\n\nVAMOS COMEÇAR!')
print()
while participacao == True:
    if id_questao <= 3:
        nivel = 'facil' 
    elif id_questao <= 6:
        nivel = 'medio'
    else:
        nivel = 'dificil'
    questao = sorteia_questao_inedita(base,nivel,questoes_ja_sorteadas)
    questoes_ja_sorteadas.append(questao)
    print_slow(questao_para_texto(questao,id_questao))
    print()
    game = True # Variável pra loop de resposta
    while game == True:
        resposta = input('Qual é a sua resposta? ')
        resposta = resposta.upper()
        if resposta == questao['correta']:
            print_slow('E está... certa a resposta! Você agora tem {0} reais!'.format(lista_premios[dinheiro+1]))
            print()
            id_questao += 1
            dinheiro += 1
            acertos += 1
            input('Aperte ENTER para prosseguir com o jogo! ')
            game = False
            if resposta == questao['correta'] and id_questao == 10:
                print('Você ganhou o jogo! Parabéns!')
                participacao = False
        elif resposta == 'AJUDA':
            if ajudas > 0:
                ajuda = gera_ajuda(questao)
                ajudas -= 1
                print_slow(ajuda)
                print()
            else:
                print_slow('Você não tem mais ajudas disponíveis!')
                print()
        elif resposta == 'PULA':
            if pulos > 0:
                print_slow('Ok, questão pulada.')
                print()
                game = False
                pulos -= 1
            else:
                print_slow('Você não tem mais pulos disponíveis!')
                print()
        elif resposta == 'PARAR':
            print_slow('Você terminou o jogo com {0} reais, acertando {1} perguntas.'.format(dinheiro,acertos)) 
            print()           
            game = False
            participacao = False
        elif resposta in questao['opcoes']:
            print_slow('E está... errada a resposta! Você, então, sai com nada! Obrigado por jogar!')
            print()
            dinheiro = lista_premios[0]
            print_slow('Você terminou o jogo com {0} reais, acertando {1} perguntas.'.format(dinheiro,acertos))
            print()
            participacao = False
            game = False
        else:
            print('Comando não reconhecido, tente de novo.')