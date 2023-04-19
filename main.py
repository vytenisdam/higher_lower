import random
from game_data import data

player_score = 0



def get_random_comparison():
    return random.choice(data)

def player_answer():
    if answer == 'A':
        return A
    else:
        return B
    
def check_higher():
    if player_choice == A and A['follower_count'] >= B['follower_count']:
        player_score += 1
        A = B
        B = get_random_comparison()
        print(f'You are right! Your current score is {player_score}.')
    elif player_choice == B and B['follower_count'] >= A['follower_count']:
        player_score += 1
        A = A
        B = get_random_comparison()
        print(f'You are right! Your current score is {player_score}.')
    else:
        print(f'Sorry, thats wrong. Final score: {player_score}.')
        
A = get_random_comparison()
print(f" Compare A: {A['name']}, a {A['description']} from {A['country']}")
B = get_random_comparison()
print(f" Compare B: {B['name']}, a {B['description']} from {B['country']}")    
answer = input("Who has more followers? Type 'A' or 'B'?").upper()
player_choice = player_answer() 

player_answer()
check_higher()
    