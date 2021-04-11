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


def codage_de_lettre(lettre,cle):
	chiffre=caractère_en_chiffre(lettre)
	chiffrecode=(chiffre+cle)%26
	lettrecode= chiffre_en_caractère(chiffrecode)
	return(lettrecode)

def codage_de_mot(mot,cle):
        motcode=""
        L=len(mot)
        for i in range(0,L):
                lettre=mot[i]
                lettrecodee = codage_de_lettre(lettre,cle)
                motcode=motcode+lettrecodee
        return(motcode)

def codage_de_phrase(mot,cle):
        motcode=""
        L=len(mot)
        for i in range(0,L):
                lettre=mot[i]
                if lettre == " " or lettre == "'" :
                        lettrecodee = lettre
                else:
                        lettrecodee = codage_de_lettre(lettre,cle)
                motcode=motcode+lettrecodee
        return(motcode)


# ou full MAl ou NON FULL MINUSCULE NE PAS MELANGER MAJ ET MINUSCUlE

print("codage de mot = "+codage_de_mot("Insérer le mots a crypter",10)) #remplacer  ce qu'il y'a entre les "" par votre mots crypter

print("codage de phrase = "+codage_de_phrase("Insérer la phrase a crypter",15)) #remplacer  ce qu'il y'a entre les "" par votre mots crypter


