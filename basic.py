
# numbers = [1, 2, 3, 4, 5]
# friends = ["jms", 2, "John"]
# # add list in another
# friends.extend(numbers)

# print(friends)

# # a few way print str
# youtuber = "Kylie Ying"

# print('subscribe to {}'.format(youtuber))
# print(f'subscribe to {youtuber}')

# # madlib
# adj = input('Adjective: ')
# ver1 = input("Verb: ")
# ver2 = input("Verb: ")
# famous_persion = input("Famous persion: ")

# madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
# I love to {ver1}. Stay hydrate and {ver2} like you are {famous_persion}!"

# print(madlib)

# # guessing numbers
# from math import radians
# import random   

# def guess(x):
#     random_num = random.randint(1 , x)
#     guess = 0 
#     while guess != random_num:
#         guess = int(input(f"Guess a number between 1 and {x}: "))
#         if guess < random_num: 
#             print("Sorry, guess again. Too low!")
#         elif guess > random_num:
#             print("Sorry, guess again. Too hight!")
#     print(f"Yay, congrats. You have guessed the number {random_num} correctly.")


# def computer_guess(x):
#     low = 1
#     hight = x
#     feedback = ""
#     while feedback != 'c' 
#         if low != hight:
#             guess = random.randint(low, hight)
#         else: 
#             guess = low
#         feedback=input(f"Is {guess} too hight(H), too low(L), correctly(C): ").lower()
#         if feedback == 'h':
#             hight = guess - 1
#         elif feedback == 'l':
#             low = guess + 1
#     print(f"Yay, congrats. You have guessed the number {guess} correctly.")

# kéo búa bao
# import random

# def play():
#     user = input("'s' kéo, 'r' búa, 'p' bao: ").lower()
#     computer = random.choice(['s', 'r', 'p'])
    
#     if user == computer:
#         print("Hòa.")
#         return
#     elif is_you_win(user, computer):
#         print("You win!")
#         return
#     else:
#         print("You lose!")
#         return

# def is_you_win(player, opponent) -> bool:
#     if (player == 's' and opponent == "p") or (player == 'r' and opponent == 's') or (player == 'p' and opponent == 
#     'r'):
#         return True
#     else:
#         return False

# play()

from sys import getsizeof
x:int = 1
print(bin(x))