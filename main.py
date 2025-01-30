
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


