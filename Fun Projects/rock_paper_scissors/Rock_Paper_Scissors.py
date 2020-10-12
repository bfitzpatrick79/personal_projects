
import random

reply = input("would you like to play a game of Rock, Paper, Scissors [y/n]: ")
reply.lower()

options = ['r', 'p', 's']

# Computer Selection


# User Selection
#user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

#statistics generation
p_win_count = 0
p_lose_count = 0
c_win_count = 0
c_lose_count = 0
game_count = 0




# Run Conditionals
while reply == 'y':
    user_choice = input("MAKE YOUR CHOICE [r, p, s]: ")
    computer_choice = random.choice(options)
    print(user_choice)

    ##player options rock
    if user_choice == 'r' and computer_choice == 'r':
        game_count +=1
        p_win_percent = ((p_win_count / game_count) * 100)
        p_lose_percent = ((p_lose_count / game_count) * 100)
        print('TIE')
        print(f'YOU PICKED{user_choice} AND THE COMPUTER PICKED {computer_choice}')
        print(f'# OF GAMES :{game_count} WINS: {p_win_count} LOSSES: {p_lose_count}')
        print(f'WIN %: {p_win_percent} LOSS %: {p_lose_percent}')
        print(" ")
        reply = input("WOULD YOU LIKE TO PLAY AGAIN [y/n]: ")
    elif user_choice == 'r' and computer_choice == 'p':
        game_count += 1
        p_lose_count += 1
        c_win_count += 1
        p_win_percent = ((p_win_count / game_count) * 100)
        p_lose_percent = ((p_lose_count / game_count) * 100)
        print('LOSE')
        print(f'YOU PICKED {user_choice} AND THE COMPUTER PICKED {computer_choice}')
        print(f'# OF GAMES :{game_count} WINS: {p_win_count} LOSSES: {p_lose_count}')
        print(f'WIN %: {p_win_percent} LOSS %: {p_lose_percent}')
        print(" ")
        reply = input("Would you like to play again [y/n]: ")
    elif user_choice == 'r' and computer_choice == 's':
        game_count += 1
        p_win_count += 1
        c_lose_count +=1
        p_win_percent = ((p_win_count / game_count) * 100)
        p_lose_percent = ((p_lose_count / game_count) * 100)
        print('WIN')
        print(f'YOU PICKED {user_choice} AND THE COMPUTER PICKED {computer_choice}')
        print(f'# OF GAMES: {game_count} WINS: {p_win_count} LOSSES: {p_lose_count}')
        print(f'WIN %: {p_win_percent} LOSS %: {p_lose_percent}')
        print(" ")
        reply = input("WOULD YOU LIKE TO PLAY AGAIN [y/n]: ")

    #Player Options Scissors
    elif user_choice == 's' and computer_choice == 's':
        game_count += 1
        p_win_percent = ((p_win_count / game_count) * 100)
        p_lose_percent = ((p_lose_count / game_count) * 100)
        print('TIE')
        print(f'YOU PICKED {user_choice} AND THE COMPUTER PICKED {computer_choice}')
        print(f'# OF GAMES :{game_count} WINS: {p_win_count} LOSSES: {p_lose_count}')
        print(f'WIN %: {p_win_percent} LOSS %: {p_lose_percent}')
        print(" ")
        reply = input("WOULD YOU LIKE TO PLAY AGAIN [y/n]: ")
    elif user_choice == 's' and computer_choice == 'r':
        game_count += 1
        p_lose_count += 1
        c_win_count += 1
        p_win_percent = ((p_win_count / game_count) * 100)
        p_lose_percent = ((p_lose_count / game_count) * 100)
        print('LOSE')
        print(f'YOU PICKED {user_choice} AND THE COMPUTER PICKED {computer_choice}')
        print(f'# OF GAMES :{game_count} WINS: {p_win_count} LOSSES: {p_lose_count}')
        print(f'WIN %: {p_win_percent} LOSS %: {p_lose_percent}')
        print(" ")
        reply = input("WOULD YOU LIKE TO PLAY AGAIN [y/n]: ")
    elif user_choice == 's' and computer_choice == 'p':
        game_count += 1
        p_win_count += 1
        c_lose_count += 1
        p_win_percent = ((p_win_count / game_count) * 100)
        p_lose_percent = ((p_lose_count / game_count) * 100)
        print('WIN')
        print(f'YOU PICKED {user_choice} AND THE COMPUTER PICKED {computer_choice}')
        print(f'# OF GAMES :{game_count} WINS: {p_win_count} LOSSES: {p_lose_count}')
        print(f'WIN %: {p_win_percent} LOSS %: {p_lose_percent}')
        print(" ")
        reply = input("WOULD YOU LIKE TO PLAY AGAIN [y/n]: ")

    #player Options Paper
    elif user_choice == 'p' and computer_choice == 'p':
        game_count += 1
        p_win_percent = ((p_win_count / game_count) * 100)
        p_lose_percent = ((p_lose_count / game_count) * 100)
        print('TIE')
        print(f'YOU PICKED {user_choice} AND THE COMPUTER PICKED {computer_choice}')
        print(f'# OF GAMES :{game_count} WINS: {p_win_count} LOSSES: {p_lose_count}')
        print(f'WIN %: {p_win_percent} LOSS %: {p_lose_percent}')
        print(" ")
        reply = input("WOULD YOU LIKE TO PLAY AGAIN [y/n]: ")
    elif user_choice == 'p' and computer_choice == 's':
        game_count += 1
        p_lose_count += 1
        c_win_count += 1
        p_win_percent = ((p_win_count / game_count) * 100)
        p_lose_percent = ((p_lose_count / game_count) * 100)
        print('LOSE')
        print(f'YOU PICKED {user_choice} AND THE COMPUTER PICKED {computer_choice}')
        print(f'# OF GAMES :{game_count} WINS: {p_win_count} LOSSES: {p_lose_count}')
        print(f'WIN %: {p_win_percent} LOSS %: {p_lose_percent}')
        print(" ")
        reply = input("WOULD YOU LIKE TO PLAY AGAIN [y/n]: ")
    elif user_choice == 'p' and computer_choice == 'r':
        game_count += 1
        p_win_count += 1
        c_lose_count += 1
        p_win_percent = ((p_win_count / game_count) * 100)
        p_lose_percent = ((p_lose_count / game_count) * 100)
        print('WIN')
        print(f'YOU PICKED {user_choice} AND THE COMPUTER PICKED {computer_choice}')
        print(f'# OF GAMES :{game_count} WINS: {p_win_count} LOSSES: {p_lose_count}')
        print(f'WIN %: {p_win_percent} LOSS %: {p_lose_percent}')
        print(" ")
        reply = input("WOULD YOU LIKE TO PLAY AGAIN [y/n]: ")

