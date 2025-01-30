import string

alphabet = string.ascii_lowercase



cle = 3



mot = "LE petit chaperon rouge"

mot_minuscule = mot.lower()



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
        #mot = lecture_fichier(titre_fichier)
    else :
        mot = str(input("Entrez la phrase : "))
    if input("Voulez-vous chiffrer ou déchiffrer ? (c/d): ") == 'c':

        print(fonction_chiffrage(cle,mot))
    else :
        print(fonction_chiffrage(-cle, mot))

chiffrement_Cesar()


