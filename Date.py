from datetime import datetime, timedelta

# Fonction pour générer les dates des mardis et vendredis dans une plage donnée
def get_euromillions_dates(start_date, end_date):
    # Initialisation de la liste des résultats
    result = []

    # Conversion des dates au format datetime
    current_date = start_date
    end_date = end_date

    # Boucle pour parcourir toutes les dates entre start_date et end_date
    while current_date <= end_date:
        # Ajouter la date à la liste si c'est un mardi (1) ou vendredi (4)
        if current_date.weekday() in [1, 4]:  # 1: Mardi, 4: Vendredi
            result.append(current_date.strftime('%d/%m/%Y :'))

        # Passer à la date suivante
        current_date += timedelta(days=1)

    return result

# Définir la plage de dates
start_date = datetime(2025, 1, 1)  # 01/01/2025
end_date = datetime(2029, 12, 31)  # 31/12/2029

# Obtenir les dates
dates = get_euromillions_dates(start_date, end_date)

# Afficher les résultats
for date in dates:
    print(date)
