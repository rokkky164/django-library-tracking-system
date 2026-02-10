import random
# rand_list =

# list_comprehension_below_10 =

# list_comprehension_below_10 =
"""
Complete the following Python tasks in the core_skills.py file.
Create a list of 10 random numbers between 1 and 20.
Filter Numbers Below 10 (List Comprehension)
Filter Numbers Below 10 (Using filter)
"""

# 1
rand_list = random.sample(range(1, 21), 10)
# 2
list_comprehension_below_10 = [i for i in rand_list if i < 10]
# 3
list_comprehension_below_10_filter = list(filter(lambda x: x < 10, rand_list))


