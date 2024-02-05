import random
from meal_plan import MealPlan


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


def increase_recommended_amounts(food_list):
    for food in food_list:
        if len(food.recommended_amounts) > 1:
            difference = food.recommended_amounts[1] - food.recommended_amounts[0]
            food.recommended_amounts.append(food.recommended_amounts[-1] + difference)
            food.recommended_amounts.pop[0]
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
        return "Das Proteinziel kann nicht erreicht werden."

    if fat < fat_goal:
        return "Das Fettziel kann nicht erreicht werden."

    if carbs < carb_goal:
        return "Das Kohlenhydrateziel kann nicht erreicht werden."

    return True


def iterative_selection(food_list, meal_plan: MealPlan):
    tolerance = {'protein': 10, 'fat': 10, 'carbs': 10}
    best_score = float('inf')
    best_plan = meal_plan

    for _ in range(50000):
        chosen_method = random.choice([insert_food, delete_food, swap_food])
        temp_plan: MealPlan = chosen_method(food_list, meal_plan)

        current_score = calculate_deviation(temp_plan)

        if best_score < current_score:
            best_score = current_score
            best_plan = temp_plan

        if best_plan.is_within_tolerance():
            print(_)
            return best_plan, _

    print(_)
    return None, _


def insert_food(food_list, meal_plan: MealPlan):
    available_foods = [food for food in food_list if food.name not in meal_plan.amounts_dictionary]

    if available_foods:
        food_to_add = random.choice(available_foods)
        recommended_amount = random.choice(food_to_add.recommended_amounts)

        current_score = calculate_deviation(meal_plan)

        meal_plan.add_food(food_to_add, recommended_amount)

        new_plan = MealPlan(meal_plan.food, meal_plan.protein_goal, meal_plan.fat_goal, meal_plan.carbohydrate_goal,
                            meal_plan.amounts_dictionary)
        new_score = calculate_deviation(new_plan)

        if new_score > current_score:
            meal_plan.remove_food(food_to_add)

    meal_plan_after_insertion = MealPlan(meal_plan.food, meal_plan.protein_goal, meal_plan.fat_goal,
                                         meal_plan.carbohydrate_goal, meal_plan.amounts_dictionary)
    return meal_plan_after_insertion


def delete_food(food_list, meal_plan: MealPlan):
    if meal_plan.food:
        food_to_remove = random.choice(meal_plan.food)

        if food_to_remove.name in meal_plan.amounts_dictionary:
            amount_to_remove = meal_plan.amounts_dictionary[food_to_remove.name]

            current_score = calculate_deviation(meal_plan)

            meal_plan.remove_food(food_to_remove)

            new_score = calculate_deviation(meal_plan)

            if new_score < current_score:
                meal_plan.add_food(food_to_remove, amount_to_remove)

    meal_plan_after_deletion = MealPlan(meal_plan.food, meal_plan.protein_goal, meal_plan.fat_goal,
                                        meal_plan.carbohydrate_goal, meal_plan.amounts_dictionary)
    return meal_plan_after_deletion


def swap_food(food_list, meal_plan: MealPlan):
    if len(meal_plan.food) < 2:
        return meal_plan

    current_score = calculate_deviation(meal_plan)

    food_to_remove = random.choice(meal_plan.food)
    amount_to_remove = meal_plan.amounts_dictionary[food_to_remove.name]

    meal_plan.remove_food(food_to_remove)

    available_foods = [food for food in food_list if
                       food.name not in meal_plan.amounts_dictionary and food != food_to_remove]

    if not available_foods:
        return meal_plan

    food_to_add = random.choice(available_foods)
    recommended_amount = random.choice(food_to_add.recommended_amounts)

    meal_plan.add_food(food_to_add, recommended_amount)

    temp_plan = MealPlan(meal_plan.food, meal_plan.protein_goal, meal_plan.fat_goal, meal_plan.carbohydrate_goal,
                         meal_plan.amounts_dictionary)
    new_score = calculate_deviation(temp_plan)

    if new_score < current_score:
        meal_plan.remove_food(food_to_add)
        meal_plan.add_food(food_to_remove, amount_to_remove)

    return meal_plan


def calculate_deviation(meal_plan: MealPlan):
    protein_deviation = abs(meal_plan.protein - meal_plan.protein_goal)
    fat_deviation = abs(meal_plan.fat - meal_plan.fat_goal)
    carbs_deviation = abs(meal_plan.carbs - meal_plan.carbohydrate_goal)
    total_deviation = protein_deviation + fat_deviation * 2.3 + carbs_deviation

    return total_deviation


def optimized_generate_meal_plans(food_list, goals):
    max_attempts = 5
    attempt = 0

    while attempt < max_attempts:
        try:
            validate(food_list, goals)
            print("Validierung erfolgreich. Fahre fort mit der Erstellung des Mahlzeitplans...")
            break
        except ValidationError as e:
            attempt += 1
            print(f"Validierungsfehler bei Versuch {attempt}: {e} - Versuche, empfohlene Mengen zu erhöhen.")
            food_list = increase_recommended_amounts(food_list)

            if attempt == max_attempts:
                print(f"Erneuter Validierungsfehler nach {max_attempts} Versuchen: {e}")
                return None, 0

    meal_plan = MealPlan([], goals[0], goals[1], goals[2], {})

    result = iterative_selection(food_list, meal_plan)

    if result[0] is not None and result[0].is_within_tolerance():
        unsorted_plan = result[0]
        counter = result[1]
        sorted_plan = unsorted_plan.sort()
        print(sorted_plan)
        return sorted_plan, counter

    counter = result[1]
    return None, counter
