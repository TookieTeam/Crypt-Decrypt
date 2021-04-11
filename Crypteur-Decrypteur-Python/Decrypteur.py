######## Fonctions données pour la partie machine##########
Alphabet = "abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def chiffre_en_caractère(chiffre):
	lettre=Alphabet[chiffre]
	return(lettre)

def caractère_en_chiffre(lettre):
        chiffre=0
        while (Alphabet[chiffre]!= lettre):
                chiffre=chiffre+1
        return(chiffre)


def decodage_de_lettre(lettrecodee,cle):
	chiffrecode=caractère_en_chiffre(lettrecodee)
	chiffre=(chiffrecode-cle)%26
	lettre= chiffre_en_caractère(chiffre)
	return(lettre)

def decodage_de_mot(mot,cle):
        motdecode=""
        L=len(mot)
        for i in range(0,L):
                lettre=mot[i]
                lettredecodee = decodage_de_lettre(lettre,cle)
                motdecode=motdecode+lettredecodee
        return(motdecode)

def decodage_de_phrase(mot,cle):
        motcode=""
        L=len(mot)
        for i in range(0,L):
                lettre=mot[i]
                if lettre == " " or lettre == "'" :
                        lettrecodee = lettre
                else:
                        lettrecodee = decodage_de_lettre(lettre,cle)
                motcode=motcode+lettrecodee
        return(motcode)


print("decodage de mot = "+decodage_de_mot("insérer le mot codée ici",10)) # remplacer  ce qu'il y'a entre les "" par votre mots crypter

print("decodage de phrase = "+decodage_de_phrase("insérer la phrase codée ici",15)) #remplacer  ce qu'il y'a entre les "" par votre phrase crypter

