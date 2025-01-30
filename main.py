import string

alphabet = string.ascii_lowercase

cle = 3

mot = "LE petit chaperon rouge"

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