def lire_fichier_texte(nom_fichier):
    with open(nom_fichier, 'r') as f:
        contenu = f.read()
    return contenu

def lire_premieres_lignes(nom_fichier, n):
    with open(nom_fichier, 'r') as f:
        lignes = f.readlines()
    premieres_lignes = lignes[:n]
    return premieres_lignes

def lire_dernieres_lignes(nom_fichier, n):
    with open(nom_fichier, 'r') as f:
        lignes = f.readlines()
    dernieres_lignes = lignes[-n:]
    return dernieres_lignes

def compter_mots(nom_fichier):
    with open(nom_fichier, 'r') as f:
        contenu = f.read()
    mots = contenu.split()
    nombre_mots = len(mots)
    return nombre_mots