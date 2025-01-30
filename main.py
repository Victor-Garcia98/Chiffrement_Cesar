import string 

cle = 3

mot = "LE petit chaperon rouge"


def dechiffrer_texte(mot,cle):
    nouveau_mot=''
    for char in mot:
        if char in alphabet:
            modif = alphabet.find(char) + cle
            lettre = alphabet[modif]
            nouveau_mot = nouveau_mot + lettre
        else :
            nouveau_mot = nouveau_mot + char

    return nouveau_mot

mot_minuscule = mot.lower()

print(mot_minuscule)


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

print(fonction_chiffrage(cle,mot_minuscule))


def lecture_fichier(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        texte = file.read()
    return texte

