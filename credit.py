
def calculate_risk(income, debt, age):
    """Évalue le niveau de risque selon le ratio dette/revenu."""

    if income <= 0:
        raise ValueError("Le revenu doit être strictement positif.")

    if debt < 0:
        raise ValueError("La dette ne peut pas être négative.")

    if age < 18:
        raise ValueError("L'âge doit être supérieur ou égal à 18 ans.")

    ratio = debt / income

    if ratio > 0.6:
        return "HIGH"
    elif ratio > 0.3:
        return "MEDIUM"
    else:
        return "LOW"
