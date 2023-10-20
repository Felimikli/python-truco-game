import random
from icecream import ic
from constants import swapTurn, ENVIDO_PATHS


def envido(playerCards, computerCards, turn):

    def envidoSum(cards):
        totalEnvido = {'e': [], 'b': [], 'o': [], 'c': [], }
        # separate the player's cards in suits
        for card in cards:
            suit = card[0]
            value = int(card[1:])
            if value >= 10:
                value = 0

            if suit in totalEnvido:
                totalEnvido[suit].append(value)

        # if two or more cards are in the same Suit, sum the 2 highest ones and add 20
        # if a suit has no values, delete it
        suitsRemoved = []
        for suit in totalEnvido:
            if len(totalEnvido[suit]) == 1:
                totalEnvido[suit] = totalEnvido[suit][0]
            elif len(totalEnvido[suit]) >= 2:
                totalEnvido[suit] = 20 + \
                    sum(sorted(totalEnvido[suit])[-2:])
            else:
                suitsRemoved.append(suit)

        for suit in suitsRemoved:
            del totalEnvido[suit]
        # set player's envido to the highest value

        totalEnvido = max(totalEnvido.values())

        return totalEnvido

    def findWinner(playerCards, computerCards, turn):
        playerEnvido = envidoSum(playerCards)
        computerEnvido = envidoSum(computerCards)
        winner = turn
        if playerEnvido > computerEnvido:
            winner = 'player'
        if playerEnvido < computerEnvido:
            winner = 'computer'
        return winner

    def getEnvidoPlayer(envidoIndex):

        options = {
            0: ['e', 're', 'fe', 'pass'],
            1: ['q', 'n', '2e', 're', 'fe'],
            2: ['q', 'n', 're', 'fe'],
            3: ['q', 'n', 'fe'],
            4: ['q', 'n']
        }

        while True:
            playerChoice = str(
                input(f'press {", ".join(options[envidoIndex])}\n'))
            if playerChoice in options[envidoIndex]:
                return playerChoice
            else:
                print('Invalid Input:\n')
                return getEnvidoPlayer(envidoIndex)

                # HARD-CODING
        # if envidoIndex == 0:
        #     return ''
        # elif envidoIndex == 1:
        #     return ''
        # elif envidoIndex == 2:
        #     return ''
        # elif envidoIndex == 3:
        #     return ''
        # elif envidoIndex == 4:
        #     return ''

    def getEnvidoComputer(envidoIndex):
        options = {
            0: ['e', 're', 'fe', 'pass'],
            1: ['q', 'n', '2e', 're', 'fe'],
            2: ['q', 'n', 're', 'fe'],
            3: ['q', 'n', 'fe'],
            4: ['q', 'n']
        }

        return random.choice(options[envidoIndex])

        # HARD-CODING
        # if envidoIndex == 0:
        #     return ''
        # elif envidoIndex == 1:
        #     return ''
        # elif envidoIndex == 2:
        #     return ''
        # elif envidoIndex == 3:
        #     return ''
        # elif envidoIndex == 4:
        #     return ''

    def main(turn, envidoIndex, pointsAtRisk):
        envidoPath = ''
        winner = ''
        for _ in range(6):
            choice = ''
            if turn == 'player':
                choice = getEnvidoPlayer(envidoIndex)
                print(f'player called {choice}')
            else:
                choice = getEnvidoComputer(envidoIndex)
                print(f'computer called {choice}')

            if envidoIndex == 0:
                if choice == 'e':
                    envidoIndex = 1
                elif choice == 're':
                    envidoIndex = 3
                elif choice == 'fe':
                    envidoIndex = 4
                elif choice == 'pass':
                    return 0
                envidoPath += choice

            elif envidoIndex == 1:
                if choice == 'q':
                    winner = findWinner(playerCards, computerCards, turn)
                elif choice == 'n':
                    winner = swapTurn(turn)
                elif choice == '2e':
                    envidoIndex = 2
                elif choice == 're':
                    envidoIndex = 3
                elif choice == 'fe':
                    envidoIndex = 4
                envidoPath += choice

            elif envidoIndex == 2:
                if choice == 'q':
                    winner = findWinner(playerCards, computerCards, turn)
                elif choice == 'n':
                    winner = swapTurn(turn)
                elif choice == 're':
                    envidoIndex = 3
                elif choice == 'fe':
                    envidoIndex = 4
                envidoPath += choice

            elif envidoIndex == 3:
                if choice == 'q':
                    winner = findWinner(playerCards, computerCards, turn)
                elif choice == 'n':
                    winner = swapTurn(turn)
                elif choice == 'fe':
                    envidoIndex = 4
                envidoPath += choice

            elif envidoIndex == 4:
                if choice == 'q':
                    winner = findWinner(playerCards, computerCards, turn)
                elif choice == 'n':
                    winner = swapTurn(turn)
                envidoPath += choice

            if envidoPath[-1] in ['q', 'n']:
                break

            turn = swapTurn(turn)
        pointsAtRisk = ENVIDO_PATHS[envidoPath]
        return winner, pointsAtRisk

    return main(turn, envidoIndex=0, pointsAtRisk=0)
