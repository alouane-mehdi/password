
def check_password_strength(password):
    # Vérifie si le mot de passe respecte les exigences de sécurité
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in "!@#$%^&*" for char in password):
        return False
    return True

def main():
    while True:
        # Demande à l'utilisateur de choisir un mot de passe
        password = input("Choisissez un mot de passe : ")

        # Vérifie si le mot de passe respecte les exigences de sécurité
        if check_password_strength(password):
            print("Mot de passe valide. Merci!")
            break
        else:
            print("Le mot de passe ne respecte pas les exigences de sécurité.")
            print("Assurez-vous qu'il contient au moins 8 caractères, une majuscule, une minuscule, un chiffre, et un caractère spécial.")

if __name__ == "__main__":
    main()

    
   
            