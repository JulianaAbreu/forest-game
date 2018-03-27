# -*- coding: utf-8 -*-
import time
import os

time.sleep(0.5)
word = "segredo"
secondWord = "comida"
treeWord = "familia"
secondWordGuesses = ''
treeWordGuesses = ''
fourWord = 'mente'
fourWordGuesses = ''
fiveWord = "mudar"
fiveWordGuesses = ''
guesses = ''
turnsFirst = 30
turnsSecond = 30
turnsTree = 30
turnsFour = 30
turnsFive = 30
pontuation = 5

print("BEM VINDO AO JOGO RPG - CACA PALAVRAS")
time.sleep(0.5)


option = str(input("Digite 1- Creditos 2- Como Jogar e 3- Iniciar jogo:"))


if '1' in option:
    os.system('clear')
    print("Juliana Cerqueira, TIA: 31894712")
    respOption = input("Deseja voltar para a tela inicial? ")

elif '2' in option:
    print("E um jogo de caca palavras, entre com letras ate que descubra a palavra secreta"
          " voce tem vidas e pontuacao para"
          "cada acerto. Boa sorte!")
    input("Deseja voltar para a tela inicial? ")

else:
    print("Iniciar jogo")
    name = str(input("Qual o seu nome? "))
    print("Oi, "+name, "quero te ajudar a sobreviver, você esta perdida(o)"+"\n"
                       "numa floresta, prestes a morrer. Cada erro no caca palavra sao"+"\n"+
                       "5 minutos a menos de vida. Mas se ganhar, você encontra o caminho de saida."+"\n"
                       "Tente sobreviver. Boa sorte!")


    while turnsFirst > 0 and turnsSecond > 0 and turnsTree > 0 and turnsFour > 0 and turnsFive > 0:
        failed = 0
        failed2 = 0
        failed3 = 0
        failed4 = 0
        failed5 = 0

        for char in word:
            if char in guesses:
                print(char)
            else:
                print("_")
                failed += 1
        if failed == 0:
            print("1° Etapa concluída. Você pode encontrar alimentos encima da arvore a sua esquerda")


            for secondChar in secondWord:
                if secondChar in guesses:
                    print(secondChar)
                else:
                    print("_")
                    failed2 += 1

            if failed2 == 0:
                print("2° Etapa concluída. Você pode encontrar alimentos encima da arvore a sua esquerda")
                break



        guess = input("Letra: ")
        guesses += guess

        if guess not in word and guess not in secondWord:
            turnsFirst -= 1
            print("wrong")
            print("Voce tem", +turnsFirst, 'chances nesta')

            if turnsFirst == 0:
                print("voce perdeu")