from time import sleep
from playsound import playsound
from random import choice

lista_notas = ["nota1.mp3", "nota2.mp3", "nota3.mp3", "nota4.mp3", "nota5.mp3", "nota6.mp3", "nota7.mp3"]

dict_notas = {"nota1.mp3": "c", 
              "nota2.mp3": "d", 
              "nota3.mp3": "e", 
              "nota4.mp3": "f", 
              "nota5.mp3": "g", 
              "nota6.mp3": "a", 
              "nota7.mp3": "b"}

lista_acordes = [["do_M.mp3", "re_M.mp3", "mi_M.mp3", "fa_M.mp3", "sol_M.mp3", "la_M.mp3", "si_M.mp3"], 
                 ["do_me.mp3", "re_me.mp3", "mi_me.mp3", "fa_me.mp3", "sol_me.mp3", "la_me.mp3", "si_me.mp3"]]
                 
dict_acordes = {"do_M.mp3": "C", "re_M.mp3": "D", "mi_M.mp3": "E","fa_M.mp3": "F",
                "sol_M.mp3": "G", "la_M.mp3": "A", "si_M.mp3": "B","do_me.mp3": "Cm", "re_me.mp3": "Dm", 
                "mi_me.mp3": "Em", "fa_me.mp3": "Fm", "sol_me.mp3": "Gm", "la_me.mp3": "Am", "si_me.mp3": "Bm"}

def main():
    # Tela de menu com opções de notas ou acordes
    menu()
    # Seleciona o modo de acordo com a opção
    if validar_opcao() == 1:
        print(nota())
    else:
        print(acorde())

def nota():
    # Se for escolhido notas
    print("3")
    sleep(0.8)
    print("2")
    sleep(0.8)
    print("1")
    sleep(0.8)
    # Toca a nota depois da contagem
    nota = choice(lista_notas)
    playsound(f"notas\\{nota}")
    # Pergunta se precisa repetir
    again = "y"
    while again == "y":
        again = input("Hear again? (y/n) ").lower()
        if again == "y":
            playsound(f"notas\\{nota}")
    # Analisa a resposta
    guess = input("Your guess: ").lower()
    if dict_notas[nota] == guess:
        return "Correct!"
    return f"No! That's {dict_notas[nota].upper()}"


def acorde():
    # Se for escolhido acordes
    print("3")
    sleep(0.8)
    print("2")
    sleep(0.8)
    print("1")
    sleep(0.8)
    # Toca o acorde depois da contagem
    acorde = choice(choice(lista_acordes))
    playsound(f"acordes\\{acorde}")
    # Pergunta se precisa repetir
    again = "y"
    while again == "y":
        again = input("Hear again? (y/n) ").lower()
        if again == "y":
            playsound(f"acordes\\{acorde}")
    # Analisa a resposta
    guess = input("Your guess: ")
    if dict_acordes[acorde] == guess:
        return "Correct!"
    return f"No! That's {dict_acordes[acorde]}"

def menu():
    # Interface do menu inicial
    print("=================================")
    print("          PERFECT PITCH          ")
    print("=================================")
    print("What do you want to practice?")
    print("1 - NOTES")
    print("2 - CHORDS")
    print("=================================")

def validar_opcao():
    # Recebe a opção e valida ela
    while True:
        try:
            opcao = int(input("Option: "))
            while opcao != 1 and opcao != 2:
                print("ErrorMessage: Only 1 or 2!")
                opcao = int(input("Option: "))
        except ValueError:
            print("ErrorMessage: Select a number!")
        else:
            return opcao


if __name__=="__main__":
    main()