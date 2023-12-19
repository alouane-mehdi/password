import re
import hashlib

def verifier_mot_de_passe(mot_de_passe):
    if len(mot_de_passe) < 8:
        return False
    elif not re.search("[a-z]", mot_de_passe):
        return False
    elif not re.search("[A-Z]", mot_de_passe):
        return False
    elif not re.search("[0-9]", mot_de_passe):
        return False
    elif not re.search("[!,@,#,$,%,^,&,*,?]", mot_de_passe):
        return False
    else:
        return True

def crypter_mot_de_passe(mot_de_passe):
    return hashlib.sha256(mot_de_passe.encode()).hexdigest()

def demander_mot_de_passe():
    while True:
        mot_de_passe = input("Veuillez choisir un mot de passe : ")
        if verifier_mot_de_passe(mot_de_passe):
            mot_de_passe_crypte = crypter_mot_de_passe(mot_de_passe)
            print("Votre mot de passe est valide et a été crypté avec succès.")
            print("Mot de passe crypté : ", mot_de_passe_crypte)
            break
        else:
            print("Votre mot de passe n'est pas valide. Veuillez réessayer.")

demander_mot_de_passe()
