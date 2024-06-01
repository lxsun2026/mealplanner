//simple algorithm to display order of recipes to be cooked
from functools import cmp_to_key

def compare_recipes_by_index(i, j):
    sorted_recipe_i = sorted(recipes[i])
    sorted_recipe_j = sorted(recipes[j])
    
    if sorted_recipe_i < sorted_recipe_j:
        return -1
    elif sorted_recipe_i > sorted_recipe_j:
        return 1
    else:
        return 0

indices = list(range(len(recipes)))
sorted_indices = sorted(indices, key=cmp_to_key(compare_recipes_by_index))
final_sorted_array = [recipes[i] for i in sorted_indices]

