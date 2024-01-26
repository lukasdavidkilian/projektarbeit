import random
from meal_plan import MealPlan

from food_sets import nutrition_set_lukas

"""
def initial_selection(food_list, goals):
    initial_selection = []
    recommended_amounts = {}
    current_calories = 0
    target_calories = (goals[0] * 4.1 + goals[1] * 9.3 + goals[2] * 4.1) * 0.2

    # TODO: ADD CHECK, IF INITIAL SELECTION ONLY IS LIKE X% OF GOAL

    while current_calories < target_calories:
        food = random.choice(food_list)
        amount = random.choice(food.recommended_amounts)

        if food not in initial_selection:
            initial_selection.append(food)
            recommended_amounts[food.name] = amount

            current_calories += calculate_calories(food, amount)

            if current_calories >= target_calories:
                break

    meal_plan = MealPlan(initial_selection, goals[0], goals[1], goals[2], recommended_amounts)
     return meal_plan
     
     
def calculate_calories(food, amount):
    calories_from_protein = food.protein * amount * 4.1
    calories_from_fat = food.fat * amount * 9.3
    calories_from_carbs = food.carbs * amount * 4.1

    calories = calories_from_protein + calories_from_fat + calories_from_carbs

    return calories
"""


class ValidationError(Exception):
    pass


def validate(food_list, goals):
    protein_goal, fat_goal, carb_goal = goals

    if len(food_list) < 3:
        raise ValidationError("Die Lebensmittelliste muss mindestens 3 Lebensmittel enthalten.")

    if protein_goal < 50:
        raise ValidationError("Das Proteinziel muss mindestens 50g sein.")

    if fat_goal < 30:
        raise ValidationError("Das Fettziel muss mindestens 30g sein.")

    if carb_goal <= 0:
        raise ValidationError("Das Kohlenhydrateziel darf nicht negativ sein.")

    if not goals_are_reachable(food_list, goals):
        raise ValidationError("Die Ziele sind mit dieser Lebensmittelliste nicht erreichbar.")

    return True

    # TODO: Check einfügen, Nutrition Density darf nicht über den Zielen liegen, also 1 Lebensmittel darf nicht schon das Ziel erreich, ggf. müssen mindestens mehrere Lebensmittel eine Density von 1/3 oder so dann haben


def increase_recommended_amounts(food_list):
    for food in food_list:
        if len(food.recommended_amounts) > 1:
            difference = food.recommended_amounts[1] - food.recommended_amounts[0]
            food.recommended_amounts.append(food.recommended_amounts[-1] + difference)
        else:
            pass

    return food_list


def goals_are_reachable(food_list, goals):
    protein_goal, fat_goal, carb_goal = goals

    protein = 0
    fat = 0
    carbs = 0

    for food in food_list:
        highest_food_amount = max(food.recommended_amounts)

        protein += food.protein * highest_food_amount
        fat += food.fat * highest_food_amount
        carbs += food.carbs * highest_food_amount

    if protein < protein_goal:
        print("Das Proteinziel kann nicht erreicht werden. ({}/{})".format(protein, protein_goal))  # entfernen
        return "Das Proteinziel kann nicht erreicht werden. ({}/{})".format(protein, protein_goal)

    if fat < fat_goal:
        return "Das Fettziel kann nicht erreicht werden."

    if carbs < carb_goal:
        return "Das Kohlenhydrateziel kann nicht erreicht werden."

    return True


def iterative_selection(food_list, meal_plan: MealPlan):
    tolerance = {'protein': 10, 'fat': 10, 'carbs': 10}
    best_score = float('inf')
    best_plan = meal_plan

    for _ in range(10000):  # Adjust the number of iterations as needed
        chosen_method = random.choice([insert_food, delete_food, swap_food])
        temp_plan: MealPlan = chosen_method(food_list, meal_plan)

        current_score = calculate_deviation(temp_plan)

        if best_score < current_score:
            best_score = current_score
            best_plan = temp_plan

        if is_within_tolerance(best_plan, tolerance):
            print(_)
            return best_plan

    print(_)
    return None


def insert_food(food_list, meal_plan: MealPlan):
    available_foods = [food for food in food_list if food.name not in meal_plan.amounts_dictionary]

    if available_foods:
        food_to_add = random.choice(available_foods)
        recommended_amount = random.choice(food_to_add.recommended_amounts)

        current_score = calculate_deviation(meal_plan)

        # Temporarily add the food to the meal plan
        meal_plan.add_food(food_to_add, recommended_amount)

        # Calculate the score before and after addition
        new_plan = MealPlan(meal_plan.food, meal_plan.protein_goal, meal_plan.fat_goal, meal_plan.carbohydrate_goal,
                            meal_plan.amounts_dictionary)
        new_score = calculate_deviation(new_plan)

        # Revert changes if the score did not improve
        if new_score > current_score:
            meal_plan.remove_food(food_to_add)

    meal_plan_after_insertion = MealPlan(meal_plan.food, meal_plan.protein_goal, meal_plan.fat_goal,
                                         meal_plan.carbohydrate_goal, meal_plan.amounts_dictionary)
    return meal_plan_after_insertion


