import time

print("BEM VINDO AO JOGO RPG - CAÇA PALAVRAS")
time.sleep(0.5)

option = input("Digite 1- Créditos 2- Como Jogar e 3- Iniciar jogo:")


def cls():
    print('\n' * 50)


if '1' in option:
    cls()
    print("Juliana Cerqueira, TIA: 31894712")
    respOption = input("Deseja voltar para a tela inicial? ")

elif '2' in option:
    print("É um jodo de caça palavras, entre com letras até que descubra a palavra secreta,"
          " você tem vidas e pontuação para"
          "cada acerto. Boa sorte!")
    input("Deseja voltar para a tela inicial? ")

else:
    print("Iniciar jogo")
    name = input("Qual o seu nome? ")
    print("Oi, "+name, "quero te ajudar a sobreviver, você está perdida(o)"+"\n"
                       "numa floresta, prestes a morrer. Cada erro no caça palavra são"+"\n"+
                       "5 minutos a menos de vida. Mas se ganhar, você encontra o caminho de saída."+"\n"
                       "Tente sobreviver. Boa sorte!")
    time.sleep(0.5)
    word = "secret"
    secondWord = "food"
    treeWord = "family"
    secondWordGuesses = ''
    treeWordGuesses = ''
    fourWord = 'kyp'
    fourWordGuesses = ''
    fiveWord = "changes"
    fiveWordGuesses = ''
    guesses = ''
    turnsFirst = 10
    turnsSecond = 10
    turnsTree = 10
    turnsFour = 10
    turnsFive = 10

    while turnsFirst > 0 and turnsSecond > 0 and turnsTree > 0 and turnsFour > 0 and turnsFive > 0:
        failed = 0

        for char in word:
            if char in guesses:
                print(char)
            else:
                print("_")
                failed += 1
        if failed == 0:
            print("1° Etapa concluída. Você pode encontrar alimentos encima da árvore à sua esquerda")
            failed2 = 0

            for secondChar in secondWord:
                if secondChar in secondWordGuesses:
                    print(secondChar)
                else:
                    print("_")
                    failed2 += 1
            if failed2 == 0:
                print("2° Etapa concluída."+"\n"+"Você pode encontrar água potável na casa abandona à 5 minutos de onde você está")
                failed3 = 0

                for treeChar in treeWord:
                    if treeChar in treeWordGuesses:
                        print(treeChar)
                    else:
                        print("_")
                        failed3 += 1
                if failed3 == 0:
                    print(
                        "3° Etapa concluída." + "\n" + "Está quase lá. Atrás da segunda árvore em sua direção,"+"\n"+
                        "há um kit de primeiros socorros. Cuide dos seus ferimentos!")
                    failed4 = 0

                    for fourChar in fourWord:
                        if fourChar in fourWordGuesses:
                            print(fourChar)
                        else:
                            print("_")
                            failed4 += 1
                    if failed4 == 0:
                        print(
                            "4° Etapa concluída." + "\n" + "Falta pouco. À sua esquerda, encontrará uma mochila com todas"+"\n"+"as ferramentas necessárias para continuar")
                        failed5 = 0

                        for fiveChar in fiveWord:
                            if fiveChar in fiveWordGuesses:
                                print(fiveChar)
                            else:
                                print("_")
                                failed5 += 1
                        if failed5 == 0:
                            print(
                                "5° Etapa concluída." + "\n" + "Parabéns!!! Agora, atrás de você terá um mapa da floresta" + "\n" +
                                "siga os pontos e a saída estará próxima."
                                +"\n"+"Agora você também está seguro")
                            break

        guess = input("Primeira letra: ")
        guesses += guess

        secondWordGuesses += guess
        treeWordGuesses += guess
        fourWordGuesses += guess
        fiveWordGuesses += guess

        if guess not in word:
            turnsFirst -= 1
            print("wrong")
            print("Voce tem", +turnsFirst, 'chances')

            if turnsFirst == 0:
                print("voce perdeu")

        if guess not in secondWord:
            turnsSecond -= 1
            print("wrong")
            print("Voce tem", +turnsSecond, 'chances')

            if turnsSecond == 0:
                print("voce perdeu")

        if guess not in treeWord:
            turnsTree -= 1
            print("wrong")
            print("Voce tem", +turnsTree, 'chances')

            if turnsTree == 0:
                print("voce perdeu e as suas chances de morrer são maiores")

        if guess not in fourWord:
            turnsFour -= 1
            print("wrong")
            print("Voce tem", +turnsFour, 'chances')

            if turnsFour == 0:
                print("voce perdeu e as suas chances de morrer são maiores")

        if guess not in fiveWord:
            turnsFive -= 1
            print("wrong")
            print("Voce tem", +turnsFive, 'chances')

            if turnsFive == 0:
                print("voce perdeu e as suas chances de morrer são maiores")