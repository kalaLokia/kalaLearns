# Neccessary imports for the project
from IPython.display import clear_output
from random import randint


# Initializers for global variables
board_elements = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def firstUser():
    '''
    Function to ask the user to choose either X or O
    Returns either X or O
    '''
    value = input('Choose who are you, X or O : ').upper()
    if(value in ['X','O']):
        return value
    else:
        print("That was a invalid entry, we choose 'X' for you.")
        return 'X'

def board(elements):
    '''
    Function to display the board view of the game.
    '''
    print('------------------------')
    print(f'   {elements[6]}   |   {elements[7]}   |   {elements[8]}   ')
    print('------------------------')
    print(f'   {elements[3]}   |   {elements[4]}   |   {elements[5]}   ')
    print('------------------------')
    print(f'   {elements[0]}   |   {elements[1]}   |   {elements[2]}   ')
    print('------------------------')

def checkWinner():
    '''
    Function to check for a winner
    Winning sequences : 123,456,789,147,258,369,159,753
    '''
    if(len(set(board_elements[0:3]))==1):
        return board_elements[0]
    elif(len(set(board_elements[3:6]))==1):
        return board_elements[3]
    elif(len(set(board_elements[6:9]))==1):
        return board_elements[6]
    elif(len(set(board_elements[0::3]))==1):
        return board_elements[0]
    elif(len(set(board_elements[1::3]))==1):
        return board_elements[1]
    elif(len(set(board_elements[2::3]))==1):
        return board_elements[2]
    elif(len(set(board_elements[2::2]))==1):
        return board_elements[2]
    elif(len(set(board_elements[0:4]))==1):
        return board_elements[0]
    else:
        return 0

def userInput(user, msg = 'Choose your position'):
    '''
    To get a valid input from users
    '''
    value = 0
    valid = False
    while(not valid):
        try:
            value = int(input(f'{user} {msg}: '))-1
            if(value > 9): 
                value = int('Show error')
        except ValueError:
            print('Please enter a valid number in between [1 - 9]')
            continue
        
        valid = True
    return value

def startGame():
    '''
    Function to begin the game
    '''
    position = []

    user1 = firstUser()
    user2 = 'O' if(user1 == 'X') else 'X'

    print(f'User 1 : {user1}\nUser 2 : {user2}')


    print('Board Display:')
    board([1,2,3,4,5,6,7,8,9])

    if(randint(0,100) % 2 == 0):
        order = ['X','O','X','O','X','O','X','O','X']
        print('X has the first move')
    else:
        order = ['O','X','O','X','O','X','O','X','O']
        print('O has the first move')

    # Game begins in here
    for move in range(1,10):
        value = order.pop()
        entry = userInput(value)
        
        while entry in position:
            entry = userInput(value, 'Choose a postion that is not entered: ')
        
        if(entry == -1):
            print(f'{value} has left the game')
            position = []
            break
                
        position.append(entry)
        board_elements[entry] = value
        clear_output()
        board(board_elements)
        if(checkWinner()=='X'):
            print('X HAS WON THE GAME.')
            break
        elif(checkWinner() == 'O'):
            print('O HAS WON THE GAME.')
            break

    position = []
    print('End of game')

ready = True
while(ready):
    startGame()
    if(input('Do you want to play again (Y/n): ').lower != 'y'):
        ready = False
        print('Game End!')
