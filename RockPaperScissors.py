#
import random

choices = ['rock', 'paper', 'scissors']



def get_user_choice():
    print ("\n Please choice : rock , paper, scissors")
    while True:
        user_choice = input(" your choice is : ").lower()
        if user_choice in choices :
            return user_choice
        print("Invalid Choice , Try Again ")

def  get_computer_choice ():
    return random.choice(choices)

def winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        return "Draw"

    elif (
    (user_choice=="rock" and computer_choice=="scissors")
    or (user_choice=="paper" and computer_choice=="rock" )
    or (user_choice=="scissors" and computer_choice=="paper" )):
        return "You Win"
    else:
        return "Computer Win"

def main ():
    user_score = 0
    computer_score = 0
    while True:

        print("Rock paper scissors game")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\n your choice is : {user_choice}")
        print(f"\n computer choice is : {computer_choice}")

        result = winner(user_choice, computer_choice)
        print("result : ", result)
        if result == "You Win":
            user_score += 1
        elif result == "Computer Win":
            computer_score += 1
        print(f"\n score : you : {user_score}  computer : {computer_score} ")

        play_again = input("Do you want to play again ? (yes , no )").lower()
        if play_again != "yes":
            print(" Thank you for playing")
            break


main()


