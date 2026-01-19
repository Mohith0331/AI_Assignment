from recipe_data import RECIPES

def suggest_recipe(user_ingredients):
    user_set = set(i.lower() for i in user_ingredients)

    best_match = None
    best_score = 0

    for recipe in RECIPES:
        score = len(user_set & recipe["ingredients"])
        if score > best_score:
            best_score = score
            best_match = recipe

    return best_match