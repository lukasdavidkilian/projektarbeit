import json

all_foods = []

class Food:
    def __init__(self, name, protein, fat, carbs, amount, unit, recommended_amounts):
        self.name = name
        self.protein = protein
        self.fat = fat
        self.carbs = carbs
        self.amount = amount
        self.unit = unit
        self.recommended_amounts = recommended_amounts
        all_foods.append(self)

    def __eq__(self, other):
        if isinstance(other, Food):
            return (
                    self.name == other.name
                    and self.protein == other.protein
                    and self.fat == other.fat
                    and self.carbs == other.carbs
                    and self.amount == other.amount
                    and self.unit == other.unit
                    and self.recommended_amounts == other.recommended_amounts
            )
        return False

    def dominant_macronutrient(self):
        max_value = max(self.protein, self.fat, self.carbs)
        if max_value == self.protein:
            return 'protein'
        elif max_value == self.fat:
            return 'fat'
        else:
            return 'carbs'
