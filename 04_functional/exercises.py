from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
print(list(map(lambda x: x.capitalize(), my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
zip_list = list(zip(my_strings, sorted(my_numbers)))
print(zip_list)

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
f_list = list(filter(lambda x: x > 50, scores))
print(f_list)

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
reduce_result = reduce(lambda acc, item: acc + item, my_numbers + scores)
print(reduce_result)

a_list = [2, 4, 6, 7, 7.3]
print(list(map(lambda x: x ** 2, a_list)))

t_list = [(1, 2), (2, 9), (7, 2), (5, 4), (3, 6)]

t_list.sort(key=lambda x: x[1])
print(t_list)
