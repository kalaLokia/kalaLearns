from deckofcards import DeckOfCards
from account import Account

player = Account('kalaLokia')
cards = DeckOfCards()
play = False
playershand = []
dealershand = []
action = ''


def showCards(items, name):
    '''
    Shows {name}'s cards and hand value
    '''
    print(f"{name}'s hand: '")
    for e in items:
        print(f'\t{e}')
    print(f"Hand value: {cards.handValue(items)}")


def bust(hand):
    '''
    Whether a someone has busted or not
    '''
    if(cards.handValue(hand) > 21):
        return True
    return False


def dealersMove():
    '''
    Dealers move: executes when player calls "stand"
    Dealer perform hit until he gets bust, wins or his hand value becomes >= 17
    When hand value is >17 and players has greater value, dealer loses ;-)
    '''

    if(cards.handValue(dealershand) == 21):
        print('Dealer got a BLACKJACK')
        print('Dealer WINS')
        return
    elif(cards.handValue(playershand) == 21):
        print(f'{player.name} got a BLACKJACK')
        print(f'{player.name} WINS')
        return

    while(not bust(dealershand)):

        if(cards.handValue(dealershand) > cards.handValue(playershand)):
            print('Dealer wins')
            showCards(dealershand, 'Dealer')
            break
        elif(cards.handValue(dealershand) == cards.handValue(playershand)):
            print("It's a TIE, so dealer wins")
            break
        elif(cards.handValue(dealershand) > 17):
            print('Dealer loses')
            print(f'{cards.handValue(playershand)} > {cards.handValue(dealershand)}')
            break

        dealershand.append(cards.hit())
    else:
        print(f'Dealer busts! {player.name} has won the game.')


def actions():
    '''
    The actiona that can be performed
    '''
    if(cards.handValue == 21):
        dealersMove()
        return
    while(not bust(playershand)):

        action = input(
            f"{player.name}'s turn: Do you want to hit or stand ? ").lower()
        if(action == 'hit'):
            playershand.append(cards.hit())
            showCards(playershand, player.name)
        elif(action == 'stand'):
            dealersMove()
            break
        else:
            print('Please enter a valid action !')
    else:
        print(f'{player.name} has been BUSTED')


if __name__ == "__main__":

    print(f'Hello {player.name}, Welcome to BlackJack Game')
    response = input('Do you want to start the game (Y/n)? ').lower()
    if(response != 'y'):
        print(response)
        play = False
        print('You have been exited game')
    else:
        play = True
    # Ask for bet amount later
    while(play):
        cards.shuffle()
        print('Cards on the table is now shuffled')
        playershand = list(cards.initiate())
        dealershand = list(cards.initiate())
        print(
            f"{player.name}'s hand:\n   {playershand[0]} - {playershand[1]}\n")
        print(f"Dealer's hand:\n   {dealershand[0]} - ?\n")

        actions()
        print('The End')
        play = False
