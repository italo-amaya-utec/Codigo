# comprehentions list

original_list = [1,2,3,4,5]

squares_list = [number ** 2 for number in original_list]

print(squares_list)

# Returns [1,4,9,16,25]

# This is the tut for list comprehentions
# https://datagy.io/list-comprehensions...


# Filtering

original_list = [1,2,3,4,5]

filtered_list = [number for number in original_list if number > 3]

print(filtered_list)

# Return [4,5]

# maping

original_list = [1,2,3,4,5]

def square(number):
  return number ** 2

squares = map(square, original_list)

squares_list = list(squares)

print(squares)

# Returns [1, 4, 9, 16, 25]

# Zip()


numbers = [1,2,3]

letters = ['a', 'b', 'c']

combined = zip(numbers, letters)

combined_list = list(combined)

# returns [(1, 'a'), (2, 'b'), (3, 'c')]

#reversed_list

original_list = [1,2,3,4,5]

reversed_list = original_list[::-1]

print(reversed_list)

# Returns: [5,4,3,2,1]

# is it in the list

games = ['Yankees', 'Yankees', 'Cubs', 'Blue Jays', 'Giants']

def isin(item, list_name):
  if item in list_name: print(f"{item} is in the list!")
  else: print(f"{item} is not in the list!")

isin('Blue Jays', games)
isin('Angels', games) 

# Returns
# Blue Jays is in the list!
# Angels is not in the list!


