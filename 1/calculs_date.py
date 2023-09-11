from datetime import date
from anneeBissextile import est_bissextile
def saisie_date_naissance() -> date:
    """
    Saisit la date de naissance depuis l'utilisateur.

    :return: Un objet date représentant la date de naissance.
    """
    try:
        day = int(input("Entrez votre jour de naissance, exemple : 19: "))
        month = int(input("Entrez votre mois de naissance exemple : 09: "))
        year = int(input("Entrez votre année de naissance exemple: 2003: "))
        my_birthday = date(year, month, day)
        return my_birthday
    except ValueError:
        print("Date de naissance invalide.")
        return None

def age(date_naissance: date) -> int:
    """
    Calcule l'âge en années à partir de la date de naissance.

    :param date_naissance: La date de naissance.
    :return: L'âge en années.
    """
    aujourdhui = date.today()
    return aujourdhui.year - date_naissance.year

def est_majeur(date_naissance: date) -> bool:
    """
    Vérifie si une personne est majeure à partir de sa date de naissance.

    :param date_naissance: La date de naissance.
    :return: True si la personne est majeure, False sinon.
    """
    age_personne = age(date_naissance)
    return age_personne >= 18

def test_acces() -> str:
    """
    Teste l'accès en fonction de l'âge.

    :return: Un message indiquant si l'accès est autorisé ou non.
    """
    date_de_naissance = saisie_date_naissance()
    if date_de_naissance:
        if est_majeur(date_de_naissance):
            return f"Bonjour, vous avez {age(date_de_naissance)} ans, Accès autorisé"
        else:
            return f"Désolé, vous avez {age(date_de_naissance)} ans, Accès interdit"
    else:
        return "Date de naissance invalide."

print(test_acces())