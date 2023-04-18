import random
from game_data import data


 
def get_random_comparison():
    return random.choice(data)

A = get_random_comparison()
print(f" Compare A: {A['name']}, a {A['description']} from {A['country']}")
B = get_random_comparison()
print(f" Compare B: {B['name']}, a {B['description']} from {B['country']}")

answer = input("Who has more followers? Type 'A' or 'B'?")
print(type(answer))