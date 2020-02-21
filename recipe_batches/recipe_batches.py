#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  max = 0
  valid = 0
  count = {}
  # print(recipe.keys())
  # print(ingredients.keys())
  for i in recipe:
        print(count)
        if recipe.keys() == ingredients.keys():
          if recipe[i] > ingredients[i]:
              max = 0
          elif recipe[i] <= ingredients[i]:
              valid += 1
              max_batches = ingredients[i]//recipe[i]
              count[i] = max_batches
        else:
              max=0

  if valid >= len(recipe)-1:
        max = min(count.values())
        return max
  else: 
    return max


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5,  'sugar':9 }
  ingredients = { 'milk': 132, 'butter': 50, 'flour': 51, 'sugar':10 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))