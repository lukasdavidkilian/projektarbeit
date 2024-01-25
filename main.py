from openpyxl import Workbook
import time

# Importieren der beiden Algorithmen-Funktionen
from generate_meal_plans import generate_meal_plans  # Bisheriger Algorithmus

# Angenommen, Sie haben mehrere Ernährungssets importiert
from food_sets import nutrition_set_standard, nutrition_set_lukas

# Alle Ihre Lebensmittellisten
food_lists = {
    "Standard": nutrition_set_standard,
    "Lukas": nutrition_set_lukas
}

# Liste der Zielsets
goal_sets = [
    [250, 65, 300],
    [160, 80, 140],
    [400, 150, 600],
    [200, 75, 220],
]

def main():
    # Erstellen eines neuen Arbeitsbuchs für die Ergebnisse
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Ergebnisse"
    # Hinzufügen der Spalten für die Anzahl der Lebensmittel und für jedes Makronährstoffziel
    sheet.append([
        "Food Set",
        "Anzahl Lebensmittel in der Liste",
        "Protein Ziel",
        "Fett Ziel",
        "Kohlenhydrate Ziel",
        "Dauer (Millisekunden)",
        "Counter",
        "Plan gefunden"
    ])

    # Durchlaufen aller Kombinationen von Lebensmittelsets und Zielsets
    for food_set_name, food_set in food_lists.items():
        food_set_count = len(food_set)  # Anzahl der Lebensmittel in der Liste
        for goal in goal_sets:
            start_time = time.time()
            meal_plan, counter = generate_meal_plans(food_set, goal)
            end_time = time.time()
            duration = (end_time - start_time) * 1000  # Umwandlung von Sekunden in Millisekunden

            # Überprüfen, ob ein Mahlzeitenplan gefunden wurde
            plan_found = "Ja" if meal_plan else "Nein"

            # Speichern der Ergebnisse im Arbeitsbuch
            sheet.append([
                food_set_name,
                food_set_count,
                goal[0],  # Protein Ziel
                goal[1],  # Fett Ziel
                goal[2],  # Kohlenhydrate Ziel
                duration,
                counter,
                plan_found
            ])

            # Optional: Ausgabe der Ergebnisse
            print(
                f"Food Set: {food_set_name}, "
                f"Anzahl Lebensmittel in der Liste: {food_set_count}, "
                f"Protein Ziel: {goal[0]}, "
                f"Fett Ziel: {goal[1]}, "
                f"Kohlenhydrate Ziel: {goal[2]}, "
                f"Dauer: {duration:.2f} Millisekunden, "
                f"Counter: {counter}, "
                f"Plan gefunden: {plan_found}"
            )

    # Speichern des Arbeitsbuchs
    workbook.save("Ergebnisse.xlsx")

# Führen Sie die Hauptfunktion aus
if __name__ == "__main__":
    main()
