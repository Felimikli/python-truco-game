from icecream import ic
import random
from constants import cards, CARD_VALUES, swapTurn
from envido import envido


def game(startingTurn):
    totalPoints = {'player': 0, 'computer': 0}

    def deal(numPlayers):
        print("shuffling...")
        random.shuffle(cards)
        # cards[i * 3:i * 3 + 3] from i * 3 to i * 3 + 3, to deal in batches of 3
        data = {}
        for i in range(1, numPlayers + 1):
            data[f'player{i}'] = cards[i * 3:i * 3 + 3]
        return data
        # or return {f'player{}': card_deck[i * 3:i * 3 + 3] for i in range(1, num_players + 1)}

    def getPlayerEnvido():

        # options = {
        #     0: ['e', 're', 'fe'],
        #     1: ['q', 'n', '2e', 're', 'fe'],
        #     2: ['q', 'n', 're', 'fe'],
        #     3: ['q', 'n', 'fe'],
        #     4: ['q', 'n']
        # }
        envidoChoice = f'e, re ,fe\n'
        return envidoChoice

    def getPlayerTruco(trucoIndex):
        options = {
            1: ['truco'],
            2: ['quiero', 'no quiero', 'retruco'],
            3: ['quiero', 'no quiero', 'valecuatro'],
            4: ['quiero', 'no quiero']
        }
        trucoChoice = f'press {", ".join(options[trucoIndex])}\n'
        return trucoChoice

    def getPlayerCard(playerCards):
        numPlayerCards = len(playerCards)

        cardChoice = str((f'press {", ".join(playerCards)}\n'))
        return cardChoice

    def getPlayerInput(playerCards, trucoIndex, round, envidoCall):

        inputMsg = ''
        if round == 0 and envidoCall == 0:
            inputMsg += getPlayerEnvido()
        inputMsg += getPlayerTruco(trucoIndex)
        inputMsg += getPlayerCard(playerCards)
        playerChoice = str(input(f'press {inputMsg}\n'))
        return playerChoice
        # try:
        #     if numPlayerCards == 3:
        #         playerInput = int(input("Press (1, 2 or 3) to throw a card\n"))
        #     elif numPlayerCards == 2:
        #         playerInput = int(input("Press (1 or 2) to throw a card\n"))
        #     elif numPlayerCards == 1:
        #         playerInput = int(input("Press (1) to throw a card\n"))

        #     if playerInput < 1 or playerInput > len(playerCards):
        #         print(f"Invalid input: ")
        #         return getPlayerInput(playerCards)
        #     else:
        #         return playerInput - 1
        # except ValueError:
        #     print(f"Invalid input: ")
        #     return getPlayerInput(playerCards)

    def getComputerInput(computerCards):
        if computerCards != []:
            computerInput = random.randint(0, len(computerCards) - 1)
            return computerInput

    def playAgain(startingTurn):
        startingTurn = swapTurn(startingTurn)
        main(startingTurn)

    def main(startingTurn):

        turn = startingTurn
        numPlayers = 2
        playerPoints = 0
        computerPoints = 0

        handCards = deal(numPlayers)
        playerCards = handCards['player1']
        computerCards = handCards['player2']

        allPlayerCards = handCards['player1']
        allComputerCards = handCards['player2']

        trucoIndex = 1

        print("-------------------\n| Your cards are: |\n-------------------")
        for card in playerCards:
            print(f"{playerCards.index(card) + 1}. | {card} |")

        for round in range(3):
            print(f"\nHand: {round + 1}")

            print(f"{turn}'s turn")
            playerThrownCard = ''
            computerThrownCard = ''

            envidoCall = 0

            for i in range(100):

                # if round == 0 and envidoCall == 0:
                #     envidoCall = envido(allPlayerCards, allComputerCards, turn)
                #     if envidoCall != 0:
                #         envidoWinner = envidoCall[0]
                #         envidoPointsWon = envidoCall[1]
                #         ic(envidoCall, envidoWinner, envidoPointsWon)
                #         totalPoints[envidoWinner] += envidoPointsWon

                if turn == 'player':
                    playerInput = getPlayerInput(
                        playerCards, trucoIndex, round, envidoCall)
                    if playerInput in playerCards:
                        playerCards.remove(playerInput)
                        print(f"You threw: {playerInput}")
                    elif playerInput in ['e', 're', 'fe']:
                        envidoCall = envido(
                            playerCards, computerCards, turn, playerInput)
                    else:
                        trucoIndex += 1
                else:
                    computerThrownCardIndex = getComputerInput(computerCards)
                    computerThrownCard = computerCards.pop(
                        computerThrownCardIndex)
                    print(f"Computer threw: {computerThrownCard}")
                turn = swapTurn(turn)
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
                        totalPoints['computer'] += trucoIndex
                        print(
                            f"Computer wins.\nPlayer points: {totalPoints['player']}, computer points: {totalPoints['computer']}")
                        playAgain(startingTurn)
                    else:
                        totalPoints['player'] += trucoIndex
                        print(
                            f"Player wins.\nPlayer points: {totalPoints['player']}, computer points: {totalPoints['computer']}")
                        playAgain(startingTurn)

            if playerPoints >= 3:
                totalPoints['player'] += trucoIndex
                print(
                    f"Player wins.\nPlayer points: {totalPoints['player']}, computer points: {totalPoints['computer']}")
                playAgain(startingTurn)
                break
            elif computerPoints >= 3:
                totalPoints['computer'] += trucoIndex
                print(
                    f"Computer wins.\nPlayer points: {totalPoints['player']}, computer points: {totalPoints['computer']}")
                playAgain(startingTurn)
                break
            else:
                continue

    main(startingTurn)


def playAgain():
    print(startingTurn)
    startingTurn = swapTurn(startingTurn)
    playAgainInput = str(input('Press Y to play again or Q to quit\n')).lower()
    if playAgainInput == 'y':
        game()
    elif playAgainInput == 'q':
        quit()
    else:
        print('Invalid input, press Y to play again or Q to quit\n')
        playAgain()


game(startingTurn=random.choice(['player', 'computer']))
