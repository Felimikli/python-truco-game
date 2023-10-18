from icecream import ic
import random
from cards import cards, CARD_VALUES
from envido import envido


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
    try:
        if numPlayerCards == 3:
            playerInput = int(input("Press (1, 2 or 3) to throw a card\n"))
        elif numPlayerCards == 2:
            playerInput = int(input("Press (1 or 2) to throw a card\n"))
        elif numPlayerCards == 1:
            playerInput = int(input("Press (1) to throw a card\n"))

        if playerInput < 1 or playerInput > 3:
            print(f"Invalid input:")
            return getPlayerInput(playerCards)
        else:
            return playerInput - 1
    except ValueError:
        print(f"Invalid input:")
        return getPlayerInput(playerCards)


def getComputerInput(computerCards):
    if computerCards != []:
        computerInput = random.randint(0, len(computerCards) - 1)
        return computerInput


def getEnvidoInput(playerCards, computerCards, startingTurn):
    envidoInput = str(
        input('Type "ENVIDO", "REAL ENVIDO", "FALTA ENVIDO" o "PASO"\n')).lower()
    validInputs = ['envido', 'real envido', 'falta envido']
    if envidoInput in validInputs:
        return envidoInput
    elif envidoInput == 'paso':
        pass
    else:
        print('Invalid input')
        getEnvidoInput(playerCards, computerCards, startingTurn)


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
    print("-------------------\n| Your cards are: |\n-------------------")
    for card in playerCards:
        print(f"{playerCards.index(card) + 1}. | {card} |")

    for round in range(3):
        print(f"Hand: {round + 1}")

        print(f"{turn}'s turn")
        playerThrownCard = ''
        computerThrownCard = ''

        while True:
            if turn == 'player':
                if round == 0:
                    envidoInput = getEnvidoInput(
                        playerCards, computerCards, startingTurn)

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
                    playerPoints += 2
                    turn = 'player'
                    print(f"hand: {round + 1} won by {turn}\n")

                elif CARD_VALUES[playerThrownCard] < CARD_VALUES[computerThrownCard]:
                    computerPoints += 2
                    turn = 'computer'
                    print(f"hand: {round + 1} won by {turn}\n")
                else:
                    # empate
                    print(f"hand: {round + 1} tied\n")
                    playerPoints += 1
                    computerPoints += 1
                break
        if round == 0:
            firstRoundWinner = turn
        if playerPoints == computerPoints:
            if round == 2:
                if firstRoundWinner == 'computer':
                    print("Computer wins")
                    playAgain()
                else:
                    print("Player wins")
                    playAgain()

        if playerPoints >= 3:
            print("player wins")
            playAgain()
            break
        elif computerPoints >= 3:
            print("Computer wins")
            playAgain()
            break
        else:

            continue


truco()
