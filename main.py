# -*- coding: utf-8 -*-
import time
import os

time.sleep(0.5)


treeWord = "familia"
secondWordGuesses = ''
treeWordGuesses = ''
fourWord = 'pensar'
fourWordGuesses = ''
fiveWord = "mudar"
fiveWordGuesses = ''
guesses = ''
turnsFirst = 15
turnsSecond = 15
turnsTree = 15
turnsFour = 15
turnsFive = 15
pontuation = 5

print("BEM VINDO AO JOGO RPG: I-HELP")
time.sleep(0.5)



def startGame():
    time.sleep(0.5)
    word = "segredo"
    secondWord = "comida"
    treeWord = "familia"
    fourWord = 'pensar'
    fiveWord = "mudar"
    guesses = ''
    turnsFirst = 15
    turnsSecond = 15
    turnsTree = 15
    turnsFour = 15
    turnsFive = 15

    os.system('clear')
    print("Iniciar jogo")
    name = str(input("Qual o seu nome? "))
    print("Oi, "+name, "quero te ajudar a sobreviver, você esta perdida(o)"+"\n"
                       "numa floresta, prestes a morrer. Cada erro no I-HELP sao"+"\n"+
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
            pontuation = 2
            print('Voce ganhou', pontuation, 'min de vida')
            print("1° Etapa concluída. Você pode encontrar alimentos encima da arvore a sua esquerda")

            pontuation += 5

            for secondChar in secondWord:
                if secondChar in guesses:
                    print(secondChar)
                else:
                    print("_")
                    failed2 += 1

            if failed2 == 0:
                pontuation +=5
                print('Voce ganhou mais', pontuation, 'min de vida')
                print("2° Etapa concluída."+"\n"+"Você pode encontrar agua potavel na casa abandona a 5 minutos de onde voce esta")
                pontuation += 5


                for treeChar in treeWord:
                    if treeChar in guesses:
                        print(treeChar)
                    else:
                        print("_")
                        failed3 += 1
                if failed3 == 0:
                    pontuation += 5
                    print('Voce ganhou', pontuation, 'min de vida')
                    print(
                        "3° Etapa concluída." + "\n" + "Esta quase la. Atras da segunda árvore em sua direção,"+"\n"+
                        "há um kit de primeiros socorros. Cuide dos seus ferimentos!")


                    for fourChar in fourWord:
                        if fourChar in guesses:
                            print(fourChar)
                        else:
                            print("_")
                            failed4 += 1
                    if failed4 == 0:
                        pontuation += 5
                        print('Voce ganhou', pontuation, 'min de vida')
                        print(
                            "4° Etapa concluida." + "\n" + "Falta pouco. A sua esquerda, encontrará uma mochila com todas"+"\n"+"as ferramentas necessárias para continuar")

                        for fiveChar in fiveWord:
                            if fiveChar in guesses:
                                print(fiveChar)
                            else:
                                print("_")
                                failed5 += 1
                        if failed5 == 0:
                            pontuation += 100;
                            print('Voce ganhou', pontuation, 'min de vida - VOCÊ ESTÁ SEGURO')
                            print(
                                "5° Etapa concluída." + "\n" + "Parabéns!! Agora, atrás de você tem um mapa da floresta" + "\n" +
                                "siga os pontos e a saída estará próxima."
                                +"\n"+"Agora você também está seguro")
                            break

        guess = input("Letra: ")
        guesses += guess

        if guess not in word and guess not in secondWord and guess not in treeWord and guess not in fourWord and guess not in fiveWord:
            turnsFirst -= 1
            print("Errou")
            print("Você tem", +turnsFirst, 'chances na 1 etapa')

            if turnsFirst == 0:
                print("Voce perdeu")


def options(value):
    os.system('clear')
    if '1' in value:
        os.system('clear')
        print("Juliana Cerqueira, TIA: 31894712")
        respToBackFirst = input("Deseja voltar para a tela inicial? ")
        if 'sim' in respToBackFirst:
            os.system('clear')
            respOption = str(input("Digite 1- Creditos 2- Como Jogar e 3- Iniciar jogo:"))
            options(respOption)
            os.system('clear')

    elif '2' in value:
        os.system('clear')
        print("Você está perdido na floresta e precisa sobreviver, para isso, precisa de ajuda. Resolva o I-HELP"
              " e ganhe dicas de sobrevivência. Voce pode ficar insguro na floresta mais rápido ou ganhar mais tempo de vida"
              " Boa sorte!")
        respToBack = input("Deseja voltar para a tela inicial? ")
        if 'sim' in respToBack:
            os.system('clear')
            respOption = str(input("Digite 1- Creditos 2- Como Jogar e 3- Iniciar jogo:"))
            os.system('clear')
            options(respOption)
            os.system('clear')
    else:
        startGame()


respOption = str(input("Digite 1- Creditos 2- Como Jogar e 3- Iniciar jogo:"))
options(respOption)

