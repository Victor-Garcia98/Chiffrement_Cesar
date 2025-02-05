import string

alphabet = string.ascii_lowercase

def lecture_fichier(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        texte = file.read()
    return texte


def fonction_chiffrage(cle, mot):
    texte_chiffre = ""

    for caractere in mot:
        if caractere in alphabet:
            index = alphabet.find(caractere)
            new_character = alphabet[(index + cle)]
        else:
            new_character = caractere

        texte_chiffre += new_character
    return texte_chiffre


def chiffrement_Cesar() :
    cle = int(input("Entrez la clé : "))
    if input("Avez vous un fichier texte ou une phrase ? (t/p): ") == 't':
        titre_fichier = input("Entrez le nom du fichier : ")
        mot = lecture_fichier(titre_fichier)
        mot = mot.lower()
    else :
        mot = str(input("Entrez la phrase : "))
        mot = mot.lower()
    if input("Voulez-vous chiffrer ou déchiffrer ? (c/d): ") == 'c':

        print(fonction_chiffrage(cle,mot))
    else :
        print(fonction_chiffrage(-cle, mot))

def menu() :
    choix = int(input("Veuillez choisir l'action que vous souhaitez réaliser :\n\n1 : Chiffrage / Déchiffrage de texte"
                      "\n2 : Méthode bruteforce pour retrouver la clé d'un texte chiffré\n\nChoix : "))
    if choix == 1 :
        chiffrement_Cesar()
    elif choix == 2 :
        placeholder = True
        ## bruteforce()
    else :
        menu()


menu()