def delete_food(food_list, meal_plan: MealPlan):
    if meal_plan.food:  # Ensure there are foods to remove
        food_to_remove = random.choice(meal_plan.food)

        if food_to_remove.name in meal_plan.amounts_dictionary:  # Check if the food is in the amounts dictionary
            amount_to_remove = meal_plan.amounts_dictionary[food_to_remove.name]

            # Calculate the current score
            current_score = calculate_deviation(meal_plan)

            # Remove the food temporarily
            meal_plan.remove_food(food_to_remove)

            # Calculate the score after removal
            new_score = calculate_deviation(meal_plan)

            # Check if the score improved, if not, add the food back
            if new_score < current_score:
                meal_plan.add_food(food_to_remove, amount_to_remove)

    meal_plan_after_deletion = MealPlan(meal_plan.food, meal_plan.protein_goal, meal_plan.fat_goal,
                                        meal_plan.carbohydrate_goal, meal_plan.amounts_dictionary)
    return meal_plan_after_deletion


def swap_food(food_list, meal_plan: MealPlan):
    if len(meal_plan.food) < 2:
        return meal_plan

    current_score = calculate_deviation(meal_plan)

    # Select a food to remove
    food_to_remove = random.choice(meal_plan.food)
    amount_to_remove = meal_plan.amounts_dictionary[food_to_remove.name]

    # Remove the selected food temporarily
    meal_plan.remove_food(food_to_remove)

    # Select a food to add
    available_foods = [food for food in food_list if
                       food.name not in meal_plan.amounts_dictionary and food != food_to_remove]
    if not available_foods:
        return meal_plan

    food_to_add = random.choice(available_foods)
    recommended_amount = random.choice(food_to_add.recommended_amounts)

    # Add the selected food temporarily
    meal_plan.add_food(food_to_add, recommended_amount)

    # Create a temporary meal plan to calculate new score
    temp_plan = MealPlan(meal_plan.food, meal_plan.protein_goal, meal_plan.fat_goal, meal_plan.carbohydrate_goal,
                         meal_plan.amounts_dictionary)
    new_score = calculate_deviation(temp_plan)

    # Check if the swap improved the score
    if new_score < current_score:
        # Revert the swap if it didn't improve the score
        meal_plan.remove_food(food_to_add)
        meal_plan.add_food(food_to_remove, amount_to_remove)

    return meal_plan


def calculate_deviation(meal_plan: MealPlan):
    protein_deviation = abs(meal_plan.protein - meal_plan.protein_goal)
    fat_deviation = abs(meal_plan.fat - meal_plan.fat_goal)
    carbs_deviation = abs(meal_plan.carbs - meal_plan.carbohydrate_goal)
    total_deviation = protein_deviation + fat_deviation * 2.3 + carbs_deviation

    # TODO: Vielleicht kann man hier einbauen, dass die Abweichung gewichtet wird in Hinblick auf die Nähe zu den Zielen

    return total_deviation


def is_within_tolerance(meal_plan, tolerance):
    return (abs(meal_plan.protein - meal_plan.protein_goal) <= tolerance['protein'] and
            abs(meal_plan.fat - meal_plan.fat_goal) <= tolerance['fat'] and
            abs(meal_plan.carbs - meal_plan.carbohydrate_goal) <= tolerance['carbs'])


def optimized_generate_meal_plans(food_list, goals):
    print("")
    print("\nTest neuer Algorithmus:")

    try:
        validate(food_list, goals)
    except ValidationError as e:
        print(f"Validierungsfehler: {e} - Versuche, empfohlene Mengen zu erhöhen.")
        food_list = increase_recommended_amounts(food_list)
        try:
            validate(food_list, goals)
        except ValidationError as e:
            print(f"Erneuter Validierungsfehler nach Erhöhung der Mengen: {e}")
            return None
    print("Validierung erfolgreich. Fahre fort mit der Erstellung des Mahlzeitplans...")

    print("")
    meal_plan = MealPlan([], goals[0], goals[1], goals[2], {})
    print("So sieht die iterative Selektion aus: ")

    unsorted_plan = iterative_selection(food_list, meal_plan)

    tolerance = {'protein': 10, 'fat': 10, 'carbs': 10}
    if unsorted_plan is not None and is_within_tolerance(unsorted_plan, tolerance):
        sorted_plan = unsorted_plan.sort()
        print(sorted_plan)
        return sorted_plan

    return None


# TODO: ggf. könnte man hier einfügen, dass man die iterative Selektion bspw. bis zu 5x durchläuft oder erneut sollte der erste Durchgang keinen optimalen Plan ergeben haben

goals = [200, 75, 220]
optimized_generate_meal_plans(nutrition_set_lukas, goals)
