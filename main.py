import string

alphabet = string.ascii_lowercase

def lecture_fichier(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        texte = file.read()
    return texte

def dictionnaire(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        dictionnaire = set(word.strip().lower() for word in f.readlines())
        return dictionnaire

def fonction_chiffrage(cle, mot):
    texte_chiffre = ""

    for caractere in mot:
        if caractere in alphabet:
            index = alphabet.find(caractere)
            new_index = (index + cle)
            if new_index > 25 :
                new_index = new_index - 25
            elif new_index < 0 :
                new_index = new_index + 25
            new_character = alphabet[new_index]
        else:
            new_character = caractere

        texte_chiffre += new_character
    return texte_chiffre


def chiffrement_Cesar() :
    cle = int(input("Entrez la clé : ")) % 25
    interrogation()
    if input("Voulez-vous chiffrer ou déchiffrer ? (c/d): ") == 'c':

        print(fonction_chiffrage(cle,mot))
    else :
        print(fonction_chiffrage(-cle, mot))

def bruteforce() :
    interrogation()
    essais = []
    for i in range(25):
        phrase = fonction_chiffrage(i, mot)
        essais.append(phrase)
        print(f"Voici les essais de déchiffrage du texte fourni :\nclé essayée =[{i}] / résultat= {phrase}\n\n")

def interrogation():
    if input("Avez vous un fichier texte ou une phrase ? (t/p): ") == 't':
        titre_fichier = input("Entrez le nom du fichier : ")
        mot = lecture_fichier(titre_fichier)
        mot = mot.lower()
    else :
        mot = str(input("Entrez la phrase : "))
        mot = mot.lower()
    return (mot)


def menu() :
    choix = int(input("Veuillez choisir l'action que vous souhaitez réaliser :\n\n1 : Chiffrage / Déchiffrage de texte"
                      "\n2 : Méthode bruteforce pour retrouver la clé d'un texte chiffré\n\nChoix : "))
    if choix == 1 :
        chiffrement_Cesar()
    elif choix == 2 :
        bruteforce()
    else :
        menu()


menu()



