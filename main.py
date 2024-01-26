from openpyxl import Workbook
import time

# Importieren der Algorithmen-Funktionen
from generate_meal_plans import generate_meal_plans  # Bisheriger Algorithmus
from optimized_generate_meal_plans import optimized_generate_meal_plans  # Neuer Algorithmus

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
    [1, 75, 220],
]

def main():
    # Erstellen eines neuen Arbeitsbuchs für die Ergebnisse
    workbook = Workbook()
    sheet1 = workbook.create_sheet(title="Ergebnisse Algo 1")
    sheet2 = workbook.create_sheet(title="Ergebnisse Algo 2")

    # Hinzufügen der Spaltenüberschriften
    headers = [
        "Food Set", "Anzahl Lebensmittel in der Liste", "Protein Ziel", "Fett Ziel",
        "Kohlenhydrate Ziel", "Dauer (ms)", "Counter", "Plan gefunden"
    ]
    sheet1.append(headers)
    sheet2.append(headers)

    # Durchlaufen aller Kombinationen von Lebensmittelsets und Zielsets
    for food_set_name, food_set in food_lists.items():
        food_set_count = len(food_set)  # Anzahl der Lebensmittel in der Liste
        for goal in goal_sets:
            # Testen des bisherigen Algorithmus
            start_time = time.time()
            meal_plan_1, counter_1 = generate_meal_plans(food_set, goal)
            duration_1 = (time.time() - start_time) * 1000
            plan_found_1 = "Ja" if meal_plan_1 else "Nein"
            # Speichern der Ergebnisse im Arbeitsbuch für Algo 1
            row = [food_set_name, food_set_count, goal[0], goal[1], goal[2], duration_1, counter_1, plan_found_1]
            sheet1.append(row)

            # Testen des neuen Algorithmus
            start_time = time.time()
            #meal_plan_2, counter_2 = optimized_generate_meal_plans(food_set, goal)
            results = optimized_generate_meal_plans(food_set, goal)
            if results is not None:
                meal_plan_2 = results[0]
                counter_2 = results[1]
            else:
                meal_plan_2 = None
                counter_2 = 9999
            duration_2 = (time.time() - start_time) * 1000
            plan_found_2 = "Ja" if meal_plan_2 else "Nein"
            # Speichern der Ergebnisse im Arbeitsbuch für Algo 2
            row = [food_set_name, food_set_count, goal[0], goal[1], goal[2], duration_2, counter_2, plan_found_2]
            sheet2.append(row)

    # Löschen des leeren ersten Sheets, das automatisch erstellt wird
    del workbook['Sheet']
    # Speichern des Arbeitsbuchs
    workbook.save("Ergebnisse.xlsx")

# Führen Sie die Hauptfunktion aus
if __name__ == "__main__":
    main()
