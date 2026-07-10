print("Recipe Explorer")
pasta=("arabiata","italian",20,"medium")
biryani=("chicken biryani","indian",45,"hard")
print(pasta)
print("pasta name:",pasta[0])
print("biryani cuisine:",biryani[1])
print("difficulty of biryani:",biryani[-1])
all_recipes= (pasta,biryani)
print(all_recipes[0][0])
print("biryani time:", all_recipes[1][2])
print("pasta recipe items")
for detail in pasta :
    print(detail)

pasta_ingredients = {"tomato", "garlic", "olive oil", "chilli", "pasta", "garlic"}
biryani_ingredients = {"rice", "chicken", "garlic", "onion", "tomato", "spices"}

pasta_ingredients.add("cheese")
pasta_ingredients.discard("chilli")
print("updated pasta ingredients")
print(pasta_ingredients)
combined = pasta_ingredients.union(biryani_ingredients)
print("all ingredients:",combined)
common =  pasta_ingredients.intersection(biryani_ingredients)
print("the common ingredients are : ", common)
only_pasta = pasta_ingredients.difference(biryani_ingredients)
unique_to_each = pasta_ingredients.symmetric_difference(biryani_ingredients)

print("these are only the pasta ingredients:" ,only_pasta)
print("these are the umique ingredients:" ,unique_to_each)
