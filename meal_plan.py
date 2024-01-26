meal_plans = []


class MealPlan:
    food: []
    protein_goal: int
    fat_goal: int
    carbohydrate_goal: int
    dict: {}
    protein: int
    fat: int
    carbs: int

    def __init__(self, food, protein_goal, fat_goal, carbohydrate_goal, amounts_dictionary):
        self.amounts_dictionary = amounts_dictionary
        self.food = food
        #self.food = sorted(food, key=lambda item: item.protein * self.amounts_dictionary[item.name], reverse=True)
        self.protein_goal = protein_goal
        self.fat_goal = fat_goal
        self.carbohydrate_goal = carbohydrate_goal
        self.protein = sum(food.protein * self.amounts_dictionary[food.name] for food in self.food)
        self.fat = sum(food.fat * self.amounts_dictionary[food.name] for food in self.food)
        self.carbs = sum(food.carbs * self.amounts_dictionary[food.name] for food in self.food)
        meal_plans.append(self)
        #print(self)



    def __str__(self):
        # Initialize a string for the meal plan
        meal_plan_str = ""

        # Calculate the maximum length of the food names and units
        # (to determine the width of the columns in the table)
        max_name_length = max(len(food.name) for food in self.food)
        max_unit_length = max(len(food.unit) for food in self.food)

        # Loop over the foods in the meal plan
        for food in self.food:
            # Calculate the daily amount of the food
            daily_amount = food.amount * self.amounts_dictionary[food.name]

            # Format the food and its daily amount as a row in the table
            meal_plan_str += (
                f"{daily_amount:>5.0f} {food.unit:<{max_unit_length}} "
                f"{food.name:<{max_name_length}}\n"
            )

        protein = 0
        fat = 0
        carbs = 0

        for food in self.food:
            protein += food.protein * self.amounts_dictionary[food.name]
            fat += food.fat * self.amounts_dictionary[food.name]
            carbs += food.carbs * self.amounts_dictionary[food.name]

        # Format the goals and totals for the macro nutrients
        macro_str = (
            "IST  : P {:3.0f}g F {:3.0f}g C {:3.0f}g\n"
            "SOLL : P {:3.0f}g F {:3.0f}g C {:3.0f}g\n"
            "I/S  : P {:3.0%} F {:3.0%} C {:3.0%}"
        ).format(
            protein, fat, carbs,
            self.protein_goal, self.fat_goal, self.carbohydrate_goal,
            protein / self.protein_goal, fat / self.fat_goal, carbs / self.carbohydrate_goal
        )

        # Return the meal plan string and macro nutrient string
        return f"\n{meal_plan_str}\n{macro_str}\n"

    def update_macros(self):
        self.protein = 0
        self.fat = 0
        self.carbs = 0

        for food in self.food:
            amount = self.amounts_dictionary[food.name]
            self.protein += food.protein * amount
            self.fat += food.fat * amount
            self.carbs += food.carbs * amount

    def add_food(self, food, amount):
        if food not in self.food and food.name not in self.amounts_dictionary:
            self.food.append(food)
            self.amounts_dictionary[food.name] = amount
            self.update_macros
        else:
            print(f"{food.name} is already in the meal plan.")

    def remove_food(self, food):
        if food in self.food:
            self.food.remove(food)
            del self.amounts_dictionary[food.name]
            self.update_macros()
        else:
            print(f"{food.name} not found in the meal plan.")

    def is_within_tolerance(self):
        tolerance = {'protein': 10, 'fat': 10, 'carbs': 10}
        protein_deviation = abs(self.protein - self.protein_goal)
        fat_deviation = abs(self.fat - self.fat_goal)
        carbs_deviation = abs(self.carbs - self.carbohydrate_goal)

        return protein_deviation <= tolerance['protein'] and fat_deviation <= tolerance['fat'] and carbs_deviation <= \
            tolerance['carbs']

    # TODO: sort function
    def sort(self):
        self.food = sorted(self.food, key=lambda item: item.protein * self.amounts_dictionary[item.name], reverse=True)
        return self


