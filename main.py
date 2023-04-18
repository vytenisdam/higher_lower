import random
from game_data import data


 
def get_random_comparison():
    return random.choice(data)

compare_A = get_random_comparison()
print(f" A is: {compare_A['name']}")
compare_B = get_random_comparison()
print(f" B is: {compare_B['name']}")