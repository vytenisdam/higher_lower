import random
from game_data import data
import os 
from art import logo, vs
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def get_random_comparison():
    """Gives a random value from game_data"""
    return random.choice(data)
    
def check_higher(A,B,answer):
    """Checks followers against user's guess and returns True if they got it right. Or False if they got it wrong."""
    if A['follower_count'] > B['follower_count']:
        return answer == 'A'
    else:
        return answer == 'B'
def game():
    print(logo)
    player_score = 0
    should_continue = True 
    A = get_random_comparison()        
    B = get_random_comparison()
    
    while should_continue == True:
        A = B
        B = get_random_comparison()
        while B == A:
            B = get_random_comparison()
        
        print(f" Compare A: {A['name']}, a {A['description']} from {A['country']}")
        print(vs)
        print(f" Against B: {B['name']}, a {B['description']} from {B['country']}")
            
        answer = input("Who has more followers? Type 'A' or 'B'? ").upper()
        is_correct = check_higher(A,B,answer)
        cls()
        print(logo)
        if is_correct == True:
            player_score += 1
            print(f"You're right! Current score: {player_score}.")
        else: 
            should_continue = False
            print(f"Sorry, that's wrong. Final score: {player_score}")
            
game()       
