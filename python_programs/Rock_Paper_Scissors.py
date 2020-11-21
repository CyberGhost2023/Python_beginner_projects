import random

computer_options = ['rock','paper','scissors']
user_name_dict = {}
user_name = input('Enter your name: ')
print('Hello, '+user_name)

def search_file():
    global user_name
    File = open('rating.txt', 'r')     
    for name in File.readlines():
        un = name.rstrip().split()
        if (un[0] == user_name):
            user_name_dict[user_name]= int(un[1])
            break
    else:
        user_name_dict[user_name] = 0
    
def user_input(user_choice):
    computer_choice = random.choice(computer_options)
    if user_choice==computer_choice:
        print(f"There is a draw ({user_choice})")
        user_name_dict[user_name] += 50
    elif user_choice == 'rock' and computer_choice == 'paper' or user_choice == 'paper' and computer_choice == 'scissors' or user_choice == 'scissors' and computer_choice == 'rock':
        print(f"Sorry, but computer chose {computer_choice}")
    else:
        print(f"Well done. Computer chose {computer_choice} and failed")
        user_name_dict[user_name] += 100

search_file()
while 1:
    user = input()
    if user=='!exit':
        print('!Bye')
        break
    elif user=='!rating':
        print('Your rating: '+str(user_name_dict[user_name]))
    elif user not in computer_options:
        print('Invalid input')
    else:
        user_input(user)