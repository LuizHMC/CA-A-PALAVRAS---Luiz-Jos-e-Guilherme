##################################### N3 ###################################################
import time
import random

def JR():
    # Variáveis do jogo
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    p1x = 60
    p2x = 40
    p3x = 20
    p4x = 10
    pontuacao_total = 0
    pontuacao_rodada = 0


    #Caças
    c1 = ["---------------------------------------------------------------------------","| E E L D Y V O R                                                         |","| O W K Q O H X J                                                         |","| B T V G S I I T                                                         |","| E S A R F D T S                                                         |","| Q I A I W B O L                                                         |","| S N Z G H I N M                                                         |","| M Z T R V J A P                                                         |","| M T T C D H R B                                                         |","---------------------------------------------------------------------------"] #Português
    c2 = ["---------------------------------------------------------------------------","| B R I I Y T F E I S                                                     |","| X A G S E K U S F F                                                     |","| X M S N V V C G Y J                                                     |","| P S I Q S N S R X S                                                     |","| B S V O U Y C I R I                                                     |","| Y M V H B E J M V Q                                                     |","| G E M T A S T A L J                                                     |","| R M D F P O R E S E                                                     |","| F L O G E H Y O A W                                                     |","| A A R W N J D E J N                                                     |","---------------------------------------------------------------------------"] #Esporte
    c3 = ["---------------------------------------------------------------------------","| X Y E O M T M R                                                         |","| H P S E L A I A                                                         |","| K I R A N W K S                                                         |","| N O C D G M I E                                                         |","| F D E L J R O C                                                         |","| X L I H D N A G                                                         |","| A Z R G Y R I V                                                         |","| B Q S E E T D W                                                         |","---------------------------------------------------------------------------"]#Líderes
    c4 = ["---------------------------------------------------------------------------","| H Y J I Z A B E S V                                                     |","| B N W V Q H J I O O                                                     |","| G L M C F A Y P K J                                                     |","| I C G C R A O M E N                                                     |","| E E Q A Q M R I C R                                                     |","| G V C T S L P O L R                                                     |","| T A P I O C A P F I                                                     |","| B P Y F X Z H X P A                                                     |","| N U D C D C Y T C T                                                     |","| V F E I J O A D A X                                                     |","---------------------------------------------------------------------------"] #Comidas típicas
    c5 = ["---------------------------------------------------------------------------","| O J W J A O V S                                                         |","| B E D X Q U O Z                                                         |","| M S M T B I K R                                                         |","| A U H L D T P Z                                                         |","| C I L N O U R O                                                         |","| S T I V E Z J N                                                         |","| E A D I B S A H                                                         |","| H S P S L J A Y                                                         |","---------------------------------------------------------------------------"] #Brasil Colônia
    c6 = ["---------------------------------------------------------------------------","| R M B O P Z P E                                                         |","| C L O R O W R W                                                         |","| T T B U O B A L                                                         |","| E M W S O M T I                                                         |","| P C S C P B A A                                                         |","| C F A Y G D K K                                                         |","| Y B A V G T H K                                                         |","| T R O N T V U Z                                                         |","---------------------------------------------------------------------------"] #quimica
    c7 = ["---------------------------------------------------------------------------","| S P C U Q W V I D S                                                     |","| J E T R C S F S A O                                                     |","| S X O V X K H H P T                                                     |","| E F G S S Y N R V L                                                     |","| M N T P S A I O D A                                                     |","| B H A W T E V Q G N                                                     |","| U O S N C A R W F A                                                     |","| T V O J J M G P J L                                                     |","| R M B I C D L A E P                                                     |","| P L A N I C I E S D                                                     |","---------------------------------------------------------------------------"] #Relevos
    c8 = ["---------------------------------------------------------------------------","| I M F X Y Q I O                                                         |","| V R U F U Z R Q                                                         |","| Z Q A A L I T U                                                         |","| Y M R C F R E I                                                         |","| C U K Y E Z X N                                                         |","| P N E T U M Q Z                                                         |","| V B Y Z R G A E                                                         |","| P R X W D J B P                                                         |","---------------------------------------------------------------------------"]#Obras literarias
    #Até aqui

    #Soluções
    s1 = ["+ + + + + V O +","O + + + O + X +","+ T + G + + I +","E S A R F + T +","+ I + I + + O +","S + + + H + N +","+ + + + + + A +","+ + + + + + + +"] #Português
    s2 = ["B + + + + T + E + +","+ A + + E + + S + +","+ + S N + + + G + +","+ + I Q + + + R + +","+ S + + U + + I + +","+ + + + + E + M + +","+ + + + + + T A + +","+ + + + + + + E + +","F L O G + + + + + +","+ + + + + + + + + +"] #Esporte
    s3 = ["+ + + + + + M R","+ + S + + A + A","+ + + A N + + S","+ + + D G + + E","+ + E + + R + C","+ L I H D N A G","A + + + + + + V","+ + + + + + + +"] #Líderes
    s4 = ["+ + + + + + + E + +","+ + + + + + J + + +","+ + + + F A + + + +","+ + + + R A + + + +","+ + + A + + R + + +","+ + C + + + + O + +","T A P I O C A + F +","+ + + + + + + + + A","+ + + + + + + + + +","+ F E I J O A D A +"] #Comidas tipícas
    s5 = ["O J + + + + + S","B E + + + + O +","M S + + + I + +","A U + + D + + +","C I + N O U R O","S T I + + + + +","E A + + + + + +","+ S + + + + + +"] #Brasil Colônia
    s6 = ["+ + B + + + P E","C L O R O + R +","+ + + + O B A +","+ + + + O M T +","+ + + C + + A +","+ + + + + + + +","+ + + + + + + +","+ + + + + + + +"] #quimica
    s7 = ["S + + + + + + + + S","+ E + + + + + + A O","+ + O + + + + H + T","+ + + S + + N + + L","+ + + + S A + + + A","+ + + + T E + + + N","+ + + N + + R + + A","+ + O + + + + P + L","+ M + + + + + + E P","P L A N I C I E S D"] #Relevos
    s8 = ["I + + + + Q + O","+ R + + U + + Q","+ + A A L I T U","+ + R C + + + I","+ U + + E + + N","P + + + + M + Z","+ + + + + + A E","+ + + + + + + +"] #Obras literárias

    print("")
    print("")
    print("")
    print("                             LOADING",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("")
    print("")
    print("")
    escolhido = random.randint(1,8)

    # Caça 1
    if escolhido == 1:
        for i in c1:
            print(i)

        print("")
        print("O tema é: Português (Lingua Portuguesa)")
        # COLOCAR AS PALAVRAS
        print("")
        print("Existem 4 palavras nesse caça palavras (escreva sem espaço e acentos)")
        print("")
        p1= str(input("Qual a primeira palavra que você achou? "))
        while cont1 != 1:
            #Inserir palavras
            if p1.upper() == "VOGAIS" or p1.upper()== "FRASE" or p1.upper()== "HIATO" or p1.upper()== "OXITONA":
                print("A palavra achada foi ",p1)
                cont1 += 1
                pontuacao_rodada += len(p1)*p1x
                pontuacao_total += pontuacao_rodada
                print("A sua pontuação é, ",pontuacao_rodada)
            #Inserir palavras
            elif p1.upper() != "VOGAIS" or p1.upper()!= "FRASE" or p1.upper()!= "HIATO" or p1.upper()!= "OXITONA":
                print("O dado colocado está inválido")
                p1= str(input("Qual a primeira palavra que você achou? "))
        print("")
        #Colocar o caça daqui
        for i in c1:
            print (i)
        #Até aqui
        print("")
        p2 = str(input("Qual a segunda palavra que você achou? "))
        while cont2 != 1:
            if p2.upper() == p1.upper():
                print("A palavra está repetida")
                p2 = str(input("Qual a segunda palavra que você achou? "))
            #Inserir palavras
            elif p2.upper() == "VOGAIS" or p2.upper()== "FRASE" or p2.upper()== "HIATO" or p2.upper()== "OXITONA":
                print("A palavra achada foi ",p2)
                cont2 += 1
                pontuacao_rodada += len(p2)*p2x
                pontuacao_total += pontuacao_rodada
                print("A sua pontuação é, ",pontuacao_rodada)
            #Inserir palavras
            elif p2.upper() != "VOGAIS" or p2.upper()!= "FRASE" or p2.upper()!= "HIATO" or p2.upper()!= "OXITONA":
                print("O dado colocado está inválido")
                p2= str(input("Qual a segunda palavra que você achou? "))
        print("")
        #Colocar o caça daqui
        for i in c1:
            print (i)
        #Até aqui
        print("")
        p3 = str(input("Qual a terceira palavra que você achou? "))
        while cont3 != 1:
            if p3.upper()==p1.upper() or p3.upper()==p2.upper():
                print("A palavra está repetida")
                p3 = str(input("Qual a terceira palavra que você achou? "))
            #Inserir palavras
            elif p3.upper() == "VOGAIS" or p3.upper()== "FRASE" or p3.upper()== "HIATO" or p3.upper()== "OXITONA":
                print("A palavra achada foi ",p3)
                cont3 += 1
                pontuacao_rodada += len(p3)*p3x
                pontuacao_total += pontuacao_rodada
                print("A sua pontuação é, ",pontuacao_rodada)
            #Inserir palavras
            elif p3.upper() != "VOGAIS" or p3.upper()!= "FRASE" or p3.upper()!= "HIATO" or p3.upper()!= "OXITONA":
                print("O dado colocado está inválido")
                p3= str(input("Qual a terceira palavra que você achou? "))
        print("")
        #Colocar o caça daqui
        for i in c1:
            print (i)
        #Até aqui
        print("")
        p4 = str(input("Qual a quarta palavra que você achou? "))
        while cont4 != 1:
            if p4==p1 or p4==p2 or p4==p3:
                print("A palavra está repetida")
                p4 = str (input("Qual a quarta palavra que você achou? "))
            #Inserir palavras
            elif p4.upper() == "VOGAIS" or p4.upper()== "FRASE" or p4.upper()== "HIATO" or p4.upper()== "OXITONA":
                print("A palavra achada foi ",p4)
                cont4 += 1
                pontuacao_rodada += len(p4)*p4x
                pontuacao_total += pontuacao_rodada
            #Inserir palavras
            elif p4.upper() != "VOGAIS" or p4.upper()!= "FRASE" or p4.upper()!= "HIATO" or p4.upper()!= "OXITONA":
                print("O dado colocado está inválido")
                p4 = str(input("Qual a quarta palavra que você achou? "))
        print("")

    #Caça 2


        print("A primeira palavra achada foi:",p1)
        print("A segunda palavra achada foi:",p2)
        print("A terceira palavra achada foi:",p3)
        print("A quarta palavra achada foi:",p4)
        print("")
        print("A sua pontuação nessa rodada foi: ",pontuacao_rodada)
        print("A sua pontuação total é:",pontuacao_total)
        print("")
        print("O quadro de respostas é:")
        #quadro de respostas daqui
        for i in s1:
            print (i)
        #até aqui
        print("")
        print("")
        print("")
        print("                             RETORNANDO PARA O MENU",end="")
        time.sleep(1)
        print(".",end="")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("")
        print("")
        print("")
        #Caça 2
    elif escolhido ==  2:
        #INSERIR TITULO E FASE^^^
        #Colocar o caça daqui
        for i in c2:
            print(i)
        #Até aqui
        print("")
        print("O tema é: Esportes")
        print("")
        print("Existem 4 palavras nesse caça palavras (escreva sem espaço e acentos)")
        print("")
        #COLOCAR AS PALAVRAS
        p1= str(input("Qual a primeira palavra que você achou? "))
        while cont1 != 1:
            #Inserir palavras
            if p1.upper() == "BASQUETE" or p1.upper()== "GOLF" or p1.upper()== "ESGRIMA" or p1.upper()== "TENIS":
                print("A palavra achada foi ",p1)
                cont1 += 1
                pontuacao_rodada += len(p1)*p4x
                pontuacao_total += pontuacao_rodada
                print("A sua pontuação é, ",pontuacao_rodada)
            #Inserir palavras
            elif p1.upper() != "BASQUETE" or p1.upper()!= "GOLF" or p1.upper()!= "ESGRIMA" or p1.upper()!= "TENIS":
                print("O dado colocado está inválido")
                p1= str(input("Qual a primeira palavra que você achou? "))
        print("")
        #Colocar o caça daqui
        for i in c2:
            print(i)
        #Até aqui
        print("")
        p2 = str(input("Qual a segunda palavra que você achou? "))
        while cont2 != 1:
            if p2.upper() == p1.upper():
                print("A palavra está repetida")
                p2 = str(input("Qual a segunda palavra que você achou? "))
            #Inserir palavras
            elif p2.upper() == "BASQUETE" or p2.upper()== "GOLF" or p2.upper()== "ESGRIMA" or p2.upper()== "TENIS":
                print("A palavra achada foi ",p2)
                cont2 += 1
                pontuacao_rodada += len(p2)*p3x
                pontuacao_total += pontuacao_rodada
                print("A sua pontuação é, ",pontuacao_rodada)
            #Inserir palavras
            elif p2.upper() != "BASQUETE" or p2.upper()!= "GOLF" or p2.upper()!= "ESGRIMA" or p2.upper()!= "TENIS":
                print("O dado colocado está inválido")
                p2= str(input("Qual a segunda palavra que você achou? "))
        print("")
        #Colocar o caça daqui
        for i in c2:
            print(i)
        #Até aqui
        print("")
        p3 = str(input("Qual a terceira palavra que você achou? "))
        while cont3 != 1:
            if p3.upper()==p1.upper() or p3.upper()==p2.upper():
                print("A palavra está repetida")
                p3 = str(input("Qual a terceira palavra que você achou? "))
            #Inserir palavras
            elif p3.upper() == "BASQUETE" or p3.upper()== "GOLF" or p3.upper()== "ESGRIMA" or p3.upper()== "TENIS":
                print("A palavra achada foi ",p3)
                cont3 += 1
                pontuacao_rodada += len(p3)*p2x
                pontuacao_total += pontuacao_rodada
                print("A sua pontuação é, ",pontuacao_rodada)
            #Inserir palavras
            elif p3.upper() != "BASQUETE" or p3.upper()!= "GOLF" or p3.upper()!= "ESGRIMA" or p3.upper()!= "TENIS":
                print("O dado colocado está inválido")
                p3= str(input("Qual a terceira palavra que você achou? "))
        print("")
        #Colocar o caça daqui
        for i in c2:
            print(i)
        #Até aqui
        print("")
        p4 = str(input("Qual a quarta palavra que você achou? "))
        while cont4 != 1:
            if p4==p1 or p4==p2 or p4==p3:
                print("A palavra está repetida")
                p4 = str (input("Qual a quarta palavra que você achou? "))
            #Inserir palavras
            elif p4.upper() == "BASQUETE" or p4.upper()== "GOLF" or p4.upper()== "ESGRIMA" or p4.upper()== "TENIS":
                print("A palavra achada foi ",p4)
                cont4 += 1
                pontuacao_rodada += len(p4)*p1x
                pontuacao_total += pontuacao_rodada
            #Inserir palavras
            elif p4.upper() != "BASQUETE" or p4.upper()!= "GOLF" or p4.upper()!= "ESGRIMA" or p4.upper()!= "TENIS":
                print("O dado colocado está inválido")
                p4 = str(input("Qual a quarta palavra que você achou? "))




        print("")
        print("A primeira palavra achada foi:",p1)
        print("A segunda palavra achada foi:",p2)
        print("A terceira palavra achada foi:",p3)
        print("A quarta palavra achada foi:",p4)

        print("")
        print("A sua pontuação nessa rodada foi: ",pontuacao_rodada)
        print("A sua pontuação total é:",pontuacao_total)
        print("")
        print("O quadro de respostas é:")
        print("")
        #quadro de respostas daqui
        for i in s2:
            print(i)
        #até aqui
        print("")
        print("")
        print("")
        print("                             RETORNANDO PARA O MENU",end="")
        time.sleep(1)
        print(".",end="")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("")
        print("")
        print("")
        #Caça 3

    elif escolhido == 3:
        for i in c3:
            print(i)

        print("")
        print("O tema é: Líderes")
        print("")
        print("Existem 4 palavras nesse caça palavras (escreva sem espaço e acentos)")
        print("")
        p1= str(input("Qual a primeira palavra que você achou? "))
        while cont1 != 1:
            #Inserir palavras
            if p1.upper() == "VARGAS" or p1.upper()== "GANDHI" or p1.upper()== "CESAR" or p1.upper()== "MANDELA":
                print("A palavra achada foi ",p1)
                cont1 += 1
                pontuacao_rodada += len(p1)*p1x
                pontuacao_total += pontuacao_rodada
                print("A sua pontuação é, ",pontuacao_rodada)
            #Inserir palavras
            elif p1.upper() != "VARGAS" or p1.upper()!= "GANDHI" or p1.upper()!= "CESAR" or p1.upper()!= "MANDELA":
                print("O dado colocado está inválido")
                p1= str(input("Qual a primeira palavra que você achou? "))
        print("")
        #Colocar o caça daqui
        for i in c3:
            print (i)
        #Até aqui
        print("")
        p2 = str(input("Qual a segunda palavra que você achou? "))
        while cont2 != 1:
            if p2.upper() == p1.upper():
                print("A palavra está repetida")
                p2 = str(input("Qual a segunda palavra que você achou? "))
            #Inserir palavras
            elif p2.upper() == "VARGAS" or p2.upper()== "GANDHI" or p2.upper()== "CESAR" or p2.upper()== "MANDELA":
                print("A palavra achada foi ",p2)
                cont2 += 1
                pontuacao_rodada += len(p2)*p2x
                pontuacao_total += pontuacao_rodada
                print("A sua pontuação é, ",pontuacao_rodada)
            #Inserir palavras
            elif p2.upper() != "VARGAS" or p2.upper()!= "GANDHI" or p2.upper()!= "CESAR" or p2.upper()!= "MANDELA":
                print("O dado colocado está inválido")
                p2= str(input("Qual a segunda palavra que você achou? "))
        print("")
        #Colocar o caça daqui
        for i in c3:
            print (i)
        #Até aqui
        print("")
        p3 = str(input("Qual a terceira palavra que você achou? "))
        while cont3 != 1:
            if p3.upper()==p1.upper() or p3.upper()==p2.upper():
                print("A palavra está repetida")
                p3 = str(input("Qual a terceira palavra que você achou? "))
            #Inserir palavras
            elif p3.upper() == "VARGAS" or p3.upper()== "GANDHI" or p3.upper()== "CESAR" or p3.upper()== "MANDELA":
                print("A palavra achada foi ",p3)
                cont3 += 1
                pontuacao_rodada += len(p3)*p3x
                pontuacao_total += pontuacao_rodada
                print("A sua pontuação é, ",pontuacao_rodada)
            #Inserir palavras
            elif p3.upper() != "VARGAS" or p3.upper()!= "GANDHI" or p3.upper()!= "CESAR" or p3.upper()!= "MANDELA":
                print("O dado colocado está inválido")
                p3= str(input("Qual a terceira palavra que você achou? "))
        print("")
        #Colocar o caça daqui
        for i in c3:
            print (i)
        #Até aqui
        print("")
        p4 = str(input("Qual a quarta palavra que você achou? "))
        while cont4 != 1:
            if p4==p1 or p4==p2 or p4==p3:
                print("A palavra está repetida")
                p4 = str (input("Qual a quarta palavra que você achou? "))
            #Inserir palavras
            elif p4.upper() == "VARGAS" or p4.upper()== "GANDHI" or p4.upper()== "CESAR" or p4.upper()== "MANDELA":
                print("A palavra achada foi ",p4)
                cont4 += 1
                pontuacao_rodada += len(p4)*p4x
                pontuacao_total += pontuacao_rodada
            #Inserir palavras
            elif p4.upper() != "VARGAS" or p4.upper()!= "GANDHI" or p4.upper()!= "CESAR" or p4.upper()!= "MANDELA":
                print("O dado colocado está inválido")
                p4 = str(input("Qual a quarta palavra que você achou? "))
        print("")
        print("A primeira palavra achada foi:",p1)
        print("A segunda palavra achada foi:",p2)
        print("A terceira palavra achada foi:",p3)
        print("A quarta palavra achada foi:",p4)
        print("")
        print("A sua pontuação nessa rodada foi: ",pontuacao_rodada)
        print("A sua pontuação total é:",pontuacao_total)
        print("")
        print("O quadro de respostas é:")
        #quadro de respostas daqui
        for i in s3:
            print (i)
        #até aqui
        print("")
        print("")
        print("")
        print("                             RETORNANDO PARA O MENU",end="")
        time.sleep(1)
        print(".",end="")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("")
        print("")
        print("")
    #Caça 4

    elif escolhido ==  4:
        #Colocar o caça daqui
        for i in c4:
            print(i)

        print("")
        print("O tema é: Comidas Típicas brasileiras.")
        print("")
        print("Existem 4 palavras nesse caça palavras (escreva sem espaço e acentos)")
        print("")
        #COLOCAR AS PALAVRAS
        p1= str(input("Qual a primeira palavra que você achou? "))
        while cont1 != 1:
            #Inserir palavras
            if p1.upper() == "ACARAJE" or p1.upper()== "TAPIOCA" or p1.upper()== "FAROFA" or p1.upper()== "FEIJOADA":
                print("A palavra achada foi ",p1)
                cont1 += 1
                pontuacao_rodada += len(p1)*p4x
                pontuacao_total += pontuacao_rodada
                print("A sua pontuação é, ",pontuacao_rodada)
            #Inserir palavras
            elif p1.upper() != "ACARAJE" or p1.upper()!= "TAPIOCA" or p1.upper()!= "FAROFA" or p1.upper()!= "FEIJOADA":
                print("O dado colocado está inválido")
                p1= str(input("Qual a primeira palavra que você achou? "))
        print("")
        #Colocar o caça daqui
        for i in c4:
            print(i)
        #Até aqui
        print("")
        p2 = str(input("Qual a segunda palavra que você achou? "))
        while cont2 != 1:
            if p2.upper() == p1.upper():
                print("A palavra está repetida")
                p2 = str(input("Qual a segunda palavra que você achou? "))
            #Inserir palavras
            elif p2.upper() == "ACARAJE" or p2.upper()== "TAPIOCA" or p2.upper()== "FAROFA" or p2.upper()== "FEIJOADA":
                print("A palavra achada foi ",p2)
                cont2 += 1
                pontuacao_rodada += len(p2)*p3x
                pontuacao_total += pontuacao_rodada
                print("A sua pontuação é, ",pontuacao_rodada)
            #Inserir palavras
            elif p2.upper() != "ACARAJE" or p2.upper()!= "TAPIOCA" or p2.upper()!= "FAROFA" or p2.upper()!= "FEIJOADA":
                print("O dado colocado está inválido")
                p2= str(input("Qual a segunda palavra que você achou? "))
        print("")
        #Colocar o caça daqui
        for i in c4:
            print(i)
        #Até aqui
        print("")
        p3 = str(input("Qual a terceira palavra que você achou? "))
        while cont3 != 1:
            if p3.upper()==p1.upper() or p3.upper()==p2.upper():
                print("A palavra está repetida")
                p3 = str(input("Qual a terceira palavra que você achou? "))
            #Inserir palavras
            elif p3.upper() == "ACARAJE" or p3.upper()== "TAPIOCA" or p3.upper()== "FAROFA" or p3.upper()== "FEIJOADA":
                print("A palavra achada foi ",p3)
                cont3 += 1
                pontuacao_rodada += len(p3)*p2x
                pontuacao_total += pontuacao_rodada
                print("A sua pontuação é, ",pontuacao_rodada)
            #Inserir palavras
            elif p3.upper() != "ACARAJE" or p3.upper()!= "TAPIOCA" or p3.upper()!= "FAROFA" or p3.upper()!= "FEIJOADA":
                print("O dado colocado está inválido")
                p3= str(input("Qual a terceira palavra que você achou? "))
        print("")
        #Colocar o caça daqui
        for i in c4:
            print(i)
        #Até aqui
        print("")
        p4 = str(input("Qual a quarta palavra que você achou? "))
        while cont4 != 1:
            if p4==p1 or p4==p2 or p4==p3:
                print("A palavra está repetida")
                p4 = str (input("Qual a quarta palavra que você achou? "))
            #Inserir palavras
            elif p4.upper() == "ACARAJE" or p4.upper()== "TAPIOCA" or p4.upper()== "FAROFA" or p4.upper()== "FEIJOADA":
                print("A palavra achada foi ",p4)
                cont4 += 1
                pontuacao_rodada += len(p4)*p1x
                pontuacao_total += pontuacao_rodada
            #Inserir palavras
            elif p4.upper() != "ACARAJE" or p4.upper()!= "TAPIOCA" or p4.upper()!= "FAROFA" or p4.upper()!= "FEIJOADA":
                print("O dado colocado está inválido")
                p4 = str(input("Qual a quarta palavra que você achou? "))




        print("")
        print("A primeira palavra achada foi:",p1)
        print("A segunda palavra achada foi:",p2)
        print("A terceira palavra achada foi:",p3)
        print("A quarta palavra achada foi:",p4)

        print("")
        print("A sua pontuação nessa rodada foi: ",pontuacao_rodada)
        print("A sua pontuação total é:",pontuacao_total)
        print("")
        print("O quadro de respostas é:")
        print("")
        #quadro de respostas daqui
        for i in s4:
            print(i)
        #até aqui
        print("")
        print("")
        print("")
        print("                             RETORNANDO PARA O MENU",end="")
        time.sleep(1)
        print(".",end="")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("")
        print("")
        print("")
    #Caça 5

    elif escolhido == 5:
        for i in c5:
            print(i)
        print("")
        print("O tema é: Brasil Colônia")
        print("")
        print("Existem 4 palavras nesse caça palavras (escreva sem espaço e acentos)")
        print("")
        p1= str(input("Qual a primeira palavra que você achou? "))
        while cont1 != 1:
            #Inserir palavras
            if p1.upper() == "INDIOS" or p1.upper()== "ESCAMBO" or p1.upper()== "OURO" or p1.upper()== "JESUITAS":
                print("A palavra achada foi ",p1)
                cont1 += 1
                pontuacao_rodada += len(p1)*p1x
                pontuacao_total += pontuacao_rodada
                print("A sua pontuação é, ",pontuacao_rodada)
            #Inserir palavras
            elif p1.upper() != "INDIOS" or p1.upper()!= "ESCAMBO" or p1.upper()!= "OURO" or p1.upper()!= "JESUITAS":
                print("O dado colocado está inválido")
                p1= str(input("Qual a primeira palavra que você achou? "))
        print("")
        #Colocar o caça daqui
        for i in c5:
            print (i)
        #Até aqui
        print("")
        p2 = str(input("Qual a segunda palavra que você achou? "))
        while cont2 != 1:
            if p2.upper() == p1.upper():
                print("A palavra está repetida")
                p2 = str(input("Qual a segunda palavra que você achou? "))
            #Inserir palavras
            elif p2.upper() == "INDIOS" or p2.upper()== "ESCAMBO" or p2.upper()== "OURO" or p2.upper()== "JESUITAS":
                print("A palavra achada foi ",p2)
                cont2 += 1
                pontuacao_rodada += len(p2)*p2x
                pontuacao_total += pontuacao_rodada
                print("A sua pontuação é, ",pontuacao_rodada)
            #Inserir palavras
            elif p2.upper() != "INDIOS" or p2.upper()!= "ESCAMBO" or p2.upper()!= "OURO" or p2.upper()!= "JESUITAS":
                print("O dado colocado está inválido")
                p2= str(input("Qual a segunda palavra que você achou? "))
        print("")
        #Colocar o caça daqui
        for i in c5:
            print (i)
        #Até aqui
        print("")
        p3 = str(input("Qual a terceira palavra que você achou? "))
        while cont3 != 1:
            if p3.upper()==p1.upper() or p3.upper()==p2.upper():
                print("A palavra está repetida")
                p3 = str(input("Qual a terceira palavra que você achou? "))
            #Inserir palavras
            elif p3.upper() == "INDIOS" or p3.upper()== "ESCAMBO" or p3.upper()== "OURO" or p3.upper()== "JESUITAS":
                print("A palavra achada foi ",p3)
                cont3 += 1
                pontuacao_rodada += len(p3)*p3x
                pontuacao_total += pontuacao_rodada
                print("A sua pontuação é, ",pontuacao_rodada)
            #Inserir palavras
            elif p3.upper() != "INDIOS" or p3.upper()!= "ESCAMBO" or p3.upper()!= "OURO" or p3.upper()!= "JESUITAS":
                print("O dado colocado está inválido")
                p3= str(input("Qual a terceira palavra que você achou? "))
        print("")
        #Colocar o caça daqui
        for i in c5:
            print (i)
        #Até aqui
        print("")
        p4 = str(input("Qual a quarta palavra que você achou? "))
        while cont4 != 1:
            if p4==p1 or p4==p2 or p4==p3:
                print("A palavra está repetida")
                p4 = str (input("Qual a quarta palavra que você achou? "))
            #Inserir palavras
            elif p4.upper() == "INDIOS" or p4.upper()== "ESCAMBO" or p4.upper()== "OURO" or p4.upper()== "JESUITAS":
                print("A palavra achada foi ",p4)
                cont4 += 1
                pontuacao_rodada += len(p4)*p4x
                pontuacao_total += pontuacao_rodada
            #Inserir palavras
            elif p4.upper() != "INDIOS" or p4.upper()!= "ESCAMBO" or p4.upper()!= "OURO" or p4.upper()!= "JESUITAS":
                print("O dado colocado está inválido")
                p4 = str(input("Qual a quarta palavra que você achou? "))
        print("")
        print("A primeira palavra achada foi:",p1)
        print("A segunda palavra achada foi:",p2)
        print("A terceira palavra achada foi:",p3)
        print("A quarta palavra achada foi:",p4)
        print("")
        print("A sua pontuação nessa rodada foi: ",pontuacao_rodada)
        print("A sua pontuação total é:",pontuacao_total)
        print("")
        print("O quadro de respostas é:")
        #quadro de respostas daqui
        for i in s5:
            print (i)
        #até aqui
        print("")
        print("")
        print("")
        print("                             RETORNANDO PARA O MENU",end="")
        time.sleep(1)
        print(".",end="")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("")
        print("")
        print("")
        #Caça 6


    elif escolhido == 6:

        for i in c6:
            print(i)

        print("")
        print("O tema é: Tabela Periódica (Química)")
        print("")
        print("Existem 4 palavras nesse caça palavras (escreva sem espaço e acentos)")
        print("")
        p1= str(input("Qual a primeira palavra que você achou? "))
        while cont1 != 1:
            #Inserir palavras
            if p1.upper() == "BROMO" or p1.upper()== "PRATA" or p1.upper()== "CLORO" or p1.upper()== "COBRE":
                print("A palavra achada foi ",p1)
                cont1 += 1
                pontuacao_rodada += len(p1)*p1x
                pontuacao_total += pontuacao_rodada
                print("A sua pontuação é, ",pontuacao_rodada)
            #Inserir palavras
            elif p1.upper() != "BROMO" or p1.upper()!= "PRATA" or p1.upper()!= "CLORO" or p1.upper()!= "COBRE":
                print("O dado colocado está inválido")
                p1= str(input("Qual a primeira palavra que você achou? "))
        print("")
        #Colocar o caça daqui
        for i in c6:
            print (i)
        #Até aqui
        print("")
        p2 = str(input("Qual a segunda palavra que você achou? "))
        while cont2 != 1:
            if p2.upper() == p1.upper():
                print("A palavra está repetida")
                p2 = str(input("Qual a segunda palavra que você achou? "))
            #Inserir palavras
            elif p2.upper() == "BROMO" or p2.upper()== "PRATA" or p2.upper()== "CLORO" or p2.upper()== "COBRE":
                print("A palavra achada foi ",p2)
                cont2 += 1
                pontuacao_rodada += len(p2)*p2x
                pontuacao_total += pontuacao_rodada
                print("A sua pontuação é, ",pontuacao_rodada)
            #Inserir palavras
            elif p2.upper() != "BROMO" or p2.upper()!= "PRATA" or p2.upper()!= "CLORO" or p2.upper()!= "COBRE":
                print("O dado colocado está inválido")
                p2= str(input("Qual a segunda palavra que você achou? "))
        print("")
        #Colocar o caça daqui
        for i in c6:
            print (i)
        #Até aqui
        print("")
        p3 = str(input("Qual a terceira palavra que você achou? "))
        while cont3 != 1:
            if p3.upper()==p1.upper() or p3.upper()==p2.upper():
                print("A palavra está repetida")
                p3 = str(input("Qual a terceira palavra que você achou? "))
            #Inserir palavras
            elif p3.upper() == "BROMO" or p3.upper()== "PRATA" or p3.upper()== "CLORO" or p3.upper()== "COBRE":
                print("A palavra achada foi ",p3)
                cont3 += 1
                pontuacao_rodada += len(p3)*p3x
                pontuacao_total += pontuacao_rodada
                print("A sua pontuação é, ",pontuacao_rodada)
            #Inserir palavras
            elif p3.upper() != "BROMO" or p3.upper()!= "PRATA" or p3.upper()!= "CLORO" or p3.upper()!= "COBRE":
                print("O dado colocado está inválido")
                p3= str(input("Qual a terceira palavra que você achou? "))
        print("")
        #Colocar o caça daqui
        for i in c6:
            print (i)
        #Até aqui
        print("")
        p4 = str(input("Qual a quarta palavra que você achou? "))
        while cont4 != 1:
            if p4==p1 or p4==p2 or p4==p3:
                print("A palavra está repetida")
                p4 = str (input("Qual a quarta palavra que você achou? "))
            #Inserir palavras
            elif p4.upper() == "BROMO" or p4.upper()== "PRATA" or p4.upper()== "CLORO" or p4.upper()== "COBRE":
                print("A palavra achada foi ",p4)
                cont4 += 1
                pontuacao_rodada += len(p4)*p4x
                pontuacao_total += pontuacao_rodada
            #Inserir palavras
            elif p4.upper() != "BROMO" or p4.upper()!= "PRATA" or p4.upper()!= "CLORO" or p4.upper()!= "COBRE":
                print("O dado colocado está inválido")
                p4 = str(input("Qual a quarta palavra que você achou? "))
        print("")
        print("A primeira palavra achada foi:",p1)
        print("A segunda palavra achada foi:",p2)
        print("A terceira palavra achada foi:",p3)
        print("A quarta palavra achada foi:",p4)
        print("")
        print("A sua pontuação nessa rodada foi: ",pontuacao_rodada)
        print("A sua pontuação total é:",pontuacao_total)
        print("")
        print("O quadro de respostas é:")
        #quadro de respostas daqui
        for i in s6:
            print (i)
        #até aqui
        print("")
        print("")
        print("")
        print("                             RETORNANDO PARA O MENU",end="")
        time.sleep(1)
        print(".",end="")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("")
        print("")
        print("")
    #Caça 7

    elif escolhido == 7:

        for i in c7:
            print(i)

        print("")
        print("O tema é: Tipos de Relevo")
        print("")
        print("Existem 4 palavras nesse caça palavras (escreva sem espaço e acentos)")
        print("")
        p1= str(input("Qual a primeira palavra que você achou? "))
        while cont1 != 1:
            #Inserir palavras
            if p1.upper() == "DEPRESSOES" or p1.upper()== "MONTANHOSAS" or p1.upper()== "PLANALTOS" or p1.upper()== "PLANICIES":
                print("A palavra achada foi ",p1)
                cont1 += 1
                pontuacao_rodada += len(p1)*p1x
                pontuacao_total += pontuacao_rodada
                print("A sua pontuação é, ",pontuacao_rodada)
            #Inserir palavras
            elif p1.upper() != "DEPRESSOES" or p1.upper()!= "MONTANHOSAS" or p1.upper()!= "PLANALTOS" or p1.upper()!= "PLANICIES":
                print("O dado colocado está inválido")
                p1= str(input("Qual a primeira palavra que você achou? "))
        print("")
        #Colocar o caça daqui
        for i in c7:
            print (i)
        #Até aqui
        print("")
        p2 = str(input("Qual a segunda palavra que você achou? "))
        while cont2 != 1:
            if p2.upper() == p1.upper():
                print("A palavra está repetida")
                p2 = str(input("Qual a segunda palavra que você achou? "))
            #Inserir palavras
            elif p2.upper() == "DEPRESSOES" or p2.upper()== "MONTANHOSAS" or p2.upper()== "PLANALTOS" or p2.upper()== "PLANICIES":
                print("A palavra achada foi ",p2)
                cont2 += 1
                pontuacao_rodada += len(p2)*p2x
                pontuacao_total += pontuacao_rodada
                print("A sua pontuação é, ",pontuacao_rodada)
            #Inserir palavras
            elif p2.upper() != "DEPRESSOES" or p2.upper()!= "MONTANHOSAS" or p2.upper()!= "PLANALTOS" or p2.upper()!= "PLANICIES":
                print("O dado colocado está inválido")
                p2= str(input("Qual a segunda palavra que você achou? "))
        print("")
        #Colocar o caça daqui
        for i in c7:
            print (i)
        #Até aqui
        print("")
        p3 = str(input("Qual a terceira palavra que você achou? "))
        while cont3 != 1:
            if p3.upper()==p1.upper() or p3.upper()==p2.upper():
                print("A palavra está repetida")
                p3 = str(input("Qual a terceira palavra que você achou? "))
            #Inserir palavras
            elif p3.upper() == "DEPRESSOES" or p3.upper()== "MONTANHOSAS" or p3.upper()== "PLANALTOS" or p3.upper()== "PLANICIES":
                print("A palavra achada foi ",p3)
                cont3 += 1
                pontuacao_rodada += len(p3)*p3x
                pontuacao_total += pontuacao_rodada
                print("A sua pontuação é, ",pontuacao_rodada)
            #Inserir palavras
            elif p3.upper() != "DEPRESSOES" or p3.upper()!= "MONTANHOSAS" or p3.upper()!= "PLANALTOS" or p3.upper()!= "PLANICIES":
                print("O dado colocado está inválido")
                p3= str(input("Qual a terceira palavra que você achou? "))
        print("")
        #Colocar o caça daqui
        for i in c7:
            print (i)
        #Até aqui
        print("")
        p4 = str(input("Qual a quarta palavra que você achou? "))
        while cont4 != 1:
            if p4==p1 or p4==p2 or p4==p3:
                print("A palavra está repetida")
                p4 = str (input("Qual a quarta palavra que você achou? "))
            #Inserir palavras
            elif p4.upper() == "DEPRESSOES" or p4.upper()== "MONTANHOSAS" or p4.upper()== "PLANALTOS" or p4.upper()== "PLANICIES":
                print("A palavra achada foi ",p4)
                cont4 += 1
                pontuacao_rodada += len(p4)*p4x
                pontuacao_total += pontuacao_rodada
            #Inserir palavras
            elif p4.upper() != "DEPRESSOES" or p4.upper()!= "MONTANHOSAS" or p4.upper()!= "PLANALTOS" or p4.upper()!= "PLANICIES":
                print("O dado colocado está inválido")
                p4 = str(input("Qual a quarta palavra que você achou? "))
        print("")
        print("A primeira palavra achada foi:",p1)
        print("A segunda palavra achada foi:",p2)
        print("A terceira palavra achada foi:",p3)
        print("A quarta palavra achada foi:",p4)
        print("")
        print("A sua pontuação nessa rodada foi: ",pontuacao_rodada)
        print("A sua pontuação total é:",pontuacao_total)
        print("")
        print("O quadro de respostas é:")
        #quadro de respostas daqui
        for i in s7:
            print (i)
        #até aqui
        print("")
        print("")
        print("")
        print("                             RETORNANDO PARA O MENU",end="")
        time.sleep(1)
        print(".",end="")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("")
        print("")
        print("")
    #Caça 8

    elif escolhido == 8:
        print("Relevos.")
        for i in c8:
            print(i)

        print("")
        print("O tema é: Obras Literárias")
        print("")
        print("Existem 4 palavras nesse caça palavras (escreva sem espaço e acentos)")
        print("")
        p1= str(input("Qual a primeira palavra que você achou? "))
        while cont1 != 1:
            #Inserir palavras
            if p1.upper() == "OQUINZE" or p1.upper()== "IRACEMA" or p1.upper()== "QUARUP" or p1.upper()== "TIL":
                print("A palavra achada foi ",p1)
                cont1 += 1
                pontuacao_rodada += len(p1)*p1x
                pontuacao_total += pontuacao_rodada
                print("A sua pontuação é, ",pontuacao_rodada)
            #Inserir palavras
            elif p1.upper() != "OQUINZE" or p1.upper()!= "IRACEMA" or p1.upper()!= "QUARUP" or p1.upper()!= "TIL":
                print("O dado colocado está inválido")
                p1= str(input("Qual a primeira palavra que você achou? "))
        print("")
        #Colocar o caça daqui
        for i in c7:
            print (i)
        #Até aqui
        print("")
        p2 = str(input("Qual a segunda palavra que você achou? "))
        while cont2 != 1:
            if p2.upper() == p1.upper():
                print("A palavra está repetida")
                p2 = str(input("Qual a segunda palavra que você achou? "))
            #Inserir palavras
            elif p2.upper() == "OQUINZE" or p2.upper()== "IRACEMA" or p2.upper()== "QUARUP" or p2.upper()== "TIL":
                print("A palavra achada foi ",p2)
                cont2 += 1
                pontuacao_rodada += len(p2)*p2x
                pontuacao_total += pontuacao_rodada
                print("A sua pontuação é, ",pontuacao_rodada)
            #Inserir palavras
            elif p2.upper() != "OQUINZE" or p2.upper()!= "IRACEMA" or p2.upper()!= "QUARUP" or p2.upper()!= "TIL":
                print("O dado colocado está inválido")
                p2= str(input("Qual a segunda palavra que você achou? "))
        print("")
        #Colocar o caça daqui
        for i in c7:
            print (i)
        #Até aqui
        print("")
        p3 = str(input("Qual a terceira palavra que você achou? "))
        while cont3 != 1:
            if p3.upper()==p1.upper() or p3.upper()==p2.upper():
                print("A palavra está repetida")
                p3 = str(input("Qual a terceira palavra que você achou? "))
            #Inserir palavras
            elif p3.upper() == "OQUINZE" or p3.upper()== "IRACEMA" or p3.upper()== "QUARUP" or p3.upper()== "TIL":
                print("A palavra achada foi ",p3)
                cont3 += 1
                pontuacao_rodada += len(p3)*p3x
                pontuacao_total += pontuacao_rodada
                print("A sua pontuação é, ",pontuacao_rodada)
            #Inserir palavras
            elif p3.upper() != "OQUINZE" or p3.upper()!= "IRACEMA" or p3.upper()!= "QUARUP" or p3.upper()!= "TIL":
                print("O dado colocado está inválido")
                p3= str(input("Qual a terceira palavra que você achou? "))
        print("")
        #Colocar o caça daqui
        for i in c7:
            print (i)
        #Até aqui
        print("")
        p4 = str(input("Qual a quarta palavra que você achou? "))
        while cont4 != 1:
            if p4==p1 or p4==p2 or p4==p3:
                print("A palavra está repetida")
                p4 = str (input("Qual a quarta palavra que você achou? "))
            #Inserir palavras
            elif p4.upper() == "OQUINZE" or p4.upper()== "IRACEMA" or p4.upper()== "QUARUP" or p4.upper()== "TIL":
                print("A palavra achada foi ",p4)
                cont4 += 1
                pontuacao_rodada += len(p4)*p4x
                pontuacao_total += pontuacao_rodada
            #Inserir palavras
            elif p4.upper() != "OQUINZE" or p4.upper()!= "IRACEMA" or p4.upper()!= "QUARUP" or p4.upper()!= "TIL":
                print("O dado colocado está inválido")
                p4 = str(input("Qual a quarta palavra que você achou? "))
        print("")
        print("A primeira palavra achada foi:",p1)
        print("A segunda palavra achada foi:",p2)
        print("A terceira palavra achada foi:",p3)
        print("A quarta palavra achada foi:",p4)
        print("")
        print("A sua pontuação nessa rodada foi: ",pontuacao_rodada)
        print("A sua pontuação total é:",pontuacao_total)
        print("")
        print("O quadro de respostas é:")
        #quadro de respostas daqui
        for i in s7:
            print (i)
        #até aqui
        print("")
        print("")
        print("")
        print("                             RETORNANDO PARA O MENU",end="")
        time.sleep(1)
        print(".",end="")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("")
        print("")
        print("")
    return menu()




##################################### N3 ###################################################
def n3():

    ##################################################
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    cont5 = 0
    cont6 = 0
    cont7 = 0
    cont8 = 0
    pontuacao_rodada = 0
    print("")
    print("Presidentes do Brasil - FASE 11")#titulo e fase
    print("")
    #FASE11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11
    print("")
    #Colocar o caça daqui
    print("A N I F Z R H K L M S M Y F R ")
    print("N L K T U H Z X V X I K F J O ")
    print("E U U A A D W F N C S E F A L ")
    print("Z Y L L G M Q B H C S G S N L ")
    print("L E R R O G A E D S Z N N I O ")
    print("Y A J M Y I L R U N O F A O C ")
    print("U Q O S X T C O F C E Z S Q O ")
    print("T C A Q E B R A D R G G X U D ")
    print("A Q G M M A I J N Z A R C A N ")
    print("R R E E M F U I N I L N J D A ")
    print("T R W L R C U H A L Z W C R N ")
    print("D T I Q U A Q G P A L I I O R ")
    print("C D K E H C S T I B U K U S E ")
    print("G E T U L I O V A R G A S L F ")
    print("N E R M G P Z G Z J W G Q X A ")
    #Até aqui
    '''fernandocollor,luizinaciolula, dilmarousseff, getuliovargas, janioquadros, itamarfranco, micheltemer, kubitschek'''
    print("")
    print("Existem 8 palavras nesse caça palavras (escreva sem espaço e acentos)")
    print("")
    #COLOCAR AS PALAVRAS
    p1= str(input("Qual a primeira palavra que você achou? "))
    while cont1 != 1:
        #Inserir palavras
        if p1.upper() == "MICHELTEMER" or p1.upper()== "LUIZINACIOLULA" or p1.upper()== "KUBITSCHEK" or p1.upper()== "JANIOQUADROS" or p1.upper()== "ITAMARFRANCO" or p1.upper()== "GETULIOVARGAS" or p1.upper()== "FERNANDOCOLLOR" or p1.upper()== "DILMAROUSSEFF":
            print("A palavra achada foi ",p1)
            cont1 += 1
            pontuacao_rodada += len(p1)*p8x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p1.upper() != "MICHELTEMER" or p1.upper()!= "LUIZINACIOLULA" or p1.upper()!= "KUBITSCHEK" or p1.upper()!= "JANIOQUADROS" or p1.upper()!= "ITAMARFRANCO" or p1.upper()!= "GETULIOVARGAS" or p1.upper()!= "FERNANDOCOLLOR" or p1.upper()!= "DILMAROUSSEFF":
            print("O dado colocado está inválido")
            p1= str(input("Qual a primeira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("A N I F Z R H K L M S M Y F R ")
    print("N L K T U H Z X V X I K F J O ")
    print("E U U A A D W F N C S E F A L ")
    print("Z Y L L G M Q B H C S G S N L ")
    print("L E R R O G A E D S Z N N I O ")
    print("Y A J M Y I L R U N O F A O C ")
    print("U Q O S X T C O F C E Z S Q O ")
    print("T C A Q E B R A D R G G X U D ")
    print("A Q G M M A I J N Z A R C A N ")
    print("R R E E M F U I N I L N J D A ")
    print("T R W L R C U H A L Z W C R N ")
    print("D T I Q U A Q G P A L I I O R ")
    print("C D K E H C S T I B U K U S E ")
    print("G E T U L I O V A R G A S L F ")
    print("N E R M G P Z G Z J W G Q X A ")
    #Até aqui
    print("")
    p2 = str(input("Qual a segunda palavra que você achou? "))
    while cont2 != 1:
        if p2.upper() == p1.upper():
            print("A palavra está repetida")
            p2 = str(input("Qual a segunda palavra que você achou? "))
        #Inserir palavras
        elif p2.upper() == "MICHELTEMER" or p2.upper()== "LUIZINACIOLULA" or p2.upper()== "KUBITSCHEK" or p2.upper()== "JANIOQUADROS" or p2.upper()== "ITAMARFRANCO" or p2.upper()== "GETULIOVARGAS"or p2.upper()== "FERNANDOCOLLOR"or p2.upper()== "DILMAROUSSEFF":
            print("A palavra achada foi ",p2)
            cont2 += 1
            pontuacao_rodada += len(p2)*p7x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p2.upper() != "MICHELTEMER" or p2.upper()!= "LUIZINACIOLULA" or p2.upper()!= "KUBITSCHEK" or p2.upper()!= "JANIOQUADROS" or p2.upper()!= "ITAMARFRANCO" or p2.upper()!= "GETULIOVARGAS"or p2.upper()!= "FERNANDOCOLLOR"or p2.upper()!= "DILMAROUSSEFF":
            print("O dado colocado está inválido")
            p2= str(input("Qual a segunda palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("A N I F Z R H K L M S M Y F R ")
    print("N L K T U H Z X V X I K F J O ")
    print("E U U A A D W F N C S E F A L ")
    print("Z Y L L G M Q B H C S G S N L ")
    print("L E R R O G A E D S Z N N I O ")
    print("Y A J M Y I L R U N O F A O C ")
    print("U Q O S X T C O F C E Z S Q O ")
    print("T C A Q E B R A D R G G X U D ")
    print("A Q G M M A I J N Z A R C A N ")
    print("R R E E M F U I N I L N J D A ")
    print("T R W L R C U H A L Z W C R N ")
    print("D T I Q U A Q G P A L I I O R ")
    print("C D K E H C S T I B U K U S E ")
    print("G E T U L I O V A R G A S L F ")
    print("N E R M G P Z G Z J W G Q X A ")
    #Até aqui
    print("")
    p3 = str(input("Qual a terceira palavra que você achou? "))
    while cont3 != 1:
        if p3.upper()==p1.upper() or p3.upper()==p2.upper():
            print("A palavra está repetida")
            p3 = str(input("Qual a terceira palavra que você achou? "))
        #Inserir palavras
        elif p3.upper() == "MICHELTEMER" or p3.upper()== "LUIZINACIOLULA" or p3.upper()== "KUBITSCHEK" or p3.upper()== "JANIOQUADROS" or p3.upper()== "ITAMARFRANCO" or p3.upper()== "GETULIOVARGAS"or p3.upper()== "FERNANDOCOLLOR"or p3.upper()== "DILMAROUSSEFF":
            print("A palavra achada foi ",p3)
            cont3 += 1
            pontuacao_rodada += len(p3)*p6x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p3.upper() != "MICHELTEMER" or p3.upper()!= "LUIZINACIOLULA" or p3.upper()!= "KUBITSCHEK" or p3.upper()!= "JANIOQUADROS" or p3.upper()!= "ITAMARFRANCO" or p3.upper()!= "GETULIOVARGAS"or p3.upper()!= "FERNANDOCOLLOR"or p3.upper()!= "DILMAROUSSEFF":
            print("O dado colocado está inválido")
            p3= str(input("Qual a terceira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("A N I F Z R H K L M S M Y F R ")
    print("N L K T U H Z X V X I K F J O ")
    print("E U U A A D W F N C S E F A L ")
    print("Z Y L L G M Q B H C S G S N L ")
    print("L E R R O G A E D S Z N N I O ")
    print("Y A J M Y I L R U N O F A O C ")
    print("U Q O S X T C O F C E Z S Q O ")
    print("T C A Q E B R A D R G G X U D ")
    print("A Q G M M A I J N Z A R C A N ")
    print("R R E E M F U I N I L N J D A ")
    print("T R W L R C U H A L Z W C R N ")
    print("D T I Q U A Q G P A L I I O R ")
    print("C D K E H C S T I B U K U S E ")
    print("G E T U L I O V A R G A S L F ")
    print("N E R M G P Z G Z J W G Q X A ")
    #Até aqui
    print("")
    p4 = str(input("Qual a quarta palavra que você achou? "))
    while cont4 != 1:
        if p4==p1 or p4==p2 or p4==p3:
            print("A palavra está repetida")
            p4 = str (input("Qual a quarta palavra que você achou? "))
        #Inserir palavras
        elif p4.upper() == "MICHELTEMER" or p4.upper()== "LUIZINACIOLULA" or p4.upper()== "KUBITSCHEK" or p4.upper()== "JANIOQUADROS" or p4.upper()== "ITAMARFRANCO" or p4.upper()== "GETULIOVARGAS"or p4.upper()== "FERNANDOCOLLOR"or p4.upper()== "DILMAROUSSEFF":
            print("A palavra achada foi ",p4)
            cont4 += 1
            pontuacao_rodada += len(p4)*p5x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p4.upper() != "MICHELTEMER" or p4.upper()!= "LUIZINACIOLULA" or p4.upper()!= "KUBITSCHEK" or p4.upper()!= "JANIOQUADROS" or p4.upper()!= "ITAMARFRANCO" or p4.upper()!= "GETULIOVARGAS"or p4.upper()!= "FERNANDOCOLLOR"or p4.upper()!= "DILMAROUSSEFF":
            print("O dado colocado está inválido")
            p4 = str(input("Qual a quarta palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("A N I F Z R H K L M S M Y F R ")
    print("N L K T U H Z X V X I K F J O ")
    print("E U U A A D W F N C S E F A L ")
    print("Z Y L L G M Q B H C S G S N L ")
    print("L E R R O G A E D S Z N N I O ")
    print("Y A J M Y I L R U N O F A O C ")
    print("U Q O S X T C O F C E Z S Q O ")
    print("T C A Q E B R A D R G G X U D ")
    print("A Q G M M A I J N Z A R C A N ")
    print("R R E E M F U I N I L N J D A ")
    print("T R W L R C U H A L Z W C R N ")
    print("D T I Q U A Q G P A L I I O R ")
    print("C D K E H C S T I B U K U S E ")
    print("G E T U L I O V A R G A S L F ")
    print("N E R M G P Z G Z J W G Q X A ")
    #Até aqui
    print("")
    p5 = str(input("Qual a quinta palavra que você achou? "))
    while cont5 !=1:
        if p5==p1 or p5==p2 or p5==p3 or p5==p4:
            print("A palavra está repetida")
            p5 = str (input("Qual a quinta palavra que você achou? "))
        #Inserir palavras
        elif p5.upper() == "" or p5.upper()== "LUIZINACIOLULA" or p5.upper()== "KUBITSCHEK" or p5.upper()== "JANIOQUADROS" or p5.upper()== "ITAMARFRANCO" or p5.upper()== "GETULIOVARGAS"or p5.upper()== "FERNANDOCOLLOR"or p5.upper()== "DILMAROUSSEFF":
            print("A palavra achada foi ",p5)
            cont5 += 1
            pontuacao_rodada += len(p5)*p4x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p5.upper() != "" or p5.upper()!= "LUIZINACIOLULA" or p5.upper()!= "KUBITSCHEK" or p5.upper()!= "JANIOQUADROS" or p5.upper()!= "ITAMARFRANCO" or p5.upper()!= "GETULIOVARGAS"or p5.upper()!= "FERNANDOCOLLOR"or p5.upper()!= "DILMAROUSSEFF":
            print("O dado colocado está inválido")
            p5 = str(input("Qual a quinta palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("A N I F Z R H K L M S M Y F R ")
    print("N L K T U H Z X V X I K F J O ")
    print("E U U A A D W F N C S E F A L ")
    print("Z Y L L G M Q B H C S G S N L ")
    print("L E R R O G A E D S Z N N I O ")
    print("Y A J M Y I L R U N O F A O C ")
    print("U Q O S X T C O F C E Z S Q O ")
    print("T C A Q E B R A D R G G X U D ")
    print("A Q G M M A I J N Z A R C A N ")
    print("R R E E M F U I N I L N J D A ")
    print("T R W L R C U H A L Z W C R N ")
    print("D T I Q U A Q G P A L I I O R ")
    print("C D K E H C S T I B U K U S E ")
    print("G E T U L I O V A R G A S L F ")
    print("N E R M G P Z G Z J W G Q X A ")
    #Até aqui
    print("")
    p6 = str(input("Qual a sexta palavra que você achou? "))
    while cont6 !=1:
        if p6==p1 or p6==p2 or p6==p3 or p6==p4 or p6==p5:
            print("A palavra está repetida")
            p6 = str (input("Qual a sexta palavra que você achou? "))
        #Inserir palavras
        elif p6.upper() == "MICHELTEMER" or p6.upper()== "LUIZINACIOLULA" or p6.upper()== "KUBITSCHEK" or p6.upper()== "JANIOQUADROS" or p6.upper()== "ITAMARFRANCO" or p6.upper()== "GETULIOVARGAS"or p6.upper()== "FERNANDOCOLLOR"or p6.upper()== "DILMAROUSSEFF":
            print("A palavra achada foi ",p6)
            cont6 += 1
            pontuacao_rodada += len(p6)*p3x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p6.upper() != "MICHELTEMER" or p6.upper()!= "LUIZINACIOLULA" or p6.upper()!= "KUBITSCHEK" or p6.upper()!= "JANIOQUADROS" or p6.upper()!= "ITAMARFRANCO" or p6.upper()!= "GETULIOVARGAS"or p6.upper()!= "FERNANDOCOLLOR"or p6.upper()!= "DILMAROUSSEFF":
            print("O dado colocado está inválido")
            p6 = str(input("Qual a sexta palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("A N I F Z R H K L M S M Y F R ")
    print("N L K T U H Z X V X I K F J O ")
    print("E U U A A D W F N C S E F A L ")
    print("Z Y L L G M Q B H C S G S N L ")
    print("L E R R O G A E D S Z N N I O ")
    print("Y A J M Y I L R U N O F A O C ")
    print("U Q O S X T C O F C E Z S Q O ")
    print("T C A Q E B R A D R G G X U D ")
    print("A Q G M M A I J N Z A R C A N ")
    print("R R E E M F U I N I L N J D A ")
    print("T R W L R C U H A L Z W C R N ")
    print("D T I Q U A Q G P A L I I O R ")
    print("C D K E H C S T I B U K U S E ")
    print("G E T U L I O V A R G A S L F ")
    print("N E R M G P Z G Z J W G Q X A ")
    #Até aqui
    print("")
    p7 = str(input("Qual a sétima palavra que você achou? "))
    while cont7 !=1:
        if p7==p1 or p7==p2 or p7==p3 or p7==p4 or p7==p5 or p7==p6:
            print("A palavra está repetida")
            p7 = str (input("Qual a sétima palavra que você achou? "))
        #Inserir palavras
        elif p7.upper() == "MICHELTEMER" or p7.upper()== "LUIZINACIOLULA" or p7.upper()== "KUBITSCHEK" or p7.upper()== "JANIOQUADROS" or p7.upper()== "ITAMARFRANCO" or p7.upper()== "GETULIOVARGAS"or p7.upper()== "FERNANDOCOLLOR"or p7.upper()== "DILMAROUSSEFF":
            print("A palavra achada foi ",p7)
            cont7 += 1
            pontuacao_rodada += len(p7)*p2x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p7.upper() != "MICHELTEMER" or p7.upper()!= "LUIZINACIOLULA" or p7.upper()!= "KUBITSCHEK" or p7.upper()!= "JANIOQUADROS" or p7.upper()!= "ITAMARFRANCO" or p7.upper()!= "GETULIOVARGAS"or p7.upper()!= "FERNANDOCOLLOR"or p7.upper()!= "DILMAROUSSEFF":
            print("O dado colocado está inválido")
            p7 = str(input("Qual a sétima palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("A N I F Z R H K L M S M Y F R ")
    print("N L K T U H Z X V X I K F J O ")
    print("E U U A A D W F N C S E F A L ")
    print("Z Y L L G M Q B H C S G S N L ")
    print("L E R R O G A E D S Z N N I O ")
    print("Y A J M Y I L R U N O F A O C ")
    print("U Q O S X T C O F C E Z S Q O ")
    print("T C A Q E B R A D R G G X U D ")
    print("A Q G M M A I J N Z A R C A N ")
    print("R R E E M F U I N I L N J D A ")
    print("T R W L R C U H A L Z W C R N ")
    print("D T I Q U A Q G P A L I I O R ")
    print("C D K E H C S T I B U K U S E ")
    print("G E T U L I O V A R G A S L F ")
    print("N E R M G P Z G Z J W G Q X A ")
    #Até aqui
    print("")
    p8 = str(input("Qual a oitava palavra que você achou? "))
    while cont8 !=1:
        if p8==p1 or p8==p2 or p8==p3 or p8==p4 or p8==p5 or p8==p6 or p8==p7:
            print("A palavra está repetida")
            p8 = str (input("Qual a oitava palavra que você achou? "))
        #Inserir palavras
        elif p8.upper() == "MICHELTEMER" or p8.upper()== "LUIZINACIOLULA" or p8.upper()== "KUBITSCHEK" or p8.upper()== "JANIOQUADROS" or p8.upper()== "ITAMARFRANCO" or p8.upper()== "GETULIOVARGAS"or p8.upper()== "FERNANDOCOLLOR"or p8.upper()== "DILMAROUSSEFF":
            print("A palavra achada foi ",p8)
            cont8 += 1
            pontuacao_rodada += len(p8)*p1x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p8.upper() != "MICHELTEMER" or p8.upper()!= "LUIZINACIOLULA" or p8.upper()!= "KUBITSCHEK" or p8.upper()!= "JANIOQUADROS" or p8.upper()!= "ITAMARFRANCO" or p8.upper()!= "GETULIOVARGAS"or p8.upper()!= "FERNANDOCOLLOR"or p8.upper()!= "DILMAROUSSEFF":
            print("O dado colocado está inválido")
            p8 = str(input("Qual a oitava palavra que você achou? "))
    print("")
    print("A primeira palavra achada foi:",p1)
    print("A segunda palavra achada foi:",p2)
    print("A terceira palavra achada foi:",p3)
    print("A quarta palavra achada foi:",p4)
    print("A quinta palavra achada foi:",p5)
    print("A sexta palavra achada foi:",p6)
    print("A sétima palavra achada foi:",p7)
    print("A oitava palavra achada foi:",p8)
    print("")
    print("A sua pontuação nessa rodada foi: ",pontuacao_rodada)
    print("A sua pontuação total é:",pontuacao_total)
    print("")
    print("O quadro de respostas é:")
    print("")
    #quadro de respostas daqui
    print("A + I + + + + + + + + M + F R ")
    print("+ L + T + + + + + + I + F J O ")
    print("+ + U + A + + + + C + E + A L ")
    print("+ + + L + M + + H + S + + N L ")
    print("+ + + + O + A E + S + + + I O ")
    print("+ + + + + I L R U + + + + O C ")
    print("+ + + + + T C O F + + + + Q O ")
    print("+ + + + E + R A + R + + + U D ")
    print("+ + + M + A + + N + A + + A N ")
    print("+ + E + M + + + + I + N + D A ")
    print("+ R + L + + + + + + Z + C R N ")
    print("+ + I + + + + + + + + I + O R ")
    print("+ D K E H C S T I B U K U S E ")
    print("G E T U L I O V A R G A S L F ")
    print("+ + + + + + + + + + + + + + + ")
    #até aqui
    ##################################################
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    cont5 = 0
    cont6 = 0
    cont7 = 0
    cont8 = 0
    pontuacao_rodada = 0
    print("")
    print("Flores - FASE12")#titulo e fase
    print("")
    #FASE12121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212
    print("")
    #Colocar o caça daqui
    print("H R E X O E B Y J C N L Z J G ")
    print("Y I O T C A T I V S I O G E N ")
    print("M L B S P X A R W W M S C R J ")
    print("F L J I A O B T F F V A B L K ")
    print("T Z L V C E N P E O M R Z O R ")
    print("F U U J G X W T B L U I V T P ")
    print("T B Z O W X R R R D O G H E R ")
    print("B W N J I K A P O Y E I G O F ")
    print("X I L Z G G I A M N Q B V I D ")
    print("A J K C Q U T M E O Y P F T G ")
    print("A I N U T E P H L P O M Z L J ")
    print("D V R Q W K V S I H M A J Z V ")
    print("A G S Q T U B V A C R A V O U ")
    print("G C S K A K B M G K J F Q T Z ")
    print("M O G G W G S B T R L J U A L ")
    #Até aqui
    '''bromelia, begonia , violeta, petunia, girasol, tulipa, cravo, rosa '''
    print("")
    print("Existem 8 palavras nesse caça palavras (escreva sem espaço e acentos)")
    print("")
    #COLOCAR AS PALAVRAS
    p1= str(input("Qual a primeira palavra que você achou? "))
    while cont1 != 1:
        #Inserir palavras
        if p1.upper() == "VIOLETA" or p1.upper()== "TULIPA" or p1.upper()== "ROSA" or p1.upper()== "PETUNIA" or p1.upper()== "GIRASOL" or p1.upper()== "CRAVO" or p1.upper()== "BROMELIA" or p1.upper()== "BEGONIA":
            print("A palavra achada foi ",p1)
            cont1 += 1
            pontuacao_rodada += len(p1)*p8x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p1.upper() != "VIOLETA" or p1.upper()!= "TULIPA" or p1.upper()!= "ROSA" or p1.upper()!= "PETUNIA" or p1.upper()!= "GIRASOL" or p1.upper()!= "CRAVO" or p1.upper()!= "BROMELIA" or p1.upper()!= "BEGONIA":
            print("O dado colocado está inválido")
            p1= str(input("Qual a primeira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("H R E X O E B Y J C N L Z J G ")
    print("Y I O T C A T I V S I O G E N ")
    print("M L B S P X A R W W M S C R J ")
    print("F L J I A O B T F F V A B L K ")
    print("T Z L V C E N P E O M R Z O R ")
    print("F U U J G X W T B L U I V T P ")
    print("T B Z O W X R R R D O G H E R ")
    print("B W N J I K A P O Y E I G O F ")
    print("X I L Z G G I A M N Q B V I D ")
    print("A J K C Q U T M E O Y P F T G ")
    print("A I N U T E P H L P O M Z L J ")
    print("D V R Q W K V S I H M A J Z V ")
    print("A G S Q T U B V A C R A V O U ")
    print("G C S K A K B M G K J F Q T Z ")
    print("M O G G W G S B T R L J U A L ")
    #Até aqui
    print("")
    p2 = str(input("Qual a segunda palavra que você achou? "))
    while cont2 != 1:
        if p2.upper() == p1.upper():
            print("A palavra está repetida")
            p2 = str(input("Qual a segunda palavra que você achou? "))
        #Inserir palavras
        elif p2.upper() == "VIOLETA" or p2.upper()== "TULIPA" or p2.upper()== "ROSA" or p2.upper()== "PETUNIA" or p2.upper()== "GIRASOL" or p2.upper()== "CRAVO"or p2.upper()== "BROMELIA"or p2.upper()== "BEGONIA":
            print("A palavra achada foi ",p2)
            cont2 += 1
            pontuacao_rodada += len(p2)*p7x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p2.upper() != "VIOLETA" or p2.upper()!= "TULIPA" or p2.upper()!= "ROSA" or p2.upper()!= "PETUNIA" or p2.upper()!= "GIRASOL" or p2.upper()!= "CRAVO"or p2.upper()!= "BROMELIA"or p2.upper()!= "BEGONIA":
            print("O dado colocado está inválido")
            p2= str(input("Qual a segunda palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("H R E X O E B Y J C N L Z J G ")
    print("Y I O T C A T I V S I O G E N ")
    print("M L B S P X A R W W M S C R J ")
    print("F L J I A O B T F F V A B L K ")
    print("T Z L V C E N P E O M R Z O R ")
    print("F U U J G X W T B L U I V T P ")
    print("T B Z O W X R R R D O G H E R ")
    print("B W N J I K A P O Y E I G O F ")
    print("X I L Z G G I A M N Q B V I D ")
    print("A J K C Q U T M E O Y P F T G ")
    print("A I N U T E P H L P O M Z L J ")
    print("D V R Q W K V S I H M A J Z V ")
    print("A G S Q T U B V A C R A V O U ")
    print("G C S K A K B M G K J F Q T Z ")
    print("M O G G W G S B T R L J U A L ")
    #Até aqui
    print("")
    p3 = str(input("Qual a terceira palavra que você achou? "))
    while cont3 != 1:
        if p3.upper()==p1.upper() or p3.upper()==p2.upper():
            print("A palavra está repetida")
            p3 = str(input("Qual a terceira palavra que você achou? "))
        #Inserir palavras
        elif p3.upper() == "VIOLETA" or p3.upper()== "TULIPA" or p3.upper()== "ROSA" or p3.upper()== "PETUNIA" or p3.upper()== "GIRASOL" or p3.upper()== "CRAVO"or p3.upper()== "BROMELIA"or p3.upper()== "BEGONIA":
            print("A palavra achada foi ",p3)
            cont3 += 1
            pontuacao_rodada += len(p3)*p6x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p3.upper() != "VIOLETA" or p3.upper()!= "TULIPA" or p3.upper()!= "ROSA" or p3.upper()!= "PETUNIA" or p3.upper()!= "GIRASOL" or p3.upper()!= "CRAVO"or p3.upper()!= "BROMELIA"or p3.upper()!= "BEGONIA":
            print("O dado colocado está inválido")
            p3= str(input("Qual a terceira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("H R E X O E B Y J C N L Z J G ")
    print("Y I O T C A T I V S I O G E N ")
    print("M L B S P X A R W W M S C R J ")
    print("F L J I A O B T F F V A B L K ")
    print("T Z L V C E N P E O M R Z O R ")
    print("F U U J G X W T B L U I V T P ")
    print("T B Z O W X R R R D O G H E R ")
    print("B W N J I K A P O Y E I G O F ")
    print("X I L Z G G I A M N Q B V I D ")
    print("A J K C Q U T M E O Y P F T G ")
    print("A I N U T E P H L P O M Z L J ")
    print("D V R Q W K V S I H M A J Z V ")
    print("A G S Q T U B V A C R A V O U ")
    print("G C S K A K B M G K J F Q T Z ")
    print("M O G G W G S B T R L J U A L ")
    #Até aqui
    print("")
    p4 = str(input("Qual a quarta palavra que você achou? "))
    while cont4 != 1:
        if p4==p1 or p4==p2 or p4==p3:
            print("A palavra está repetida")
            p4 = str (input("Qual a quarta palavra que você achou? "))
        #Inserir palavras
        elif p4.upper() == "VIOLETA" or p4.upper()== "TULIPA" or p4.upper()== "ROSA" or p4.upper()== "PETUNIA" or p4.upper()== "GIRASOL" or p4.upper()== "CRAVO"or p4.upper()== "BROMELIA"or p4.upper()== "BEGONIA":
            print("A palavra achada foi ",p4)
            cont4 += 1
            pontuacao_rodada += len(p4)*p5x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p4.upper() != "VIOLETA" or p4.upper()!= "TULIPA" or p4.upper()!= "ROSA" or p4.upper()!= "PETUNIA" or p4.upper()!= "GIRASOL" or p4.upper()!= "CRAVO"or p4.upper()!= "BROMELIA"or p4.upper()!= "BEGONIA":
            print("O dado colocado está inválido")
            p4 = str(input("Qual a quarta palavra que você achou? "))

    print("")
    #Colocar o caça daqui
    print("H R E X O E B Y J C N L Z J G ")
    print("Y I O T C A T I V S I O G E N ")
    print("M L B S P X A R W W M S C R J ")
    print("F L J I A O B T F F V A B L K ")
    print("T Z L V C E N P E O M R Z O R ")
    print("F U U J G X W T B L U I V T P ")
    print("T B Z O W X R R R D O G H E R ")
    print("B W N J I K A P O Y E I G O F ")
    print("X I L Z G G I A M N Q B V I D ")
    print("A J K C Q U T M E O Y P F T G ")
    print("A I N U T E P H L P O M Z L J ")
    print("D V R Q W K V S I H M A J Z V ")
    print("A G S Q T U B V A C R A V O U ")
    print("G C S K A K B M G K J F Q T Z ")
    print("M O G G W G S B T R L J U A L ")
    #Até aqui
    print("")
    p5 = str(input("Qual a quinta palavra que você achou? "))
    while cont5 !=1:
        if p5==p1 or p5==p2 or p5==p3 or p5==p4:
            print("A palavra está repetida")
            p5 = str (input("Qual a quinta palavra que você achou? "))
        #Inserir palavras
        elif p5.upper() == "VIOLETA" or p5.upper()== "TULIPA" or p5.upper()== "ROSA" or p5.upper()== "PETUNIA" or p5.upper()== "GIRASOL" or p5.upper()== "CRAVO"or p5.upper()== "BROMELIA"or p5.upper()== "BEGONIA":
            print("A palavra achada foi ",p5)
            cont5 += 1
            pontuacao_rodada += len(p5)*p4x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p5.upper() != "VIOLETA" or p5.upper()!= "TULIPA" or p5.upper()!= "ROSA" or p5.upper()!= "PETUNIA" or p5.upper()!= "GIRASOL" or p5.upper()!= "CRAVO"or p5.upper()!= "BROMELIA"or p5.upper()!= "BEGONIA":
            print("O dado colocado está inválido")
            p5 = str(input("Qual a quinta palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("H R E X O E B Y J C N L Z J G ")
    print("Y I O T C A T I V S I O G E N ")
    print("M L B S P X A R W W M S C R J ")
    print("F L J I A O B T F F V A B L K ")
    print("T Z L V C E N P E O M R Z O R ")
    print("F U U J G X W T B L U I V T P ")
    print("T B Z O W X R R R D O G H E R ")
    print("B W N J I K A P O Y E I G O F ")
    print("X I L Z G G I A M N Q B V I D ")
    print("A J K C Q U T M E O Y P F T G ")
    print("A I N U T E P H L P O M Z L J ")
    print("D V R Q W K V S I H M A J Z V ")
    print("A G S Q T U B V A C R A V O U ")
    print("G C S K A K B M G K J F Q T Z ")
    print("M O G G W G S B T R L J U A L ")
    #Até aqui
    print("")
    p6 = str(input("Qual a sexta palavra que você achou? "))
    while cont6 !=1:
        if p6==p1 or p6==p2 or p6==p3 or p6==p4 or p6==p5:
            print("A palavra está repetida")
            p6 = str (input("Qual a sexta palavra que você achou? "))
        #Inserir palavras
        elif p6.upper() == "VIOLETA" or p6.upper()== "TULIPA" or p6.upper()== "ROSA" or p6.upper()== "PETUNIA" or p6.upper()== "GIRASOL" or p6.upper()== "CRAVO"or p6.upper()== "BROMELIA"or p6.upper()== "BEGONIA":
            print("A palavra achada foi ",p6)
            cont6 += 1
            pontuacao_rodada += len(p6)*p3x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p6.upper() != "VIOLETA" or p6.upper()!= "TULIPA" or p6.upper()!= "ROSA" or p6.upper()!= "PETUNIA" or p6.upper()!= "GIRASOL" or p6.upper()!= "CRAVO"or p6.upper()!= "BROMELIA"or p6.upper()!= "BEGONIA":
            print("O dado colocado está inválido")
            p6 = str(input("Qual a sexta palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("H R E X O E B Y J C N L Z J G ")
    print("Y I O T C A T I V S I O G E N ")
    print("M L B S P X A R W W M S C R J ")
    print("F L J I A O B T F F V A B L K ")
    print("T Z L V C E N P E O M R Z O R ")
    print("F U U J G X W T B L U I V T P ")
    print("T B Z O W X R R R D O G H E R ")
    print("B W N J I K A P O Y E I G O F ")
    print("X I L Z G G I A M N Q B V I D ")
    print("A J K C Q U T M E O Y P F T G ")
    print("A I N U T E P H L P O M Z L J ")
    print("D V R Q W K V S I H M A J Z V ")
    print("A G S Q T U B V A C R A V O U ")
    print("G C S K A K B M G K J F Q T Z ")
    print("M O G G W G S B T R L J U A L ")
    #Até aqui
    print("")
    p7 = str(input("Qual a sétima palavra que você achou? "))
    while cont7 !=1:
        if p7==p1 or p7==p2 or p7==p3 or p7==p4 or p7==p5 or p7==p6:
            print("A palavra está repetida")
            p7 = str (input("Qual a sétima palavra que você achou? "))
        #Inserir palavras
        elif p7.upper() == "VIOLETA" or p7.upper()== "TULIPA" or p7.upper()== "ROSA" or p7.upper()== "PETUNIA" or p7.upper()== "GIRASOL" or p7.upper()== "CRAVO"or p7.upper()== "BROMELIA"or p7.upper()== "BEGONIA":
            print("A palavra achada foi ",p7)
            cont7 += 1
            pontuacao_rodada += len(p7)*p2x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p7.upper() != "VIOLETA" or p7.upper()!= "TULIPA" or p7.upper()!= "ROSA" or p7.upper()!= "PETUNIA" or p7.upper()!= "GIRASOL" or p7.upper()!= "CRAVO"or p7.upper()!= "BROMELIA"or p7.upper()!= "BEGONIA":
            print("O dado colocado está inválido")
            p7 = str(input("Qual a sétima palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("H R E X O E B Y J C N L Z J G ")
    print("Y I O T C A T I V S I O G E N ")
    print("M L B S P X A R W W M S C R J ")
    print("F L J I A O B T F F V A B L K ")
    print("T Z L V C E N P E O M R Z O R ")
    print("F U U J G X W T B L U I V T P ")
    print("T B Z O W X R R R D O G H E R ")
    print("B W N J I K A P O Y E I G O F ")
    print("X I L Z G G I A M N Q B V I D ")
    print("A J K C Q U T M E O Y P F T G ")
    print("A I N U T E P H L P O M Z L J ")
    print("D V R Q W K V S I H M A J Z V ")
    print("A G S Q T U B V A C R A V O U ")
    print("G C S K A K B M G K J F Q T Z ")
    print("M O G G W G S B T R L J U A L ")
    #Até aqui
    print("")
    p8 = str(input("Qual a oitava palavra que você achou? "))
    while cont8 !=1:
        if p8==p1 or p8==p2 or p8==p3 or p8==p4 or p8==p5 or p8==p6 or p8==p7:
            print("A palavra está repetida")
            p8 = str (input("Qual a oitava palavra que você achou? "))
        #Inserir palavras
        elif p8.upper() == "VIOLETA" or p8.upper()== "TULIPA" or p8.upper()== "ROSA" or p8.upper()== "PETUNIA" or p8.upper()== "GIRASOL" or p8.upper()== "CRAVO"or p8.upper()== "BROMELIA"or p8.upper()== "BEGONIA":
            print("A palavra achada foi ",p8)
            cont8 += 1
            pontuacao_rodada += len(p8)*p1x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p8.upper() != "VIOLETA" or p8.upper()!= "TULIPA" or p8.upper()!= "ROSA" or p8.upper()!= "PETUNIA" or p8.upper()!= "GIRASOL" or p8.upper()!= "CRAVO"or p8.upper()!= "BROMELIA"or p8.upper()!= "BEGONIA":
            print("O dado colocado está inválido")
            p8 = str(input("Qual a oitava palavra que você achou? "))
    print("")
    print("A primeira palavra achada foi:",p1)
    print("A segunda palavra achada foi:",p2)
    print("A terceira palavra achada foi:",p3)
    print("A quarta palavra achada foi:",p4)
    print("A quinta palavra achada foi:",p5)
    print("A sexta palavra achada foi:",p6)
    print("A sétima palavra achada foi:",p7)
    print("A oitava palavra achada foi:",p8)
    print("")
    print("A sua pontuação nessa rodada foi: ",pontuacao_rodada)
    print("A sua pontuação total é:",pontuacao_total)
    print("")
    print("O quadro de respostas é:")
    print("")
    #quadro de respostas daqui
    print("+ R + + + + + + + + + L + + + ")
    print("+ + O + + A + + + + + O + + + ")
    print("+ + + S P + A + + + + S + + + ")
    print("+ + + I A + B T + + + A + + + ")
    print("+ + L + + E + + E + + R + + + ")
    print("+ U + + G + + + B L + I + + + ")
    print("T + + O + + + + R + O G + + + ")
    print("+ + N + + + + + O + + I + + + ")
    print("+ I + + + + + + M + + + V + + ")
    print("A + + + + + + + E + + + + + + ")
    print("A I N U T E P + L + + + + + + ")
    print("+ + + + + + + + I + + + + + + ")
    print("+ + + + + + + + A C R A V O + ")
    print("+ + + + + + + + + + + + + + + ")
    print("+ + + + + + + + + + + + + + + ")
    #até aqui
    ##################################################
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    cont5 = 0
    cont6 = 0
    cont7 = 0
    cont8 = 0
    pontuacao_rodada = 0
    print("")
    print("Segunda Guerra Mundial - FASE 13")#titulo e fase
    print("")
    #FASE1313131313131313131313131313131313131313131313131313131313131313131313131313131313131313131313131313131313131313131313131313131313131313131313131313
    print("")
    #Colocar o caça daqui
    print("Z L B X D N Q H E H B F O D P ")
    print("C F G S I N I L O S S U M I E ")
    print("S I Z K B R V L E W R C S X A ")
    print("I S T R E D O A U S X F I V R ")
    print("W W O L J C S T A L I N Z U L ")
    print("G F T D A Z Z S B G Z H A R H ")
    print("P I S U A C I M E T H G N R A ")
    print("H W S G R I N X G I N V X B R ")
    print("X T I I C H L H R O X J O J B ")
    print("O D X K T O E A H M T O Y B O ")
    print("Z B W I M S P E Y S W X J S R ")
    print("E I N K B A O Y P D I T C B M ")
    print("O Z U H O C E E C C P B I C V ")
    print("O E U J O T M L D S Q B N F N ")
    print("P M R F E X I V V P N X I K M ")
    #Até aqui
    '''pearlharbor,holocausto,mussolini, aliados, nazismo ,hitler, stalin, eixo'''
    print("")
    print("Existem 8 palavras nesse caça palavras (escreva sem espaço e acentos)")
    print("")
    #COLOCAR AS PALAVRAS
    p1= str(input("Qual a primeira palavra que você achou? "))
    while cont1 != 1:
        #Inserir palavras
        if p1.upper() == "STALIN" or p1.upper()== "PEARLHARBOR" or p1.upper()== "NAZISMO" or p1.upper()== "MUSSOLINI" or p1.upper()== "HOLOCAUSTO" or p1.upper()== "HITLER" or p1.upper()== "EIXO" or p1.upper()== "ALIADOS":
            print("A palavra achada foi ",p1)
            cont1 += 1
            pontuacao_rodada += len(p1)*p8x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p1.upper() != "STALIN" or p1.upper()!= "PEARLHARBOR" or p1.upper()!= "NAZISMO" or p1.upper()!= "MUSSOLINI" or p1.upper()!= "HOLOCAUSTO" or p1.upper()!= "HITLER" or p1.upper()!= "EIXO" or p1.upper()!= "ALIADOS":
            print("O dado colocado está inválido")
            p1= str(input("Qual a primeira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("Z L B X D N Q H E H B F O D P ")
    print("C F G S I N I L O S S U M I E ")
    print("S I Z K B R V L E W R C S X A ")
    print("I S T R E D O A U S X F I V R ")
    print("W W O L J C S T A L I N Z U L ")
    print("G F T D A Z Z S B G Z H A R H ")
    print("P I S U A C I M E T H G N R A ")
    print("H W S G R I N X G I N V X B R ")
    print("X T I I C H L H R O X J O J B ")
    print("O D X K T O E A H M T O Y B O ")
    print("Z B W I M S P E Y S W X J S R ")
    print("E I N K B A O Y P D I T C B M ")
    print("O Z U H O C E E C C P B I C V ")
    print("O E U J O T M L D S Q B N F N ")
    print("P M R F E X I V V P N X I K M ")
    #Até aqui
    print("")
    p2 = str(input("Qual a segunda palavra que você achou? "))
    while cont2 != 1:
        if p2.upper() == p1.upper():
            print("A palavra está repetida")
            p2 = str(input("Qual a segunda palavra que você achou? "))
        #Inserir palavras
        elif p2.upper() == "STALIN" or p2.upper()== "PEARLHARBOR" or p2.upper()== "NAZISMO" or p2.upper()== "MUSSOLINI" or p2.upper()== "HOLOCAUSTO" or p2.upper()== "HITLER"or p2.upper()== "EIXO"or p2.upper()== "ALIADOS":
            print("A palavra achada foi ",p2)
            cont2 += 1
            pontuacao_rodada += len(p2)*p7x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p2.upper() != "STALIN" or p2.upper()!= "PEARLHARBOR" or p2.upper()!= "NAZISMO" or p2.upper()!= "MUSSOLINI" or p2.upper()!= "HOLOCAUSTO" or p2.upper()!= "HITLER"or p2.upper()!= "EIXO"or p2.upper()!= "ALIADOS":
            print("O dado colocado está inválido")
            p2= str(input("Qual a segunda palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("Z L B X D N Q H E H B F O D P ")
    print("C F G S I N I L O S S U M I E ")
    print("S I Z K B R V L E W R C S X A ")
    print("I S T R E D O A U S X F I V R ")
    print("W W O L J C S T A L I N Z U L ")
    print("G F T D A Z Z S B G Z H A R H ")
    print("P I S U A C I M E T H G N R A ")
    print("H W S G R I N X G I N V X B R ")
    print("X T I I C H L H R O X J O J B ")
    print("O D X K T O E A H M T O Y B O ")
    print("Z B W I M S P E Y S W X J S R ")
    print("E I N K B A O Y P D I T C B M ")
    print("O Z U H O C E E C C P B I C V ")
    print("O E U J O T M L D S Q B N F N ")
    print("P M R F E X I V V P N X I K M ")
    #Até aqui
    print("")
    p3 = str(input("Qual a terceira palavra que você achou? "))
    while cont3 != 1:
        if p3.upper()==p1.upper() or p3.upper()==p2.upper():
            print("A palavra está repetida")
            p3 = str(input("Qual a terceira palavra que você achou? "))
        #Inserir palavras
        elif p3.upper() == "STALIN" or p3.upper()== "PEARLHARBOR" or p3.upper()== "NAZISMO" or p3.upper()== "MUSSOLINI" or p3.upper()== "HOLOCAUSTO" or p3.upper()== "HITLER"or p3.upper()== "EIXO"or p3.upper()== "ALIADOS":
            print("A palavra achada foi ",p3)
            cont3 += 1
            pontuacao_rodada += len(p3)*p6x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p3.upper() != "STALIN" or p3.upper()!= "PEARLHARBOR" or p3.upper()!= "NAZISMO" or p3.upper()!= "MUSSOLINI" or p3.upper()!= "HOLOCAUSTO" or p3.upper()!= "HITLER"or p3.upper()!= "EIXO"or p3.upper()!= "ALIADOS":
            print("O dado colocado está inválido")
            p3= str(input("Qual a terceira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("Z L B X D N Q H E H B F O D P ")
    print("C F G S I N I L O S S U M I E ")
    print("S I Z K B R V L E W R C S X A ")
    print("I S T R E D O A U S X F I V R ")
    print("W W O L J C S T A L I N Z U L ")
    print("G F T D A Z Z S B G Z H A R H ")
    print("P I S U A C I M E T H G N R A ")
    print("H W S G R I N X G I N V X B R ")
    print("X T I I C H L H R O X J O J B ")
    print("O D X K T O E A H M T O Y B O ")
    print("Z B W I M S P E Y S W X J S R ")
    print("E I N K B A O Y P D I T C B M ")
    print("O Z U H O C E E C C P B I C V ")
    print("O E U J O T M L D S Q B N F N ")
    print("P M R F E X I V V P N X I K M ")
    #Até aqui
    print("")
    p4 = str(input("Qual a quarta palavra que você achou? "))
    while cont4 != 1:
        if p4==p1 or p4==p2 or p4==p3:
            print("A palavra está repetida")
            p4 = str (input("Qual a quarta palavra que você achou? "))
        #Inserir palavras
        elif p4.upper() == "STALIN" or p4.upper()== "PEARLHARBOR" or p4.upper()== "NAZISMO" or p4.upper()== "MUSSOLINI" or p4.upper()== "HOLOCAUSTO" or p4.upper()== "HITLER"or p4.upper()== "EIXO"or p4.upper()== "ALIADOS":
            print("A palavra achada foi ",p4)
            cont4 += 1
            pontuacao_rodada += len(p4)*p5x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p4.upper() != "STALIN" or p4.upper()!= "PEARLHARBOR" or p4.upper()!= "NAZISMO" or p4.upper()!= "MUSSOLINI" or p4.upper()!= "HOLOCAUSTO" or p4.upper()!= "HITLER"or p4.upper()!= "EIXO"or p4.upper()!= "ALIADOS":
            print("O dado colocado está inválido")
            p4 = str(input("Qual a quarta palavra que você achou? "))

    print("")
    #Colocar o caça daqui
    print("Z L B X D N Q H E H B F O D P ")
    print("C F G S I N I L O S S U M I E ")
    print("S I Z K B R V L E W R C S X A ")
    print("I S T R E D O A U S X F I V R ")
    print("W W O L J C S T A L I N Z U L ")
    print("G F T D A Z Z S B G Z H A R H ")
    print("P I S U A C I M E T H G N R A ")
    print("H W S G R I N X G I N V X B R ")
    print("X T I I C H L H R O X J O J B ")
    print("O D X K T O E A H M T O Y B O ")
    print("Z B W I M S P E Y S W X J S R ")
    print("E I N K B A O Y P D I T C B M ")
    print("O Z U H O C E E C C P B I C V ")
    print("O E U J O T M L D S Q B N F N ")
    print("P M R F E X I V V P N X I K M ")
    #Até aqui
    print("")
    p5 = str(input("Qual a quinta palavra que você achou? "))
    while cont5 !=1:
        if p5==p1 or p5==p2 or p5==p3 or p5==p4:
            print("A palavra está repetida")
            p5 = str (input("Qual a quinta palavra que você achou? "))
        #Inserir palavras
        elif p5.upper() == "STALIN" or p5.upper()== "PEARLHARBOR" or p5.upper()== "NAZISMO" or p5.upper()== "MUSSOLINI" or p5.upper()== "HOLOCAUSTO" or p5.upper()== "HITLER"or p5.upper()== "EIXO"or p5.upper()== "ALIADOS":
            print("A palavra achada foi ",p5)
            cont5 += 1
            pontuacao_rodada += len(p5)*p4x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p5.upper() != "STALIN" or p5.upper()!= "PEARLHARBOR" or p5.upper()!= "NAZISMO" or p5.upper()!= "MUSSOLINI" or p5.upper()!= "HOLOCAUSTO" or p5.upper()!= "HITLER"or p5.upper()!= "EIXO"or p5.upper()!= "ALIADOS":
            print("O dado colocado está inválido")
            p5 = str(input("Qual a quinta palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("Z L B X D N Q H E H B F O D P ")
    print("C F G S I N I L O S S U M I E ")
    print("S I Z K B R V L E W R C S X A ")
    print("I S T R E D O A U S X F I V R ")
    print("W W O L J C S T A L I N Z U L ")
    print("G F T D A Z Z S B G Z H A R H ")
    print("P I S U A C I M E T H G N R A ")
    print("H W S G R I N X G I N V X B R ")
    print("X T I I C H L H R O X J O J B ")
    print("O D X K T O E A H M T O Y B O ")
    print("Z B W I M S P E Y S W X J S R ")
    print("E I N K B A O Y P D I T C B M ")
    print("O Z U H O C E E C C P B I C V ")
    print("O E U J O T M L D S Q B N F N ")
    print("P M R F E X I V V P N X I K M ")
    #Até aqui
    print("")
    p6 = str(input("Qual a sexta palavra que você achou? "))
    while cont6 !=1:
        if p6==p1 or p6==p2 or p6==p3 or p6==p4 or p6==p5:
            print("A palavra está repetida")
            p6 = str (input("Qual a sexta palavra que você achou? "))
        #Inserir palavras
        elif p6.upper() == "STALIN" or p6.upper()== "PEARLHARBOR" or p6.upper()== "NAZISMO" or p6.upper()== "MUSSOLINI" or p6.upper()== "HOLOCAUSTO" or p6.upper()== "HITLER"or p6.upper()== "EIXO"or p6.upper()== "ALIADOS":
            print("A palavra achada foi ",p6)
            cont6 += 1
            pontuacao_rodada += len(p6)*p3x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p6.upper() != "STALIN" or p6.upper()!= "PEARLHARBOR" or p6.upper()!= "NAZISMO" or p6.upper()!= "MUSSOLINI" or p6.upper()!= "HOLOCAUSTO" or p6.upper()!= "HITLER"or p6.upper()!= "EIXO"or p6.upper()!= "ALIADOS":
            print("O dado colocado está inválido")
            p6 = str(input("Qual a sexta palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("Z L B X D N Q H E H B F O D P ")
    print("C F G S I N I L O S S U M I E ")
    print("S I Z K B R V L E W R C S X A ")
    print("I S T R E D O A U S X F I V R ")
    print("W W O L J C S T A L I N Z U L ")
    print("G F T D A Z Z S B G Z H A R H ")
    print("P I S U A C I M E T H G N R A ")
    print("H W S G R I N X G I N V X B R ")
    print("X T I I C H L H R O X J O J B ")
    print("O D X K T O E A H M T O Y B O ")
    print("Z B W I M S P E Y S W X J S R ")
    print("E I N K B A O Y P D I T C B M ")
    print("O Z U H O C E E C C P B I C V ")
    print("O E U J O T M L D S Q B N F N ")
    print("P M R F E X I V V P N X I K M ")
    #Até aqui
    print("")
    p7 = str(input("Qual a sétima palavra que você achou? "))
    while cont7 !=1:
        if p7==p1 or p7==p2 or p7==p3 or p7==p4 or p7==p5 or p7==p6:
            print("A palavra está repetida")
            p7 = str (input("Qual a sétima palavra que você achou? "))
        #Inserir palavras
        elif p7.upper() == "STALIN" or p7.upper()== "PEARLHARBOR" or p7.upper()== "NAZISMO" or p7.upper()== "MUSSOLINI" or p7.upper()== "HOLOCAUSTO" or p7.upper()== "HITLER"or p7.upper()== "EIXO"or p7.upper()== "ALIADOS":
            print("A palavra achada foi ",p7)
            cont7 += 1
            pontuacao_rodada += len(p7)*p2x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p7.upper() != "STALIN" or p7.upper()!= "PEARLHARBOR" or p7.upper()!= "NAZISMO" or p7.upper()!= "MUSSOLINI" or p7.upper()!= "HOLOCAUSTO" or p7.upper()!= "HITLER"or p7.upper()!= "EIXO"or p7.upper()!= "ALIADOS":
            print("O dado colocado está inválido")
            p7 = str(input("Qual a sétima palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("Z L B X D N Q H E H B F O D P ")
    print("C F G S I N I L O S S U M I E ")
    print("S I Z K B R V L E W R C S X A ")
    print("I S T R E D O A U S X F I V R ")
    print("W W O L J C S T A L I N Z U L ")
    print("G F T D A Z Z S B G Z H A R H ")
    print("P I S U A C I M E T H G N R A ")
    print("H W S G R I N X G I N V X B R ")
    print("X T I I C H L H R O X J O J B ")
    print("O D X K T O E A H M T O Y B O ")
    print("Z B W I M S P E Y S W X J S R ")
    print("E I N K B A O Y P D I T C B M ")
    print("O Z U H O C E E C C P B I C V ")
    print("O E U J O T M L D S Q B N F N ")
    print("P M R F E X I V V P N X I K M ")
    #Até aqui
    print("")
    p8 = str(input("Qual a oitava palavra que você achou? "))
    while cont8 !=1:
        if p8==p1 or p8==p2 or p8==p3 or p8==p4 or p8==p5 or p8==p6 or p8==p7:
            print("A palavra está repetida")
            p8 = str (input("Qual a oitava palavra que você achou? "))
        #Inserir palavras
        elif p8.upper() == "STALIN" or p8.upper()== "PEARLHARBOR" or p8.upper()== "NAZISMO" or p8.upper()== "MUSSOLINI" or p8.upper()== "HOLOCAUSTO" or p8.upper()== "HITLER"or p8.upper()== "EIXO"or p8.upper()== "ALIADOS":
            print("A palavra achada foi ",p8)
            cont8 += 1
            pontuacao_rodada += len(p8)*p1x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p8.upper() != "STALIN" or p8.upper()!= "PEARLHARBOR" or p8.upper()!= "NAZISMO" or p8.upper()!= "MUSSOLINI" or p8.upper()!= "HOLOCAUSTO" or p8.upper()!= "HITLER"or p8.upper()!= "EIXO"or p8.upper()!= "ALIADOS":
            print("O dado colocado está inválido")
            p8 = str(input("Qual a oitava palavra que você achou? "))
    print("")
    print("A primeira palavra achada foi:",p1)
    print("A segunda palavra achada foi:",p2)
    print("A terceira palavra achada foi:",p3)
    print("A quarta palavra achada foi:",p4)
    print("A quinta palavra achada foi:",p5)
    print("A sexta palavra achada foi:",p6)
    print("A sétima palavra achada foi:",p7)
    print("A oitava palavra achada foi:",p8)
    print("")
    print("A sua pontuação nessa rodada foi: ",pontuacao_rodada)
    print("A sua pontuação total é:",pontuacao_total)
    print("")
    print("O quadro de respostas é:")
    print("")
    #quadro de respostas daqui
    print("+ + + + + + + + + H + + O + P ")
    print("+ + + + I N I L O S S U M + E ")
    print("+ + + + + R + L + + + + S + A ")
    print("+ S + + E + O + + + + + I + R ")
    print("+ + O L + C S T A L I N Z + L ")
    print("+ + T D A + + + + + + + A + H ")
    print("+ I + U A + + + E + + + N + A ")
    print("H + S + + I + + + I + + + + R ")
    print("+ T + + + + L + + + X + + + B ")
    print("O + + + + + + A + + + O + + O ")
    print("+ + + + + + + + + + + + + + R ")
    print("+ + + + + + + + + + + + + + + ")
    print("+ + + + + + + + + + + + + + + ")
    print("+ + + + + + + + + + + + + + + ")
    print("+ + + + + + + + + + + + + + + ")
    #até aqui

    ##################################################
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    cont5 = 0
    cont6 = 0
    cont7 = 0
    cont8 = 0
    pontuacao_rodada = 0
    print("")
    print("Iluminismo - FASE 14")#titulo e fase
    print("")
    #FASE141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414
    print("")
    #Colocar o caça daqui
    print("S P M N P V U J U Z G J M E Q ")
    print("K E A O J E K O T Q O J L Z Y ")
    print("D F Z V N K W V W H B Y A D M ")
    print("R C O U M T E U N G A V F U D ")
    print("R K N F L Z E L X B K I D V C ")
    print("W Y I Z V S O S E K O W A L E ")
    print("P X P B G C A R Q A A R V U G ")
    print("W T S Y K C R D V U S N I C Y ")
    print("E E H E H E C W O X I U D Q H ")
    print("Q A C E I I Z Z L L E E H P W ")
    print("T Q U P L W I M L G U E U G L ")
    print("R E R I A T L O V C D C M E U ")
    print("I S A A C N E W T O N Y E C W ")
    print("C D B O T Y J W Z X S K V S I ")
    print("W S X H P Y B M P R A P M Q S ")
    #Até aqui
    '''seculodasluzes
    , Baruchspinoza
    , montesquieu
    , pierrebayle
    , isaacnewton
    , davidhume
    , johnlocke
    , voltaire'''
    print("")
    print("Existem 8 palavras nesse caça palavras (escreva sem espaço e acentos)")
    print("")
    #COLOCAR AS PALAVRAS
    p1= str(input("Qual a primeira palavra que você achou? "))
    while cont1 != 1:
        #Inserir palavras
        if p1.upper() == "VOLTAIRE" or p1.upper()== "SECULODASLUZES" or p1.upper()== "PIERREBAYLE" or p1.upper()== "MONTESQUIEU" or p1.upper()== "JOHNLOCKE" or p1.upper()== "ISAACNEWTON" or p1.upper()== "DAVIDHUME" or p1.upper()== "BARUCHSPINOZA":
            print("A palavra achada foi ",p1)
            cont1 += 1
            pontuacao_rodada += len(p1)*p8x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p1.upper() != "VOLTAIRE" or p1.upper()!= "SECULODASLUZES" or p1.upper()!= "PIERREBAYLE" or p1.upper()!= "MONTESQUIEU" or p1.upper()!= "JOHNLOCKE" or p1.upper()!= "ISAACNEWTON" or p1.upper()!= "DAVIDHUME" or p1.upper()!= "BARUCHSPINOZA":
            print("O dado colocado está inválido")
            p1= str(input("Qual a primeira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("S P M N P V U J U Z G J M E Q ")
    print("K E A O J E K O T Q O J L Z Y ")
    print("D F Z V N K W V W H B Y A D M ")
    print("R C O U M T E U N G A V F U D ")
    print("R K N F L Z E L X B K I D V C ")
    print("W Y I Z V S O S E K O W A L E ")
    print("P X P B G C A R Q A A R V U G ")
    print("W T S Y K C R D V U S N I C Y ")
    print("E E H E H E C W O X I U D Q H ")
    print("Q A C E I I Z Z L L E E H P W ")
    print("T Q U P L W I M L G U E U G L ")
    print("R E R I A T L O V C D C M E U ")
    print("I S A A C N E W T O N Y E C W ")
    print("C D B O T Y J W Z X S K V S I ")
    print("W S X H P Y B M P R A P M Q S ")
    #Até aqui
    print("")
    p2 = str(input("Qual a segunda palavra que você achou? "))
    while cont2 != 1:
        if p2.upper() == p1.upper():
            print("A palavra está repetida")
            p2 = str(input("Qual a segunda palavra que você achou? "))
        #Inserir palavras
        elif p2.upper() == "VOLTAIRE" or p2.upper()== "SECULODASLUZES" or p2.upper()== "PIERREBAYLE" or p2.upper()== "MONTESQUIEU" or p2.upper()== "JOHNLOCKE" or p2.upper()== "ISAACNEWTON"or p2.upper()== "DAVIDHUME"or p2.upper()== "BARUCHSPINOZA":
            print("A palavra achada foi ",p2)
            cont2 += 1
            pontuacao_rodada += len(p2)*p7x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p2.upper() != "VOLTAIRE" or p2.upper()!= "SECULODASLUZES" or p2.upper()!= "PIERREBAYLE" or p2.upper()!= "MONTESQUIEU" or p2.upper()!= "JOHNLOCKE" or p2.upper()!= "ISAACNEWTON"or p2.upper()!= "DAVIDHUME"or p2.upper()!= "BARUCHSPINOZA":
            print("O dado colocado está inválido")
            p2= str(input("Qual a segunda palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("S P M N P V U J U Z G J M E Q ")
    print("K E A O J E K O T Q O J L Z Y ")
    print("D F Z V N K W V W H B Y A D M ")
    print("R C O U M T E U N G A V F U D ")
    print("R K N F L Z E L X B K I D V C ")
    print("W Y I Z V S O S E K O W A L E ")
    print("P X P B G C A R Q A A R V U G ")
    print("W T S Y K C R D V U S N I C Y ")
    print("E E H E H E C W O X I U D Q H ")
    print("Q A C E I I Z Z L L E E H P W ")
    print("T Q U P L W I M L G U E U G L ")
    print("R E R I A T L O V C D C M E U ")
    print("I S A A C N E W T O N Y E C W ")
    print("C D B O T Y J W Z X S K V S I ")
    print("W S X H P Y B M P R A P M Q S ")
    #Até aqui
    print("")
    p3 = str(input("Qual a terceira palavra que você achou? "))
    while cont3 != 1:
        if p3.upper()==p1.upper() or p3.upper()==p2.upper():
            print("A palavra está repetida")
            p3 = str(input("Qual a terceira palavra que você achou? "))
        #Inserir palavras
        elif p3.upper() == "VOLTAIRE" or p3.upper()== "SECULODASLUZES" or p3.upper()== "PIERREBAYLE" or p3.upper()== "MONTESQUIEU" or p3.upper()== "JOHNLOCKE" or p3.upper()== "ISAACNEWTON"or p3.upper()== "DAVIDHUME"or p3.upper()== "BARUCHSPINOZA":
            print("A palavra achada foi ",p3)
            cont3 += 1
            pontuacao_rodada += len(p3)*p6x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p3.upper() != "VOLTAIRE" or p3.upper()!= "SECULODASLUZES" or p3.upper()!= "PIERREBAYLE" or p3.upper()!= "MONTESQUIEU" or p3.upper()!= "JOHNLOCKE" or p3.upper()!= "ISAACNEWTON"or p3.upper()!= "DAVIDHUME"or p3.upper()!= "BARUCHSPINOZA":
            print("O dado colocado está inválido")
            p3= str(input("Qual a terceira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("S P M N P V U J U Z G J M E Q ")
    print("K E A O J E K O T Q O J L Z Y ")
    print("D F Z V N K W V W H B Y A D M ")
    print("R C O U M T E U N G A V F U D ")
    print("R K N F L Z E L X B K I D V C ")
    print("W Y I Z V S O S E K O W A L E ")
    print("P X P B G C A R Q A A R V U G ")
    print("W T S Y K C R D V U S N I C Y ")
    print("E E H E H E C W O X I U D Q H ")
    print("Q A C E I I Z Z L L E E H P W ")
    print("T Q U P L W I M L G U E U G L ")
    print("R E R I A T L O V C D C M E U ")
    print("I S A A C N E W T O N Y E C W ")
    print("C D B O T Y J W Z X S K V S I ")
    print("W S X H P Y B M P R A P M Q S ")
    #Até aqui
    print("")
    p4 = str(input("Qual a quarta palavra que você achou? "))
    while cont4 != 1:
        if p4==p1 or p4==p2 or p4==p3:
            print("A palavra está repetida")
            p4 = str (input("Qual a quarta palavra que você achou? "))
        #Inserir palavras
        elif p4.upper() == "VOLTAIRE" or p4.upper()== "SECULODASLUZES" or p4.upper()== "PIERREBAYLE" or p4.upper()== "MONTESQUIEU" or p4.upper()== "JOHNLOCKE" or p4.upper()== "ISAACNEWTON"or p4.upper()== "DAVIDHUME"or p4.upper()== "BARUCHSPINOZA":
            print("A palavra achada foi ",p4)
            cont4 += 1
            pontuacao_rodada += len(p4)*p5x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p4.upper() != "VOLTAIRE" or p4.upper()!= "SECULODASLUZES" or p4.upper()!= "PIERREBAYLE" or p4.upper()!= "MONTESQUIEU" or p4.upper()!= "JOHNLOCKE" or p4.upper()!= "ISAACNEWTON"or p4.upper()!= "DAVIDHUME"or p4.upper()!= "BARUCHSPINOZA":
            print("O dado colocado está inválido")
            p4 = str(input("Qual a quarta palavra que você achou? "))

    print("")
    #Colocar o caça daqui
    print("S P M N P V U J U Z G J M E Q ")
    print("K E A O J E K O T Q O J L Z Y ")
    print("D F Z V N K W V W H B Y A D M ")
    print("R C O U M T E U N G A V F U D ")
    print("R K N F L Z E L X B K I D V C ")
    print("W Y I Z V S O S E K O W A L E ")
    print("P X P B G C A R Q A A R V U G ")
    print("W T S Y K C R D V U S N I C Y ")
    print("E E H E H E C W O X I U D Q H ")
    print("Q A C E I I Z Z L L E E H P W ")
    print("T Q U P L W I M L G U E U G L ")
    print("R E R I A T L O V C D C M E U ")
    print("I S A A C N E W T O N Y E C W ")
    print("C D B O T Y J W Z X S K V S I ")
    print("W S X H P Y B M P R A P M Q S ")
    #Até aqui
    print("")
    p5 = str(input("Qual a quinta palavra que você achou? "))
    while cont5 !=1:
        if p5==p1 or p5==p2 or p5==p3 or p5==p4:
            print("A palavra está repetida")
            p5 = str (input("Qual a quinta palavra que você achou? "))
        #Inserir palavras
        elif p5.upper() == "VOLTAIRE" or p5.upper()== "SECULODASLUZES" or p5.upper()== "PIERREBAYLE" or p5.upper()== "MONTESQUIEU" or p5.upper()== "JOHNLOCKE" or p5.upper()== "ISAACNEWTON"or p5.upper()== "DAVIDHUME"or p5.upper()== "BARUCHSPINOZA":
            print("A palavra achada foi ",p5)
            cont5 += 1
            pontuacao_rodada += len(p5)*p4x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p5.upper() != "VOLTAIRE" or p5.upper()!= "SECULODASLUZES" or p5.upper()!= "PIERREBAYLE" or p5.upper()!= "MONTESQUIEU" or p5.upper()!= "JOHNLOCKE" or p5.upper()!= "ISAACNEWTON"or p5.upper()!= "DAVIDHUME"or p5.upper()!= "BARUCHSPINOZA":
            print("O dado colocado está inválido")
            p5 = str(input("Qual a quinta palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("S P M N P V U J U Z G J M E Q ")
    print("K E A O J E K O T Q O J L Z Y ")
    print("D F Z V N K W V W H B Y A D M ")
    print("R C O U M T E U N G A V F U D ")
    print("R K N F L Z E L X B K I D V C ")
    print("W Y I Z V S O S E K O W A L E ")
    print("P X P B G C A R Q A A R V U G ")
    print("W T S Y K C R D V U S N I C Y ")
    print("E E H E H E C W O X I U D Q H ")
    print("Q A C E I I Z Z L L E E H P W ")
    print("T Q U P L W I M L G U E U G L ")
    print("R E R I A T L O V C D C M E U ")
    print("I S A A C N E W T O N Y E C W ")
    print("C D B O T Y J W Z X S K V S I ")
    print("W S X H P Y B M P R A P M Q S ")
    #Até aqui
    print("")
    p6 = str(input("Qual a sexta palavra que você achou? "))
    while cont6 !=1:
        if p6==p1 or p6==p2 or p6==p3 or p6==p4 or p6==p5:
            print("A palavra está repetida")
            p6 = str (input("Qual a sexta palavra que você achou? "))
        #Inserir palavras
        elif p6.upper() == "VOLTAIRE" or p6.upper()== "SECULODASLUZES" or p6.upper()== "PIERREBAYLE" or p6.upper()== "MONTESQUIEU" or p6.upper()== "JOHNLOCKE" or p6.upper()== "ISAACNEWTON"or p6.upper()== "DAVIDHUME"or p6.upper()== "BARUCHSPINOZA":
            print("A palavra achada foi ",p6)
            cont6 += 1
            pontuacao_rodada += len(p6)*p3x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p6.upper() != "VOLTAIRE" or p6.upper()!= "SECULODASLUZES" or p6.upper()!= "PIERREBAYLE" or p6.upper()!= "MONTESQUIEU" or p6.upper()!= "JOHNLOCKE" or p6.upper()!= "ISAACNEWTON"or p6.upper()!= "DAVIDHUME"or p6.upper()!= "BARUCHSPINOZA":
            print("O dado colocado está inválido")
            p6 = str(input("Qual a sexta palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("S P M N P V U J U Z G J M E Q ")
    print("K E A O J E K O T Q O J L Z Y ")
    print("D F Z V N K W V W H B Y A D M ")
    print("R C O U M T E U N G A V F U D ")
    print("R K N F L Z E L X B K I D V C ")
    print("W Y I Z V S O S E K O W A L E ")
    print("P X P B G C A R Q A A R V U G ")
    print("W T S Y K C R D V U S N I C Y ")
    print("E E H E H E C W O X I U D Q H ")
    print("Q A C E I I Z Z L L E E H P W ")
    print("T Q U P L W I M L G U E U G L ")
    print("R E R I A T L O V C D C M E U ")
    print("I S A A C N E W T O N Y E C W ")
    print("C D B O T Y J W Z X S K V S I ")
    print("W S X H P Y B M P R A P M Q S ")
    #Até aqui
    print("")
    p7 = str(input("Qual a sétima palavra que você achou? "))
    while cont7 !=1:
        if p7==p1 or p7==p2 or p7==p3 or p7==p4 or p7==p5 or p7==p6:
            print("A palavra está repetida")
            p7 = str (input("Qual a sétima palavra que você achou? "))
        #Inserir palavras
        elif p7.upper() == "VOLTAIRE" or p7.upper()== "SECULODASLUZES" or p7.upper()== "PIERREBAYLE" or p7.upper()== "MONTESQUIEU" or p7.upper()== "JOHNLOCKE" or p7.upper()== "ISAACNEWTON"or p7.upper()== "DAVIDHUME"or p7.upper()== "BARUCHSPINOZA":
            print("A palavra achada foi ",p7)
            cont7 += 1
            pontuacao_rodada += len(p7)*p2x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p7.upper() != "VOLTAIRE" or p7.upper()!= "SECULODASLUZES" or p7.upper()!= "PIERREBAYLE" or p7.upper()!= "MONTESQUIEU" or p7.upper()!= "JOHNLOCKE" or p7.upper()!= "ISAACNEWTON"or p7.upper()!= "DAVIDHUME"or p7.upper()!= "BARUCHSPINOZA":
            print("O dado colocado está inválido")
            p7 = str(input("Qual a sétima palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("S P M N P V U J U Z G J M E Q ")
    print("K E A O J E K O T Q O J L Z Y ")
    print("D F Z V N K W V W H B Y A D M ")
    print("R C O U M T E U N G A V F U D ")
    print("R K N F L Z E L X B K I D V C ")
    print("W Y I Z V S O S E K O W A L E ")
    print("P X P B G C A R Q A A R V U G ")
    print("W T S Y K C R D V U S N I C Y ")
    print("E E H E H E C W O X I U D Q H ")
    print("Q A C E I I Z Z L L E E H P W ")
    print("T Q U P L W I M L G U E U G L ")
    print("R E R I A T L O V C D C M E U ")
    print("I S A A C N E W T O N Y E C W ")
    print("C D B O T Y J W Z X S K V S I ")
    print("W S X H P Y B M P R A P M Q S ")
    #Até aqui
    print("")
    p8 = str(input("Qual a oitava palavra que você achou? "))
    while cont8 !=1:
        if p8==p1 or p8==p2 or p8==p3 or p8==p4 or p8==p5 or p8==p6 or p8==p7:
            print("A palavra está repetida")
            p8 = str (input("Qual a oitava palavra que você achou? "))
        #Inserir palavras
        elif p8.upper() == "VOLTAIRE" or p8.upper()== "SECULODASLUZES" or p8.upper()== "PIERREBAYLE" or p8.upper()== "MONTESQUIEU" or p8.upper()== "JOHNLOCKE" or p8.upper()== "ISAACNEWTON"or p8.upper()== "DAVIDHUME"or p8.upper()== "BARUCHSPINOZA":
            print("A palavra achada foi ",p8)
            cont8 += 1
            pontuacao_rodada += len(p8)*p1x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p8.upper() != "VOLTAIRE" or p8.upper()!= "SECULODASLUZES" or p8.upper()!= "PIERREBAYLE" or p8.upper()!= "MONTESQUIEU" or p8.upper()!= "JOHNLOCKE" or p8.upper()!= "ISAACNEWTON"or p8.upper()!= "DAVIDHUME"or p8.upper()!= "BARUCHSPINOZA":
            print("O dado colocado está inválido")
            p8 = str(input("Qual a oitava palavra que você achou? "))
    print("")
    print("A primeira palavra achada foi:",p1)
    print("A segunda palavra achada foi:",p2)
    print("A terceira palavra achada foi:",p3)
    print("A quarta palavra achada foi:",p4)
    print("A quinta palavra achada foi:",p5)
    print("A sexta palavra achada foi:",p6)
    print("A sétima palavra achada foi:",p7)
    print("A oitava palavra achada foi:",p8)
    print("")
    print("A sua pontuação nessa rodada foi: ",pontuacao_rodada)
    print("A sua pontuação total é:",pontuacao_total)
    print("")
    print("O quadro de respostas é:")
    print("")
    #quadro de respostas daqui
    print("S + M + + + + + + + + J + E + ")
    print("+ E A O + + + + + + O + L + + ")
    print("+ + Z + N + + + + H + Y + + + ")
    print("+ + O U + T + + N + A + + + + ")
    print("+ + N + L + E L + B + + D + + ")
    print("+ + I + + S O S E + + + A + + ")
    print("+ + P + + C A R Q + + + V + + ")
    print("+ + S + K + R D + U + + I + + ")
    print("+ + H E + E + + O + I + D + + ")
    print("+ + C + I + + + + L + E H + + ")
    print("+ + U P + + + + + + U + U + + ")
    print("+ E R I A T L O V + + C M + + ")
    print("I S A A C N E W T O N + E + + ")
    print("+ + B + + + + + + + + + + S + ")
    print("+ + + + + + + + + + + + + + + ")
    #até aqui
    ##################################################
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    cont5 = 0
    cont6 = 0
    cont7 = 0
    cont8 = 0
    pontuacao_rodada = 0
    print("")
    print("Componentes do computador - FASE 15")#titulo e fase
    print("")
    #FASE151515151515151515151515151515151515151515151515151515151515151515151515151515151515151515151515151515151515151515151515151515151515151515151515151515
    print("")
    #Colocar o caça daqui
    print("K V T U Y O T M X R K L K P E ")
    print("G V F K P W W F E K V D L T I ")
    print("J U M L R F T L R N A A E G O ")
    print("F C U W N F S I I I C N D H F ")
    print("N O D O X L P W A A I C Y H P ")
    print("E F N K K V X N D B B I D R F ")
    print("A V K T Z H Z E A L W V G C W ")
    print("M K I D E Z V G T H Y H W C H ")
    print("A F K R U I N V X H H F C A M ")
    print("C R V Z D M A R A I R O M E M ")
    print("A L I E I D Z F D V X G S G Q ")
    print("L J O T F V R U R H H N J Q G ")
    print("P C O O L E R A D I N E M Z S ")
    print("T A E H X Z B N H O E H N Z Y ")
    print("C R E G I S T R A D O R X Z P ")
    #Até aqui
    ''' placadevideo, registrador, memoriaram, harddrive,gabinete, placamae, cooler, fonte'''
    print("")
    print("Existem 8 palavras nesse caça palavras (escreva sem espaço e acentos)")
    print("")
    #COLOCAR AS PALAVRAS
    p1= str(input("Qual a primeira palavra que você achou? "))
    while cont1 != 1:
        #Inserir palavras
        if p1.upper() == "REGISTRADOR" or p1.upper()== "PLACAMAE" or p1.upper()== "PLACADEVIDEO" or p1.upper()== "MEMORIARAM" or p1.upper()== "HARDDRIVE" or p1.upper()== "GABINETE" or p1.upper()== "FONTE" or p1.upper()== "COOLER":
            print("A palavra achada foi ",p1)
            cont1 += 1
            pontuacao_rodada += len(p1)*p8x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p1.upper() != "REGISTRADOR" or p1.upper()!= "PLACAMAE" or p1.upper()!= "PLACADEVIDEO" or p1.upper()!= "MEMORIARAM" or p1.upper()!= "HARDDRIVE" or p1.upper()!= "GABINETE" or p1.upper()!= "FONTE" or p1.upper()!= "COOLER":
            print("O dado colocado está inválido")
            p1= str(input("Qual a primeira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("K V T U Y O T M X R K L K P E ")
    print("G V F K P W W F E K V D L T I ")
    print("J U M L R F T L R N A A E G O ")
    print("F C U W N F S I I I C N D H F ")
    print("N O D O X L P W A A I C Y H P ")
    print("E F N K K V X N D B B I D R F ")
    print("A V K T Z H Z E A L W V G C W ")
    print("M K I D E Z V G T H Y H W C H ")
    print("A F K R U I N V X H H F C A M ")
    print("C R V Z D M A R A I R O M E M ")
    print("A L I E I D Z F D V X G S G Q ")
    print("L J O T F V R U R H H N J Q G ")
    print("P C O O L E R A D I N E M Z S ")
    print("T A E H X Z B N H O E H N Z Y ")
    print("C R E G I S T R A D O R X Z P ")
    #Até aqui
    print("")
    p2 = str(input("Qual a segunda palavra que você achou? "))
    while cont2 != 1:
        if p2.upper() == p1.upper():
            print("A palavra está repetida")
            p2 = str(input("Qual a segunda palavra que você achou? "))
        #Inserir palavras
        elif p2.upper() == "REGISTRADOR" or p2.upper()== "PLACAMAE" or p2.upper()== "PLACADEVIDEO" or p2.upper()== "MEMORIARAM" or p2.upper()== "HARDDRIVE" or p2.upper()== "GABINETE"or p2.upper()== "FONTE"or p2.upper()== "COOLER":
            print("A palavra achada foi ",p2)
            cont2 += 1
            pontuacao_rodada += len(p2)*p7x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p2.upper() != "REGISTRADOR" or p2.upper()!= "PLACAMAE" or p2.upper()!= "PLACADEVIDEO" or p2.upper()!= "MEMORIARAM" or p2.upper()!= "HARDDRIVE" or p2.upper()!= "GABINETE"or p2.upper()!= "FONTE"or p2.upper()!= "COOLER":
            print("O dado colocado está inválido")
            p2= str(input("Qual a segunda palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("K V T U Y O T M X R K L K P E ")
    print("G V F K P W W F E K V D L T I ")
    print("J U M L R F T L R N A A E G O ")
    print("F C U W N F S I I I C N D H F ")
    print("N O D O X L P W A A I C Y H P ")
    print("E F N K K V X N D B B I D R F ")
    print("A V K T Z H Z E A L W V G C W ")
    print("M K I D E Z V G T H Y H W C H ")
    print("A F K R U I N V X H H F C A M ")
    print("C R V Z D M A R A I R O M E M ")
    print("A L I E I D Z F D V X G S G Q ")
    print("L J O T F V R U R H H N J Q G ")
    print("P C O O L E R A D I N E M Z S ")
    print("T A E H X Z B N H O E H N Z Y ")
    print("C R E G I S T R A D O R X Z P ")
    #Até aqui
    print("")
    p3 = str(input("Qual a terceira palavra que você achou? "))
    while cont3 != 1:
        if p3.upper()==p1.upper() or p3.upper()==p2.upper():
            print("A palavra está repetida")
            p3 = str(input("Qual a terceira palavra que você achou? "))
        #Inserir palavras
        elif p3.upper() == "REGISTRADOR" or p3.upper()== "PLACAMAE" or p3.upper()== "PLACADEVIDEO" or p3.upper()== "MEMORIARAM" or p3.upper()== "HARDDRIVE" or p3.upper()== "GABINETE"or p3.upper()== "FONTE"or p3.upper()== "COOLER":
            print("A palavra achada foi ",p3)
            cont3 += 1
            pontuacao_rodada += len(p3)*p6x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p3.upper() != "REGISTRADOR" or p3.upper()!= "PLACAMAE" or p3.upper()!= "PLACADEVIDEO" or p3.upper()!= "MEMORIARAM" or p3.upper()!= "HARDDRIVE" or p3.upper()!= "GABINETE"or p3.upper()!= "FONTE"or p3.upper()!= "COOLER":
            print("O dado colocado está inválido")
            p3= str(input("Qual a terceira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("K V T U Y O T M X R K L K P E ")
    print("G V F K P W W F E K V D L T I ")
    print("J U M L R F T L R N A A E G O ")
    print("F C U W N F S I I I C N D H F ")
    print("N O D O X L P W A A I C Y H P ")
    print("E F N K K V X N D B B I D R F ")
    print("A V K T Z H Z E A L W V G C W ")
    print("M K I D E Z V G T H Y H W C H ")
    print("A F K R U I N V X H H F C A M ")
    print("C R V Z D M A R A I R O M E M ")
    print("A L I E I D Z F D V X G S G Q ")
    print("L J O T F V R U R H H N J Q G ")
    print("P C O O L E R A D I N E M Z S ")
    print("T A E H X Z B N H O E H N Z Y ")
    print("C R E G I S T R A D O R X Z P ")
    #Até aqui
    print("")
    p4 = str(input("Qual a quarta palavra que você achou? "))
    while cont4 != 1:
        if p4==p1 or p4==p2 or p4==p3:
            print("A palavra está repetida")
            p4 = str (input("Qual a quarta palavra que você achou? "))
        #Inserir palavras
        elif p4.upper() == "REGISTRADOR" or p4.upper()== "PLACAMAE" or p4.upper()== "PLACADEVIDEO" or p4.upper()== "MEMORIARAM" or p4.upper()== "HARDDRIVE" or p4.upper()== "GABINETE"or p4.upper()== "FONTE"or p4.upper()== "COOLER":
            print("A palavra achada foi ",p4)
            cont4 += 1
            pontuacao_rodada += len(p4)*p5x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p4.upper() != "REGISTRADOR" or p4.upper()!= "PLACAMAE" or p4.upper()!= "PLACADEVIDEO" or p4.upper()!= "MEMORIARAM" or p4.upper()!= "HARDDRIVE" or p4.upper()!= "GABINETE"or p4.upper()!= "FONTE"or p4.upper()!= "COOLER":
            print("O dado colocado está inválido")
            p4 = str(input("Qual a quarta palavra que você achou? "))

    print("")
    #Colocar o caça daqui
    print("K V T U Y O T M X R K L K P E ")
    print("G V F K P W W F E K V D L T I ")
    print("J U M L R F T L R N A A E G O ")
    print("F C U W N F S I I I C N D H F ")
    print("N O D O X L P W A A I C Y H P ")
    print("E F N K K V X N D B B I D R F ")
    print("A V K T Z H Z E A L W V G C W ")
    print("M K I D E Z V G T H Y H W C H ")
    print("A F K R U I N V X H H F C A M ")
    print("C R V Z D M A R A I R O M E M ")
    print("A L I E I D Z F D V X G S G Q ")
    print("L J O T F V R U R H H N J Q G ")
    print("P C O O L E R A D I N E M Z S ")
    print("T A E H X Z B N H O E H N Z Y ")
    print("C R E G I S T R A D O R X Z P ")
    #Até aqui
    print("")
    p5 = str(input("Qual a quinta palavra que você achou? "))
    while cont5 !=1:
        if p5==p1 or p5==p2 or p5==p3 or p5==p4:
            print("A palavra está repetida")
            p5 = str (input("Qual a quinta palavra que você achou? "))
        #Inserir palavras
        elif p5.upper() == "REGISTRADOR" or p5.upper()== "PLACAMAE" or p5.upper()== "PLACADEVIDEO" or p5.upper()== "MEMORIARAM" or p5.upper()== "HARDDRIVE" or p5.upper()== "GABINETE"or p5.upper()== "FONTE"or p5.upper()== "COOLER":
            print("A palavra achada foi ",p5)
            cont5 += 1
            pontuacao_rodada += len(p5)*p4x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p5.upper() != "REGISTRADOR" or p5.upper()!= "PLACAMAE" or p5.upper()!= "PLACADEVIDEO" or p5.upper()!= "MEMORIARAM" or p5.upper()!= "HARDDRIVE" or p5.upper()!= "GABINETE"or p5.upper()!= "FONTE"or p5.upper()!= "COOLER":
            print("O dado colocado está inválido")
            p5 = str(input("Qual a quinta palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("K V T U Y O T M X R K L K P E ")
    print("G V F K P W W F E K V D L T I ")
    print("J U M L R F T L R N A A E G O ")
    print("F C U W N F S I I I C N D H F ")
    print("N O D O X L P W A A I C Y H P ")
    print("E F N K K V X N D B B I D R F ")
    print("A V K T Z H Z E A L W V G C W ")
    print("M K I D E Z V G T H Y H W C H ")
    print("A F K R U I N V X H H F C A M ")
    print("C R V Z D M A R A I R O M E M ")
    print("A L I E I D Z F D V X G S G Q ")
    print("L J O T F V R U R H H N J Q G ")
    print("P C O O L E R A D I N E M Z S ")
    print("T A E H X Z B N H O E H N Z Y ")
    print("C R E G I S T R A D O R X Z P ")
    #Até aqui
    print("")
    p6 = str(input("Qual a sexta palavra que você achou? "))
    while cont6 !=1:
        if p6==p1 or p6==p2 or p6==p3 or p6==p4 or p6==p5:
            print("A palavra está repetida")
            p6 = str (input("Qual a sexta palavra que você achou? "))
        #Inserir palavras
        elif p6.upper() == "REGISTRADOR" or p6.upper()== "PLACAMAE" or p6.upper()== "PLACADEVIDEO" or p6.upper()== "MEMORIARAM" or p6.upper()== "HARDDRIVE" or p6.upper()== "GABINETE"or p6.upper()== "FONTE"or p6.upper()== "COOLER":
            print("A palavra achada foi ",p6)
            cont6 += 1
            pontuacao_rodada += len(p6)*p3x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p6.upper() != "REGISTRADOR" or p6.upper()!= "PLACAMAE" or p6.upper()!= "PLACADEVIDEO" or p6.upper()!= "MEMORIARAM" or p6.upper()!= "HARDDRIVE" or p6.upper()!= "GABINETE"or p6.upper()!= "FONTE"or p6.upper()!= "COOLER":
            print("O dado colocado está inválido")
            p6 = str(input("Qual a sexta palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("K V T U Y O T M X R K L K P E ")
    print("G V F K P W W F E K V D L T I ")
    print("J U M L R F T L R N A A E G O ")
    print("F C U W N F S I I I C N D H F ")
    print("N O D O X L P W A A I C Y H P ")
    print("E F N K K V X N D B B I D R F ")
    print("A V K T Z H Z E A L W V G C W ")
    print("M K I D E Z V G T H Y H W C H ")
    print("A F K R U I N V X H H F C A M ")
    print("C R V Z D M A R A I R O M E M ")
    print("A L I E I D Z F D V X G S G Q ")
    print("L J O T F V R U R H H N J Q G ")
    print("P C O O L E R A D I N E M Z S ")
    print("T A E H X Z B N H O E H N Z Y ")
    print("C R E G I S T R A D O R X Z P ")
    #Até aqui
    print("")
    p7 = str(input("Qual a sétima palavra que você achou? "))
    while cont7 !=1:
        if p7==p1 or p7==p2 or p7==p3 or p7==p4 or p7==p5 or p7==p6:
            print("A palavra está repetida")
            p7 = str (input("Qual a sétima palavra que você achou? "))
        #Inserir palavras
        elif p7.upper() == "REGISTRADOR" or p7.upper()== "PLACAMAE" or p7.upper()== "PLACADEVIDEO" or p7.upper()== "MEMORIARAM" or p7.upper()== "HARDDRIVE" or p7.upper()== "GABINETE"or p7.upper()== "FONTE"or p7.upper()== "COOLER":
            print("A palavra achada foi ",p7)
            cont7 += 1
            pontuacao_rodada += len(p7)*p2x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p7.upper() != "REGISTRADOR" or p7.upper()!= "PLACAMAE" or p7.upper()!= "PLACADEVIDEO" or p7.upper()!= "MEMORIARAM" or p7.upper()!= "HARDDRIVE" or p7.upper()!= "GABINETE"or p7.upper()!= "FONTE"or p7.upper()!= "COOLER":
            print("O dado colocado está inválido")
            p7 = str(input("Qual a sétima palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("K V T U Y O T M X R K L K P E ")
    print("G V F K P W W F E K V D L T I ")
    print("J U M L R F T L R N A A E G O ")
    print("F C U W N F S I I I C N D H F ")
    print("N O D O X L P W A A I C Y H P ")
    print("E F N K K V X N D B B I D R F ")
    print("A V K T Z H Z E A L W V G C W ")
    print("M K I D E Z V G T H Y H W C H ")
    print("A F K R U I N V X H H F C A M ")
    print("C R V Z D M A R A I R O M E M ")
    print("A L I E I D Z F D V X G S G Q ")
    print("L J O T F V R U R H H N J Q G ")
    print("P C O O L E R A D I N E M Z S ")
    print("T A E H X Z B N H O E H N Z Y ")
    print("C R E G I S T R A D O R X Z P ")
    #Até aqui
    print("")
    p8 = str(input("Qual a oitava palavra que você achou? "))
    while cont8 !=1:
        if p8==p1 or p8==p2 or p8==p3 or p8==p4 or p8==p5 or p8==p6 or p8==p7:
            print("A palavra está repetida")
            p8 = str (input("Qual a oitava palavra que você achou? "))
        #Inserir palavras
        elif p8.upper() == "REGISTRADOR" or p8.upper()== "PLACAMAE" or p8.upper()== "PLACADEVIDEO" or p8.upper()== "MEMORIARAM" or p8.upper()== "HARDDRIVE" or p8.upper()== "GABINETE"or p8.upper()== "FONTE"or p8.upper()== "COOLER":
            print("A palavra achada foi ",p8)
            cont8 += 1
            pontuacao_rodada += len(p8)*p1x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p8.upper() != "REGISTRADOR" or p8.upper()!= "PLACAMAE" or p8.upper()!= "PLACADEVIDEO" or p8.upper()!= "MEMORIARAM" or p8.upper()!= "HARDDRIVE" or p8.upper()!= "GABINETE"or p8.upper()!= "FONTE"or p8.upper()!= "COOLER":
            print("O dado colocado está inválido")
            p8 = str(input("Qual a oitava palavra que você achou? "))
    print("")
    print("A primeira palavra achada foi:",p1)
    print("A segunda palavra achada foi:",p2)
    print("A terceira palavra achada foi:",p3)
    print("A quarta palavra achada foi:",p4)
    print("A quinta palavra achada foi:",p5)
    print("A sexta palavra achada foi:",p6)
    print("A sétima palavra achada foi:",p7)
    print("A oitava palavra achada foi:",p8)
    print("")
    print("A sua pontuação nessa rodada foi: ",pontuacao_rodada)
    print("A sua pontuação total é:",pontuacao_total)
    print("")
    print("O quadro de respostas é:")
    print("")
    #quadro de respostas daqui
    print("+ + + + + + + + + + + + + P E ")
    print("+ + + + + + + + + + + + L T + ")
    print("+ + + + + + + + + + + A E + + ")
    print("F + + + + + + + + + C N + + + ")
    print("+ O + + + + + + + A I + + + + ")
    print("E + N + + + + + D B + + + + + ")
    print("A V + T + + + E A + + + + + + ")
    print("M + I + E + V G + + + + + + + ")
    print("A + + R + I + + + + + + + + + ")
    print("C + + + D M A R A I R O M E M ")
    print("A + + E + D + + + + + + + + + ")
    print("L + O + + + R + + + + + + + + ")
    print("P C O O L E R A + + + + + + + ")
    print("+ + + + + + + + H + + + + + + ")
    print("+ R E G I S T R A D O R + + + ")
    #até aqui

    if pontuacao_dificil >= 107140: #maximo
        print("PARABÉNS! Você fez a pontuação máxima de ",pontuacao_dificil," no modo díficil! Você é um MESTRE SUPREMO DO MODO DÍFICIL!")
    elif pontuacao_dificil <= 78790: #minimo
        print("A sua pontuação no modo médio foi a menor possível:",pontuacao_dificil," .Você é um fracasso no modo díficil") #Fracasso deve estar meio forte. Mudar depois.
    elif pontuacao_dificil >= 92965 and pontuacao_dificil < 107140: #entre metade e maximo
        print("A sua pontuação de ",pontuacao_dificil," está entre a metade e o máximo! Você é um veterano do modo díficil!")
    elif pontuacao_dificil > 78790 and pontuacao_dificil < 92965:
        print("A sua pontuação de ",pontuacao_dificil," está entre a metade e o mínimo. Você é um iniciante do modo díficil")


    return menu()


def n3():

    ##################################################
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    cont5 = 0
    cont6 = 0
    cont7 = 0
    cont8 = 0
    pontuacao_rodada = 0
    pontuacao_total = 0
    pontuacao_facil = 0
    pontuacao_medio = 0
    pontuacao_dificil = 0
    #multiplicadores para os caça palavras
    p4x = 40
    p3x = 30
    p2x = 20
    p1x = 10
    #Essas variaveis vão ser os multiplicadores adcionais para os caça palavras 10x10
    p6x = 60
    p5x = 50
    #Essas variaveis vão ser os multiplicadores adcionais para os caça palavras 15x15
    p8x = 80
    p7x = 70
    print("")
    print("")
    print("")
    print("                             LOADING",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("")
    print("")
    print("")
    print("NÍVEL DIFICIL")
    print("")
    print("---------------------------------------------------------------------------")
    print("| Presidentes do Brasil - FASE 11                                         |")#titulo e fase
    print("|                                                                         |")
    #FASE11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11-11
    print("|                                                                         |")
    #Colocar o caça daqui
    print("| A N I F Z R H K L M S M Y F R                                           |")
    print("| N L K T U H Z X V X I K F J O                                           |")
    print("| E U U A A D W F N C S E F A L                                           |")
    print("| Z Y L L G M Q B H C S G S N L                                           |")
    print("| L E R R O G A E D S Z N N I O                                           |")
    print("| Y A J M Y I L R U N O F A O C                                           |")
    print("| U Q O S X T C O F C E Z S Q O                                           |")
    print("| T C A Q E B R A D R G G X U D                                           |")
    print("| A Q G M M A I J N Z A R C A N                                           |")
    print("| R R E E M F U I N I L N J D A                                           |")
    print("| T R W L R C U H A L Z W C R N                                           |")
    print("| D T I Q U A Q G P A L I I O R                                           |")
    print("| C D K E H C S T I B U K U S E                                           |")
    print("| G E T U L I O V A R G A S L F                                           |")
    print("| N E R M G P Z G Z J W G Q X A                                           |")
    #Até aqui
    '''fernandocollor,luizinaciolula, dilmarousseff, getuliovargas, janioquadros, itamarfranco, micheltemer, kubitschek'''
    print("|                                                                         |")
    print("| Existem 8 palavras nesse caça palavras (escreva sem espaço e acentos)   |")
    print("---------------------------------------------------------------------------")
    print("")
    print("Dicas:")
    print("   1-Presidente que renunciou à presidência depois de condenado pelo senado por crime de responsabilidade. Hoje é senador por Alagoas.")
    print("   2-Presidente que tem em seu nome uma espécie de um animal marinho da classe dos cefalópodes.")
    print("   3-Primeira presidente mulher do Brasil.")
    print("   4-Em seu governo foi inaugurada a Petrobras. Se matou no palácio do Catete.")
    print("   5-Utilizou como mote da campanha o varre, varre vassourinha, varre a corrupção")
    print("   6-Sucessor do primeiro presidente que sofreu processo de impeachment (ele era seu vice).")
    print("   7-Sucessor do segundo presidente que sofreu processo de impeachment (ele era seu vice).")
    print("   8-Utilizou como slogan de campanha 50 anos em 5.")
    print("")
    #COLOCAR AS PALAVRAS
    p1= str(input("Qual a primeira palavra que você achou? "))
    while cont1 != 1:
        #Inserir palavras
        if p1.upper() == "MICHELTEMER" or p1.upper()== "LUIZINACIOLULA" or p1.upper()== "KUBITSCHEK" or p1.upper()== "JANIOQUADROS" or p1.upper()== "ITAMARFRANCO" or p1.upper()== "GETULIOVARGAS" or p1.upper()== "FERNANDOCOLLOR" or p1.upper()== "DILMAROUSSEFF":
            print("A palavra achada foi ",p1)
            cont1 += 1
            pontuacao_rodada += len(p1)*p8x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p1.upper() != "MICHELTEMER" or p1.upper()!= "LUIZINACIOLULA" or p1.upper()!= "KUBITSCHEK" or p1.upper()!= "JANIOQUADROS" or p1.upper()!= "ITAMARFRANCO" or p1.upper()!= "GETULIOVARGAS" or p1.upper()!= "FERNANDOCOLLOR" or p1.upper()!= "DILMAROUSSEFF":
            print("O dado colocado está inválido")
            p1= str(input("Qual a primeira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| A N I F Z R H K L M S M Y F R                                           |")
    print("| N L K T U H Z X V X I K F J O                                           |")
    print("| E U U A A D W F N C S E F A L                                           |")
    print("| Z Y L L G M Q B H C S G S N L                                           |")
    print("| L E R R O G A E D S Z N N I O                                           |")
    print("| Y A J M Y I L R U N O F A O C                                           |")
    print("| U Q O S X T C O F C E Z S Q O                                           |")
    print("| T C A Q E B R A D R G G X U D                                           |")
    print("| A Q G M M A I J N Z A R C A N                                           |")
    print("| R R E E M F U I N I L N J D A                                           |")
    print("| T R W L R C U H A L Z W C R N                                           |")
    print("| D T I Q U A Q G P A L I I O R                                           |")
    print("| C D K E H C S T I B U K U S E                                           |")
    print("| G E T U L I O V A R G A S L F                                           |")
    print("| N E R M G P Z G Z J W G Q X A                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p2 = str(input("Qual a segunda palavra que você achou? "))
    while cont2 != 1:
        if p2.upper() == p1.upper():
            print("A palavra está repetida")
            p2 = str(input("Qual a segunda palavra que você achou? "))
        #Inserir palavras
        elif p2.upper() == "MICHELTEMER" or p2.upper()== "LUIZINACIOLULA" or p2.upper()== "KUBITSCHEK" or p2.upper()== "JANIOQUADROS" or p2.upper()== "ITAMARFRANCO" or p2.upper()== "GETULIOVARGAS"or p2.upper()== "FERNANDOCOLLOR"or p2.upper()== "DILMAROUSSEFF":
            print("A palavra achada foi ",p2)
            cont2 += 1
            pontuacao_rodada += len(p2)*p7x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p2.upper() != "MICHELTEMER" or p2.upper()!= "LUIZINACIOLULA" or p2.upper()!= "KUBITSCHEK" or p2.upper()!= "JANIOQUADROS" or p2.upper()!= "ITAMARFRANCO" or p2.upper()!= "GETULIOVARGAS"or p2.upper()!= "FERNANDOCOLLOR"or p2.upper()!= "DILMAROUSSEFF":
            print("O dado colocado está inválido")
            p2= str(input("Qual a segunda palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| A N I F Z R H K L M S M Y F R                                           |")
    print("| N L K T U H Z X V X I K F J O                                           |")
    print("| E U U A A D W F N C S E F A L                                           |")
    print("| Z Y L L G M Q B H C S G S N L                                           |")
    print("| L E R R O G A E D S Z N N I O                                           |")
    print("| Y A J M Y I L R U N O F A O C                                           |")
    print("| U Q O S X T C O F C E Z S Q O                                           |")
    print("| T C A Q E B R A D R G G X U D                                           |")
    print("| A Q G M M A I J N Z A R C A N                                           |")
    print("| R R E E M F U I N I L N J D A                                           |")
    print("| T R W L R C U H A L Z W C R N                                           |")
    print("| D T I Q U A Q G P A L I I O R                                           |")
    print("| C D K E H C S T I B U K U S E                                           |")
    print("| G E T U L I O V A R G A S L F                                           |")
    print("| N E R M G P Z G Z J W G Q X A                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p3 = str(input("Qual a terceira palavra que você achou? "))
    while cont3 != 1:
        if p3.upper()==p1.upper() or p3.upper()==p2.upper():
            print("A palavra está repetida")
            p3 = str(input("Qual a terceira palavra que você achou? "))
        #Inserir palavras
        elif p3.upper() == "MICHELTEMER" or p3.upper()== "LUIZINACIOLULA" or p3.upper()== "KUBITSCHEK" or p3.upper()== "JANIOQUADROS" or p3.upper()== "ITAMARFRANCO" or p3.upper()== "GETULIOVARGAS"or p3.upper()== "FERNANDOCOLLOR"or p3.upper()== "DILMAROUSSEFF":
            print("A palavra achada foi ",p3)
            cont3 += 1
            pontuacao_rodada += len(p3)*p6x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p3.upper() != "MICHELTEMER" or p3.upper()!= "LUIZINACIOLULA" or p3.upper()!= "KUBITSCHEK" or p3.upper()!= "JANIOQUADROS" or p3.upper()!= "ITAMARFRANCO" or p3.upper()!= "GETULIOVARGAS"or p3.upper()!= "FERNANDOCOLLOR"or p3.upper()!= "DILMAROUSSEFF":
            print("O dado colocado está inválido")
            p3= str(input("Qual a terceira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| A N I F Z R H K L M S M Y F R                                           |")
    print("| N L K T U H Z X V X I K F J O                                           |")
    print("| E U U A A D W F N C S E F A L                                           |")
    print("| Z Y L L G M Q B H C S G S N L                                           |")
    print("| L E R R O G A E D S Z N N I O                                           |")
    print("| Y A J M Y I L R U N O F A O C                                           |")
    print("| U Q O S X T C O F C E Z S Q O                                           |")
    print("| T C A Q E B R A D R G G X U D                                           |")
    print("| A Q G M M A I J N Z A R C A N                                           |")
    print("| R R E E M F U I N I L N J D A                                           |")
    print("| T R W L R C U H A L Z W C R N                                           |")
    print("| D T I Q U A Q G P A L I I O R                                           |")
    print("| C D K E H C S T I B U K U S E                                           |")
    print("| G E T U L I O V A R G A S L F                                           |")
    print("| N E R M G P Z G Z J W G Q X A                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p4 = str(input("Qual a quarta palavra que você achou? "))
    while cont4 != 1:
        if p4==p1 or p4==p2 or p4==p3:
            print("A palavra está repetida")
            p4 = str (input("Qual a quarta palavra que você achou? "))
        #Inserir palavras
        elif p4.upper() == "MICHELTEMER" or p4.upper()== "LUIZINACIOLULA" or p4.upper()== "KUBITSCHEK" or p4.upper()== "JANIOQUADROS" or p4.upper()== "ITAMARFRANCO" or p4.upper()== "GETULIOVARGAS"or p4.upper()== "FERNANDOCOLLOR"or p4.upper()== "DILMAROUSSEFF":
            print("A palavra achada foi ",p4)
            cont4 += 1
            pontuacao_rodada += len(p4)*p5x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p4.upper() != "MICHELTEMER" or p4.upper()!= "LUIZINACIOLULA" or p4.upper()!= "KUBITSCHEK" or p4.upper()!= "JANIOQUADROS" or p4.upper()!= "ITAMARFRANCO" or p4.upper()!= "GETULIOVARGAS"or p4.upper()!= "FERNANDOCOLLOR"or p4.upper()!= "DILMAROUSSEFF":
            print("O dado colocado está inválido")
            p4 = str(input("Qual a quarta palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| A N I F Z R H K L M S M Y F R                                           |")
    print("| N L K T U H Z X V X I K F J O                                           |")
    print("| E U U A A D W F N C S E F A L                                           |")
    print("| Z Y L L G M Q B H C S G S N L                                           |")
    print("| L E R R O G A E D S Z N N I O                                           |")
    print("| Y A J M Y I L R U N O F A O C                                           |")
    print("| U Q O S X T C O F C E Z S Q O                                           |")
    print("| T C A Q E B R A D R G G X U D                                           |")
    print("| A Q G M M A I J N Z A R C A N                                           |")
    print("| R R E E M F U I N I L N J D A                                           |")
    print("| T R W L R C U H A L Z W C R N                                           |")
    print("| D T I Q U A Q G P A L I I O R                                           |")
    print("| C D K E H C S T I B U K U S E                                           |")
    print("| G E T U L I O V A R G A S L F                                           |")
    print("| N E R M G P Z G Z J W G Q X A                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p5 = str(input("Qual a quinta palavra que você achou? "))
    while cont5 !=1:
        if p5==p1 or p5==p2 or p5==p3 or p5==p4:
            print("A palavra está repetida")
            p5 = str (input("Qual a quinta palavra que você achou? "))
        #Inserir palavras
        elif p5.upper() == "" or p5.upper()== "LUIZINACIOLULA" or p5.upper()== "KUBITSCHEK" or p5.upper()== "JANIOQUADROS" or p5.upper()== "ITAMARFRANCO" or p5.upper()== "GETULIOVARGAS"or p5.upper()== "FERNANDOCOLLOR"or p5.upper()== "DILMAROUSSEFF":
            print("A palavra achada foi ",p5)
            cont5 += 1
            pontuacao_rodada += len(p5)*p4x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p5.upper() != "" or p5.upper()!= "LUIZINACIOLULA" or p5.upper()!= "KUBITSCHEK" or p5.upper()!= "JANIOQUADROS" or p5.upper()!= "ITAMARFRANCO" or p5.upper()!= "GETULIOVARGAS"or p5.upper()!= "FERNANDOCOLLOR"or p5.upper()!= "DILMAROUSSEFF":
            print("O dado colocado está inválido")
            p5 = str(input("Qual a quinta palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| A N I F Z R H K L M S M Y F R                                           |")
    print("| N L K T U H Z X V X I K F J O                                           |")
    print("| E U U A A D W F N C S E F A L                                           |")
    print("| Z Y L L G M Q B H C S G S N L                                           |")
    print("| L E R R O G A E D S Z N N I O                                           |")
    print("| Y A J M Y I L R U N O F A O C                                           |")
    print("| U Q O S X T C O F C E Z S Q O                                           |")
    print("| T C A Q E B R A D R G G X U D                                           |")
    print("| A Q G M M A I J N Z A R C A N                                           |")
    print("| R R E E M F U I N I L N J D A                                           |")
    print("| T R W L R C U H A L Z W C R N                                           |")
    print("| D T I Q U A Q G P A L I I O R                                           |")
    print("| C D K E H C S T I B U K U S E                                           |")
    print("| G E T U L I O V A R G A S L F                                           |")
    print("| N E R M G P Z G Z J W G Q X A                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p6 = str(input("Qual a sexta palavra que você achou? "))
    while cont6 !=1:
        if p6==p1 or p6==p2 or p6==p3 or p6==p4 or p6==p5:
            print("A palavra está repetida")
            p6 = str (input("Qual a sexta palavra que você achou? "))
        #Inserir palavras
        elif p6.upper() == "MICHELTEMER" or p6.upper()== "LUIZINACIOLULA" or p6.upper()== "KUBITSCHEK" or p6.upper()== "JANIOQUADROS" or p6.upper()== "ITAMARFRANCO" or p6.upper()== "GETULIOVARGAS"or p6.upper()== "FERNANDOCOLLOR"or p6.upper()== "DILMAROUSSEFF":
            print("A palavra achada foi ",p6)
            cont6 += 1
            pontuacao_rodada += len(p6)*p3x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p6.upper() != "MICHELTEMER" or p6.upper()!= "LUIZINACIOLULA" or p6.upper()!= "KUBITSCHEK" or p6.upper()!= "JANIOQUADROS" or p6.upper()!= "ITAMARFRANCO" or p6.upper()!= "GETULIOVARGAS"or p6.upper()!= "FERNANDOCOLLOR"or p6.upper()!= "DILMAROUSSEFF":
            print("O dado colocado está inválido")
            p6 = str(input("Qual a sexta palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| A N I F Z R H K L M S M Y F R                                           |")
    print("| N L K T U H Z X V X I K F J O                                           |")
    print("| E U U A A D W F N C S E F A L                                           |")
    print("| Z Y L L G M Q B H C S G S N L                                           |")
    print("| L E R R O G A E D S Z N N I O                                           |")
    print("| Y A J M Y I L R U N O F A O C                                           |")
    print("| U Q O S X T C O F C E Z S Q O                                           |")
    print("| T C A Q E B R A D R G G X U D                                           |")
    print("| A Q G M M A I J N Z A R C A N                                           |")
    print("| R R E E M F U I N I L N J D A                                           |")
    print("| T R W L R C U H A L Z W C R N                                           |")
    print("| D T I Q U A Q G P A L I I O R                                           |")
    print("| C D K E H C S T I B U K U S E                                           |")
    print("| G E T U L I O V A R G A S L F                                           |")
    print("| N E R M G P Z G Z J W G Q X A                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p7 = str(input("Qual a sétima palavra que você achou? "))
    while cont7 !=1:
        if p7==p1 or p7==p2 or p7==p3 or p7==p4 or p7==p5 or p7==p6:
            print("A palavra está repetida")
            p7 = str (input("Qual a sétima palavra que você achou? "))
        #Inserir palavras
        elif p7.upper() == "MICHELTEMER" or p7.upper()== "LUIZINACIOLULA" or p7.upper()== "KUBITSCHEK" or p7.upper()== "JANIOQUADROS" or p7.upper()== "ITAMARFRANCO" or p7.upper()== "GETULIOVARGAS"or p7.upper()== "FERNANDOCOLLOR"or p7.upper()== "DILMAROUSSEFF":
            print("A palavra achada foi ",p7)
            cont7 += 1
            pontuacao_rodada += len(p7)*p2x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p7.upper() != "MICHELTEMER" or p7.upper()!= "LUIZINACIOLULA" or p7.upper()!= "KUBITSCHEK" or p7.upper()!= "JANIOQUADROS" or p7.upper()!= "ITAMARFRANCO" or p7.upper()!= "GETULIOVARGAS"or p7.upper()!= "FERNANDOCOLLOR"or p7.upper()!= "DILMAROUSSEFF":
            print("O dado colocado está inválido")
            p7 = str(input("Qual a sétima palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| A N I F Z R H K L M S M Y F R                                           |")
    print("| N L K T U H Z X V X I K F J O                                           |")
    print("| E U U A A D W F N C S E F A L                                           |")
    print("| Z Y L L G M Q B H C S G S N L                                           |")
    print("| L E R R O G A E D S Z N N I O                                           |")
    print("| Y A J M Y I L R U N O F A O C                                           |")
    print("| U Q O S X T C O F C E Z S Q O                                           |")
    print("| T C A Q E B R A D R G G X U D                                           |")
    print("| A Q G M M A I J N Z A R C A N                                           |")
    print("| R R E E M F U I N I L N J D A                                           |")
    print("| T R W L R C U H A L Z W C R N                                           |")
    print("| D T I Q U A Q G P A L I I O R                                           |")
    print("| C D K E H C S T I B U K U S E                                           |")
    print("| G E T U L I O V A R G A S L F                                           |")
    print("| N E R M G P Z G Z J W G Q X A                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p8 = str(input("Qual a oitava palavra que você achou? "))
    while cont8 !=1:
        if p8==p1 or p8==p2 or p8==p3 or p8==p4 or p8==p5 or p8==p6 or p8==p7:
            print("A palavra está repetida")
            p8 = str (input("Qual a oitava palavra que você achou? "))
        #Inserir palavras
        elif p8.upper() == "MICHELTEMER" or p8.upper()== "LUIZINACIOLULA" or p8.upper()== "KUBITSCHEK" or p8.upper()== "JANIOQUADROS" or p8.upper()== "ITAMARFRANCO" or p8.upper()== "GETULIOVARGAS"or p8.upper()== "FERNANDOCOLLOR"or p8.upper()== "DILMAROUSSEFF":
            print("A palavra achada foi ",p8)
            cont8 += 1
            pontuacao_rodada += len(p8)*p1x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p8.upper() != "MICHELTEMER" or p8.upper()!= "LUIZINACIOLULA" or p8.upper()!= "KUBITSCHEK" or p8.upper()!= "JANIOQUADROS" or p8.upper()!= "ITAMARFRANCO" or p8.upper()!= "GETULIOVARGAS"or p8.upper()!= "FERNANDOCOLLOR"or p8.upper()!= "DILMAROUSSEFF":
            print("O dado colocado está inválido")
            p8 = str(input("Qual a oitava palavra que você achou? "))
    print("")
    print("A primeira palavra achada foi:",p1)
    print("A segunda palavra achada foi:",p2)
    print("A terceira palavra achada foi:",p3)
    print("A quarta palavra achada foi:",p4)
    print("A quinta palavra achada foi:",p5)
    print("A sexta palavra achada foi:",p6)
    print("A sétima palavra achada foi:",p7)
    print("A oitava palavra achada foi:",p8)
    print("")
    print("A sua pontuação nessa rodada foi: ",pontuacao_rodada)
    print("A sua pontuação total é:",pontuacao_total)
    print("")
    print("O quadro de respostas é:")
    print("")
    #quadro de respostas daqui
    print("A + I + + + + + + + + M + F R ")
    print("+ L + T + + + + + + I + F J O ")
    print("+ + U + A + + + + C + E + A L ")
    print("+ + + L + M + + H + S + + N L ")
    print("+ + + + O + A E + S + + + I O ")
    print("+ + + + + I L R U + + + + O C ")
    print("+ + + + + T C O F + + + + Q O ")
    print("+ + + + E + R A + R + + + U D ")
    print("+ + + M + A + + N + A + + A N ")
    print("+ + E + M + + + + I + N + D A ")
    print("+ R + L + + + + + + Z + C R N ")
    print("+ + I + + + + + + + + I + O R ")
    print("+ D K E H C S T I B U K U S E ")
    print("G E T U L I O V A R G A S L F ")
    print("+ + + + + + + + + + + + + + + ")
    #até aqui
    ##################################################
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    cont5 = 0
    cont6 = 0
    cont7 = 0
    cont8 = 0
    pontuacao_rodada = 0
    print("")
    print("")
    print("")
    print("                             LOADING",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("")
    print("")
    print("")
    print("---------------------------------------------------------------------------")
    print("| Flores - FASE 12                                                        |")#titulo e fase
    print("|                                                                         |")
    #FASE12121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212
    print("|                                                                         |")
    #Colocar o caça daqui
    print("| H R E X O E B Y J C N L Z J G                                           |")
    print("| Y I O T C A T I V S I O G E N                                           |")
    print("| M L B S P X A R W W M S C R J                                           |")
    print("| F L J I A O B T F F V A B L K                                           |")
    print("| T Z L V C E N P E O M R Z O R                                           |")
    print("| F U U J G X W T B L U I V T P                                           |")
    print("| T B Z O W X R R R D O G H E R                                           |")
    print("| B W N J I K A P O Y E I G O F                                           |")
    print("| X I L Z G G I A M N Q B V I D                                           |")
    print("| A J K C Q U T M E O Y P F T G                                           |")
    print("| A I N U T E P H L P O M Z L J                                           |")
    print("| D V R Q W K V S I H M A J Z V                                           |")
    print("| A G S Q T U B V A C R A V O U                                           |")
    print("| G C S K A K B M G K J F Q T Z                                           |")
    print("| M O G G W G S B T R L J U A L                                           |")
    #Até aqui
    '''bromelia, begonia , violeta, petunia, girasol, tulipa, cravo, rosa '''
    print("|                                                                         |")
    print("| Existem 8 palavras nesse caça palavras (escreva sem espaço e acentos)   |")
    print("---------------------------------------------------------------------------")
    print("")
    print("Dicas:")
    print("   1-As espécies deste gênero estão distribuidos pelas regiões tropicais dos continentes americanos, e sua principal característica é a de suas flores apresentarem um cálice muito profundo.")
    print("   2-As folhas delas são, sem dúvida, o seu maior atractivo. De forma reniforme, incomum, e usualmente extremamente coloridas, são muito visadas para canteiros sombreados.")
    print("   3-Tem uma cor que pode ser obtida da mistura de magenta e azul (é o mesmo nome da flor).")
    print("   4-Seu nome também pode ser um nome próprio de menina (não e nome de cor).")
    print("   5-Gosta de seguir o sol.")
    print("   6-Têm folhas que podem ser oblongas, ovais ou lanceoladas (em forma de lança). Do centro da folhagem surge uma haste ereta, com flor solitária formada por seis pétalas.")
    print("   7-Essa dica serve para duas palavras: O ______ brigou com a ______.")
    print("")
    #COLOCAR AS PALAVRAS
    p1= str(input("Qual a primeira palavra que você achou? "))
    while cont1 != 1:
        #Inserir palavras
        if p1.upper() == "VIOLETA" or p1.upper()== "TULIPA" or p1.upper()== "ROSA" or p1.upper()== "PETUNIA" or p1.upper()== "GIRASOL" or p1.upper()== "CRAVO" or p1.upper()== "BROMELIA" or p1.upper()== "BEGONIA":
            print("A palavra achada foi ",p1)
            cont1 += 1
            pontuacao_rodada += len(p1)*p8x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p1.upper() != "VIOLETA" or p1.upper()!= "TULIPA" or p1.upper()!= "ROSA" or p1.upper()!= "PETUNIA" or p1.upper()!= "GIRASOL" or p1.upper()!= "CRAVO" or p1.upper()!= "BROMELIA" or p1.upper()!= "BEGONIA":
            print("O dado colocado está inválido")
            p1= str(input("Qual a primeira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| H R E X O E B Y J C N L Z J G                                           |")
    print("| Y I O T C A T I V S I O G E N                                           |")
    print("| M L B S P X A R W W M S C R J                                           |")
    print("| F L J I A O B T F F V A B L K                                           |")
    print("| T Z L V C E N P E O M R Z O R                                           |")
    print("| F U U J G X W T B L U I V T P                                           |")
    print("| T B Z O W X R R R D O G H E R                                           |")
    print("| B W N J I K A P O Y E I G O F                                           |")
    print("| X I L Z G G I A M N Q B V I D                                           |")
    print("| A J K C Q U T M E O Y P F T G                                           |")
    print("| A I N U T E P H L P O M Z L J                                           |")
    print("| D V R Q W K V S I H M A J Z V                                           |")
    print("| A G S Q T U B V A C R A V O U                                           |")
    print("| G C S K A K B M G K J F Q T Z                                           |")
    print("| M O G G W G S B T R L J U A L                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p2 = str(input("Qual a segunda palavra que você achou? "))
    while cont2 != 1:
        if p2.upper() == p1.upper():
            print("A palavra está repetida")
            p2 = str(input("Qual a segunda palavra que você achou? "))
        #Inserir palavras
        elif p2.upper() == "VIOLETA" or p2.upper()== "TULIPA" or p2.upper()== "ROSA" or p2.upper()== "PETUNIA" or p2.upper()== "GIRASOL" or p2.upper()== "CRAVO"or p2.upper()== "BROMELIA"or p2.upper()== "BEGONIA":
            print("A palavra achada foi ",p2)
            cont2 += 1
            pontuacao_rodada += len(p2)*p7x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p2.upper() != "VIOLETA" or p2.upper()!= "TULIPA" or p2.upper()!= "ROSA" or p2.upper()!= "PETUNIA" or p2.upper()!= "GIRASOL" or p2.upper()!= "CRAVO"or p2.upper()!= "BROMELIA"or p2.upper()!= "BEGONIA":
            print("O dado colocado está inválido")
            p2= str(input("Qual a segunda palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| H R E X O E B Y J C N L Z J G                                           |")
    print("| Y I O T C A T I V S I O G E N                                           |")
    print("| M L B S P X A R W W M S C R J                                           |")
    print("| F L J I A O B T F F V A B L K                                           |")
    print("| T Z L V C E N P E O M R Z O R                                           |")
    print("| F U U J G X W T B L U I V T P                                           |")
    print("| T B Z O W X R R R D O G H E R                                           |")
    print("| B W N J I K A P O Y E I G O F                                           |")
    print("| X I L Z G G I A M N Q B V I D                                           |")
    print("| A J K C Q U T M E O Y P F T G                                           |")
    print("| A I N U T E P H L P O M Z L J                                           |")
    print("| D V R Q W K V S I H M A J Z V                                           |")
    print("| A G S Q T U B V A C R A V O U                                           |")
    print("| G C S K A K B M G K J F Q T Z                                           |")
    print("| M O G G W G S B T R L J U A L                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p3 = str(input("Qual a terceira palavra que você achou? "))
    while cont3 != 1:
        if p3.upper()==p1.upper() or p3.upper()==p2.upper():
            print("A palavra está repetida")
            p3 = str(input("Qual a terceira palavra que você achou? "))
        #Inserir palavras
        elif p3.upper() == "VIOLETA" or p3.upper()== "TULIPA" or p3.upper()== "ROSA" or p3.upper()== "PETUNIA" or p3.upper()== "GIRASOL" or p3.upper()== "CRAVO"or p3.upper()== "BROMELIA"or p3.upper()== "BEGONIA":
            print("A palavra achada foi ",p3)
            cont3 += 1
            pontuacao_rodada += len(p3)*p6x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p3.upper() != "VIOLETA" or p3.upper()!= "TULIPA" or p3.upper()!= "ROSA" or p3.upper()!= "PETUNIA" or p3.upper()!= "GIRASOL" or p3.upper()!= "CRAVO"or p3.upper()!= "BROMELIA"or p3.upper()!= "BEGONIA":
            print("O dado colocado está inválido")
            p3= str(input("Qual a terceira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| H R E X O E B Y J C N L Z J G                                           |")
    print("| Y I O T C A T I V S I O G E N                                           |")
    print("| M L B S P X A R W W M S C R J                                           |")
    print("| F L J I A O B T F F V A B L K                                           |")
    print("| T Z L V C E N P E O M R Z O R                                           |")
    print("| F U U J G X W T B L U I V T P                                           |")
    print("| T B Z O W X R R R D O G H E R                                           |")
    print("| B W N J I K A P O Y E I G O F                                           |")
    print("| X I L Z G G I A M N Q B V I D                                           |")
    print("| A J K C Q U T M E O Y P F T G                                           |")
    print("| A I N U T E P H L P O M Z L J                                           |")
    print("| D V R Q W K V S I H M A J Z V                                           |")
    print("| A G S Q T U B V A C R A V O U                                           |")
    print("| G C S K A K B M G K J F Q T Z                                           |")
    print("| M O G G W G S B T R L J U A L                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p4 = str(input("Qual a quarta palavra que você achou? "))
    while cont4 != 1:
        if p4==p1 or p4==p2 or p4==p3:
            print("A palavra está repetida")
            p4 = str (input("Qual a quarta palavra que você achou? "))
        #Inserir palavras
        elif p4.upper() == "VIOLETA" or p4.upper()== "TULIPA" or p4.upper()== "ROSA" or p4.upper()== "PETUNIA" or p4.upper()== "GIRASOL" or p4.upper()== "CRAVO"or p4.upper()== "BROMELIA"or p4.upper()== "BEGONIA":
            print("A palavra achada foi ",p4)
            cont4 += 1
            pontuacao_rodada += len(p4)*p5x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p4.upper() != "VIOLETA" or p4.upper()!= "TULIPA" or p4.upper()!= "ROSA" or p4.upper()!= "PETUNIA" or p4.upper()!= "GIRASOL" or p4.upper()!= "CRAVO"or p4.upper()!= "BROMELIA"or p4.upper()!= "BEGONIA":
            print("O dado colocado está inválido")
            p4 = str(input("Qual a quarta palavra que você achou? "))

    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| H R E X O E B Y J C N L Z J G                                           |")
    print("| Y I O T C A T I V S I O G E N                                           |")
    print("| M L B S P X A R W W M S C R J                                           |")
    print("| F L J I A O B T F F V A B L K                                           |")
    print("| T Z L V C E N P E O M R Z O R                                           |")
    print("| F U U J G X W T B L U I V T P                                           |")
    print("| T B Z O W X R R R D O G H E R                                           |")
    print("| B W N J I K A P O Y E I G O F                                           |")
    print("| X I L Z G G I A M N Q B V I D                                           |")
    print("| A J K C Q U T M E O Y P F T G                                           |")
    print("| A I N U T E P H L P O M Z L J                                           |")
    print("| D V R Q W K V S I H M A J Z V                                           |")
    print("| A G S Q T U B V A C R A V O U                                           |")
    print("| G C S K A K B M G K J F Q T Z                                           |")
    print("| M O G G W G S B T R L J U A L                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p5 = str(input("Qual a quinta palavra que você achou? "))
    while cont5 !=1:
        if p5==p1 or p5==p2 or p5==p3 or p5==p4:
            print("A palavra está repetida")
            p5 = str (input("Qual a quinta palavra que você achou? "))
        #Inserir palavras
        elif p5.upper() == "VIOLETA" or p5.upper()== "TULIPA" or p5.upper()== "ROSA" or p5.upper()== "PETUNIA" or p5.upper()== "GIRASOL" or p5.upper()== "CRAVO"or p5.upper()== "BROMELIA"or p5.upper()== "BEGONIA":
            print("A palavra achada foi ",p5)
            cont5 += 1
            pontuacao_rodada += len(p5)*p4x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p5.upper() != "VIOLETA" or p5.upper()!= "TULIPA" or p5.upper()!= "ROSA" or p5.upper()!= "PETUNIA" or p5.upper()!= "GIRASOL" or p5.upper()!= "CRAVO"or p5.upper()!= "BROMELIA"or p5.upper()!= "BEGONIA":
            print("O dado colocado está inválido")
            p5 = str(input("Qual a quinta palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| H R E X O E B Y J C N L Z J G                                           |")
    print("| Y I O T C A T I V S I O G E N                                           |")
    print("| M L B S P X A R W W M S C R J                                           |")
    print("| F L J I A O B T F F V A B L K                                           |")
    print("| T Z L V C E N P E O M R Z O R                                           |")
    print("| F U U J G X W T B L U I V T P                                           |")
    print("| T B Z O W X R R R D O G H E R                                           |")
    print("| B W N J I K A P O Y E I G O F                                           |")
    print("| X I L Z G G I A M N Q B V I D                                           |")
    print("| A J K C Q U T M E O Y P F T G                                           |")
    print("| A I N U T E P H L P O M Z L J                                           |")
    print("| D V R Q W K V S I H M A J Z V                                           |")
    print("| A G S Q T U B V A C R A V O U                                           |")
    print("| G C S K A K B M G K J F Q T Z                                           |")
    print("| M O G G W G S B T R L J U A L                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p6 = str(input("Qual a sexta palavra que você achou? "))
    while cont6 !=1:
        if p6==p1 or p6==p2 or p6==p3 or p6==p4 or p6==p5:
            print("A palavra está repetida")
            p6 = str (input("Qual a sexta palavra que você achou? "))
        #Inserir palavras
        elif p6.upper() == "VIOLETA" or p6.upper()== "TULIPA" or p6.upper()== "ROSA" or p6.upper()== "PETUNIA" or p6.upper()== "GIRASOL" or p6.upper()== "CRAVO"or p6.upper()== "BROMELIA"or p6.upper()== "BEGONIA":
            print("A palavra achada foi ",p6)
            cont6 += 1
            pontuacao_rodada += len(p6)*p3x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p6.upper() != "VIOLETA" or p6.upper()!= "TULIPA" or p6.upper()!= "ROSA" or p6.upper()!= "PETUNIA" or p6.upper()!= "GIRASOL" or p6.upper()!= "CRAVO"or p6.upper()!= "BROMELIA"or p6.upper()!= "BEGONIA":
            print("O dado colocado está inválido")
            p6 = str(input("Qual a sexta palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| H R E X O E B Y J C N L Z J G                                           |")
    print("| Y I O T C A T I V S I O G E N                                           |")
    print("| M L B S P X A R W W M S C R J                                           |")
    print("| F L J I A O B T F F V A B L K                                           |")
    print("| T Z L V C E N P E O M R Z O R                                           |")
    print("| F U U J G X W T B L U I V T P                                           |")
    print("| T B Z O W X R R R D O G H E R                                           |")
    print("| B W N J I K A P O Y E I G O F                                           |")
    print("| X I L Z G G I A M N Q B V I D                                           |")
    print("| A J K C Q U T M E O Y P F T G                                           |")
    print("| A I N U T E P H L P O M Z L J                                           |")
    print("| D V R Q W K V S I H M A J Z V                                           |")
    print("| A G S Q T U B V A C R A V O U                                           |")
    print("| G C S K A K B M G K J F Q T Z                                           |")
    print("| M O G G W G S B T R L J U A L                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p7 = str(input("Qual a sétima palavra que você achou? "))
    while cont7 !=1:
        if p7==p1 or p7==p2 or p7==p3 or p7==p4 or p7==p5 or p7==p6:
            print("A palavra está repetida")
            p7 = str (input("Qual a sétima palavra que você achou? "))
        #Inserir palavras
        elif p7.upper() == "VIOLETA" or p7.upper()== "TULIPA" or p7.upper()== "ROSA" or p7.upper()== "PETUNIA" or p7.upper()== "GIRASOL" or p7.upper()== "CRAVO"or p7.upper()== "BROMELIA"or p7.upper()== "BEGONIA":
            print("A palavra achada foi ",p7)
            cont7 += 1
            pontuacao_rodada += len(p7)*p2x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p7.upper() != "VIOLETA" or p7.upper()!= "TULIPA" or p7.upper()!= "ROSA" or p7.upper()!= "PETUNIA" or p7.upper()!= "GIRASOL" or p7.upper()!= "CRAVO"or p7.upper()!= "BROMELIA"or p7.upper()!= "BEGONIA":
            print("O dado colocado está inválido")
            p7 = str(input("Qual a sétima palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| H R E X O E B Y J C N L Z J G                                           |")
    print("| Y I O T C A T I V S I O G E N                                           |")
    print("| M L B S P X A R W W M S C R J                                           |")
    print("| F L J I A O B T F F V A B L K                                           |")
    print("| T Z L V C E N P E O M R Z O R                                           |")
    print("| F U U J G X W T B L U I V T P                                           |")
    print("| T B Z O W X R R R D O G H E R                                           |")
    print("| B W N J I K A P O Y E I G O F                                           |")
    print("| X I L Z G G I A M N Q B V I D                                           |")
    print("| A J K C Q U T M E O Y P F T G                                           |")
    print("| A I N U T E P H L P O M Z L J                                           |")
    print("| D V R Q W K V S I H M A J Z V                                           |")
    print("| A G S Q T U B V A C R A V O U                                           |")
    print("| G C S K A K B M G K J F Q T Z                                           |")
    print("| M O G G W G S B T R L J U A L                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p8 = str(input("Qual a oitava palavra que você achou? "))
    while cont8 !=1:
        if p8==p1 or p8==p2 or p8==p3 or p8==p4 or p8==p5 or p8==p6 or p8==p7:
            print("A palavra está repetida")
            p8 = str (input("Qual a oitava palavra que você achou? "))
        #Inserir palavras
        elif p8.upper() == "VIOLETA" or p8.upper()== "TULIPA" or p8.upper()== "ROSA" or p8.upper()== "PETUNIA" or p8.upper()== "GIRASOL" or p8.upper()== "CRAVO"or p8.upper()== "BROMELIA"or p8.upper()== "BEGONIA":
            print("A palavra achada foi ",p8)
            cont8 += 1
            pontuacao_rodada += len(p8)*p1x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p8.upper() != "VIOLETA" or p8.upper()!= "TULIPA" or p8.upper()!= "ROSA" or p8.upper()!= "PETUNIA" or p8.upper()!= "GIRASOL" or p8.upper()!= "CRAVO"or p8.upper()!= "BROMELIA"or p8.upper()!= "BEGONIA":
            print("O dado colocado está inválido")
            p8 = str(input("Qual a oitava palavra que você achou? "))
    print("")
    print("A primeira palavra achada foi:",p1)
    print("A segunda palavra achada foi:",p2)
    print("A terceira palavra achada foi:",p3)
    print("A quarta palavra achada foi:",p4)
    print("A quinta palavra achada foi:",p5)
    print("A sexta palavra achada foi:",p6)
    print("A sétima palavra achada foi:",p7)
    print("A oitava palavra achada foi:",p8)
    print("")
    print("A sua pontuação nessa rodada foi: ",pontuacao_rodada)
    print("A sua pontuação total é:",pontuacao_total)
    print("")
    print("O quadro de respostas é:")
    print("")
    #quadro de respostas daqui
    print("+ R + + + + + + + + + L + + + ")
    print("+ + O + + A + + + + + O + + + ")
    print("+ + + S P + A + + + + S + + + ")
    print("+ + + I A + B T + + + A + + + ")
    print("+ + L + + E + + E + + R + + + ")
    print("+ U + + G + + + B L + I + + + ")
    print("T + + O + + + + R + O G + + + ")
    print("+ + N + + + + + O + + I + + + ")
    print("+ I + + + + + + M + + + V + + ")
    print("A + + + + + + + E + + + + + + ")
    print("A I N U T E P + L + + + + + + ")
    print("+ + + + + + + + I + + + + + + ")
    print("+ + + + + + + + A C R A V O + ")
    print("+ + + + + + + + + + + + + + + ")
    print("+ + + + + + + + + + + + + + + ")
    #até aqui
    ##################################################
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    cont5 = 0
    cont6 = 0
    cont7 = 0
    cont8 = 0
    pontuacao_rodada = 0
    print("")
    print("")
    print("")
    print("                             LOADING",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("")
    print("")
    print("")
    print("---------------------------------------------------------------------------")
    print("| Segunda Guerra Mundial - FASE 13                                        |")#titulo e fase
    print("|                                                                         |")
    #FASE1313131313131313131313131313131313131313131313131313131313131313131313131313131313131313131313131313131313131313131313131313131313131313131313131313
    print("|                                                                         |")
    #Colocar o caça daqui
    print("| Z L B X D N Q H E H B F O D P                                           |")
    print("| C F G S I N I L O S S U M I E                                           |")
    print("| S I Z K B R V L E W R C S X A                                           |")
    print("| I S T R E D O A U S X F I V R                                           |")
    print("| W W O L J C S T A L I N Z U L                                           |")
    print("| G F T D A Z Z S B G Z H A R H                                           |")
    print("| P I S U A C I M E T H G N R A                                           |")
    print("| H W S G R I N X G I N V X B R                                           |")
    print("| X T I I C H L H R O X J O J B                                           |")
    print("| O D X K T O E A H M T O Y B O                                           |")
    print("| Z B W I M S P E Y S W X J S R                                           |")
    print("| E I N K B A O Y P D I T C B M                                           |")
    print("| O Z U H O C E E C C P B I C V                                           |")
    print("| O E U J O T M L D S Q B N F N                                           |")
    print("| P M R F E X I V V P N X I K M                                           |")
    #Até aqui
    '''pearlharbor,holocausto,mussolini, aliados, nazismo ,hitler, stalin, eixo'''
    print("|                                                                         |")
    print("| Existem 8 palavras nesse caça palavras (escreva sem espaço e acentos)   |")
    print("---------------------------------------------------------------------------")
    print("")
    print("Dicas:")
    print("   1-É uma base naval dos Estados Unidos e o quartel-general da frota norte-americana do Pacífico, na ilha de O'ahu, Havaí. Foi atacada pelos japoneses na segunda guerra.")
    print("   2-Foi o genocídio ou assassinato em massa de cerca de seis milhões de judeus durante a Segunda Guerra Mundial.")
    print("   3-Primeiro-ministro da Itália. Lider do Facismo.")
    print("   4-Grupo composto por União Soviética, Estados Unidos, Império Britânico, China, França, entre outros.")
    print("   5-É a ideologia associada ao Partido Nazista, ao Estado nazista, bem como a outros grupos de extrema-direita.")
    print("   6-Ele era o Führer da Alemanha. Lider do partido Nazista.")
    print("   7-Lider da União Soviética na Segunda Guerra.")
    print("   8-Grupo formado por Alemanha, Japão e Itália.")
    print("")
    #COLOCAR AS PALAVRAS
    p1= str(input("Qual a primeira palavra que você achou? "))
    while cont1 != 1:
        #Inserir palavras
        if p1.upper() == "STALIN" or p1.upper()== "PEARLHARBOR" or p1.upper()== "NAZISMO" or p1.upper()== "MUSSOLINI" or p1.upper()== "HOLOCAUSTO" or p1.upper()== "HITLER" or p1.upper()== "EIXO" or p1.upper()== "ALIADOS":
            print("A palavra achada foi ",p1)
            cont1 += 1
            pontuacao_rodada += len(p1)*p8x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p1.upper() != "STALIN" or p1.upper()!= "PEARLHARBOR" or p1.upper()!= "NAZISMO" or p1.upper()!= "MUSSOLINI" or p1.upper()!= "HOLOCAUSTO" or p1.upper()!= "HITLER" or p1.upper()!= "EIXO" or p1.upper()!= "ALIADOS":
            print("O dado colocado está inválido")
            p1= str(input("Qual a primeira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| Z L B X D N Q H E H B F O D P                                           |")
    print("| C F G S I N I L O S S U M I E                                           |")
    print("| S I Z K B R V L E W R C S X A                                           |")
    print("| I S T R E D O A U S X F I V R                                           |")
    print("| W W O L J C S T A L I N Z U L                                           |")
    print("| G F T D A Z Z S B G Z H A R H                                           |")
    print("| P I S U A C I M E T H G N R A                                           |")
    print("| H W S G R I N X G I N V X B R                                           |")
    print("| X T I I C H L H R O X J O J B                                           |")
    print("| O D X K T O E A H M T O Y B O                                           |")
    print("| Z B W I M S P E Y S W X J S R                                           |")
    print("| E I N K B A O Y P D I T C B M                                           |")
    print("| O Z U H O C E E C C P B I C V                                           |")
    print("| O E U J O T M L D S Q B N F N                                           |")
    print("| P M R F E X I V V P N X I K M                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p2 = str(input("Qual a segunda palavra que você achou? "))
    while cont2 != 1:
        if p2.upper() == p1.upper():
            print("A palavra está repetida")
            p2 = str(input("Qual a segunda palavra que você achou? "))
        #Inserir palavras
        elif p2.upper() == "STALIN" or p2.upper()== "PEARLHARBOR" or p2.upper()== "NAZISMO" or p2.upper()== "MUSSOLINI" or p2.upper()== "HOLOCAUSTO" or p2.upper()== "HITLER"or p2.upper()== "EIXO"or p2.upper()== "ALIADOS":
            print("A palavra achada foi ",p2)
            cont2 += 1
            pontuacao_rodada += len(p2)*p7x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p2.upper() != "STALIN" or p2.upper()!= "PEARLHARBOR" or p2.upper()!= "NAZISMO" or p2.upper()!= "MUSSOLINI" or p2.upper()!= "HOLOCAUSTO" or p2.upper()!= "HITLER"or p2.upper()!= "EIXO"or p2.upper()!= "ALIADOS":
            print("O dado colocado está inválido")
            p2= str(input("Qual a segunda palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| Z L B X D N Q H E H B F O D P                                           |")
    print("| C F G S I N I L O S S U M I E                                           |")
    print("| S I Z K B R V L E W R C S X A                                           |")
    print("| I S T R E D O A U S X F I V R                                           |")
    print("| W W O L J C S T A L I N Z U L                                           |")
    print("| G F T D A Z Z S B G Z H A R H                                           |")
    print("| P I S U A C I M E T H G N R A                                           |")
    print("| H W S G R I N X G I N V X B R                                           |")
    print("| X T I I C H L H R O X J O J B                                           |")
    print("| O D X K T O E A H M T O Y B O                                           |")
    print("| Z B W I M S P E Y S W X J S R                                           |")
    print("| E I N K B A O Y P D I T C B M                                           |")
    print("| O Z U H O C E E C C P B I C V                                           |")
    print("| O E U J O T M L D S Q B N F N                                           |")
    print("| P M R F E X I V V P N X I K M                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p3 = str(input("Qual a terceira palavra que você achou? "))
    while cont3 != 1:
        if p3.upper()==p1.upper() or p3.upper()==p2.upper():
            print("A palavra está repetida")
            p3 = str(input("Qual a terceira palavra que você achou? "))
        #Inserir palavras
        elif p3.upper() == "STALIN" or p3.upper()== "PEARLHARBOR" or p3.upper()== "NAZISMO" or p3.upper()== "MUSSOLINI" or p3.upper()== "HOLOCAUSTO" or p3.upper()== "HITLER"or p3.upper()== "EIXO"or p3.upper()== "ALIADOS":
            print("A palavra achada foi ",p3)
            cont3 += 1
            pontuacao_rodada += len(p3)*p6x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p3.upper() != "STALIN" or p3.upper()!= "PEARLHARBOR" or p3.upper()!= "NAZISMO" or p3.upper()!= "MUSSOLINI" or p3.upper()!= "HOLOCAUSTO" or p3.upper()!= "HITLER"or p3.upper()!= "EIXO"or p3.upper()!= "ALIADOS":
            print("O dado colocado está inválido")
            p3= str(input("Qual a terceira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| Z L B X D N Q H E H B F O D P                                           |")
    print("| C F G S I N I L O S S U M I E                                           |")
    print("| S I Z K B R V L E W R C S X A                                           |")
    print("| I S T R E D O A U S X F I V R                                           |")
    print("| W W O L J C S T A L I N Z U L                                           |")
    print("| G F T D A Z Z S B G Z H A R H                                           |")
    print("| P I S U A C I M E T H G N R A                                           |")
    print("| H W S G R I N X G I N V X B R                                           |")
    print("| X T I I C H L H R O X J O J B                                           |")
    print("| O D X K T O E A H M T O Y B O                                           |")
    print("| Z B W I M S P E Y S W X J S R                                           |")
    print("| E I N K B A O Y P D I T C B M                                           |")
    print("| O Z U H O C E E C C P B I C V                                           |")
    print("| O E U J O T M L D S Q B N F N                                           |")
    print("| P M R F E X I V V P N X I K M                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p4 = str(input("Qual a quarta palavra que você achou? "))
    while cont4 != 1:
        if p4==p1 or p4==p2 or p4==p3:
            print("A palavra está repetida")
            p4 = str (input("Qual a quarta palavra que você achou? "))
        #Inserir palavras
        elif p4.upper() == "STALIN" or p4.upper()== "PEARLHARBOR" or p4.upper()== "NAZISMO" or p4.upper()== "MUSSOLINI" or p4.upper()== "HOLOCAUSTO" or p4.upper()== "HITLER"or p4.upper()== "EIXO"or p4.upper()== "ALIADOS":
            print("A palavra achada foi ",p4)
            cont4 += 1
            pontuacao_rodada += len(p4)*p5x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p4.upper() != "STALIN" or p4.upper()!= "PEARLHARBOR" or p4.upper()!= "NAZISMO" or p4.upper()!= "MUSSOLINI" or p4.upper()!= "HOLOCAUSTO" or p4.upper()!= "HITLER"or p4.upper()!= "EIXO"or p4.upper()!= "ALIADOS":
            print("O dado colocado está inválido")
            p4 = str(input("Qual a quarta palavra que você achou? "))

    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| Z L B X D N Q H E H B F O D P                                           |")
    print("| C F G S I N I L O S S U M I E                                           |")
    print("| S I Z K B R V L E W R C S X A                                           |")
    print("| I S T R E D O A U S X F I V R                                           |")
    print("| W W O L J C S T A L I N Z U L                                           |")
    print("| G F T D A Z Z S B G Z H A R H                                           |")
    print("| P I S U A C I M E T H G N R A                                           |")
    print("| H W S G R I N X G I N V X B R                                           |")
    print("| X T I I C H L H R O X J O J B                                           |")
    print("| O D X K T O E A H M T O Y B O                                           |")
    print("| Z B W I M S P E Y S W X J S R                                           |")
    print("| E I N K B A O Y P D I T C B M                                           |")
    print("| O Z U H O C E E C C P B I C V                                           |")
    print("| O E U J O T M L D S Q B N F N                                           |")
    print("| P M R F E X I V V P N X I K M                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p5 = str(input("Qual a quinta palavra que você achou? "))
    while cont5 !=1:
        if p5==p1 or p5==p2 or p5==p3 or p5==p4:
            print("A palavra está repetida")
            p5 = str (input("Qual a quinta palavra que você achou? "))
        #Inserir palavras
        elif p5.upper() == "STALIN" or p5.upper()== "PEARLHARBOR" or p5.upper()== "NAZISMO" or p5.upper()== "MUSSOLINI" or p5.upper()== "HOLOCAUSTO" or p5.upper()== "HITLER"or p5.upper()== "EIXO"or p5.upper()== "ALIADOS":
            print("A palavra achada foi ",p5)
            cont5 += 1
            pontuacao_rodada += len(p5)*p4x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p5.upper() != "STALIN" or p5.upper()!= "PEARLHARBOR" or p5.upper()!= "NAZISMO" or p5.upper()!= "MUSSOLINI" or p5.upper()!= "HOLOCAUSTO" or p5.upper()!= "HITLER"or p5.upper()!= "EIXO"or p5.upper()!= "ALIADOS":
            print("O dado colocado está inválido")
            p5 = str(input("Qual a quinta palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| Z L B X D N Q H E H B F O D P                                           |")
    print("| C F G S I N I L O S S U M I E                                           |")
    print("| S I Z K B R V L E W R C S X A                                           |")
    print("| I S T R E D O A U S X F I V R                                           |")
    print("| W W O L J C S T A L I N Z U L                                           |")
    print("| G F T D A Z Z S B G Z H A R H                                           |")
    print("| P I S U A C I M E T H G N R A                                           |")
    print("| H W S G R I N X G I N V X B R                                           |")
    print("| X T I I C H L H R O X J O J B                                           |")
    print("| O D X K T O E A H M T O Y B O                                           |")
    print("| Z B W I M S P E Y S W X J S R                                           |")
    print("| E I N K B A O Y P D I T C B M                                           |")
    print("| O Z U H O C E E C C P B I C V                                           |")
    print("| O E U J O T M L D S Q B N F N                                           |")
    print("| P M R F E X I V V P N X I K M                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p6 = str(input("Qual a sexta palavra que você achou? "))
    while cont6 !=1:
        if p6==p1 or p6==p2 or p6==p3 or p6==p4 or p6==p5:
            print("A palavra está repetida")
            p6 = str (input("Qual a sexta palavra que você achou? "))
        #Inserir palavras
        elif p6.upper() == "STALIN" or p6.upper()== "PEARLHARBOR" or p6.upper()== "NAZISMO" or p6.upper()== "MUSSOLINI" or p6.upper()== "HOLOCAUSTO" or p6.upper()== "HITLER"or p6.upper()== "EIXO"or p6.upper()== "ALIADOS":
            print("A palavra achada foi ",p6)
            cont6 += 1
            pontuacao_rodada += len(p6)*p3x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p6.upper() != "STALIN" or p6.upper()!= "PEARLHARBOR" or p6.upper()!= "NAZISMO" or p6.upper()!= "MUSSOLINI" or p6.upper()!= "HOLOCAUSTO" or p6.upper()!= "HITLER"or p6.upper()!= "EIXO"or p6.upper()!= "ALIADOS":
            print("O dado colocado está inválido")
            p6 = str(input("Qual a sexta palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| Z L B X D N Q H E H B F O D P                                           |")
    print("| C F G S I N I L O S S U M I E                                           |")
    print("| S I Z K B R V L E W R C S X A                                           |")
    print("| I S T R E D O A U S X F I V R                                           |")
    print("| W W O L J C S T A L I N Z U L                                           |")
    print("| G F T D A Z Z S B G Z H A R H                                           |")
    print("| P I S U A C I M E T H G N R A                                           |")
    print("| H W S G R I N X G I N V X B R                                           |")
    print("| X T I I C H L H R O X J O J B                                           |")
    print("| O D X K T O E A H M T O Y B O                                           |")
    print("| Z B W I M S P E Y S W X J S R                                           |")
    print("| E I N K B A O Y P D I T C B M                                           |")
    print("| O Z U H O C E E C C P B I C V                                           |")
    print("| O E U J O T M L D S Q B N F N                                           |")
    print("| P M R F E X I V V P N X I K M                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p7 = str(input("Qual a sétima palavra que você achou? "))
    while cont7 !=1:
        if p7==p1 or p7==p2 or p7==p3 or p7==p4 or p7==p5 or p7==p6:
            print("A palavra está repetida")
            p7 = str (input("Qual a sétima palavra que você achou? "))
        #Inserir palavras
        elif p7.upper() == "STALIN" or p7.upper()== "PEARLHARBOR" or p7.upper()== "NAZISMO" or p7.upper()== "MUSSOLINI" or p7.upper()== "HOLOCAUSTO" or p7.upper()== "HITLER"or p7.upper()== "EIXO"or p7.upper()== "ALIADOS":
            print("A palavra achada foi ",p7)
            cont7 += 1
            pontuacao_rodada += len(p7)*p2x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p7.upper() != "STALIN" or p7.upper()!= "PEARLHARBOR" or p7.upper()!= "NAZISMO" or p7.upper()!= "MUSSOLINI" or p7.upper()!= "HOLOCAUSTO" or p7.upper()!= "HITLER"or p7.upper()!= "EIXO"or p7.upper()!= "ALIADOS":
            print("O dado colocado está inválido")
            p7 = str(input("Qual a sétima palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| Z L B X D N Q H E H B F O D P                                           |")
    print("| C F G S I N I L O S S U M I E                                           |")
    print("| S I Z K B R V L E W R C S X A                                           |")
    print("| I S T R E D O A U S X F I V R                                           |")
    print("| W W O L J C S T A L I N Z U L                                           |")
    print("| G F T D A Z Z S B G Z H A R H                                           |")
    print("| P I S U A C I M E T H G N R A                                           |")
    print("| H W S G R I N X G I N V X B R                                           |")
    print("| X T I I C H L H R O X J O J B                                           |")
    print("| O D X K T O E A H M T O Y B O                                           |")
    print("| Z B W I M S P E Y S W X J S R                                           |")
    print("| E I N K B A O Y P D I T C B M                                           |")
    print("| O Z U H O C E E C C P B I C V                                           |")
    print("| O E U J O T M L D S Q B N F N                                           |")
    print("| P M R F E X I V V P N X I K M                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p8 = str(input("Qual a oitava palavra que você achou? "))
    while cont8 !=1:
        if p8==p1 or p8==p2 or p8==p3 or p8==p4 or p8==p5 or p8==p6 or p8==p7:
            print("A palavra está repetida")
            p8 = str (input("Qual a oitava palavra que você achou? "))
        #Inserir palavras
        elif p8.upper() == "STALIN" or p8.upper()== "PEARLHARBOR" or p8.upper()== "NAZISMO" or p8.upper()== "MUSSOLINI" or p8.upper()== "HOLOCAUSTO" or p8.upper()== "HITLER"or p8.upper()== "EIXO"or p8.upper()== "ALIADOS":
            print("A palavra achada foi ",p8)
            cont8 += 1
            pontuacao_rodada += len(p8)*p1x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p8.upper() != "STALIN" or p8.upper()!= "PEARLHARBOR" or p8.upper()!= "NAZISMO" or p8.upper()!= "MUSSOLINI" or p8.upper()!= "HOLOCAUSTO" or p8.upper()!= "HITLER"or p8.upper()!= "EIXO"or p8.upper()!= "ALIADOS":
            print("O dado colocado está inválido")
            p8 = str(input("Qual a oitava palavra que você achou? "))
    print("")
    print("A primeira palavra achada foi:",p1)
    print("A segunda palavra achada foi:",p2)
    print("A terceira palavra achada foi:",p3)
    print("A quarta palavra achada foi:",p4)
    print("A quinta palavra achada foi:",p5)
    print("A sexta palavra achada foi:",p6)
    print("A sétima palavra achada foi:",p7)
    print("A oitava palavra achada foi:",p8)
    print("")
    print("A sua pontuação nessa rodada foi: ",pontuacao_rodada)
    print("A sua pontuação total é:",pontuacao_total)
    print("")
    print("O quadro de respostas é:")
    print("")
    #quadro de respostas daqui
    print("+ + + + + + + + + H + + O + P ")
    print("+ + + + I N I L O S S U M + E ")
    print("+ + + + + R + L + + + + S + A ")
    print("+ S + + E + O + + + + + I + R ")
    print("+ + O L + C S T A L I N Z + L ")
    print("+ + T D A + + + + + + + A + H ")
    print("+ I + U A + + + E + + + N + A ")
    print("H + S + + I + + + I + + + + R ")
    print("+ T + + + + L + + + X + + + B ")
    print("O + + + + + + A + + + O + + O ")
    print("+ + + + + + + + + + + + + + R ")
    print("+ + + + + + + + + + + + + + + ")
    print("+ + + + + + + + + + + + + + + ")
    print("+ + + + + + + + + + + + + + + ")
    print("+ + + + + + + + + + + + + + + ")
    #até aqui

    ##################################################
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    cont5 = 0
    cont6 = 0
    cont7 = 0
    cont8 = 0
    pontuacao_rodada = 0
    print("")
    print("")
    print("")
    print("                             LOADING",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("")
    print("")
    print("")
    print("---------------------------------------------------------------------------")
    print("| Iluminismo - FASE 14                                                    |")#titulo e fase
    print("|                                                                         |")
    #FASE141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414
    print("|                                                                         |")
    #Colocar o caça daqui
    print("| S P M N P V U J U Z G J M E Q                                           |")
    print("| K E A O J E K O T Q O J L Z Y                                           |")
    print("| D F Z V N K W V W H B Y A D M                                           |")
    print("| R C O U M T E U N G A V F U D                                           |")
    print("| R K N F L Z E L X B K I D V C                                           |")
    print("| W Y I Z V S O S E K O W A L E                                           |")
    print("| P X P B G C A R Q A A R V U G                                           |")
    print("| W T S Y K C R D V U S N I C Y                                           |")
    print("| E E H E H E C W O X I U D Q H                                           |")
    print("| Q A C E I I Z Z L L E E H P W                                           |")
    print("| T Q U P L W I M L G U E U G L                                           |")
    print("| R E R I A T L O V C D C M E U                                           |")
    print("| I S A A C N E W T O N Y E C W                                           |")
    print("| C D B O T Y J W Z X S K V S I                                           |")
    print("| W S X H P Y B M P R A P M Q S                                           |")
    #Até aqui
    '''seculodasluzes
    , Baruchspinoza
    , montesquieu
    , pierrebayle
    , isaacnewton
    , davidhume
    , johnlocke
    , voltaire'''
    print("|                                                                         |")
    print("| Existem 8 palavras nesse caça palavras (escreva sem espaço e acentos)   |")
    print("---------------------------------------------------------------------------")
    print("")
    print("Dicas:")
    print("   1-Também é conhecido como Iluminismo.")
    print("   2-Foi um dos grandes racionalistas e filósofos do século XVII dentro da chamada Filosofia Moderna, juntamente com René Descartes e Gottfried Leibniz. Nasceu em Amsterdã, nos Países Baixos, no seio de uma família judaica portuguesa e é considerado o fundador do criticismo bíblico moderno.")
    print("   3-Foi um político, filósofo e escritor francês. Ficou famoso pela sua teoria da separação dos poderes, atualmente consagrada em muitas das modernas constituições internacionais.")
    print("   4-Foi um filósofo cético e escritor francês, pai da tolerância religiosa e autor do “Dicionário Histórico e Crítico”, o livro mais popular na Europa no fim do século XVII e começo do século XVIII.")
    print("   5-Pai da lei da gravitação. Diz a lenda que ele começou a desenvolver a lei depois que uma maçã caiu em sua cabeça.")
    print("   6-Segundo ele, todos mantêm um número de crenças, ações individuais e instituições sociais. Tais crenças bases incluem a realidade das relações causais (que algumas coisas podem e causam mudanças em outras coisas), a realidade do mundo externo(que a existência do mundo não depende de estar sendo observado) e da existência continuada do conhecimento do eu.")
    print("   7-Foi um filósofo inglês conhecido como o “pai do liberalismo”, sendo considerado o principal representante do empirismo britânico e um dos principais teóricos do contrato social.")
    print("   8-Conhecido pela sua perspicácia e espirituosidade na defesa das liberdades civis, inclusive liberdade religiosa e livre comércio, é uma dentre muitas figuras do Iluminismo cujas obras e ideias influenciaram pensadores importantes tanto da Revolução Francesa quanto da Americana.")
    print("")
    #COLOCAR AS PALAVRAS
    p1= str(input("Qual a primeira palavra que você achou? "))
    while cont1 != 1:
        #Inserir palavras
        if p1.upper() == "VOLTAIRE" or p1.upper()== "SECULODASLUZES" or p1.upper()== "PIERREBAYLE" or p1.upper()== "MONTESQUIEU" or p1.upper()== "JOHNLOCKE" or p1.upper()== "ISAACNEWTON" or p1.upper()== "DAVIDHUME" or p1.upper()== "BARUCHSPINOZA":
            print("A palavra achada foi ",p1)
            cont1 += 1
            pontuacao_rodada += len(p1)*p8x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p1.upper() != "VOLTAIRE" or p1.upper()!= "SECULODASLUZES" or p1.upper()!= "PIERREBAYLE" or p1.upper()!= "MONTESQUIEU" or p1.upper()!= "JOHNLOCKE" or p1.upper()!= "ISAACNEWTON" or p1.upper()!= "DAVIDHUME" or p1.upper()!= "BARUCHSPINOZA":
            print("O dado colocado está inválido")
            p1= str(input("Qual a primeira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| S P M N P V U J U Z G J M E Q                                           |")
    print("| K E A O J E K O T Q O J L Z Y                                           |")
    print("| D F Z V N K W V W H B Y A D M                                           |")
    print("| R C O U M T E U N G A V F U D                                           |")
    print("| R K N F L Z E L X B K I D V C                                           |")
    print("| W Y I Z V S O S E K O W A L E                                           |")
    print("| P X P B G C A R Q A A R V U G                                           |")
    print("| W T S Y K C R D V U S N I C Y                                           |")
    print("| E E H E H E C W O X I U D Q H                                           |")
    print("| Q A C E I I Z Z L L E E H P W                                           |")
    print("| T Q U P L W I M L G U E U G L                                           |")
    print("| R E R I A T L O V C D C M E U                                           |")
    print("| I S A A C N E W T O N Y E C W                                           |")
    print("| C D B O T Y J W Z X S K V S I                                           |")
    print("| W S X H P Y B M P R A P M Q S                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p2 = str(input("Qual a segunda palavra que você achou? "))
    while cont2 != 1:
        if p2.upper() == p1.upper():
            print("A palavra está repetida")
            p2 = str(input("Qual a segunda palavra que você achou? "))
        #Inserir palavras
        elif p2.upper() == "VOLTAIRE" or p2.upper()== "SECULODASLUZES" or p2.upper()== "PIERREBAYLE" or p2.upper()== "MONTESQUIEU" or p2.upper()== "JOHNLOCKE" or p2.upper()== "ISAACNEWTON"or p2.upper()== "DAVIDHUME"or p2.upper()== "BARUCHSPINOZA":
            print("A palavra achada foi ",p2)
            cont2 += 1
            pontuacao_rodada += len(p2)*p7x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p2.upper() != "VOLTAIRE" or p2.upper()!= "SECULODASLUZES" or p2.upper()!= "PIERREBAYLE" or p2.upper()!= "MONTESQUIEU" or p2.upper()!= "JOHNLOCKE" or p2.upper()!= "ISAACNEWTON"or p2.upper()!= "DAVIDHUME"or p2.upper()!= "BARUCHSPINOZA":
            print("O dado colocado está inválido")
            p2= str(input("Qual a segunda palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| S P M N P V U J U Z G J M E Q                                           |")
    print("| K E A O J E K O T Q O J L Z Y                                           |")
    print("| D F Z V N K W V W H B Y A D M                                           |")
    print("| R C O U M T E U N G A V F U D                                           |")
    print("| R K N F L Z E L X B K I D V C                                           |")
    print("| W Y I Z V S O S E K O W A L E                                           |")
    print("| P X P B G C A R Q A A R V U G                                           |")
    print("| W T S Y K C R D V U S N I C Y                                           |")
    print("| E E H E H E C W O X I U D Q H                                           |")
    print("| Q A C E I I Z Z L L E E H P W                                           |")
    print("| T Q U P L W I M L G U E U G L                                           |")
    print("| R E R I A T L O V C D C M E U                                           |")
    print("| I S A A C N E W T O N Y E C W                                           |")
    print("| C D B O T Y J W Z X S K V S I                                           |")
    print("| W S X H P Y B M P R A P M Q S                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p3 = str(input("Qual a terceira palavra que você achou? "))
    while cont3 != 1:
        if p3.upper()==p1.upper() or p3.upper()==p2.upper():
            print("A palavra está repetida")
            p3 = str(input("Qual a terceira palavra que você achou? "))
        #Inserir palavras
        elif p3.upper() == "VOLTAIRE" or p3.upper()== "SECULODASLUZES" or p3.upper()== "PIERREBAYLE" or p3.upper()== "MONTESQUIEU" or p3.upper()== "JOHNLOCKE" or p3.upper()== "ISAACNEWTON"or p3.upper()== "DAVIDHUME"or p3.upper()== "BARUCHSPINOZA":
            print("A palavra achada foi ",p3)
            cont3 += 1
            pontuacao_rodada += len(p3)*p6x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p3.upper() != "VOLTAIRE" or p3.upper()!= "SECULODASLUZES" or p3.upper()!= "PIERREBAYLE" or p3.upper()!= "MONTESQUIEU" or p3.upper()!= "JOHNLOCKE" or p3.upper()!= "ISAACNEWTON"or p3.upper()!= "DAVIDHUME"or p3.upper()!= "BARUCHSPINOZA":
            print("O dado colocado está inválido")
            p3= str(input("Qual a terceira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| S P M N P V U J U Z G J M E Q                                           |")
    print("| K E A O J E K O T Q O J L Z Y                                           |")
    print("| D F Z V N K W V W H B Y A D M                                           |")
    print("| R C O U M T E U N G A V F U D                                           |")
    print("| R K N F L Z E L X B K I D V C                                           |")
    print("| W Y I Z V S O S E K O W A L E                                           |")
    print("| P X P B G C A R Q A A R V U G                                           |")
    print("| W T S Y K C R D V U S N I C Y                                           |")
    print("| E E H E H E C W O X I U D Q H                                           |")
    print("| Q A C E I I Z Z L L E E H P W                                           |")
    print("| T Q U P L W I M L G U E U G L                                           |")
    print("| R E R I A T L O V C D C M E U                                           |")
    print("| I S A A C N E W T O N Y E C W                                           |")
    print("| C D B O T Y J W Z X S K V S I                                           |")
    print("| W S X H P Y B M P R A P M Q S                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p4 = str(input("Qual a quarta palavra que você achou? "))
    while cont4 != 1:
        if p4==p1 or p4==p2 or p4==p3:
            print("A palavra está repetida")
            p4 = str (input("Qual a quarta palavra que você achou? "))
        #Inserir palavras
        elif p4.upper() == "VOLTAIRE" or p4.upper()== "SECULODASLUZES" or p4.upper()== "PIERREBAYLE" or p4.upper()== "MONTESQUIEU" or p4.upper()== "JOHNLOCKE" or p4.upper()== "ISAACNEWTON"or p4.upper()== "DAVIDHUME"or p4.upper()== "BARUCHSPINOZA":
            print("A palavra achada foi ",p4)
            cont4 += 1
            pontuacao_rodada += len(p4)*p5x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p4.upper() != "VOLTAIRE" or p4.upper()!= "SECULODASLUZES" or p4.upper()!= "PIERREBAYLE" or p4.upper()!= "MONTESQUIEU" or p4.upper()!= "JOHNLOCKE" or p4.upper()!= "ISAACNEWTON"or p4.upper()!= "DAVIDHUME"or p4.upper()!= "BARUCHSPINOZA":
            print("O dado colocado está inválido")
            p4 = str(input("Qual a quarta palavra que você achou? "))

    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| S P M N P V U J U Z G J M E Q                                           |")
    print("| K E A O J E K O T Q O J L Z Y                                           |")
    print("| D F Z V N K W V W H B Y A D M                                           |")
    print("| R C O U M T E U N G A V F U D                                           |")
    print("| R K N F L Z E L X B K I D V C                                           |")
    print("| W Y I Z V S O S E K O W A L E                                           |")
    print("| P X P B G C A R Q A A R V U G                                           |")
    print("| W T S Y K C R D V U S N I C Y                                           |")
    print("| E E H E H E C W O X I U D Q H                                           |")
    print("| Q A C E I I Z Z L L E E H P W                                           |")
    print("| T Q U P L W I M L G U E U G L                                           |")
    print("| R E R I A T L O V C D C M E U                                           |")
    print("| I S A A C N E W T O N Y E C W                                           |")
    print("| C D B O T Y J W Z X S K V S I                                           |")
    print("| W S X H P Y B M P R A P M Q S                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p5 = str(input("Qual a quinta palavra que você achou? "))
    while cont5 !=1:
        if p5==p1 or p5==p2 or p5==p3 or p5==p4:
            print("A palavra está repetida")
            p5 = str (input("Qual a quinta palavra que você achou? "))
        #Inserir palavras
        elif p5.upper() == "VOLTAIRE" or p5.upper()== "SECULODASLUZES" or p5.upper()== "PIERREBAYLE" or p5.upper()== "MONTESQUIEU" or p5.upper()== "JOHNLOCKE" or p5.upper()== "ISAACNEWTON"or p5.upper()== "DAVIDHUME"or p5.upper()== "BARUCHSPINOZA":
            print("A palavra achada foi ",p5)
            cont5 += 1
            pontuacao_rodada += len(p5)*p4x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p5.upper() != "VOLTAIRE" or p5.upper()!= "SECULODASLUZES" or p5.upper()!= "PIERREBAYLE" or p5.upper()!= "MONTESQUIEU" or p5.upper()!= "JOHNLOCKE" or p5.upper()!= "ISAACNEWTON"or p5.upper()!= "DAVIDHUME"or p5.upper()!= "BARUCHSPINOZA":
            print("O dado colocado está inválido")
            p5 = str(input("Qual a quinta palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| S P M N P V U J U Z G J M E Q                                           |")
    print("| K E A O J E K O T Q O J L Z Y                                           |")
    print("| D F Z V N K W V W H B Y A D M                                           |")
    print("| R C O U M T E U N G A V F U D                                           |")
    print("| R K N F L Z E L X B K I D V C                                           |")
    print("| W Y I Z V S O S E K O W A L E                                           |")
    print("| P X P B G C A R Q A A R V U G                                           |")
    print("| W T S Y K C R D V U S N I C Y                                           |")
    print("| E E H E H E C W O X I U D Q H                                           |")
    print("| Q A C E I I Z Z L L E E H P W                                           |")
    print("| T Q U P L W I M L G U E U G L                                           |")
    print("| R E R I A T L O V C D C M E U                                           |")
    print("| I S A A C N E W T O N Y E C W                                           |")
    print("| C D B O T Y J W Z X S K V S I                                           |")
    print("| W S X H P Y B M P R A P M Q S                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p6 = str(input("Qual a sexta palavra que você achou? "))
    while cont6 !=1:
        if p6==p1 or p6==p2 or p6==p3 or p6==p4 or p6==p5:
            print("A palavra está repetida")
            p6 = str (input("Qual a sexta palavra que você achou? "))
        #Inserir palavras
        elif p6.upper() == "VOLTAIRE" or p6.upper()== "SECULODASLUZES" or p6.upper()== "PIERREBAYLE" or p6.upper()== "MONTESQUIEU" or p6.upper()== "JOHNLOCKE" or p6.upper()== "ISAACNEWTON"or p6.upper()== "DAVIDHUME"or p6.upper()== "BARUCHSPINOZA":
            print("A palavra achada foi ",p6)
            cont6 += 1
            pontuacao_rodada += len(p6)*p3x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p6.upper() != "VOLTAIRE" or p6.upper()!= "SECULODASLUZES" or p6.upper()!= "PIERREBAYLE" or p6.upper()!= "MONTESQUIEU" or p6.upper()!= "JOHNLOCKE" or p6.upper()!= "ISAACNEWTON"or p6.upper()!= "DAVIDHUME"or p6.upper()!= "BARUCHSPINOZA":
            print("O dado colocado está inválido")
            p6 = str(input("Qual a sexta palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| S P M N P V U J U Z G J M E Q                                           |")
    print("| K E A O J E K O T Q O J L Z Y                                           |")
    print("| D F Z V N K W V W H B Y A D M                                           |")
    print("| R C O U M T E U N G A V F U D                                           |")
    print("| R K N F L Z E L X B K I D V C                                           |")
    print("| W Y I Z V S O S E K O W A L E                                           |")
    print("| P X P B G C A R Q A A R V U G                                           |")
    print("| W T S Y K C R D V U S N I C Y                                           |")
    print("| E E H E H E C W O X I U D Q H                                           |")
    print("| Q A C E I I Z Z L L E E H P W                                           |")
    print("| T Q U P L W I M L G U E U G L                                           |")
    print("| R E R I A T L O V C D C M E U                                           |")
    print("| I S A A C N E W T O N Y E C W                                           |")
    print("| C D B O T Y J W Z X S K V S I                                           |")
    print("| W S X H P Y B M P R A P M Q S                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p7 = str(input("Qual a sétima palavra que você achou? "))
    while cont7 !=1:
        if p7==p1 or p7==p2 or p7==p3 or p7==p4 or p7==p5 or p7==p6:
            print("A palavra está repetida")
            p7 = str (input("Qual a sétima palavra que você achou? "))
        #Inserir palavras
        elif p7.upper() == "VOLTAIRE" or p7.upper()== "SECULODASLUZES" or p7.upper()== "PIERREBAYLE" or p7.upper()== "MONTESQUIEU" or p7.upper()== "JOHNLOCKE" or p7.upper()== "ISAACNEWTON"or p7.upper()== "DAVIDHUME"or p7.upper()== "BARUCHSPINOZA":
            print("A palavra achada foi ",p7)
            cont7 += 1
            pontuacao_rodada += len(p7)*p2x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p7.upper() != "VOLTAIRE" or p7.upper()!= "SECULODASLUZES" or p7.upper()!= "PIERREBAYLE" or p7.upper()!= "MONTESQUIEU" or p7.upper()!= "JOHNLOCKE" or p7.upper()!= "ISAACNEWTON"or p7.upper()!= "DAVIDHUME"or p7.upper()!= "BARUCHSPINOZA":
            print("O dado colocado está inválido")
            p7 = str(input("Qual a sétima palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| S P M N P V U J U Z G J M E Q                                           |")
    print("| K E A O J E K O T Q O J L Z Y                                           |")
    print("| D F Z V N K W V W H B Y A D M                                           |")
    print("| R C O U M T E U N G A V F U D                                           |")
    print("| R K N F L Z E L X B K I D V C                                           |")
    print("| W Y I Z V S O S E K O W A L E                                           |")
    print("| P X P B G C A R Q A A R V U G                                           |")
    print("| W T S Y K C R D V U S N I C Y                                           |")
    print("| E E H E H E C W O X I U D Q H                                           |")
    print("| Q A C E I I Z Z L L E E H P W                                           |")
    print("| T Q U P L W I M L G U E U G L                                           |")
    print("| R E R I A T L O V C D C M E U                                           |")
    print("| I S A A C N E W T O N Y E C W                                           |")
    print("| C D B O T Y J W Z X S K V S I                                           |")
    print("| W S X H P Y B M P R A P M Q S                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p8 = str(input("Qual a oitava palavra que você achou? "))
    while cont8 !=1:
        if p8==p1 or p8==p2 or p8==p3 or p8==p4 or p8==p5 or p8==p6 or p8==p7:
            print("A palavra está repetida")
            p8 = str (input("Qual a oitava palavra que você achou? "))
        #Inserir palavras
        elif p8.upper() == "VOLTAIRE" or p8.upper()== "SECULODASLUZES" or p8.upper()== "PIERREBAYLE" or p8.upper()== "MONTESQUIEU" or p8.upper()== "JOHNLOCKE" or p8.upper()== "ISAACNEWTON"or p8.upper()== "DAVIDHUME"or p8.upper()== "BARUCHSPINOZA":
            print("A palavra achada foi ",p8)
            cont8 += 1
            pontuacao_rodada += len(p8)*p1x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p8.upper() != "VOLTAIRE" or p8.upper()!= "SECULODASLUZES" or p8.upper()!= "PIERREBAYLE" or p8.upper()!= "MONTESQUIEU" or p8.upper()!= "JOHNLOCKE" or p8.upper()!= "ISAACNEWTON"or p8.upper()!= "DAVIDHUME"or p8.upper()!= "BARUCHSPINOZA":
            print("O dado colocado está inválido")
            p8 = str(input("Qual a oitava palavra que você achou? "))
    print("")
    print("A primeira palavra achada foi:",p1)
    print("A segunda palavra achada foi:",p2)
    print("A terceira palavra achada foi:",p3)
    print("A quarta palavra achada foi:",p4)
    print("A quinta palavra achada foi:",p5)
    print("A sexta palavra achada foi:",p6)
    print("A sétima palavra achada foi:",p7)
    print("A oitava palavra achada foi:",p8)
    print("")
    print("A sua pontuação nessa rodada foi: ",pontuacao_rodada)
    print("A sua pontuação total é:",pontuacao_total)
    print("")
    print("O quadro de respostas é:")
    print("")
    #quadro de respostas daqui
    print("S + M + + + + + + + + J + E + ")
    print("+ E A O + + + + + + O + L + + ")
    print("+ + Z + N + + + + H + Y + + + ")
    print("+ + O U + T + + N + A + + + + ")
    print("+ + N + L + E L + B + + D + + ")
    print("+ + I + + S O S E + + + A + + ")
    print("+ + P + + C A R Q + + + V + + ")
    print("+ + S + K + R D + U + + I + + ")
    print("+ + H E + E + + O + I + D + + ")
    print("+ + C + I + + + + L + E H + + ")
    print("+ + U P + + + + + + U + U + + ")
    print("+ E R I A T L O V + + C M + + ")
    print("I S A A C N E W T O N + E + + ")
    print("+ + B + + + + + + + + + + S + ")
    print("+ + + + + + + + + + + + + + + ")
    #até aqui
    ##################################################
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    cont5 = 0
    cont6 = 0
    cont7 = 0
    cont8 = 0
    pontuacao_rodada = 0
    print("")
    print("")
    print("")
    print("                             LOADING",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("")
    print("")
    print("")
    print("---------------------------------------------------------------------------")
    print("| Componentes do computador - FASE 15                                     |")#titulo e fase
    print("|                                                                         |")
    #FASE151515151515151515151515151515151515151515151515151515151515151515151515151515151515151515151515151515151515151515151515151515151515151515151515151515
    print("|                                                                         |")
    #Colocar o caça daqui
    print("| K V T U Y O T M X R K L K P E                                           |")
    print("| G V F K P W W F E K V D L T I                                           |")
    print("| J U M L R F T L R N A A E G O                                           |")
    print("| F C U W N F S I I I C N D H F                                           |")
    print("| N O D O X L P W A A I C Y H P                                           |")
    print("| E F N K K V X N D B B I D R F                                           |")
    print("| A V K T Z H Z E A L W V G C W                                           |")
    print("| M K I D E Z V G T H Y H W C H                                           |")
    print("| A F K R U I N V X H H F C A M                                           |")
    print("| C R V Z D M A R A I R O M E M                                           |")
    print("| A L I E I D Z F D V X G S G Q                                           |")
    print("| L J O T F V R U R H H N J Q G                                           |")
    print("| P C O O L E R A D I N E M Z S                                           |")
    print("| T A E H X Z B N H O E H N Z Y                                           |")
    print("| C R E G I S T R A D O R X Z P                                           |")
    #Até aqui
    ''' placadevideo, registrador, memoriaram, harddrive,gabinete, placamae, cooler, fonte'''
    print("|                                                                         |")
    print("Existem 8 palavras nesse caça palavras (escreva sem espaço e acentos)")
    print("---------------------------------------------------------------------------")
    print("")
    print("Dicas:")
    print("   1-É um componente de um computador que envia sinais deste para o ecrã, de forma que possam ser apresentadas imagens ao utilizador. Normalmente possui memória, com capacidade medida em catetos.")
    print("   2-É uma pequena porção de memória localizada no processador central. Permitem acessos muito rápidos a dados e são usados para aumentar a velocidade de execução de programas.")
    print("   3-É um tipo de memória que permite a leitura e a escrita, utilizada como memória primária em sistemas eletrônicos digitais.")
    print("   4-É a parte do computador onde são armazenados os dados. É uma memória não-volátil, ou seja, as informações não são perdidas quando o computador é desligado, sendo considerado o principal meio de armazenamento de dados em massa. (Em inglês)")
    print("   5-É o compartimento que contém a maioria dos componentes de um computador.")
    print("   6-É a parte do computador responsável por conectar e interligar todos os componentes do computador, ou seja, processador com memória RAM, disco rígido, placa gráfica, entre outros.")
    print("   7-É um sistema de arrefecimento usado em diversos tipos de hardwares eletrônicos com o objetivo de evitar a sobrecarga de calor que estes componentes geram.")
    print("   8-É um equipamento usado para alimentar cargas elétricas.")
    print("")
    #COLOCAR AS PALAVRAS
    p1= str(input("Qual a primeira palavra que você achou? "))
    while cont1 != 1:
        #Inserir palavras
        if p1.upper() == "REGISTRADOR" or p1.upper()== "PLACAMAE" or p1.upper()== "PLACADEVIDEO" or p1.upper()== "MEMORIARAM" or p1.upper()== "HARDDRIVE" or p1.upper()== "GABINETE" or p1.upper()== "FONTE" or p1.upper()== "COOLER":
            print("A palavra achada foi ",p1)
            cont1 += 1
            pontuacao_rodada += len(p1)*p8x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p1.upper() != "REGISTRADOR" or p1.upper()!= "PLACAMAE" or p1.upper()!= "PLACADEVIDEO" or p1.upper()!= "MEMORIARAM" or p1.upper()!= "HARDDRIVE" or p1.upper()!= "GABINETE" or p1.upper()!= "FONTE" or p1.upper()!= "COOLER":
            print("O dado colocado está inválido")
            p1= str(input("Qual a primeira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| K V T U Y O T M X R K L K P E                                           |")
    print("| G V F K P W W F E K V D L T I                                           |")
    print("| J U M L R F T L R N A A E G O                                           |")
    print("| F C U W N F S I I I C N D H F                                           |")
    print("| N O D O X L P W A A I C Y H P                                           |")
    print("| E F N K K V X N D B B I D R F                                           |")
    print("| A V K T Z H Z E A L W V G C W                                           |")
    print("| M K I D E Z V G T H Y H W C H                                           |")
    print("| A F K R U I N V X H H F C A M                                           |")
    print("| C R V Z D M A R A I R O M E M                                           |")
    print("| A L I E I D Z F D V X G S G Q                                           |")
    print("| L J O T F V R U R H H N J Q G                                           |")
    print("| P C O O L E R A D I N E M Z S                                           |")
    print("| T A E H X Z B N H O E H N Z Y                                           |")
    print("| C R E G I S T R A D O R X Z P                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p2 = str(input("Qual a segunda palavra que você achou? "))
    while cont2 != 1:
        if p2.upper() == p1.upper():
            print("A palavra está repetida")
            p2 = str(input("Qual a segunda palavra que você achou? "))
        #Inserir palavras
        elif p2.upper() == "REGISTRADOR" or p2.upper()== "PLACAMAE" or p2.upper()== "PLACADEVIDEO" or p2.upper()== "MEMORIARAM" or p2.upper()== "HARDDRIVE" or p2.upper()== "GABINETE"or p2.upper()== "FONTE"or p2.upper()== "COOLER":
            print("A palavra achada foi ",p2)
            cont2 += 1
            pontuacao_rodada += len(p2)*p7x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p2.upper() != "REGISTRADOR" or p2.upper()!= "PLACAMAE" or p2.upper()!= "PLACADEVIDEO" or p2.upper()!= "MEMORIARAM" or p2.upper()!= "HARDDRIVE" or p2.upper()!= "GABINETE"or p2.upper()!= "FONTE"or p2.upper()!= "COOLER":
            print("O dado colocado está inválido")
            p2= str(input("Qual a segunda palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| K V T U Y O T M X R K L K P E                                           |")
    print("| G V F K P W W F E K V D L T I                                           |")
    print("| J U M L R F T L R N A A E G O                                           |")
    print("| F C U W N F S I I I C N D H F                                           |")
    print("| N O D O X L P W A A I C Y H P                                           |")
    print("| E F N K K V X N D B B I D R F                                           |")
    print("| A V K T Z H Z E A L W V G C W                                           |")
    print("| M K I D E Z V G T H Y H W C H                                           |")
    print("| A F K R U I N V X H H F C A M                                           |")
    print("| C R V Z D M A R A I R O M E M                                           |")
    print("| A L I E I D Z F D V X G S G Q                                           |")
    print("| L J O T F V R U R H H N J Q G                                           |")
    print("| P C O O L E R A D I N E M Z S                                           |")
    print("| T A E H X Z B N H O E H N Z Y                                           |")
    print("| C R E G I S T R A D O R X Z P                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p3 = str(input("Qual a terceira palavra que você achou? "))
    while cont3 != 1:
        if p3.upper()==p1.upper() or p3.upper()==p2.upper():
            print("A palavra está repetida")
            p3 = str(input("Qual a terceira palavra que você achou? "))
        #Inserir palavras
        elif p3.upper() == "REGISTRADOR" or p3.upper()== "PLACAMAE" or p3.upper()== "PLACADEVIDEO" or p3.upper()== "MEMORIARAM" or p3.upper()== "HARDDRIVE" or p3.upper()== "GABINETE"or p3.upper()== "FONTE"or p3.upper()== "COOLER":
            print("A palavra achada foi ",p3)
            cont3 += 1
            pontuacao_rodada += len(p3)*p6x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p3.upper() != "REGISTRADOR" or p3.upper()!= "PLACAMAE" or p3.upper()!= "PLACADEVIDEO" or p3.upper()!= "MEMORIARAM" or p3.upper()!= "HARDDRIVE" or p3.upper()!= "GABINETE"or p3.upper()!= "FONTE"or p3.upper()!= "COOLER":
            print("O dado colocado está inválido")
            p3= str(input("Qual a terceira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| K V T U Y O T M X R K L K P E                                           |")
    print("| G V F K P W W F E K V D L T I                                           |")
    print("| J U M L R F T L R N A A E G O                                           |")
    print("| F C U W N F S I I I C N D H F                                           |")
    print("| N O D O X L P W A A I C Y H P                                           |")
    print("| E F N K K V X N D B B I D R F                                           |")
    print("| A V K T Z H Z E A L W V G C W                                           |")
    print("| M K I D E Z V G T H Y H W C H                                           |")
    print("| A F K R U I N V X H H F C A M                                           |")
    print("| C R V Z D M A R A I R O M E M                                           |")
    print("| A L I E I D Z F D V X G S G Q                                           |")
    print("| L J O T F V R U R H H N J Q G                                           |")
    print("| P C O O L E R A D I N E M Z S                                           |")
    print("| T A E H X Z B N H O E H N Z Y                                           |")
    print("| C R E G I S T R A D O R X Z P                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p4 = str(input("Qual a quarta palavra que você achou? "))
    while cont4 != 1:
        if p4==p1 or p4==p2 or p4==p3:
            print("A palavra está repetida")
            p4 = str (input("Qual a quarta palavra que você achou? "))
        #Inserir palavras
        elif p4.upper() == "REGISTRADOR" or p4.upper()== "PLACAMAE" or p4.upper()== "PLACADEVIDEO" or p4.upper()== "MEMORIARAM" or p4.upper()== "HARDDRIVE" or p4.upper()== "GABINETE"or p4.upper()== "FONTE"or p4.upper()== "COOLER":
            print("A palavra achada foi ",p4)
            cont4 += 1
            pontuacao_rodada += len(p4)*p5x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p4.upper() != "REGISTRADOR" or p4.upper()!= "PLACAMAE" or p4.upper()!= "PLACADEVIDEO" or p4.upper()!= "MEMORIARAM" or p4.upper()!= "HARDDRIVE" or p4.upper()!= "GABINETE"or p4.upper()!= "FONTE"or p4.upper()!= "COOLER":
            print("O dado colocado está inválido")
            p4 = str(input("Qual a quarta palavra que você achou? "))

    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| K V T U Y O T M X R K L K P E                                           |")
    print("| G V F K P W W F E K V D L T I                                           |")
    print("| J U M L R F T L R N A A E G O                                           |")
    print("| F C U W N F S I I I C N D H F                                           |")
    print("| N O D O X L P W A A I C Y H P                                           |")
    print("| E F N K K V X N D B B I D R F                                           |")
    print("| A V K T Z H Z E A L W V G C W                                           |")
    print("| M K I D E Z V G T H Y H W C H                                           |")
    print("| A F K R U I N V X H H F C A M                                           |")
    print("| C R V Z D M A R A I R O M E M                                           |")
    print("| A L I E I D Z F D V X G S G Q                                           |")
    print("| L J O T F V R U R H H N J Q G                                           |")
    print("| P C O O L E R A D I N E M Z S                                           |")
    print("| T A E H X Z B N H O E H N Z Y                                           |")
    print("| C R E G I S T R A D O R X Z P                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p5 = str(input("Qual a quinta palavra que você achou? "))
    while cont5 !=1:
        if p5==p1 or p5==p2 or p5==p3 or p5==p4:
            print("A palavra está repetida")
            p5 = str (input("Qual a quinta palavra que você achou? "))
        #Inserir palavras
        elif p5.upper() == "REGISTRADOR" or p5.upper()== "PLACAMAE" or p5.upper()== "PLACADEVIDEO" or p5.upper()== "MEMORIARAM" or p5.upper()== "HARDDRIVE" or p5.upper()== "GABINETE"or p5.upper()== "FONTE"or p5.upper()== "COOLER":
            print("A palavra achada foi ",p5)
            cont5 += 1
            pontuacao_rodada += len(p5)*p4x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p5.upper() != "REGISTRADOR" or p5.upper()!= "PLACAMAE" or p5.upper()!= "PLACADEVIDEO" or p5.upper()!= "MEMORIARAM" or p5.upper()!= "HARDDRIVE" or p5.upper()!= "GABINETE"or p5.upper()!= "FONTE"or p5.upper()!= "COOLER":
            print("O dado colocado está inválido")
            p5 = str(input("Qual a quinta palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| K V T U Y O T M X R K L K P E                                           |")
    print("| G V F K P W W F E K V D L T I                                           |")
    print("| J U M L R F T L R N A A E G O                                           |")
    print("| F C U W N F S I I I C N D H F                                           |")
    print("| N O D O X L P W A A I C Y H P                                           |")
    print("| E F N K K V X N D B B I D R F                                           |")
    print("| A V K T Z H Z E A L W V G C W                                           |")
    print("| M K I D E Z V G T H Y H W C H                                           |")
    print("| A F K R U I N V X H H F C A M                                           |")
    print("| C R V Z D M A R A I R O M E M                                           |")
    print("| A L I E I D Z F D V X G S G Q                                           |")
    print("| L J O T F V R U R H H N J Q G                                           |")
    print("| P C O O L E R A D I N E M Z S                                           |")
    print("| T A E H X Z B N H O E H N Z Y                                           |")
    print("| C R E G I S T R A D O R X Z P                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p6 = str(input("Qual a sexta palavra que você achou? "))
    while cont6 !=1:
        if p6==p1 or p6==p2 or p6==p3 or p6==p4 or p6==p5:
            print("A palavra está repetida")
            p6 = str (input("Qual a sexta palavra que você achou? "))
        #Inserir palavras
        elif p6.upper() == "REGISTRADOR" or p6.upper()== "PLACAMAE" or p6.upper()== "PLACADEVIDEO" or p6.upper()== "MEMORIARAM" or p6.upper()== "HARDDRIVE" or p6.upper()== "GABINETE"or p6.upper()== "FONTE"or p6.upper()== "COOLER":
            print("A palavra achada foi ",p6)
            cont6 += 1
            pontuacao_rodada += len(p6)*p3x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p6.upper() != "REGISTRADOR" or p6.upper()!= "PLACAMAE" or p6.upper()!= "PLACADEVIDEO" or p6.upper()!= "MEMORIARAM" or p6.upper()!= "HARDDRIVE" or p6.upper()!= "GABINETE"or p6.upper()!= "FONTE"or p6.upper()!= "COOLER":
            print("O dado colocado está inválido")
            p6 = str(input("Qual a sexta palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| K V T U Y O T M X R K L K P E                                           |")
    print("| G V F K P W W F E K V D L T I                                           |")
    print("| J U M L R F T L R N A A E G O                                           |")
    print("| F C U W N F S I I I C N D H F                                           |")
    print("| N O D O X L P W A A I C Y H P                                           |")
    print("| E F N K K V X N D B B I D R F                                           |")
    print("| A V K T Z H Z E A L W V G C W                                           |")
    print("| M K I D E Z V G T H Y H W C H                                           |")
    print("| A F K R U I N V X H H F C A M                                           |")
    print("| C R V Z D M A R A I R O M E M                                           |")
    print("| A L I E I D Z F D V X G S G Q                                           |")
    print("| L J O T F V R U R H H N J Q G                                           |")
    print("| P C O O L E R A D I N E M Z S                                           |")
    print("| T A E H X Z B N H O E H N Z Y                                           |")
    print("| C R E G I S T R A D O R X Z P                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p7 = str(input("Qual a sétima palavra que você achou? "))
    while cont7 !=1:
        if p7==p1 or p7==p2 or p7==p3 or p7==p4 or p7==p5 or p7==p6:
            print("A palavra está repetida")
            p7 = str (input("Qual a sétima palavra que você achou? "))
        #Inserir palavras
        elif p7.upper() == "REGISTRADOR" or p7.upper()== "PLACAMAE" or p7.upper()== "PLACADEVIDEO" or p7.upper()== "MEMORIARAM" or p7.upper()== "HARDDRIVE" or p7.upper()== "GABINETE"or p7.upper()== "FONTE"or p7.upper()== "COOLER":
            print("A palavra achada foi ",p7)
            cont7 += 1
            pontuacao_rodada += len(p7)*p2x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p7.upper() != "REGISTRADOR" or p7.upper()!= "PLACAMAE" or p7.upper()!= "PLACADEVIDEO" or p7.upper()!= "MEMORIARAM" or p7.upper()!= "HARDDRIVE" or p7.upper()!= "GABINETE"or p7.upper()!= "FONTE"or p7.upper()!= "COOLER":
            print("O dado colocado está inválido")
            p7 = str(input("Qual a sétima palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| K V T U Y O T M X R K L K P E                                           |")
    print("| G V F K P W W F E K V D L T I                                           |")
    print("| J U M L R F T L R N A A E G O                                           |")
    print("| F C U W N F S I I I C N D H F                                           |")
    print("| N O D O X L P W A A I C Y H P                                           |")
    print("| E F N K K V X N D B B I D R F                                           |")
    print("| A V K T Z H Z E A L W V G C W                                           |")
    print("| M K I D E Z V G T H Y H W C H                                           |")
    print("| A F K R U I N V X H H F C A M                                           |")
    print("| C R V Z D M A R A I R O M E M                                           |")
    print("| A L I E I D Z F D V X G S G Q                                           |")
    print("| L J O T F V R U R H H N J Q G                                           |")
    print("| P C O O L E R A D I N E M Z S                                           |")
    print("| T A E H X Z B N H O E H N Z Y                                           |")
    print("| C R E G I S T R A D O R X Z P                                           |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p8 = str(input("Qual a oitava palavra que você achou? "))
    while cont8 !=1:
        if p8==p1 or p8==p2 or p8==p3 or p8==p4 or p8==p5 or p8==p6 or p8==p7:
            print("A palavra está repetida")
            p8 = str (input("Qual a oitava palavra que você achou? "))
        #Inserir palavras
        elif p8.upper() == "REGISTRADOR" or p8.upper()== "PLACAMAE" or p8.upper()== "PLACADEVIDEO" or p8.upper()== "MEMORIARAM" or p8.upper()== "HARDDRIVE" or p8.upper()== "GABINETE"or p8.upper()== "FONTE"or p8.upper()== "COOLER":
            print("A palavra achada foi ",p8)
            cont8 += 1
            pontuacao_rodada += len(p8)*p1x
            pontuacao_total += pontuacao_rodada
            pontuacao_dificil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p8.upper() != "REGISTRADOR" or p8.upper()!= "PLACAMAE" or p8.upper()!= "PLACADEVIDEO" or p8.upper()!= "MEMORIARAM" or p8.upper()!= "HARDDRIVE" or p8.upper()!= "GABINETE"or p8.upper()!= "FONTE"or p8.upper()!= "COOLER":
            print("O dado colocado está inválido")
            p8 = str(input("Qual a oitava palavra que você achou? "))
    print("")
    print("A primeira palavra achada foi:",p1)
    print("A segunda palavra achada foi:",p2)
    print("A terceira palavra achada foi:",p3)
    print("A quarta palavra achada foi:",p4)
    print("A quinta palavra achada foi:",p5)
    print("A sexta palavra achada foi:",p6)
    print("A sétima palavra achada foi:",p7)
    print("A oitava palavra achada foi:",p8)
    print("")
    print("A sua pontuação nessa rodada foi: ",pontuacao_rodada)
    print("A sua pontuação total é:",pontuacao_total)
    print("")
    print("O quadro de respostas é:")
    print("")
    #quadro de respostas daqui
    print("+ + + + + + + + + + + + + P E ")
    print("+ + + + + + + + + + + + L T + ")
    print("+ + + + + + + + + + + A E + + ")
    print("F + + + + + + + + + C N + + + ")
    print("+ O + + + + + + + A I + + + + ")
    print("E + N + + + + + D B + + + + + ")
    print("A V + T + + + E A + + + + + + ")
    print("M + I + E + V G + + + + + + + ")
    print("A + + R + I + + + + + + + + + ")
    print("C + + + D M A R A I R O M E M ")
    print("A + + E + D + + + + + + + + + ")
    print("L + O + + + R + + + + + + + + ")
    print("P C O O L E R A + + + + + + + ")
    print("+ + + + + + + + H + + + + + + ")
    print("+ R E G I S T R A D O R + + + ")
    #até aqui

    if pontuacao_dificil >= 107140: #maximo
        print("PARABÉNS! Você fez a pontuação máxima de ",pontuacao_dificil," no modo díficil! Você é um MESTRE SUPREMO DO MODO DÍFICIL!")
    elif pontuacao_dificil <= 78790: #minimo
        print("A sua pontuação no modo médio foi a menor possível:",pontuacao_dificil," .Você é um fracasso no modo díficil") #Fracasso deve estar meio forte. Mudar depois.
    elif pontuacao_dificil >= 92965 and pontuacao_dificil < 107140: #entre metade e maximo
        print("A sua pontuação de ",pontuacao_dificil," está entre a metade e o máximo! Você é um veterano do modo díficil!")
    elif pontuacao_dificil > 78790 and pontuacao_dificil < 92965:
        print("A sua pontuação de ",pontuacao_dificil," está entre a metade e o mínimo. Você é um iniciante do modo díficil")
    print("")
    print("")
    print("")
    print("                             VOCÊ TERMINOU O JOGO!! VOCÊ SERÁ REDIRECIONADO PARA O MENU",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("")
    print("")
    print("")


    return menu()


###################################################################################################################################################################3


################################################################################### N2 ############################################################################


def n2():
    #AGORA COMEÇA O CAÇA PALAVRAS DE NIVEL MÉDIO 10X10
    ##################################################
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    #Dois novos contadores para o nivel médio e suas 2 palavras adcionais
    cont5 = 0
    cont6 = 0
    pontuacao_rodada = 0
    pontuacao_total = 0
    pontuacao_facil = 0
    pontuacao_medio = 0
    pontuacao_dificil = 0
    #multiplicadores para os caça palavras
    p4x = 40
    p3x = 30
    p2x = 20
    p1x = 10
    #Essas variaveis vão ser os multiplicadores adcionais para os caça palavras 10x10
    p6x = 60
    p5x = 50
    #Essas variaveis vão ser os multiplicadores adcionais para os caça palavras 15x15
    p8x = 80
    p7x = 70
    print("")
    print("")
    print("")
    print("                             LOADING",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("")
    print("")
    print("")
    print("                             NÍVEL MÉDIO")
    print("---------------------------------------------------------------------------")
    print("| Pré história - FASE 6                                                   |")
    print("|                                                                         |")
    print("|                                                                         |")
    #SEXTA FASE6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    print("|                                                                         |")
    #Colocar o caça daqui
    print("| F H K J J U U X D A                                                     |")
    print("| U O B G R T W G I N                                                     |")
    print("| V D G J V A T G D E                                                     |")
    print("| W E W O E V R X V O                                                     |")
    print("| F K T Z Z U O Y Q L                                                     |")
    print("| J M I N L C K I F I                                                     |")
    print("| N O M A D I S M O T                                                     |")
    print("| E Z T N C I N G I I                                                     |")
    print("| U E A C I M A R E C                                                     |")
    print("| M R U P E S T R E O                                                     |")
    #Até aqui
    '''metalurgia,neolitico,nomadismo, ceramica, rupestre, fogo'''
    print("|                                                                         |")
    print("| Existem 6 palavras nesse caça palavras (escreva sem espaço e acentos)   |")
    print("---------------------------------------------------------------------------")
    print("")
    print("Dicas:")
    print("   1-É a ciência que estuda e gerencia os metais desde sua extração do subsolo até sua transformação em produtos adequados ao uso")
    print("   2-É o período histórico que vai aproximadamente do décimo milênio a.C., com o início da sedentarização e surgimento da agricultura, ao terceiro milênio a.C., dando lugar à Idade dos Metais.")
    print("   3-É a prática dos povos nômades, ou seja, que não têm uma habitação fixa, que vivem permanentemente mudando de lugar.")
    print("   4-É a arte ou a técnica de produção de artefatos de objetos tendo a argila como matéria-prima.")
    print("   5-É o termo que denomina as representações artísticas pré-históricas realizadas em paredes, tetos e outras superfícies de cavernas e abrigos rochosos, ou mesmo sobre superfícies rochosas ao ar livre.")
    print("   6-É a rápida oxidação de um material combustível liberando calor, luz e produtos de reação, tais como o dióxido de carbono e a água. Muito utilizado para espantar insetos e animais e cozinhar alimentos.")
    print("")
    #COLOCAR AS PALAVRAS
    p1= str(input("Qual a primeira palavra que você achou? "))
    while cont1 != 1:
        #Inserir palavras
        if p1.upper() == "CERAMICA" or p1.upper()== "FOGO" or p1.upper()== "METALURGIA" or p1.upper()== "NEOLITICO" or p1.upper()== "NOMADISMO" or p1.upper()== "RUPESTRE":
            print("A palavra achada foi ",p1)
            cont1 += 1
            pontuacao_rodada += len(p1)*p6x
            pontuacao_total += pontuacao_rodada
            pontuacao_medio += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p1.upper() != "CERAMICA" or p1.upper()!= "FOGO" or p1.upper()!= "METALURGIA" or p1.upper()!= "NEOLITICO" or p1.upper()!= "NOMADISMO" or p1.upper()!= "RUPESTRE":
            print("O dado colocado está inválido")
            p1= str(input("Qual a primeira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| F H K J J U U X D A                                                     |")
    print("| U O B G R T W G I N                                                     |")
    print("| V D G J V A T G D E                                                     |")
    print("| W E W O E V R X V O                                                     |")
    print("| F K T Z Z U O Y Q L                                                     |")
    print("| J M I N L C K I F I                                                     |")
    print("| N O M A D I S M O T                                                     |")
    print("| E Z T N C I N G I I                                                     |")
    print("| U E A C I M A R E C                                                     |")
    print("| M R U P E S T R E O                                                     |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p2 = str(input("Qual a segunda palavra que você achou? "))
    while cont2 != 1:
        if p2.upper() == p1.upper():
            print("A palavra está repetida")
            p2 = str(input("Qual a segunda palavra que você achou? "))
        #Inserir palavras
        elif p2.upper() == "CERAMICA" or p2.upper()== "FOGO" or p2.upper()== "METALURGIA" or p2.upper()== "NEOLITICO" or p2.upper()== "NOMADISMO" or p2.upper()== "RUPESTRE":
            print("A palavra achada foi ",p2)
            cont2 += 1
            pontuacao_rodada += len(p2)*p5x
            pontuacao_total += pontuacao_rodada
            pontuacao_medio += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p2.upper() != "CERAMICA" or p2.upper()!= "FOGO" or p2.upper()!= "METALURGIA" or p2.upper()!= "NEOLITICO" or p2.upper()!= "NOMADISMO" or p2.upper()!= "RUPESTRE":
            print("O dado colocado está inválido")
            p2= str(input("Qual a segunda palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| F H K J J U U X D A                                                     |")
    print("| U O B G R T W G I N                                                     |")
    print("| V D G J V A T G D E                                                     |")
    print("| W E W O E V R X V O                                                     |")
    print("| F K T Z Z U O Y Q L                                                     |")
    print("| J M I N L C K I F I                                                     |")
    print("| N O M A D I S M O T                                                     |")
    print("| E Z T N C I N G I I                                                     |")
    print("| U E A C I M A R E C                                                     |")
    print("| M R U P E S T R E O                                                     |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p3 = str(input("Qual a terceira palavra que você achou? "))
    while cont3 != 1:
        if p3.upper()==p1.upper() or p3.upper()==p2.upper():
            print("A palavra está repetida")
            p3 = str(input("Qual a terceira palavra que você achou? "))
        #Inserir palavras
        elif p3.upper() == "CERAMICA" or p3.upper()== "FOGO" or p3.upper()== "METALURGIA" or p3.upper()== "NEOLITICO" or p3.upper()== "NOMADISMO" or p3.upper()== "RUPESTRE":
            print("A palavra achada foi ",p3)
            cont3 += 1
            pontuacao_rodada += len(p3)*p4x
            pontuacao_total += pontuacao_rodada
            pontuacao_medio += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p3.upper() != "CERAMICA" or p3.upper()!= "FOGO" or p3.upper()!= "METALURGIA" or p3.upper()!= "NEOLITICO" or p3.upper()!= "NOMADISMO" or p3.upper()!= "RUPESTRE":
            print("O dado colocado está inválido")
            p3= str(input("Qual a terceira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| F H K J J U U X D A                                                     |")
    print("| U O B G R T W G I N                                                     |")
    print("| V D G J V A T G D E                                                     |")
    print("| W E W O E V R X V O                                                     |")
    print("| F K T Z Z U O Y Q L                                                     |")
    print("| J M I N L C K I F I                                                     |")
    print("| N O M A D I S M O T                                                     |")
    print("| E Z T N C I N G I I                                                     |")
    print("| U E A C I M A R E C                                                     |")
    print("| M R U P E S T R E O                                                     |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p4 = str(input("Qual a quarta palavra que você achou? "))
    while cont4 != 1:
        if p4==p1 or p4==p2 or p4==p3:
            print("A palavra está repetida")
            p4 = str (input("Qual a quarta palavra que você achou? "))
        #Inserir palavras
        elif p4.upper() == "CERAMICA" or p4.upper()== "FOGO" or p4.upper()== "METALURGIA" or p4.upper()== "NEOLITICO" or p4.upper()== "NOMADISMO" or p4.upper()== "RUPESTRE":
            print("A palavra achada foi ",p4)
            cont4 += 1
            pontuacao_rodada += len(p4)*p3x
            pontuacao_total += pontuacao_rodada
            pontuacao_medio += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p4.upper() != "CERAMICA" or p4.upper()!= "FOGO" or p4.upper()!= "METALURGIA" or p4.upper()!= "NEOLITICO" or p4.upper()!= "NOMADISMO" or p4.upper()!= "RUPESTRE":
            print("O dado colocado está inválido")
            p4 = str(input("Qual a quarta palavra que você achou? "))
    print("")
    print("---------------------------------------------------------------------------")
    print("| F H K J J U U X D A                                                     |")
    print("| U O B G R T W G I N                                                     |")
    print("| V D G J V A T G D E                                                     |")
    print("| W E W O E V R X V O                                                     |")
    print("| F K T Z Z U O Y Q L                                                     |")
    print("| J M I N L C K I F I                                                     |")
    print("| N O M A D I S M O T                                                     |")
    print("| E Z T N C I N G I I                                                     |")
    print("| U E A C I M A R E C                                                     |")
    print("| M R U P E S T R E O                                                     |")
    print("---------------------------------------------------------------------------")
    print("")
    p5 = str(input("Qual a quinta palavra que você achou? "))
    while cont5 !=1:
        if p5==p1 or p5==p2 or p5==p3 or p5==p4:
            print("A palavra está repetida")
            p5 = str (input("Qual a quinta palavra que você achou? "))
        elif p5.upper() == "CERAMICA" or p5.upper()== "FOGO" or p5.upper()== "METALURGIA" or p5.upper()== "NEOLITICO" or p5.upper()== "NOMADISMO" or p5.upper()== "RUPESTRE":
            print("A palavra achada foi ",p5)
            cont5 += 1
            pontuacao_rodada += len(p5)*p2x
            pontuacao_total += pontuacao_rodada
            pontuacao_medio += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        elif p5.upper() != "CERAMICA" or p5.upper()!= "FOGO" or p5.upper()!= "METALURGIA" or p5.upper()!= "NEOLITICO" or p5.upper()!= "NOMADISMO" or p5.upper()!= "RUPESTRE":
            print("O dado colocado está inválido")
            p5 = str(input("Qual a quinta palavra que você achou? "))
    print("")
    print("---------------------------------------------------------------------------")
    print("| F H K J J U U X D A                                                     |")
    print("| U O B G R T W G I N                                                     |")
    print("| V D G J V A T G D E                                                     |")
    print("| W E W O E V R X V O                                                     |")
    print("| F K T Z Z U O Y Q L                                                     |")
    print("| J M I N L C K I F I                                                     |")
    print("| N O M A D I S M O T                                                     |")
    print("| E Z T N C I N G I I                                                     |")
    print("| U E A C I M A R E C                                                     |")
    print("| M R U P E S T R E O                                                     |")
    print("---------------------------------------------------------------------------")
    print("")
    p6 = str(input("Qual a sexta palavra que você achou? "))
    while cont6 !=1:
        if p6==p1 or p6==p2 or p6==p3 or p6==p4 or p6==p5:
            print("A palavra está repetida")
            p6 = str (input("Qual a sexta palavra que você achou? "))
        elif p6.upper() == "CERAMICA" or p6.upper()== "FOGO" or p6.upper()== "METALURGIA" or p6.upper()== "NEOLITICO" or p6.upper()== "NOMADISMO" or p6.upper()== "RUPESTRE":
            print("A palavra achada foi ",p6)
            cont6 += 1
            pontuacao_rodada += len(p6)*p1x
            pontuacao_total += pontuacao_rodada
            pontuacao_medio += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        elif p6.upper() != "CERAMICA" or p6.upper()!= "FOGO" or p6.upper()!= "METALURGIA" or p6.upper()!= "NEOLITICO" or p6.upper()!= "NOMADISMO" or p6.upper()!= "RUPESTRE":
            print("O dado colocado está inválido")
            p6 = str(input("Qual a sexta palavra que você achou? "))


    print("")
    print("A primeira palavra achada foi:",p1)
    print("A segunda palavra achada foi:",p2)
    print("A terceira palavra achada foi:",p3)
    print("A quarta palavra achada foi:",p4)
    print("A quinta palavra achada foi:",p5)
    print("A sexta palavra achada foi:",p6)
    print("")
    print("A sua pontuação nessa rodada foi: ",pontuacao_rodada)
    print("A sua pontuação total é:",pontuacao_total)
    print("")
    print("O quadro de respostas é:")
    #quadro de respostas daqui
    print("F + + + + + + + + A ")
    print("+ O + + + + + + I N ")
    print("+ + G + + + + G + E ")
    print("+ + + O + + R + + O ")
    print("+ + + + + U + + + L ")
    print("+ + + + L + + + + I ")
    print("N O M A D I S M O T ")
    print("+ + T + + + + + + I ")
    print("+ E A C I M A R E C ")
    print("M R U P E S T R E O ")
    #até aqui
    ##################################################
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    cont5 = 0
    cont6 = 0
    pontuacao_rodada = 0
    print("")
    print("")
    print("")
    print("                             LOADING",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("")
    print("")
    print("")
    print("---------------------------------------------------------------------------")
    print("| Revolução Russa - FASE 7                                                |")
    print("|                                                                         |")
    #SETIMA FASE77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    #Colocar o caça daqui
    print("| S S Z S A M S R N O                                                     |")
    print("| H O S B Z Y T S I T                                                     |")
    print("| F R V I S E A S T R                                                     |")
    print("| U O F I F C L X U O                                                     |")
    print("| O C B Q E X I W P T                                                     |")
    print("| P T Y A S T N D S S                                                     |")
    print("| S Y K Z Q B E S A K                                                     |")
    print("| G Q L E N I N S R I                                                     |")
    print("| Z D L W A G W I Q R                                                     |")
    print("| W X T C H Q T U N H                                                     |")
    '''rasputin, sovietes, trotski, stalin, lenin, urss'''
    #Até aqui
    print("|                                                                         |")
    print("| Existem 6 palavras nesse caça palavras (escreva sem espaço e acentos)   |")
    print("---------------------------------------------------------------------------")
    print("")
    print("Dicas:")
    print("   1-Foi um místico russo, e auto proclamado homem santo que se aproximou da família do czar Nicolau II e se tornou uma figura politicamente influente no final do período czarista. A influência dele teria provocado o distanciamento dos monarcas de seu povo.")
    print("   2-São colegiados, ou corpos deliberativos, constituídos de operários ou membros da classe trabalhadora que regulam e organizam a produção material de um determinado território, ou mesmo indústria. Este termo é comumente usado para descrever trabalhadores governando a si mesmos, sem patrões, em regime de autogestão.")
    print("   3-Foi um intelectual marxista e revolucionário bolchevique, organizador do Exército Vermelho e, após a morte de Lenin, rival de Stalin na disputa pela hegemonia do Partido Comunista da União Soviética (PCUS).")
    print("   4-Sucessor de Lenin depois de sua morte. Considerado um dos ditadores mais cruéis que já existiram.")
    print("   5-Foi o maior líder da Revolução Russa, além de revolucionário exemplar.")
    print("   6-Foi um Estado socialista localizado na Eurásia que existiu entre 1922 e 1991. Uma união de várias repúblicas soviéticas subnacionais.")
    print("")
    #COLOCAR AS PALAVRAS
    p1= str(input("Qual a primeira palavra que você achou? "))
    while cont1 != 1:
        #Inserir palavras
        if p1.upper() == "LENIN" or p1.upper()== "RASPUTIN" or p1.upper()== "SOVIETES" or p1.upper()== "STALIN" or p1.upper()== "TROTSKI" or p1.upper()== "URSS":
            print("A palavra achada foi ",p1)
            cont1 += 1
            pontuacao_rodada += len(p1)*p6x
            pontuacao_total += pontuacao_rodada
            pontuacao_medio += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p1.upper() != "LENIN" or p1.upper()!= "RASPUTIN" or p1.upper()!= "SOVIETES" or p1.upper()!= "STALIN" or p1.upper()!= "TROTSKI" or p1.upper()!= "URSS":
            print("O dado colocado está inválido")
            p1= str(input("Qual a primeira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| S S Z S A M S R N O                                                     |")
    print("| H O S B Z Y T S I T                                                     |")
    print("| F R V I S E A S T R                                                     |")
    print("| U O F I F C L X U O                                                     |")
    print("| O C B Q E X I W P T                                                     |")
    print("| P T Y A S T N D S S                                                     |")
    print("| S Y K Z Q B E S A K                                                     |")
    print("| G Q L E N I N S R I                                                     |")
    print("| Z D L W A G W I Q R                                                     |")
    print("| W X T C H Q T U N H                                                     |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p2 = str(input("Qual a segunda palavra que você achou? "))
    while cont2 != 1:
        if p2.upper() == p1.upper():
            print("A palavra está repetida")
            p2 = str(input("Qual a segunda palavra que você achou? "))
        #Inserir palavras
        elif p2.upper() == "LENIN" or p2.upper()== "RASPUTIN" or p2.upper()== "SOVIETES" or p2.upper()== "STALIN" or p2.upper()== "TROTSKI" or p2.upper()== "URSS":
            print("A palavra achada foi ",p2)
            cont2 += 1
            pontuacao_rodada += len(p2)*p5x
            pontuacao_total += pontuacao_rodada
            pontuacao_medio += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p2.upper() != "LENIN" or p2.upper()!= "RASPUTIN" or p2.upper()!= "SOVIETES" or p2.upper()!= "STALIN" or p2.upper()!= "TROTSKI" or p2.upper()!= "URSS":
            print("O dado colocado está inválido")
            p2= str(input("Qual a segunda palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| S S Z S A M S R N O                                                     |")
    print("| H O S B Z Y T S I T                                                     |")
    print("| F R V I S E A S T R                                                     |")
    print("| U O F I F C L X U O                                                     |")
    print("| O C B Q E X I W P T                                                     |")
    print("| P T Y A S T N D S S                                                     |")
    print("| S Y K Z Q B E S A K                                                     |")
    print("| G Q L E N I N S R I                                                     |")
    print("| Z D L W A G W I Q R                                                     |")
    print("| W X T C H Q T U N H                                                     |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p3 = str(input("Qual a terceira palavra que você achou? "))
    while cont3 != 1:
        if p3.upper()==p1.upper() or p3.upper()==p2.upper():
            print("A palavra está repetida")
            p3 = str(input("Qual a terceira palavra que você achou? "))
        #Inserir palavras
        elif p3.upper() == "LENIN" or p3.upper()== "RASPUTIN" or p3.upper()== "SOVIETES" or p3.upper()== "STALIN" or p3.upper()== "TROTSKI" or p3.upper()== "URSS":
            print("A palavra achada foi ",p3)
            cont3 += 1
            pontuacao_rodada += len(p3)*p4x
            pontuacao_total += pontuacao_rodada
            pontuacao_medio += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p3.upper() != "LENIN" or p3.upper()!= "RASPUTIN" or p3.upper()!= "SOVIETES" or p3.upper()!= "STALIN" or p3.upper()!= "TROTSKI" or p3.upper()!= "URSS":
            print("O dado colocado está inválido")
            p3= str(input("Qual a terceira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| S S Z S A M S R N O                                                     |")
    print("| H O S B Z Y T S I T                                                     |")
    print("| F R V I S E A S T R                                                     |")
    print("| U O F I F C L X U O                                                     |")
    print("| O C B Q E X I W P T                                                     |")
    print("| P T Y A S T N D S S                                                     |")
    print("| S Y K Z Q B E S A K                                                     |")
    print("| G Q L E N I N S R I                                                     |")
    print("| Z D L W A G W I Q R                                                     |")
    print("| W X T C H Q T U N H                                                     |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p4 = str(input("Qual a quarta palavra que você achou? "))
    while cont4 != 1:
        if p4==p1 or p4==p2 or p4==p3:
            print("A palavra está repetida")
            p4 = str (input("Qual a quarta palavra que você achou? "))
        #Inserir palavras
        elif p4.upper() == "LENIN" or p4.upper()== "RASPUTIN" or p4.upper()== "SOVIETES" or p4.upper()== "STALIN" or p4.upper()== "TROTSKI" or p4.upper()== "URSS":
            print("A palavra achada foi ",p4)
            cont4 += 1
            pontuacao_rodada += len(p4)*p3x
            pontuacao_total += pontuacao_rodada
            pontuacao_medio += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p4.upper() != "LENIN" or p4.upper()!= "RASPUTIN" or p4.upper()!= "SOVIETES" or p4.upper()!= "STALIN" or p4.upper()!= "TROTSKI" or p4.upper()!= "URSS":
            print("O dado colocado está inválido")
            p4 = str(input("Qual a quarta palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| S S Z S A M S R N O                                                     |")
    print("| H O S B Z Y T S I T                                                     |")
    print("| F R V I S E A S T R                                                     |")
    print("| U O F I F C L X U O                                                     |")
    print("| O C B Q E X I W P T                                                     |")
    print("| P T Y A S T N D S S                                                     |")
    print("| S Y K Z Q B E S A K                                                     |")
    print("| G Q L E N I N S R I                                                     |")
    print("| Z D L W A G W I Q R                                                     |")
    print("| W X T C H Q T U N H                                                     |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p5 = str(input("Qual a quinta palavra que você achou? "))
    while cont5 !=1:
        if p5==p1 or p5==p2 or p5==p3 or p5==p4:
            print("A palavra está repetida")
            p5 = str (input("Qual a quinta palavra que você achou? "))
        elif p5.upper() == "LENIN" or p5.upper()== "RASPUTIN" or p5.upper()== "SOVIETES" or p5.upper()== "STALIN" or p5.upper()== "TROTSKI" or p5.upper()== "URSS":
            print("A palavra achada foi ",p5)
            cont5 += 1
            pontuacao_rodada += len(p5)*p2x
            pontuacao_total += pontuacao_rodada
            pontuacao_medio += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        elif p5.upper() != "LENIN" or p5.upper()!= "RASPUTIN" or p5.upper()!= "SOVIETES" or p5.upper()!= "STALIN" or p5.upper()!= "TROTSKI" or p5.upper()!= "URSS":
            print("O dado colocado está inválido")
            p5 = str(input("Qual a quinta palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| S S Z S A M S R N O                                                     |")
    print("| H O S B Z Y T S I T                                                     |")
    print("| F R V I S E A S T R                                                     |")
    print("| U O F I F C L X U O                                                     |")
    print("| O C B Q E X I W P T                                                     |")
    print("| P T Y A S T N D S S                                                     |")
    print("| S Y K Z Q B E S A K                                                     |")
    print("| G Q L E N I N S R I                                                     |")
    print("| Z D L W A G W I Q R                                                     |")
    print("| W X T C H Q T U N H                                                     |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p6 = str(input("Qual a sexta palavra que você achou? "))
    while cont6 !=1:
        if p6==p1 or p6==p2 or p6==p3 or p6==p4 or p6==p5:
            print("A palavra está repetida")
            p6 = str (input("Qual a sexta palavra que você achou? "))
        elif p6.upper() == "LENIN" or p6.upper()== "RASPUTIN" or p6.upper()== "SOVIETES" or p6.upper()== "STALIN" or p6.upper()== "TROTSKI" or p6.upper()== "URSS":
            print("A palavra achada foi ",p6)
            cont6 += 1
            pontuacao_rodada += len(p6)*p1x
            pontuacao_total += pontuacao_rodada
            pontuacao_medio += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        elif p6.upper() != "LENIN" or p6.upper()!= "RASPUTIN" or p6.upper()!= "SOVIETES" or p6.upper()!= "STALIN" or p6.upper()!= "TROTSKI" or p6.upper()!= "URSS":
            print("O dado colocado está inválido")
            p6 = str(input("Qual a sexta palavra que você achou? "))


    print("")
    print("A primeira palavra achada foi:",p1)
    print("A segunda palavra achada foi:",p2)
    print("A terceira palavra achada foi:",p3)
    print("A quarta palavra achada foi:",p4)
    print("A quinta palavra achada foi:",p5)
    print("A sexta palavra achada foi:",p6)
    print("")
    print("A sua pontuação nessa rodada foi: ",pontuacao_rodada)
    print("A sua pontuação total é:",pontuacao_total)
    print("")
    print("O quadro de respostas é:")
    print("")
    #quadro de respostas daqui
    print("S + + S + + S + N + ")
    print("+ O S + + + T + I T ")
    print("+ R V + + + A + T R ")
    print("U + + I + + L + U O ")
    print("+ + + + E + I + P T ")
    print("+ + + + + T N + S S ")
    print("+ + + + + + E + A K ")
    print("+ + L E N I N S R I ")
    print("+ + + + + + + + + + ")
    print("+ + + + + + + + + + ")
    #até aqui
    ##################################################
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    cont5 = 0
    cont6 = 0
    pontuacao_rodada = 0
    print("")
    print("")
    print("")
    print("                             LOADING",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("")
    print("")
    print("")
    print("---------------------------------------------------------------------------")
    print("| Países - FASE 8                                                         |")
    print("|                                                                         |")
    #OITAVA FASE888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
    print("|                                                                         |")
    #Colocar o caça daqui
    print("| A U W D H E R Y N C                                                     |")
    print("| F G X O N T A I F T                                                     |")
    print("| L Z E I E R C R M D                                                     |")
    print("| I R U U N A P E R U                                                     |")
    print("| S G S K R B Z O G Q                                                     |")
    print("| A A J A K O W O I A                                                     |")
    print("| R U G T C Z N H H O                                                     |")
    print("| B U A I D N A L S I                                                     |")
    print("| A L M E Y P L K D P                                                     |")
    print("| E J E X U Z I W Z M                                                     |")
    #Até aqui
    '''nicaragua,islandia,noruega,brasil, guine, peru'''
    print("|                                                                         |")
    print("| Existem 6 palavras nesse caça palavras (escreva sem espaço e acentos)   |")
    print("---------------------------------------------------------------------------")
    print("")
    print("Dicas:")
    print("   1-Antiga colônia Espanhola na América Central. Sua capital é Manágua")
    print("   2-É um pais da Europa. É considerado o país com a menor população, que se classificou para uma Copa do Mundo.")
    print("   3-É um pais da Europa. Foi classificado como o país mais desenvolvido do mundo em todos os relatórios de desenvolvimento humano desde 2001.")
    print("   4-É o maior país da América do Sul e da região da América Latina.")
    print("   5-É um pais da África. Foi uma colônia da França e sua capital é Conacri.")
    print("   6-Antiga colônia Espanhola na América Central. Machu Picchu fica em meu território.")
    print("")
    #COLOCAR AS PALAVRAS
    p1= str(input("Qual a primeira palavra que você achou? "))
    while cont1 != 1:
        #Inserir palavras
        if p1.upper() == "BRASIL" or p1.upper()== "GUINE" or p1.upper()== "ISLANDIA" or p1.upper()== "NICARAGUA" or p1.upper()== "NORUEGA" or p1.upper()== "PERU":
            print("A palavra achada foi ",p1)
            cont1 += 1
            pontuacao_rodada += len(p1)*p6x
            pontuacao_total += pontuacao_rodada
            pontuacao_medio += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p1.upper() != "BRASIL" or p1.upper()!= "GUINE" or p1.upper()!= "ISLANDIA" or p1.upper()!= "NICARAGUA" or p1.upper()!= "NORUEGA" or p1.upper()!= "PERU":
            print("O dado colocado está inválido")
            p1= str(input("Qual a primeira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| A U W D H E R Y N C                                                     |")
    print("| F G X O N T A I F T                                                     |")
    print("| L Z E I E R C R M D                                                     |")
    print("| I R U U N A P E R U                                                     |")
    print("| S G S K R B Z O G Q                                                     |")
    print("| A A J A K O W O I A                                                     |")
    print("| R U G T C Z N H H O                                                     |")
    print("| B U A I D N A L S I                                                     |")
    print("| A L M E Y P L K D P                                                     |")
    print("| E J E X U Z I W Z M                                                     |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p2 = str(input("Qual a segunda palavra que você achou? "))
    while cont2 != 1:
        if p2.upper() == p1.upper():
            print("A palavra está repetida")
            p2 = str(input("Qual a segunda palavra que você achou? "))
        #Inserir palavras
        elif p2.upper() == "BRASIL" or p2.upper()== "GUINE" or p2.upper()== "ISLANDIA" or p2.upper()== "NICARAGUA" or p2.upper()== "NORUEGA" or p2.upper()== "PERU":
            print("A palavra achada foi ",p2)
            cont2 += 1
            pontuacao_rodada += len(p2)*p5x
            pontuacao_total += pontuacao_rodada
            pontuacao_medio += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p2.upper() != "BRASIL" or p2.upper()!= "GUINE" or p2.upper()!= "ISLANDIA" or p2.upper()!= "NICARAGUA" or p2.upper()!= "NORUEGA" or p2.upper()!= "PERU":
            print("O dado colocado está inválido")
            p2= str(input("Qual a segunda palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| A U W D H E R Y N C                                                     |")
    print("| F G X O N T A I F T                                                     |")
    print("| L Z E I E R C R M D                                                     |")
    print("| I R U U N A P E R U                                                     |")
    print("| S G S K R B Z O G Q                                                     |")
    print("| A A J A K O W O I A                                                     |")
    print("| R U G T C Z N H H O                                                     |")
    print("| B U A I D N A L S I                                                     |")
    print("| A L M E Y P L K D P                                                     |")
    print("| E J E X U Z I W Z M                                                     |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p3 = str(input("Qual a terceira palavra que você achou? "))
    while cont3 != 1:
        if p3.upper()==p1.upper() or p3.upper()==p2.upper():
            print("A palavra está repetida")
            p3 = str(input("Qual a terceira palavra que você achou? "))
        #Inserir palavras
        elif p3.upper() == "BRASIL" or p3.upper()== "GUINE" or p3.upper()== "ISLANDIA" or p3.upper()== "NICARAGUA" or p3.upper()== "NORUEGA" or p3.upper()== "PERU":
            print("A palavra achada foi ",p3)
            cont3 += 1
            pontuacao_rodada += len(p3)*p4x
            pontuacao_total += pontuacao_rodada
            pontuacao_medio += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p3.upper() != "BRASIL" or p3.upper()!= "GUINE" or p3.upper()!= "ISLANDIA" or p3.upper()!= "NICARAGUA" or p3.upper()!= "NORUEGA" or p3.upper()!= "PERU":
            print("O dado colocado está inválido")
            p3= str(input("Qual a terceira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| A U W D H E R Y N C                                                     |")
    print("| F G X O N T A I F T                                                     |")
    print("| L Z E I E R C R M D                                                     |")
    print("| I R U U N A P E R U                                                     |")
    print("| S G S K R B Z O G Q                                                     |")
    print("| A A J A K O W O I A                                                     |")
    print("| R U G T C Z N H H O                                                     |")
    print("| B U A I D N A L S I                                                     |")
    print("| A L M E Y P L K D P                                                     |")
    print("| E J E X U Z I W Z M                                                     |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p4 = str(input("Qual a quarta palavra que você achou? "))
    while cont4 != 1:
        if p4==p1 or p4==p2 or p4==p3:
            print("A palavra está repetida")
            p4 = str (input("Qual a quarta palavra que você achou? "))
        #Inserir palavras
        elif p4.upper() == "BRASIL" or p4.upper()== "GUINE" or p4.upper()== "ISLANDIA" or p4.upper()== "NICARAGUA" or p4.upper()== "NORUEGA" or p4.upper()== "PERU":
            print("A palavra achada foi ",p4)
            cont4 += 1
            pontuacao_rodada += len(p4)*p3x
            pontuacao_total += pontuacao_rodada
            pontuacao_medio += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p4.upper() != "BRASIL" or p4.upper()!= "GUINE" or p4.upper()!= "ISLANDIA" or p4.upper()!= "NICARAGUA" or p4.upper()!= "NORUEGA" or p4.upper()!= "PERU":
            print("O dado colocado está inválido")
            p4 = str(input("Qual a quarta palavra que você achou? "))

    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| A U W D H E R Y N C                                                     |")
    print("| F G X O N T A I F T                                                     |")
    print("| L Z E I E R C R M D                                                     |")
    print("| I R U U N A P E R U                                                     |")
    print("| S G S K R B Z O G Q                                                     |")
    print("| A A J A K O W O I A                                                     |")
    print("| R U G T C Z N H H O                                                     |")
    print("| B U A I D N A L S I                                                     |")
    print("| A L M E Y P L K D P                                                     |")
    print("| E J E X U Z I W Z M                                                     |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p5 = str(input("Qual a quinta palavra que você achou? "))
    while cont5 !=1:
        if p5==p1 or p5==p2 or p5==p3 or p5==p4:
            print("A palavra está repetida")
            p5 = str (input("Qual a quinta palavra que você achou? "))
        elif p5.upper() == "BRASIL" or p5.upper()== "GUINE" or p5.upper()== "ISLANDIA" or p5.upper()== "NICARAGUA" or p5.upper()== "NORUEGA" or p5.upper()== "PERU":
            print("A palavra achada foi ",p5)
            cont5 += 1
            pontuacao_rodada += len(p5)*p2x
            pontuacao_total += pontuacao_rodada
            pontuacao_medio += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        elif p5.upper() != "BRASIL" or p5.upper()!= "GUINE" or p5.upper()!= "ISLANDIA" or p5.upper()!= "NICARAGUA" or p5.upper()!= "NORUEGA" or p5.upper()!= "PERU":
            print("O dado colocado está inválido")
            p5 = str(input("Qual a quinta palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| A U W D H E R Y N C                                                     |")
    print("| F G X O N T A I F T                                                     |")
    print("| L Z E I E R C R M D                                                     |")
    print("| I R U U N A P E R U                                                     |")
    print("| S G S K R B Z O G Q                                                     |")
    print("| A A J A K O W O I A                                                     |")
    print("| R U G T C Z N H H O                                                     |")
    print("| B U A I D N A L S I                                                     |")
    print("| A L M E Y P L K D P                                                     |")
    print("| E J E X U Z I W Z M                                                     |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p6 = str(input("Qual a sexta palavra que você achou? "))
    while cont6 !=1:
        if p6==p1 or p6==p2 or p6==p3 or p6==p4 or p6==p5:
            print("A palavra está repetida")
            p6 = str (input("Qual a sexta palavra que você achou? "))
        elif p6.upper() == "BRASIL" or p6.upper()== "GUINE" or p6.upper()== "ISLANDIA" or p6.upper()== "NICARAGUA" or p6.upper()== "NORUEGA" or p6.upper()== "PERU":
            print("A palavra achada foi ",p6)
            cont6 += 1
            pontuacao_rodada += len(p6)*p1x
            pontuacao_total += pontuacao_rodada
            pontuacao_medio += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        elif p6.upper() != "BRASIL" or p6.upper()!= "GUINE" or p6.upper()!= "ISLANDIA" or p6.upper()!= "NICARAGUA" or p6.upper()!= "NORUEGA" or p6.upper()!= "PERU":
            print("O dado colocado está inválido")
            p6 = str(input("Qual a sexta palavra que você achou? "))


    print("")
    print("A primeira palavra achada foi:",p1)
    print("A segunda palavra achada foi:",p2)
    print("A terceira palavra achada foi:",p3)
    print("A quarta palavra achada foi:",p4)
    print("A quinta palavra achada foi:",p5)
    print("A sexta palavra achada foi:",p6)
    print("")
    print("A sua pontuação nessa rodada foi: ",pontuacao_rodada)
    print("A sua pontuação total é:",pontuacao_total)
    print("")
    print("O quadro de respostas é:")
    print("")
    #quadro de respostas daqui
    print("A + + + + E + + N + ")
    print("+ G + + N + + I + + ")
    print("L + E I + + C + + + ")
    print("I + U U + A P E R U ")
    print("S G + + R + + + + + ")
    print("A + + A + O + + + + ")
    print("R + G + + + N + + + ")
    print("B U A I D N A L S I ")
    print("A + + + + + + + + + ")
    print("+ + + + + + + + + + ")
    #até aqui
    ##################################################
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    cont5 = 0
    cont6 = 0
    pontuacao_rodada = 0
    print("")
    print("")
    print("")
    print("                             LOADING",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("")
    print("")
    print("")
    print("---------------------------------------------------------------------------")
    print("| Doenças - FASE 9                                                        |")
    print("|                                                                         |")
    #NONA FASE999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    print("|                                                                         |")
    #Colocar o caça daqui
    print("| D N S U M C I V A G                                                     |")
    print("| K I E D A E P I R G                                                     |")
    print("| V C A N I T S U T S                                                     |")
    print("| O Q C B D A G I R G                                                     |")
    print("| T E K F E Z S D O E                                                     |")
    print("| R Q I A T T M E S L                                                     |")
    print("| U X T J K D E A E D                                                     |")
    print("| P E K T O D C S C R                                                     |")
    print("| P N E U M O N I A V                                                     |")
    print("| I Q L K G L Z K R B                                                     |")
    #Até aqui
    '''pneumonia, diabetes, artrose, cancer, gripe, aids'''
    print("|                                                                         |")
    print("Existem 6 palavras nesse caça palavras (escreva sem espaço e acentos)")
    print("---------------------------------------------------------------------------")
    print("")
    print("Dicas:")
    print("   1-É uma doença inflamatória no pulmão. Os sintomas típicos incluem tosse, dor torácica, febre e dificuldade para respirar. Os agentes infecciosos são: bactérias, vírus, fungos e parasitas.")
    print("   2-É um grupo de doenças metabólicas em que se verificam níveis elevados de glicose no sangue durante um longo intervalo de tempo. Os sintomas da elevada quantidade de glicose incluem necessidade frequente de urinar e aumento da sede e da fome. É causada pela produção insuficiente de insulina pelo pâncreas.")
    print("   3-É um tipo de doença das articulações que resulta da degeneração da cartilagem e do osso subjacente. Os sintomas mais comuns são rigidez e dor nas articulações. As causas mais comuns são lesões anteriores nas articulações, anormalidades no desenvolvimento das articulações ou dos membros e fatores hereditários.")
    print("   4-É um grupo de doenças que envolvem o crescimento celular anormal, com potencial para invadir e espalhar-se para outras partes do corpo, além do local original.Há mais de cem diferentes tipos conhecidos que afetam os seres humanos.")
    print("   5-É uma doença infecciosa provocada por diversos vírus ARN da família Orthomyxoviridae e que afeta aves e mamíferos. Os sintomas mais comuns são calafrios, febre, rinorreia, dores de garganta, dores musculares, dores de cabeça, tosse, fadiga e sensação geral de desconforto. É geralmente transmitida por via aérea através de tosse ou de espirros, os quais propagam partículas que contêm o vírus.")
    print("   6-É uma doença do sistema imunológicohumano causada pelo vírus da imunodeficiência humana. Durante a infecção inicial, uma pessoa pode passar por um breve período doente, com sintomas semelhantes aos da gripe. Normalmente isto é seguido por um período prolongado sem qualquer outro sintoma. À medida que a doença progride, ela interfere mais e mais no sistema imunológico, tornando a pessoa muito mais propensa a ter outros tipos de doenças.")
    print("")
    #COLOCAR AS PALAVRAS
    p1= str(input("Qual a primeira palavra que você achou? "))
    while cont1 != 1:
        #Inserir palavras
        if p1.upper() == "AIDS" or p1.upper()== "ARTROSE" or p1.upper()== "CANCER" or p1.upper()== "DIABETES" or p1.upper()== "GRIPE" or p1.upper()== "PNEUMONIA":
            print("A palavra achada foi ",p1)
            cont1 += 1
            pontuacao_rodada += len(p1)*p6x
            pontuacao_total += pontuacao_rodada
            pontuacao_medio += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p1.upper() != "AIDS" or p1.upper()!= "ARTROSE" or p1.upper()!= "CANCER" or p1.upper()!= "DIABETES" or p1.upper()!= "GRIPE" or p1.upper()!= "PNEUMONIA":
            print("O dado colocado está inválido")
            p1= str(input("Qual a primeira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| D N S U M C I V A G                                                     |")
    print("| K I E D A E P I R G                                                     |")
    print("| V C A N I T S U T S                                                     |")
    print("| O Q C B D A G I R G                                                     |")
    print("| T E K F E Z S D O E                                                     |")
    print("| R Q I A T T M E S L                                                     |")
    print("| U X T J K D E A E D                                                     |")
    print("| P E K T O D C S C R                                                     |")
    print("| P N E U M O N I A V                                                     |")
    print("| I Q L K G L Z K R B                                                     |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p2 = str(input("Qual a segunda palavra que você achou? "))
    while cont2 != 1:
        if p2.upper() == p1.upper():
            print("A palavra está repetida")
            p2 = str(input("Qual a segunda palavra que você achou? "))
        #Inserir palavras
        elif p2.upper() == "AIDS" or p2.upper()== "ARTROSE" or p2.upper()== "CANCER" or p2.upper()== "DIABETES" or p2.upper()== "GRIPE" or p2.upper()== "PNEUMONIA":
            print("A palavra achada foi ",p2)
            cont2 += 1
            pontuacao_rodada += len(p2)*p5x
            pontuacao_total += pontuacao_rodada
            pontuacao_medio += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p2.upper() != "AIDS" or p2.upper()!= "ARTROSE" or p2.upper()!= "CANCER" or p2.upper()!= "DIABETES" or p2.upper()!= "GRIPE" or p2.upper()!= "PNEUMONIA":
            print("O dado colocado está inválido")
            p2= str(input("Qual a segunda palavra que você achou? "))
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| D N S U M C I V A G                                                     |")
    print("| K I E D A E P I R G                                                     |")
    print("| V C A N I T S U T S                                                     |")
    print("| O Q C B D A G I R G                                                     |")
    print("| T E K F E Z S D O E                                                     |")
    print("| R Q I A T T M E S L                                                     |")
    print("| U X T J K D E A E D                                                     |")
    print("| P E K T O D C S C R                                                     |")
    print("| P N E U M O N I A V                                                     |")
    print("| I Q L K G L Z K R B                                                     |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p3 = str(input("Qual a terceira palavra que você achou? "))
    while cont3 != 1:
        if p3.upper()==p1.upper() or p3.upper()==p2.upper():
            print("A palavra está repetida")
            p3 = str(input("Qual a terceira palavra que você achou? "))
        #Inserir palavras
        elif p3.upper() == "AIDS" or p3.upper()== "ARTROSE" or p3.upper()== "CANCER" or p3.upper()== "DIABETES" or p3.upper()== "GRIPE" or p3.upper()== "PNEUMONIA":
            print("A palavra achada foi ",p3)
            cont3 += 1
            pontuacao_rodada += len(p3)*p4x
            pontuacao_total += pontuacao_rodada
            pontuacao_medio += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p3.upper() != "AIDS" or p3.upper()!= "ARTROSE" or p3.upper()!= "CANCER" or p3.upper()!= "DIABETES" or p3.upper()!= "GRIPE" or p3.upper()!= "PNEUMONIA":
            print("O dado colocado está inválido")
            p3= str(input("Qual a terceira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| D N S U M C I V A G                                                     |")
    print("| K I E D A E P I R G                                                     |")
    print("| V C A N I T S U T S                                                     |")
    print("| O Q C B D A G I R G                                                     |")
    print("| T E K F E Z S D O E                                                     |")
    print("| R Q I A T T M E S L                                                     |")
    print("| U X T J K D E A E D                                                     |")
    print("| P E K T O D C S C R                                                     |")
    print("| P N E U M O N I A V                                                     |")
    print("| I Q L K G L Z K R B                                                     |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p4 = str(input("Qual a quarta palavra que você achou? "))
    while cont4 != 1:
        if p4==p1 or p4==p2 or p4==p3:
            print("A palavra está repetida")
            p4 = str (input("Qual a quarta palavra que você achou? "))
        #Inserir palavras
        elif p4.upper() == "AIDS" or p4.upper()== "ARTROSE" or p4.upper()== "CANCER" or p4.upper()== "DIABETES" or p4.upper()== "GRIPE" or p4.upper()== "PNEUMONIA":
            print("A palavra achada foi ",p4)
            cont4 += 1
            pontuacao_rodada += len(p4)*p3x
            pontuacao_total += pontuacao_rodada
            pontuacao_medio += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p4.upper() != "AIDS" or p4.upper()!= "ARTROSE" or p4.upper()!= "CANCER" or p4.upper()!= "DIABETES" or p4.upper()!= "GRIPE" or p4.upper()!= "PNEUMONIA":
            print("O dado colocado está inválido")
            p4 = str(input("Qual a quarta palavra que você achou? "))

    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| D N S U M C I V A G                                                     |")
    print("| K I E D A E P I R G                                                     |")
    print("| V C A N I T S U T S                                                     |")
    print("| O Q C B D A G I R G                                                     |")
    print("| T E K F E Z S D O E                                                     |")
    print("| R Q I A T T M E S L                                                     |")
    print("| U X T J K D E A E D                                                     |")
    print("| P E K T O D C S C R                                                     |")
    print("| P N E U M O N I A V                                                     |")
    print("| I Q L K G L Z K R B                                                     |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p5 = str(input("Qual a quinta palavra que você achou? "))
    while cont5 !=1:
        if p5==p1 or p5==p2 or p5==p3 or p5==p4:
            print("A palavra está repetida")
            p5 = str (input("Qual a quinta palavra que você achou? "))
        elif p5.upper() == "AIDS" or p5.upper()== "ARTROSE" or p5.upper()== "CANCER" or p5.upper()== "DIABETES" or p5.upper()== "GRIPE" or p5.upper()== "PNEUMONIA":
            print("A palavra achada foi ",p5)
            cont5 += 1
            pontuacao_rodada += len(p5)*p2x
            pontuacao_total += pontuacao_rodada
            pontuacao_medio += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        elif p5.upper() != "AIDS" or p5.upper()!= "ARTROSE" or p5.upper()!= "CANCER" or p5.upper()!= "DIABETES" or p5.upper()!= "GRIPE" or p5.upper()!= "PNEUMONIA":
            print("O dado colocado está inválido")
            p5 = str(input("Qual a quinta palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| D N S U M C I V A G                                                     |")
    print("| K I E D A E P I R G                                                     |")
    print("| V C A N I T S U T S                                                     |")
    print("| O Q C B D A G I R G                                                     |")
    print("| T E K F E Z S D O E                                                     |")
    print("| R Q I A T T M E S L                                                     |")
    print("| U X T J K D E A E D                                                     |")
    print("| P E K T O D C S C R                                                     |")
    print("| P N E U M O N I A V                                                     |")
    print("| I Q L K G L Z K R B                                                     |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p6 = str(input("Qual a sexta palavra que você achou? "))
    while cont6 !=1:
        if p6==p1 or p6==p2 or p6==p3 or p6==p4 or p6==p5:
            print("A palavra está repetida")
            p6 = str (input("Qual a sexta palavra que você achou? "))
        elif p6.upper() == "AIDS" or p6.upper()== "ARTROSE" or p6.upper()== "CANCER" or p6.upper()== "DIABETES" or p6.upper()== "GRIPE" or p6.upper()== "PNEUMONIA":
            print("A palavra achada foi ",p6)
            cont6 += 1
            pontuacao_rodada += len(p6)*p1x
            pontuacao_total += pontuacao_rodada
            pontuacao_medio += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        elif p6.upper() != "AIDS" or p6.upper()!= "ARTROSE" or p6.upper()!= "CANCER" or p6.upper()!= "DIABETES" or p6.upper()!= "GRIPE" or p6.upper()!= "PNEUMONIA":
            print("O dado colocado está inválido")
            p6 = str(input("Qual a sexta palavra que você achou? "))


    print("")
    print("A primeira palavra achada foi:",p1)
    print("A segunda palavra achada foi:",p2)
    print("A terceira palavra achada foi:",p3)
    print("A quarta palavra achada foi:",p4)
    print("A quinta palavra achada foi:",p5)
    print("A sexta palavra achada foi:",p6)
    print("")
    print("A sua pontuação nessa rodada foi: ",pontuacao_rodada)
    print("A sua pontuação total é:",pontuacao_total)
    print("")
    print("O quadro de respostas é:")
    print("")
    #quadro de respostas daqui
    print("D + S + + C + + A + ")
    print("+ I + D A E P I R G ")
    print("+ + A N I + + + T + ")
    print("+ + C B + A + + R + ")
    print("+ E + + E + + + O + ")
    print("R + + + + T + + S + ")
    print("+ + + + + + E + E + ")
    print("+ + + + + + + S + + ")
    print("P N E U M O N I A + ")
    print("+ + + + + + + + + + ")
    #até aqui
    ##################################################
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    cont5 = 0
    cont6 = 0
    pontuacao_rodada = 0
    print("")
    print("")
    print("")
    print("                             LOADING",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("")
    print("")
    print("")
    print("---------------------------------------------------------------------------")
    print("| Répteis - FASE 10                                                       |")
    print("|                                                                         |")
    #DECIMA FASE10101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010
    print("|                                                                         |")
    #Colocar o caça daqui
    print("| Z J B D I R J Y O T                                                     |")
    print("| O A E L A M A C T A                                                     |")
    print("| C C J G G Q Y G R R                                                     |")
    print("| O C M D S P J J A T                                                     |")
    print("| O N J D Y M E O G A                                                     |")
    print("| A M P B X R T I A R                                                     |")
    print("| Q G Q Z A Y P Z L U                                                     |")
    print("| C R O C O D I L O G                                                     |")
    print("| B M A C C O B R A A                                                     |")
    print("| P J J L P D V D V U                                                     |")
    #Até aqui
    '''tartaruga, crocodilo, camaleao, lagarto, jacare, cobra'''
    print("|                                                                         |")
    print("| Existem 6 palavras nesse caça palavras (escreva sem espaço e acentos)   |")
    print("---------------------------------------------------------------------------")
    print("")
    print("Dicas:")
    print("   1-Esses animais apresentam placas ósseas dérmicas, que se fundem originando uma carapaça dorsal e um plastrão ventral rígidos, que protegem o corpo. As vértebras e costelas fundem-se a essas estruturas.")
    print("   2-Animal semiaquático carnívoro que pertence à família Crocodilidae com pele utilizada pela indústria da moda.")
    print("   3-Animal que tem a habilidade de trocar de cor.")
    print("   4-Um exemplo de espécie que pertence ao grupo desse tipo de réptil é o dragão-de-komodo.")
    print("   5-Existe uma personagem do sítio do pica-pau amarelo que é da minha espécie.")
    print("   6-É o nome dado a répteis rastejantes, de corpo alongado e sem patas. Na verdade, chamar esses animais de “serpentes” é mais correto.")
    print("")
    #COLOCAR AS PALAVRAS
    p1= str(input("Qual a primeira palavra que você achou? "))
    while cont1 != 1:
        #Inserir palavras
        if p1.upper() == "CAMALEAO" or p1.upper()== "COBRA" or p1.upper()== "CROCODILO" or p1.upper()== "JACARE" or p1.upper()== "LAGARTO" or p1.upper()== "TARTARUGA":
            print("A palavra achada foi ",p1)
            cont1 += 1
            pontuacao_rodada += len(p1)*p6x
            pontuacao_total += pontuacao_rodada
            pontuacao_medio += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p1.upper() != "CAMALEAO" or p1.upper()!= "COBRA" or p1.upper()!= "CROCODILO" or p1.upper()!= "JACARE" or p1.upper()!= "LAGARTO" or p1.upper()!= "TARTARUGA":
            print("O dado colocado está inválido")
            p1= str(input("Qual a primeira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| Z J B D I R J Y O T                                                     |")
    print("| O A E L A M A C T A                                                     |")
    print("| C C J G G Q Y G R R                                                     |")
    print("| O C M D S P J J A T                                                     |")
    print("| O N J D Y M E O G A                                                     |")
    print("| A M P B X R T I A R                                                     |")
    print("| Q G Q Z A Y P Z L U                                                     |")
    print("| C R O C O D I L O G                                                     |")
    print("| B M A C C O B R A A                                                     |")
    print("| P J J L P D V D V U                                                     |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p2 = str(input("Qual a segunda palavra que você achou? "))
    while cont2 != 1:
        if p2.upper() == p1.upper():
            print("A palavra está repetida")
            p2 = str(input("Qual a segunda palavra que você achou? "))
        #Inserir palavras
        elif p2.upper() == "CAMALEAO" or p2.upper()== "COBRA" or p2.upper()== "CROCODILO" or p2.upper()== "JACARE" or p2.upper()== "LAGARTO" or p2.upper()== "TARTARUGA":
            print("A palavra achada foi ",p2)
            cont2 += 1
            pontuacao_rodada += len(p2)*p5x
            pontuacao_total += pontuacao_rodada
            pontuacao_medio += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p2.upper() != "CAMALEAO" or p2.upper()!= "COBRA" or p2.upper()!= "CROCODILO" or p2.upper()!= "JACARE" or p2.upper()!= "LAGARTO" or p2.upper()!= "TARTARUGA":
            print("O dado colocado está inválido")
            p2= str(input("Qual a segunda palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| Z J B D I R J Y O T                                                     |")
    print("| O A E L A M A C T A                                                     |")
    print("| C C J G G Q Y G R R                                                     |")
    print("| O C M D S P J J A T                                                     |")
    print("| O N J D Y M E O G A                                                     |")
    print("| A M P B X R T I A R                                                     |")
    print("| Q G Q Z A Y P Z L U                                                     |")
    print("| C R O C O D I L O G                                                     |")
    print("| B M A C C O B R A A                                                     |")
    print("| P J J L P D V D V U                                                     |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p3 = str(input("Qual a terceira palavra que você achou? "))
    while cont3 != 1:
        if p3.upper()==p1.upper() or p3.upper()==p2.upper():
            print("A palavra está repetida")
            p3 = str(input("Qual a terceira palavra que você achou? "))
        #Inserir palavras
        elif p3.upper() == "CAMALEAO" or p3.upper()== "COBRA" or p3.upper()== "CROCODILO" or p3.upper()== "JACARE" or p3.upper()== "LAGARTO" or p3.upper()== "TARTARUGA":
            print("A palavra achada foi ",p3)
            cont3 += 1
            pontuacao_rodada += len(p3)*p4x
            pontuacao_total += pontuacao_rodada
            pontuacao_medio += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p3.upper() != "CAMALEAO" or p3.upper()!= "COBRA" or p3.upper()!= "CROCODILO" or p3.upper()!= "JACARE" or p3.upper()!= "LAGARTO" or p3.upper()!= "TARTARUGA":
            print("O dado colocado está inválido")
            p3= str(input("Qual a terceira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| Z J B D I R J Y O T                                                     |")
    print("| O A E L A M A C T A                                                     |")
    print("| C C J G G Q Y G R R                                                     |")
    print("| O C M D S P J J A T                                                     |")
    print("| O N J D Y M E O G A                                                     |")
    print("| A M P B X R T I A R                                                     |")
    print("| Q G Q Z A Y P Z L U                                                     |")
    print("| C R O C O D I L O G                                                     |")
    print("| B M A C C O B R A A                                                     |")
    print("| P J J L P D V D V U                                                     |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p4 = str(input("Qual a quarta palavra que você achou? "))
    while cont4 != 1:
        if p4==p1 or p4==p2 or p4==p3:
            print("A palavra está repetida")
            p4 = str (input("Qual a quarta palavra que você achou? "))
        #Inserir palavras
        elif p4.upper() == "CAMALEAO" or p4.upper()== "COBRA" or p4.upper()== "CROCODILO" or p4.upper()== "JACARE" or p4.upper()== "LAGARTO" or p4.upper()== "TARTARUGA":
            print("A palavra achada foi ",p4)
            cont4 += 1
            pontuacao_rodada += len(p4)*p3x
            pontuacao_total += pontuacao_rodada
            pontuacao_medio += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p4.upper() != "CAMALEAO" or p4.upper()!= "COBRA" or p4.upper()!= "CROCODILO" or p4.upper()!= "JACARE" or p4.upper()!= "LAGARTO" or p4.upper()!= "TARTARUGA":
            print("O dado colocado está inválido")
            p4 = str(input("Qual a quarta palavra que você achou? "))

    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| Z J B D I R J Y O T                                                     |")
    print("| O A E L A M A C T A                                                     |")
    print("| C C J G G Q Y G R R                                                     |")
    print("| O C M D S P J J A T                                                     |")
    print("| O N J D Y M E O G A                                                     |")
    print("| A M P B X R T I A R                                                     |")
    print("| Q G Q Z A Y P Z L U                                                     |")
    print("| C R O C O D I L O G                                                     |")
    print("| B M A C C O B R A A                                                     |")
    print("| P J J L P D V D V U                                                     |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p5 = str(input("Qual a quinta palavra que você achou? "))
    while cont5 !=1:
        if p5==p1 or p5==p2 or p5==p3 or p5==p4:
            print("A palavra está repetida")
            p5 = str (input("Qual a quinta palavra que você achou? "))
        #Inserir palavras
        elif p5.upper() == "CAMALEAO" or p5.upper()== "COBRA" or p5.upper()== "CROCODILO" or p5.upper()== "JACARE" or p5.upper()== "LAGARTO" or p5.upper()== "TARTARUGA":
            print("A palavra achada foi ",p5)
            cont5 += 1
            pontuacao_rodada += len(p5)*p2x
            pontuacao_total += pontuacao_rodada
            pontuacao_medio += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p5.upper() != "CAMALEAO" or p5.upper()!= "COBRA" or p5.upper()!= "CROCODILO" or p5.upper()!= "JACARE" or p5.upper()!= "LAGARTO" or p5.upper()!= "TARTARUGA":
            print("O dado colocado está inválido")
            p5 = str(input("Qual a quinta palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| Z J B D I R J Y O T                                                     |")
    print("| O A E L A M A C T A                                                     |")
    print("| C C J G G Q Y G R R                                                     |")
    print("| O C M D S P J J A T                                                     |")
    print("| O N J D Y M E O G A                                                     |")
    print("| A M P B X R T I A R                                                     |")
    print("| Q G Q Z A Y P Z L U                                                     |")
    print("| C R O C O D I L O G                                                     |")
    print("| B M A C C O B R A A                                                     |")
    print("| P J J L P D V D V U                                                     |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p6 = str(input("Qual a sexta palavra que você achou? "))
    while cont6 !=1:
        if p6==p1 or p6==p2 or p6==p3 or p6==p4 or p6==p5:
            print("A palavra está repetida")
            p6 = str (input("Qual a sexta palavra que você achou? "))
        #Inserir palavras
        elif p6.upper() == "CAMALEAO" or p6.upper()== "COBRA" or p6.upper()== "CROCODILO" or p6.upper()== "JACARE" or p6.upper()== "LAGARTO" or p6.upper()== "TARTARUGA":
            print("A palavra achada foi ",p6)
            cont6 += 1
            pontuacao_rodada += len(p6)*p1x
            pontuacao_total += pontuacao_rodada
            pontuacao_medio += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p6.upper() != "CAMALEAO" or p6.upper()!= "COBRA" or p6.upper()!= "CROCODILO" or p6.upper()!= "JACARE" or p6.upper()!= "LAGARTO" or p6.upper()!= "TARTARUGA":
            print("O dado colocado está inválido")
            p6 = str(input("Qual a sexta palavra que você achou? "))


    print("")
    print("A primeira palavra achada foi:",p1)
    print("A segunda palavra achada foi:",p2)
    print("A terceira palavra achada foi:",p3)
    print("A quarta palavra achada foi:",p4)
    print("A quinta palavra achada foi:",p5)
    print("A sexta palavra achada foi:",p6)
    print("")
    print("A sua pontuação nessa rodada foi: ",pontuacao_rodada)
    print("A sua pontuação total é:",pontuacao_total)
    print("")
    print("O quadro de respostas é:")
    print("")
    #quadro de respostas daqui
    print("+ + + + + + + + O T ")
    print("O A E L A M A C T A ")
    print("+ + + + + + + + R R ")
    print("+ + + + + + + + A T ")
    print("+ + + + + + E + G A ")
    print("+ + + + + R + + A R ")
    print("+ + + + A + + + L U ")
    print("C R O C O D I L O G ")
    print("+ + A + C O B R A A ")
    print("+ J + + + + + + + + ")
    #até aqui
    #Pontuação-medio####################################################################################################################################
    if pontuacao_medio >= 37120: #maximo
        print("PARABÉNS! Você fez a pontuação máxima de ",pontuacao_medio," no modo médio! Você é um MESTRE SUPREMO DO MODO MÉDIO!")
    elif pontuacao_medio <= 25640: #minimo
        print("A sua pontuação no modo médio foi a menor possível:",pontuacao_medio," .Você é um fracasso no modo médio") #Fracasso deve estar meio forte. Mudar depois.
    elif pontuacao_medio >= 31380 and pontuacao_medio < 37120: #entre metade e maximo
        print("A sua pontuação de ",pontuacao_medio," está entre a metade e o máximo! Você é um veterano do modo médio!")
    elif pontuacao_medio > 25640 and pontuacao_medio < 31380:
        print("A sua pontuação de ",pontuacao_medio," está entre a metade e o mínimo. Você é um iniciante do modo médio")
    time.sleep(1)
    print("Parabens, você chegou ao nível difícil!!!.",
          "\nA senha para o acesso direto ao nível difícil caso queira parar é: om1zv",
          "\nGuarde ela bem")
    time.sleep(1)

    return n3()
##############################################################################################################################################################################



################################################################################### N1 #################################################################################


def n1():

    '''Caça palavras nivel fácil 8X8'''
    #
    #PRIMEIRA FASE1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    #
    print("                             LOADING",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("                             NÍVEL FÁCIL")
    print("---------------------------------------------------------------------------")
    print("| Estados do Brasil - FASE 1                                              |")
    print("|                                                                         |")
    print("| A W U F O D P G                                                         |")
    print("| F M Q S B H A D                                                         |")
    print("| F M A A S T R U                                                         |")
    print("| S J H Z Z R A H                                                         |")
    print("| E I G V O D N V                                                         |")
    print("| A A X E F N A S                                                         |")
    print("| E R C A P D A O                                                         |")
    print("| Y D A R V H K S                                                         |")
    print("|                                                                         |")
    print("| Existem 4 palavras nesse caça palavras (escreva sem espaço e acentos)   |")
    print("---------------------------------------------------------------------------")
    print("")
    print("Dicas:")
    print("   1-Sua Capital é Curitiba")
    print("   2-Sua Capital é Manaus")
    print("   3-Sua Capital é Salvador")
    print("   4-Sua Capital é Rio Branco")
    print("")
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    #para cada cont é uma palavra e ele é zerado sempre que um caça acaba. Assim podendo ser utilizado de novo.
    '''Para esse caça a pontuação max é adquirida na ordem: Amazonas, parana, bahia, acre.
    E a minima é ao contrário'''
    #Pontuações
    #Uma pontuação de rodada por caça palavras que é zerada sempre que o caça palavras termina
    #Uma pontuação que é somada ao longo do jogo
    pontuacao_rodada = 0
    pontuacao_total = 0
    pontuacao_facil = 0
    pontuacao_medio = 0
    pontuacao_dificil = 0
    #multiplicadores para os caça palavras
    p4x = 40
    p3x = 30
    p2x = 20
    p1x = 10
    #Essas variaveis vão ser os multiplicadores adcionais para os caça palavras 10x10
    p6x = 60
    p5x = 50
    #Essas variaveis vão ser os multiplicadores adcionais para os caça palavras 15x15
    p8x = 80
    p7x = 70
    p1= str(input("Qual a primeira palavra que você achou? "))
    while cont1 != 1:
        if p1.upper() == "AMAZONAS" or p1.upper()== "ACRE" or p1.upper()== "BAHIA" or p1.upper()== "PARANA":
            print("A palavra achada foi ",p1)
            cont1 += 1
            #caso acerte soma um no cont1 e para o while
            pontuacao_rodada += len(p1)*p4x
            pontuacao_total += pontuacao_rodada
            pontuacao_facil += pontuacao_rodada
            #somas das pontuações da rodada e da pontuação total
            print("A sua pontuação é, ",pontuacao_rodada)
            #no final do caça palavra a pontuação total é printada mas a cada acerto é feito um print da pontuação da rodada
        elif p1.upper() != "AMAZONAS" or p1.upper()!= "ACRE" or p1.upper()!= "BAHIA" or p1.upper()!= "PARANA":
            print("O dado colocado está inválido")
            p1= str(input("Qual a primeira palavra que você achou? "))
    #printando de novo o caça palavras para ele não ficar muito longe do usuário
    print("")
    print("---------------------------------------------------------------------------")
    print("| A W U F O D P G                                                         |")
    print("| F M Q S B H A D                                                         |")
    print("| F M A A S T R U                                                         |")
    print("| S J H Z Z R A H                                                         |")
    print("| E I G V O D N V                                                         |")
    print("| A A X E F N A S                                                         |")
    print("| E R C A P D A O                                                         |")
    print("| Y D A R V H K S                                                         |")
    print("---------------------------------------------------------------------------")
    print("")

    p2 = str(input("Qual a segunda palavra que você achou? "))
    while cont2 != 1:
        if p2.upper() == p1.upper():
            print("A palavra está repetida")
            p2 = str(input("Qual a segunda palavra que você achou? "))
        elif p2.upper() == "AMAZONAS" or p2.upper()== "ACRE" or p2.upper()== "BAHIA" or p2.upper()== "PARANA":
            print("A palavra achada foi ",p2)
            cont2 += 1
            pontuacao_rodada += len(p2)*p3x
            pontuacao_total += pontuacao_rodada
            pontuacao_facil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        elif p2.upper() != "AMAZONAS" or p2.upper()!= "ACRE" or p2.upper()!= "BAHIA" or p2.upper()!= "PARANA":
            print("O dado colocado está inválido")
            p2= str(input("Qual a segunda palavra que você achou? "))
    print("")
    print("---------------------------------------------------------------------------")
    print("| A W U F O D P G                                                         |")
    print("| F M Q S B H A D                                                         |")
    print("| F M A A S T R U                                                         |")
    print("| S J H Z Z R A H                                                         |")
    print("| E I G V O D N V                                                         |")
    print("| A A X E F N A S                                                         |")
    print("| E R C A P D A O                                                         |")
    print("| Y D A R V H K S                                                         |")
    print("---------------------------------------------------------------------------")
    print("")
    p3 = str(input("Qual a terceira palavra que você achou? "))
    while cont3 != 1:
        if p3.upper()==p1.upper() or p3.upper()==p2.upper():
            print("A palavra está repetida")
            p3 = str(input("Qual a terceira palavra que você achou? "))
        elif p3.upper() == "AMAZONAS" or p3.upper()== "ACRE" or p3.upper()== "BAHIA" or p3.upper()== "PARANA":
            print("A palavra achada foi ",p3)
            cont3 += 1
            pontuacao_rodada += len(p3)*p2x
            pontuacao_total += pontuacao_rodada
            pontuacao_facil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        elif p3.upper() != "AMAZONAS" or p3.upper()!= "ACRE" or p3.upper()!= "BAHIA" or p3.upper()!= "PARANA":
            print("O dado colocado está inválido")
            p3= str(input("Qual a terceira palavra que você achou? "))
    print("")
    print("---------------------------------------------------------------------------")
    print("| A W U F O D P G                                                         |")
    print("| F M Q S B H A D                                                         |")
    print("| F M A A S T R U                                                         |")
    print("| S J H Z Z R A H                                                         |")
    print("| E I G V O D N V                                                         |")
    print("| A A X E F N A S                                                         |")
    print("| E R C A P D A O                                                         |")
    print("| Y D A R V H K S                                                         |")
    print("---------------------------------------------------------------------------")
    print("")
    p4 = str(input("Qual a quarta palavra que você achou? "))
    while cont4 != 1:
        if p4==p1 or p4==p2 or p4==p3:
            print("A palavra está repetida")
            p4 = str (input("Qual a quarta palavra que você achou? "))
        elif p4.upper() == "AMAZONAS" or p4.upper()== "ACRE" or p4.upper()== "BAHIA" or p4.upper()== "PARANA":
            print("A palavra achada foi ",p4)
            cont4 += 1
            pontuacao_rodada += len(p4)*p1x
            pontuacao_total += pontuacao_rodada
            pontuacao_facil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        elif p4.upper() != "AMAZONAS" or p4.upper()!= "ACRE" or p4.upper()!= "BAHIA" or p4.upper()!= "PARANA":
            print("O dado colocado está inválido")
            p4 = str(input("Qual a quarta palavra que você achou? "))
    print("")
    print("A primeira palavra achada foi:",p1)
    print("A segunda palavra achada foi:",p2)
    print("A terceira palavra achada foi:",p3)
    print("A quarta palavra achada foi:",p4)
    print("")
    print("A sua pontuação nessa rodada foi: ",pontuacao_rodada)
    print("A sua pontuação total é:",pontuacao_total)
    print("")
    print("O quadro de respostas é:")
    print("A + + + + + P + ")
    print("+ M + + B + A + ")
    print("+ + A A + + R + ")
    print("+ + H Z + + A + ")
    print("+ I + + O + N + ")
    print("A + + + + N A + ")
    print("E R C A + + A + ")
    print("+ + + + + + + S ")



    '''Segundo Caça palavras'''
    #
    #SEGUNDA FASE22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
    #
    #zerando variaveis para não ter que criar novas
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    #zerando pontuação da rodada pois o jogador entra em uma nova fase
    pontuacao_rodada = 0
    print("")
    print("")
    print("")
    print("                             LOADING",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("")
    print("")
    print("")
    print("---------------------------------------------------------------------------")
    print("| Capitais do Brasil - FASE 2                                             |")
    print("|                                                                         |")
    print("| M N I S Q U W A                                                         |")
    print("| X A X R O B B Z                                                         |")
    print("| E T C Z B I I A                                                         |")
    print("| Z A X E T O O B                                                         |")
    print("| Q L P I I X V A                                                         |")
    print("| O W R U D O N E                                                         |")
    print("| I U J T H Z N X                                                         |")
    print("| C G O I A N I A                                                         |")
    print("|                                                                         |")
    print("| Existem 4 palavras nesse caça palavras (escreva sem espaço e acentos)   |")
    print("---------------------------------------------------------------------------")
    print("")
    print("Dicas:")
    print("   1-É a Capital do Paraná")
    print("   2-É a Capital de Goiás")
    print("   3-É a Capital de Alagoas")
    print("   4-É a Capital do Rio Grande do Norte")
    print("")
    '''Curitiba,goiania,maceio,natalpontução maxima'''
    p1= str(input("Qual a primeira palavra que você achou? "))
    while cont1 != 1:
        if p1.upper() == "GOIANIA" or p1.upper()== "CURITIBA" or p1.upper()== "MACEIO" or p1.upper()== "NATAL":
            print("A palavra achada foi ",p1)
            cont1 += 1
            pontuacao_rodada += len(p1)*p4x
            pontuacao_total += pontuacao_rodada
            pontuacao_facil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        elif p1.upper() != "GOIANIA" or p1.upper()!= "CURITIBA" or p1.upper()!= "MACEIO" or p1.upper()!= "NATAL":
            print("O dado colocado está inválido")
            p1= str(input("Qual a primeira palavra que você achou? "))
    print("---------------------------------------------------------------------------")
    print("| M N I S Q U W A                                                         |")
    print("| X A X R O B B Z                                                         |")
    print("| E T C Z B I I A                                                         |")
    print("| Z A X E T O O B                                                         |")
    print("| Q L P I I X V A                                                         |")
    print("| O W R U D O N E                                                         |")
    print("| I U J T H Z N X                                                         |")
    print("| C G O I A N I A                                                         |")
    print("---------------------------------------------------------------------------")
    p2 = str(input("Qual a segunda palavra que você achou? "))
    while cont2 != 1:
        if p2.upper() == p1.upper():
            print("A palavra está repetida")
            p2 = str(input("Qual a segunda palavra que você achou? "))
        elif p2.upper() == "GOIANIA" or p2.upper()== "CURITIBA" or p2.upper()== "MACEIO" or p2.upper()== "NATAL":
            print("A palavra achada foi ",p2)
            cont2 += 1
            pontuacao_rodada += len(p2)*p3x
            pontuacao_total += pontuacao_rodada
            pontuacao_facil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        elif p2.upper() != "GOIANIA" or p2.upper()!= "CURITIBA" or p2.upper()!= "MACEIO" or p2.upper()!= "NATAL":
            print("O dado colocado está inválido")
            p2= str(input("Qual a segunda palavra que você achou? "))
    print("---------------------------------------------------------------------------")
    print("| M N I S Q U W A                                                         |")
    print("| X A X R O B B Z                                                         |")
    print("| E T C Z B I I A                                                         |")
    print("| Z A X E T O O B                                                         |")
    print("| Q L P I I X V A                                                         |")
    print("| O W R U D O N E                                                         |")
    print("| I U J T H Z N X                                                         |")
    print("| C G O I A N I A                                                         |")
    print("---------------------------------------------------------------------------")
    p3 = str(input("Qual a terceira palavra que você achou? "))
    while cont3 != 1:
        if p3.upper()==p1.upper() or p3.upper()==p2.upper():
            print("A palavra está repetida")
            p3 = str(input("Qual a terceira palavra que você achou? "))
        elif p3.upper() == "GOIANIA" or p3.upper()== "CURITIBA" or p3.upper()== "MACEIO" or p3.upper()== "NATAL":
            print("A palavra achada foi ",p3)
            cont3 += 1
            pontuacao_rodada += len(p3)*p2x
            pontuacao_total += pontuacao_rodada
            pontuacao_facil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        elif p3.upper() != "GOIANIA" or p3.upper()!= "CURITIBA" or p3.upper()!= "MACEIO" or p3.upper()!= "NATAL":
            print("O dado colocado está inválido")
            p3= str(input("Qual a terceira palavra que você achou? "))
    print("---------------------------------------------------------------------------")
    print("| M N I S Q U W A                                                         |")
    print("| X A X R O B B Z                                                         |")
    print("| E T C Z B I I A                                                         |")
    print("| Z A X E T O O B                                                         |")
    print("| Q L P I I X V A                                                         |")
    print("| O W R U D O N E                                                         |")
    print("| I U J T H Z N X                                                         |")
    print("| C G O I A N I A                                                         |")
    print("---------------------------------------------------------------------------")
    p4 = str(input("Qual a quarta palavra que você achou? "))
    while cont4 != 1:
        if p4==p1 or p4==p2 or p4==p3:
            print("A palavra está repetida")
            p4 = str (input("Qual a quarta palavra que você achou? "))
        elif p4.upper() == "GOIANIA" or p4.upper()== "CURITIBA" or p4.upper()== "MACEIO" or p4.upper()== "NATAL":
            print("A palavra achada foi ",p4)
            cont4 += 1
            pontuacao_rodada += len(p4)*p1x
            pontuacao_total += pontuacao_rodada
            pontuacao_facil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        elif p4.upper() != "GOIANIA" or p4.upper()!= "CURITIBA" or p4.upper()!= "MACEIO" or p4.upper()!= "NATAL":
            print("O dado colocado está inválido")
            p4 = str(input("Qual a quarta palavra que você achou? "))
    print("")
    print("A primeira palavra achada foi:",p1)
    print("A segunda palavra achada foi:",p2)
    print("A terceira palavra achada foi:",p3)
    print("A quarta palavra achada foi:",p4)
    print("")
    print("A sua pontuação nessa rodada foi: ",pontuacao_rodada)
    print("A sua pontuação total é:",pontuacao_total)
    print("")
    print("O quadro de respostas é:")
    print("M N + + + + + A ")
    print("+ A + + + + B + ")
    print("+ T C + + I + + ")
    print("+ A + E T + + + ")
    print("+ L + I I + + + ")
    print("+ + R + + O + + ")
    print("+ U + + + + + + ")
    print("C G O I A N I A ")
    ##################################################
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0

    pontuacao_rodada = 0
    print("")
    print("")
    print("")
    print("                             LOADING",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("")
    print("")
    print("")
    #
    #TERCEIRA FASE33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    #
    print("---------------------------------------------------------------------------")
    print("| Mamíferos - FASE 3                                                      |")
    print("|                                                                         |")
    #Colocar o caça daqui
    print("| A Y Y V Q A O J                                                         |")
    print("| F R P R R H H T                                                         |")
    print("| I V I B A F L H                                                         |")
    print("| H X E E C F E Z                                                         |")
    print("| V Z I T P W O A                                                         |")
    print("| R A T O U U C Q                                                         |")
    print("| X B H O B C O X                                                         |")
    print("| S V L I J J H T                                                         |")
    #Até aqui
    print("|                                                                         |")
    print("|Existem 4 palavras nesse caça palavras (escreva sem espaço e acentos)    |")
    print("---------------------------------------------------------------------------")
    print("")
    print("Dicas:")
    print("   1-Animal que vive em tocas e galerias subterrâneas e, devido ao seu modo de vida, são total ou parcialmente cegas")
    print("   2-Existe um personagem animado muito famoso da Warner Bros. (Looney Tunes) que é dessa espécie")
    print("   3-Animal com o corpo listrado da cor preta e branca")
    print("   4-Animal que gosta muito de queijo")
    print("")
    #COLOCAR AS PALAVRAS
    '''toupeira,coelho,zebra,rato'''
    p1= str(input("Qual a primeira palavra que você achou? "))
    while cont1 != 1:
        #Inserir palavras
        if p1.upper() == "COELHO" or p1.upper()== "RATO" or p1.upper()== "TOUPEIRA" or p1.upper()== "ZEBRA":
            print("A palavra achada foi ",p1)
            cont1 += 1
            pontuacao_rodada += len(p1)*p4x
            pontuacao_total += pontuacao_rodada
            pontuacao_facil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p1.upper() != "COELHO" or p1.upper()!= "RATO" or p1.upper()!= "TOUPEIRA" or p1.upper()!= "ZEBRA":
            print("O dado colocado está inválido")
            p1= str(input("Qual a primeira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| A Y Y V Q A O J                                                         |")
    print("| F R P R R H H T                                                         |")
    print("| I V I B A F L H                                                         |")
    print("| H X E E C F E Z                                                         |")
    print("| V Z I T P W O A                                                         |")
    print("| R A T O U U C Q                                                         |")
    print("| X B H O B C O X                                                         |")
    print("| S V L I J J H T                                                         |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p2 = str(input("Qual a segunda palavra que você achou? "))
    while cont2 != 1:
        if p2.upper() == p1.upper():
            print("A palavra está repetida")
            p2 = str(input("Qual a segunda palavra que você achou? "))
        #Inserir palavras
        elif p2.upper() == "COELHO" or p2.upper()== "RATO" or p2.upper()== "TOUPEIRA" or p2.upper()== "ZEBRA":
            print("A palavra achada foi ",p2)
            cont2 += 1
            pontuacao_rodada += len(p2)*p3x
            pontuacao_total += pontuacao_rodada
            pontuacao_facil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p2.upper() != "COELHO" or p2.upper()!= "RATO" or p2.upper()!= "TOUPEIRA" or p2.upper()!= "ZEBRA":
            print("O dado colocado está inválido")
            p2= str(input("Qual a segunda palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| A Y Y V Q A O J                                                         |")
    print("| F R P R R H H T                                                         |")
    print("| I V I B A F L H                                                         |")
    print("| H X E E C F E Z                                                         |")
    print("| V Z I T P W O A                                                         |")
    print("| R A T O U U C Q                                                         |")
    print("| X B H O B C O X                                                         |")
    print("| S V L I J J H T                                                         |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p3 = str(input("Qual a terceira palavra que você achou? "))
    while cont3 != 1:
        if p3.upper()==p1.upper() or p3.upper()==p2.upper():
            print("A palavra está repetida")
            p3 = str(input("Qual a terceira palavra que você achou? "))
        #Inserir palavras
        elif p3.upper() == "COELHO" or p3.upper()== "RATO" or p3.upper()== "TOUPEIRA" or p3.upper()== "ZEBRA":
            print("A palavra achada foi ",p3)
            cont3 += 1
            pontuacao_rodada += len(p3)*p2x
            pontuacao_total += pontuacao_rodada
            pontuacao_facil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p3.upper() != "COELHO" or p3.upper()!= "RATO" or p3.upper()!= "TOUPEIRA" or p3.upper()!= "ZEBRA":
            print("O dado colocado está inválido")
            p3= str(input("Qual a terceira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| A Y Y V Q A O J                                                         |")
    print("| F R P R R H H T                                                         |")
    print("| I V I B A F L H                                                         |")
    print("| H X E E C F E Z                                                         |")
    print("| V Z I T P W O A                                                         |")
    print("| R A T O U U C Q                                                         |")
    print("| X B H O B C O X                                                         |")
    print("| S V L I J J H T                                                         |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p4 = str(input("Qual a quarta palavra que você achou? "))
    while cont4 != 1:
        if p4==p1 or p4==p2 or p4==p3:
            print("A palavra está repetida")
            p4 = str (input("Qual a quarta palavra que você achou? "))
        #Inserir palavras
        elif p4.upper() == "COELHO" or p4.upper()== "RATO" or p4.upper()== "TOUPEIRA" or p4.upper()== "ZEBRA":
            print("A palavra achada foi ",p4)
            cont4 += 1
            pontuacao_rodada += len(p4)*p1x
            pontuacao_total += pontuacao_rodada
            pontuacao_facil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p4.upper() != "COELHO" or p4.upper()!= "RATO" or p4.upper()!= "TOUPEIRA" or p4.upper()!= "ZEBRA":
            print("O dado colocado está inválido")
            p4 = str(input("Qual a quarta palavra que você achou? "))
    print("")
    print("A primeira palavra achada foi:",p1)
    print("A segunda palavra achada foi:",p2)
    print("A terceira palavra achada foi:",p3)
    print("A quarta palavra achada foi:",p4)
    print("")
    print("A sua pontuação nessa rodada foi: ",pontuacao_rodada)
    print("A sua pontuação total é:",pontuacao_total)
    print("")
    print("O quadro de respostas é:")
    #quadro de respostas daqui
    print("A + + + + A O + ")
    print("+ R + + R + H + ")
    print("+ + I B + + L + ")
    print("+ + E E + + E + ")
    print("+ Z + + P + O + ")
    print("R A T O + U C + ")
    print("+ + + + + + O + ")
    print("+ + + + + + + T ")
    #até aqui
    ##################################################
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0

    pontuacao_rodada = 0
    print("")
    print("")
    print("")
    print("                             LOADING",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("")
    print("")
    print("")
    #
    #QUARTA FASE44444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
    #
    print("---------------------------------------------------------------------------")
    print("| Grécia Antiga - FASE 4                                                  |")
    print("|                                                                         |")
    #Colocar o caça daqui
    print("| Y K C L D A X S                                                         |")
    print("| P L A T A O O H                                                         |")
    print("| B H J J R V P N                                                         |")
    print("| J Q I E A O I K                                                         |")
    print("| M L K R E Q I N                                                         |")
    print("| D C C R G Q B A                                                         |")
    print("| M S V H E Y K R                                                         |")
    print("| E C T R U D H L                                                         |")
    #Até aqui
    print("|                                                                         |")
    print("| Existem 4 palavras nesse caça palavras (escreva sem espaço e acentos)   |")
    print("---------------------------------------------------------------------------")
    print("")
    print("Dicas:")
    print("   1-Pessoas que eram propriedades de um senhor, sendo forçadas a trabalhar sem direitos trabalhistas ou salário")
    print("   2-Filósofo e matemático grego, considerado  um dos principais pensadores gregos, pois influenciou profundamente a filosofia ocidental. Suas ideias baseiam-se na diferenciação do mundo entre as coisas sensíveis (mundo das ideias e a inteligência) e as coisas visíveis (seres vivos e a matéria).")
    print("   3-Cidade que foi invadida graças a uma tática utilizando um cavalo de madeira gigante, cheio de soldados, como presente para os troianos, que levaram o cavalo para dentro da cidade, e a noite os soldados escondidos saíram do cavalo e dominaram a cidade")
    print("   4-Na mitologia helênica, ele se jogou no mar espumante, tendo assim o mar sendo apelidado com seu nome. Esse mar situa-se na bacia do mar Mediterrâneo")
    print("")
    #COLOCAR AS PALAVRAS
    '''escravos,platao,troia,egeu'''
    p1= str(input("Qual a primeira palavra que você achou? "))
    while cont1 != 1:
        #Inserir palavras
        if p1.upper() == "EGEU" or p1.upper()== "ESCRAVOS" or p1.upper()== "PLATAO" or p1.upper()== "TROIA":
            print("A palavra achada foi ",p1)
            cont1 += 1
            pontuacao_rodada += len(p1)*p4x
            pontuacao_total += pontuacao_rodada
            pontuacao_facil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p1.upper() != "EGEU" or p1.upper()!= "ESCRAVOS" or p1.upper()!= "PLATAO" or p1.upper()!= "TROIA":
            print("O dado colocado está inválido")
            p1= str(input("Qual a primeira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| Y K C L D A X S                                                         |")
    print("| P L A T A O O H                                                         |")
    print("| B H J J R V P N                                                         |")
    print("| J Q I E A O I K                                                         |")
    print("| M L K R E Q I N                                                         |")
    print("| D C C R G Q B A                                                         |")
    print("| M S V H E Y K R                                                         |")
    print("| E C T R U D H L                                                         |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p2 = str(input("Qual a segunda palavra que você achou? "))
    while cont2 != 1:
        if p2.upper() == p1.upper():
            print("A palavra está repetida")
            p2 = str(input("Qual a segunda palavra que você achou? "))
        #Inserir palavras
        elif p2.upper() == "EGEU" or p2.upper()== "ESCRAVOS" or p2.upper()== "PLATAO" or p2.upper()== "TROIA":
            print("A palavra achada foi ",p2)
            cont2 += 1
            pontuacao_rodada += len(p2)*p3x
            pontuacao_total += pontuacao_rodada
            pontuacao_facil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p2.upper() != "EGEU" or p2.upper()!= "ESCRAVOS" or p2.upper()!= "PLATAO" or p2.upper()!= "TROIA":
            print("O dado colocado está inválido")
            p2= str(input("Qual a segunda palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| Y K C L D A X S                                                         |")
    print("| P L A T A O O H                                                         |")
    print("| B H J J R V P N                                                         |")
    print("| J Q I E A O I K                                                         |")
    print("| M L K R E Q I N                                                         |")
    print("| D C C R G Q B A                                                         |")
    print("| M S V H E Y K R                                                         |")
    print("| E C T R U D H L                                                         |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p3 = str(input("Qual a terceira palavra que você achou? "))
    while cont3 != 1:
        if p3.upper()==p1.upper() or p3.upper()==p2.upper():
            print("A palavra está repetida")
            p3 = str(input("Qual a terceira palavra que você achou? "))
        #Inserir palavras
        elif p3.upper() == "EGEU" or p3.upper()== "ESCRAVOS" or p3.upper()== "PLATAO" or p3.upper()== "TROIA":
            print("A palavra achada foi ",p3)
            cont3 += 1
            pontuacao_rodada += len(p3)*p2x
            pontuacao_total += pontuacao_rodada
            pontuacao_facil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p3.upper() != "EGEU" or p3.upper()!= "ESCRAVOS" or p3.upper()!= "PLATAO" or p3.upper()!= "TROIA":
            print("O dado colocado está inválido")
            p3= str(input("Qual a terceira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| Y K C L D A X S                                                         |")
    print("| P L A T A O O H                                                         |")
    print("| B H J J R V P N                                                         |")
    print("| J Q I E A O I K                                                         |")
    print("| M L K R E Q I N                                                         |")
    print("| D C C R G Q B A                                                         |")
    print("| M S V H E Y K R                                                         |")
    print("| E C T R U D H L                                                         |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p4 = str(input("Qual a quarta palavra que você achou? "))
    while cont4 != 1:
        if p4==p1 or p4==p2 or p4==p3:
            print("A palavra está repetida")
            p4 = str (input("Qual a quarta palavra que você achou? "))
        #Inserir palavras
        elif p4.upper() == "EGEU" or p4.upper()== "ESCRAVOS" or p4.upper()== "PLATAO" or p4.upper()== "TROIA":
            print("A palavra achada foi ",p4)
            cont4 += 1
            pontuacao_rodada += len(p4)*p1x
            pontuacao_total += pontuacao_rodada
            pontuacao_facil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p4.upper() != "EGEU" or p4.upper()!= "ESCRAVOS" or p4.upper()!= "PLATAO" or p4.upper()!= "TROIA":
            print("O dado colocado está inválido")
            p4 = str(input("Qual a quarta palavra que você achou? "))
    print("")
    print("A primeira palavra achada foi:",p1)
    print("A segunda palavra achada foi:",p2)
    print("A terceira palavra achada foi:",p3)
    print("A quarta palavra achada foi:",p4)
    print("")
    print("A sua pontuação nessa rodada foi: ",pontuacao_rodada)
    print("A sua pontuação total é:",pontuacao_total)
    print("")
    print("O quadro de respostas é:")
    #quadro de respostas daqui
    print("+ + + + + + + S ")
    print("P L A T A O O + ")
    print("+ + + + R V + + ")
    print("+ + + + A O + + ")
    print("+ + + R E + I + ")
    print("+ + C + G + + A ")
    print("+ S + + E + + + ")
    print("E + + + U + + + ")
    #até aqui
    ##################################################
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0

    pontuacao_rodada = 0
    print("")
    print("")
    print("")
    print("                             LOADING",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("")
    print("")
    print("")
    #
    #QUINTA FASE555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
    #
    print("---------------------------------------------------------------------------")
    print("| Egito Antigo - FASE 5                                                   |")
    print("|                                                                         |")
    #Colocar o caça daqui
    print("| A F N C M Z S P                                                         |")
    print("| M B U S T V I O                                                         |")
    print("| N Q M B V R C L                                                         |")
    print("| P E Q U A M F I                                                         |")
    print("| I I D M T G J N                                                         |")
    print("| E T I E U Q P F                                                         |")
    print("| A D D V K A P L                                                         |")
    print("| E O T R E S E D                                                         |")
    #Até aqui
    print("|                                                                         |")
    print("| Existem 4 palavras nesse caça palavras (escreva sem espaço e acentos)   |")
    print("---------------------------------------------------------------------------")
    print("")
    print("Dicas:")
    print("   1-É um sólido geométrico, que tem um de seus exemplos no mundo considerado como uma das sete maravilhas do mundo antigo, situado no Egito")
    print("   2-Região que pode ser quente ou fria, que recebe pouca precipitação pluviométrica (Há pouca chuva durante o ano)")
    print("   3-Câmara onde fica o sarcófago com os restos mortais de alguém, dentro de mausoléu, pirâmide ou em construção mortuária subterrânea")
    print("   4-Rio mais extenso do mundo")
    print("")

    #COLOCAR AS PALAVRAS
    '''piramide,deserto,tumba,nilo'''
    p1= str(input("Qual a primeira palavra que você achou? "))
    while cont1 != 1:
        #Inserir palavras
        if p1.upper() == "DESERTO" or p1.upper()== "NILO" or p1.upper()== "PIRAMIDE" or p1.upper()== "TUMBA":
            print("A palavra achada foi ",p1)
            cont1 += 1
            pontuacao_rodada += len(p1)*p4x
            pontuacao_total += pontuacao_rodada
            pontuacao_facil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p1.upper() != "DESERTO" or p1.upper()!= "NILO" or p1.upper()!= "PIRAMIDE" or p1.upper()!= "TUMBA":
            print("O dado colocado está inválido")
            p1= str(input("Qual a primeira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| A F N C M Z S P                                                         |")
    print("| M B U S T V I O                                                         |")
    print("| N Q M B V R C L                                                         |")
    print("| P E Q U A M F I                                                         |")
    print("| I I D M T G J N                                                         |")
    print("| E T I E U Q P F                                                         |")
    print("| A D D V K A P L                                                         |")
    print("| E O T R E S E D                                                         |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p2 = str(input("Qual a segunda palavra que você achou? "))
    while cont2 != 1:
        if p2.upper() == p1.upper():
            print("A palavra está repetida")
            p2 = str(input("Qual a segunda palavra que você achou? "))
        #Inserir palavras
        elif p2.upper() == "DESERTO" or p2.upper()== "NILO" or p2.upper()== "PIRAMIDE" or p2.upper()== "TUMBA":
            print("A palavra achada foi ",p2)
            cont2 += 1
            pontuacao_rodada += len(p2)*p3x
            pontuacao_total += pontuacao_rodada
            pontuacao_facil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p2.upper() != "DESERTO" or p2.upper()!= "NILO" or p2.upper()!= "PIRAMIDE" or p2.upper()!= "TUMBA":
            print("O dado colocado está inválido")
            p2= str(input("Qual a segunda palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| A F N C M Z S P                                                         |")
    print("| M B U S T V I O                                                         |")
    print("| N Q M B V R C L                                                         |")
    print("| P E Q U A M F I                                                         |")
    print("| I I D M T G J N                                                         |")
    print("| E T I E U Q P F                                                         |")
    print("| A D D V K A P L                                                         |")
    print("| E O T R E S E D                                                         |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p3 = str(input("Qual a terceira palavra que você achou? "))
    while cont3 != 1:
        if p3.upper()==p1.upper() or p3.upper()==p2.upper():
            print("A palavra está repetida")
            p3 = str(input("Qual a terceira palavra que você achou? "))
        #Inserir palavras
        elif p3.upper() == "DESERTO" or p3.upper()== "NILO" or p3.upper()== "PIRAMIDE" or p3.upper()== "TUMBA":
            print("A palavra achada foi ",p3)
            cont3 += 1
            pontuacao_rodada += len(p3)*p2x
            pontuacao_total += pontuacao_rodada
            pontuacao_facil += pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p3.upper() != "DESERTO" or p3.upper()!= "NILO" or p3.upper()!= "PIRAMIDE" or p3.upper()!= "TUMBA":
            print("O dado colocado está inválido")
            p3= str(input("Qual a terceira palavra que você achou? "))
    print("")
    #Colocar o caça daqui
    print("---------------------------------------------------------------------------")
    print("| A F N C M Z S P                                                         |")
    print("| M B U S T V I O                                                         |")
    print("| N Q M B V R C L                                                         |")
    print("| P E Q U A M F I                                                         |")
    print("| I I D M T G J N                                                         |")
    print("| E T I E U Q P F                                                         |")
    print("| A D D V K A P L                                                         |")
    print("| E O T R E S E D                                                         |")
    print("---------------------------------------------------------------------------")
    #Até aqui
    print("")
    p4 = str(input("Qual a quarta palavra que você achou? "))
    while cont4 != 1:
        if p4==p1 or p4==p2 or p4==p3:
            print("A palavra está repetida")
            p4 = str (input("Qual a quarta palavra que você achou? "))
        #Inserir palavras
        elif p4.upper() == "DESERTO" or p4.upper()== "NILO" or p4.upper()== "PIRAMIDE" or p4.upper()== "TUMBA":
            print("A palavra achada foi ",p4)
            cont4 += 1
            pontuacao_rodada += len(p4)*p1x
            pontuacao_facil += pontuacao_rodada
            pontuacao_total+= pontuacao_rodada
            print("A sua pontuação é, ",pontuacao_rodada)
        #Inserir palavras
        elif p4.upper() != "DESERTO" or p4.upper()!= "NILO" or p4.upper()!= "PIRAMIDE" or p4.upper()!= "TUMBA":
            print("O dado colocado está inválido")
            p4 = str(input("Qual a quarta palavra que você achou? "))
    print("")
    print("A primeira palavra achada foi:",p1)
    print("A segunda palavra achada foi:",p2)
    print("A terceira palavra achada foi:",p3)
    print("A quarta palavra achada foi:",p4)
    print("")
    print("A sua pontuação nessa rodada foi: ",pontuacao_rodada)
    print("A sua pontuação total é:",pontuacao_total)
    print("")
    print("O quadro de respostas é:")
    #quadro de respostas daqui
    print("A + + + + + + P ")
    print("+ B + + + + I O ")
    print("+ + M + + R + L ")
    print("+ + + U A + + I ")
    print("+ + + M T + + N ")
    print("+ + I + + + + + ")
    print("+ D + + + + + + ")
    print("E O T R E S E D ")
    print("")
    #até aqui
    #Pontuação-fácil####################################################################################################################################
    if pontuacao_facil >= 10530: #maximo
        print("PARABÉNS! Você fez a pontuação máxima de ",pontuacao_facil," no modo fácil! Você é um MESTRE SUPREMO DO MODO FÁCIL!")
    elif pontuacao_facil <= 7380: #minimo
        print("A sua pontuação no modo fácil foi a menor possível:",pontuacao_facil," .Você é um fracasso no modo fácil") #Fracasso deve estar meio forte. Mudar depois.
    elif pontuacao_facil >= 8955 and pontuacao_facil <10530: #entre metade e maximo
        print("A sua pontuação de ",pontuacao_facil," está entre a metade e o máximo! Você é um veterano do modo fácil!")
    elif pontuacao_facil > 7380 and pontuacao_facil < 8955:
        print("A sua pontuação de ",pontuacao_facil," está entre a metade e o mínimo. Você é um iniciante do modo fácil")
    print("Parabens, você chegou ao nível médio!!!.",
          "\nA senha para o acesso direto ao nível médio caso queira parar é: ma0k1",
          "\nGuarde ela bem")
    time.sleep(1)

    return n2()


#######################################################################################################################################################################33
def manual():
    print("")
    print("")
    print("")
    print("                             LOADING",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("")
    print("")
    print("")
    print("                         ---MANUAL---")
    print("")
    print("---SOBRE O JOGO---")
    print("")
    print("Bem vindo ao Word Hunters, o jogo da palavra-cruzada.\nSeu objetivo é acertar todas as palavras que tem na cruzadinha, priorizando as palavras maiores primeiro,\npois valerão mais pontos.")
    print("")
    print("---MODOS DE JOGO---")
    print("")
    print("Modo rápido (1 partida):")
    print("Modo onde será sorteado um caça-palavras (dos 8 criados além dos do modo carreira) para você fazer.\nNeste modo terão caça-palavras de dimensões 8x8 e 10x10.")
    print("Modo carreira (original):")
    print("5 caça-palavras com 3 dificuldades diferentes (fácil, médio e difícil) no qual o objetivos é apenas terminar o caça palavras.\nNesse modo de jogo existe o sistema de senhas por nível (fácil, médio, difícil), para que você não precise recomeçar o jogo caso queria parar.\nTerá dicas para ajudar o jogador")
    print("")
    print("OBS: As respostas nos dois modos devem ser escritas sem acentos e sem espaços (exs: saopaulo, lewishamilton.")
    print("")
    print("---MÉTODO DE PONTUAÇÃO---")
    print("")
    print("A pontuação será feita em base do tamanho da palavra encontrada, quanto maior a palavra mais pontos, e a palavra que for achada primeiro tem um multiplicador maior.\nPalavra mínima de 3 letras e palavra máxima com X letras.\nTente encontrar as maiores palavras primeiro, pois elas alem de valerem mais, o multiplicador de pontuação diminui a cada palavra encontrada")
    print("")
    print("")
    voltar=input("Digite qualquer coisa para voltar para o menu")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("                             RETORNANDO PARA O MENU",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("")
    print("")
    print("")
    return menu()












################################### MENU ################################################3

def menu():
    cont = 0
    print("        Word Hunters")
    print("----------------------------")
    print("|          MENU            |")
    print("|1- Novo Jogo              |",
          "\n|2- Carregar Jogo          |",
          "\n|3- Manual                 |")
    print("----------------------------")
    escolha=input("Escolha a opção desejada:")
    while escolha != "1" and escolha != "2" and escolha !="3":
        escolha=input("Opção Inválida!! Escolha a opção desejada:")
    if escolha == "1":
        print("")
        print("       MODOS DE JOGO")
        print("----------------------------")
        print("|1- Modo Clássico          |",
              "\n|2- Modo Rápido            |")
        print("----------------------------")
        escolha=input("Escolha a opção desejada:")
        while escolha != "1" and escolha != "2" and escolha != "3":
            escolha=input("Opção Inválida!! Escolha a opção desejada:")
        if escolha == "1":
            #Levar para o primeiro nivel do modo clássico com uma Função
            n1()

        elif escolha == "2":
            #Levar para o Modo Rápido com uma Função
            JR()
    elif escolha == "3":
            manual()

    elif escolha == "2":
        print("")
        print("        PASSWORD")
        print("")
        senha=input("Digite a senha do nível desejado:")
        #while cont <= 2:
        while senha != "ma0k1" and senha != "om1zv" and cont <=2:
            senha=input("Senha inválida!! Digite a senha do nível desejado:")
            cont += 1
        if senha == "ma0k1":
            #Função para ir pro nível médio
            n2() #Chama nível 2

        elif senha == "om1zv":
            n3() # Chama nível 3
        print()
        print("Você será levado de volta ao menu!")
        print()
        print("                             RETORNANDO PARA O MENU",end="")
        time.sleep(1)
        print(".",end="")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("")
        print("")
        print("")
        menu()
            #Função para ir pro nível difícil
    #OBS: Tirar os prints que eu coloquei para testar o código , ex: 1 , 2, médio, difícil

####################################################################################################################################



if 1 > 0:
    menu()
