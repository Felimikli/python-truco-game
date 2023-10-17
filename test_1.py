from icecream import ic
import random

espada = ['e1', 'e2', 'e3', 'e4', 'e5',
          'e6', 'e7', 'e10', 'e11', 'e12']
basto = ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b10', 'b11', 'b12']
oro = ['o1', 'o2', 'o3', 'o4', 'o5', 'o6', 'o7', 'o10', 'o11', 'o12']
copa = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c10', 'c11', 'c12']
CARD_VALUES = {'e1': 14, 'b1': 13, 'e7': 12, 'o7': 11, 'e3': 10, 'b3': 10, 'o3': 10, 'c3': 10, 'e2': 9, 'b2': 9, 'o2': 9, 'c2': 9, 'o1': 8, 'c1': 8, 'e12': 7, 'b12': 7, 'o12': 7, 'c12': 7, 'e11': 6, 'b11': 6,
               'o11': 6, 'c11': 6, 'e10': 5, 'b10': 5, 'o10': 5, 'c10': 5, 'b7': 4, 'c7': 4, 'e6': 3, 'b6': 3, 'o6': 3, 'c6': 3, 'e5': 2, 'b5': 2, 'o5': 2, 'c5': 2, 'e4': 1, 'b4': 1, 'o4': 1, 'c4': 1, }
cards = espada + basto + oro + copa


def deal(numPlayers):
    random.shuffle(cards)
    # cards[i * 3:i * 3 + 3] from i * 3 to i * 3 + 3, to deal in batches of 3
    data = {}
    for i in range(1, numPlayers + 1):
        data[f'player{i}'] = cards[i * 3:i * 3 + 3]
    return data
    # or return {f'player{}': card_deck[i * 3:i * 3 + 3] for i in range(1, num_players + 1)}


def getPlayerInput(playerCards):
    numPlayerCards = len(playerCards)
    # Showing the cards:
    for card in playerCards:
        print(f"{playerCards.index(card) + 1}. {card}")
    try:
        if numPlayerCards == 3:
            playerInput = int(input("Press (1, 2 or 3) to throw a card\n"))
        elif numPlayerCards == 2:
            playerInput = int(input("Press (1 or 2) to throw a card\n"))
        elif numPlayerCards == 1:
            playerInput = int(input("Press (1) to throw a card\n"))

        if playerInput < 1 or playerInput > 3:
            print(f"Invalid input, enter (1 to {numPlayerCards})\n")
            getPlayerInput(playerCards)
        else:
            return playerInput - 1
    except ValueError:
        print(f"Invalid input, enter (1 to {numPlayerCards})\n")
        getPlayerInput(playerCards)


def getComputerInput(computerCards):
    if computerCards != []:
        computerInput = random.randint(0, len(computerCards) - 1)
        return computerInput


def playAgain():
    playAgainInput = str(input('Press Y to play again or Q to quit\n')).lower()
    if playAgainInput == 'y':
        truco()
    elif playAgainInput == 'q':
        quit()
    else:
        print('Invalid input, press Y to play again or Q to quit\n')
        playAgain()


def truco():

    startingTurn = 'computer'
    turn = startingTurn

    numPlayers = 2
    playerPoints = 0
    computerPoints = 0

    handCards = deal(numPlayers)
    playerCards = handCards['player1']
    computerCards = handCards['player2']

    for hand in range(3):
        print(f"Hand: {hand + 1}")

        print(f"{turn}'s turn")
        playerThrownCard = ''
        computerThrownCard = ''

        while True:
            if turn == 'player':
                playerThrownCardIndex = getPlayerInput(playerCards)
                playerThrownCard = playerCards.pop(playerThrownCardIndex)
                turn = 'computer'
                print(f"You threw: {playerThrownCard}")
            else:
                computerThrownCardIndex = getComputerInput(computerCards)
                computerThrownCard = computerCards.pop(computerThrownCardIndex)
                turn = 'player'
                print(f"Computer threw: {computerThrownCard}")
            if playerThrownCard and computerThrownCard:
                if CARD_VALUES[playerThrownCard] > CARD_VALUES[computerThrownCard]:
                    playerPoints += 1
                    turn = 'player'
                    print(f"hand: {hand + 1} won by {turn}\n")
                elif CARD_VALUES[playerThrownCard] < CARD_VALUES[computerThrownCard]:
                    computerPoints += 1
                    turn = 'computer'
                    print(f"hand: {hand + 1} won by {turn}\n")
                else:
                    # empate
                    playerPoints += 1
                    computerPoints += 1
                    print(f"hand: {hand + 1} tied\n")

                break
        if playerPoints == 2:
            print("player wins")
            playAgain()
            break
        elif computerPoints == 2:
            print("Computer wins")
            playAgain()
            break
        else:

            continue


truco()
