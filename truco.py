import random
from constants import swapTurn


def getPlayerTruco(trucoPointsAtRisk):
    options = {
        0: ['truco', 'pass'],
        1: ['quiero', 'no quiero', 'retruco'],
        2: ['quiero', 'no quiero', 'valecuatro'],
        3: ['quiero', 'no quiero']
    }
    playerChoice = str(
        input(f'press {", ".join(options[trucoPointsAtRisk])}\n'))
    if playerChoice in options[trucoPointsAtRisk]:
        return playerChoice
    else:
        print('Invalid Input:\n')
        return getPlayerTruco(trucoPointsAtRisk)


def getComputerTruco(trucoPointsAtRisk):
    options = {
        0: ['truco', 'pass'],
        1: ['quiero', 'no quiero', 'retruco'],
        2: ['quiero', 'no quiero', 'valecuatro'],
        3: ['quiero', 'no quiero']
    }
    return random.choice(options[trucoPointsAtRisk])


def callTruco(trucoPointsAtRisk, turn):

    for _ in range(4):
        choice = ''
        if turn == 'player':
            choice = getPlayerTruco(trucoPointsAtRisk)
            print(f'player called {choice}')
        else:
            choice = getComputerTruco(trucoPointsAtRisk)
            print(f'computer called {choice}')

        if choice == 'quiero':
            trucoPointsAtRisk += 1
            break
        elif choice == 'no quiero':
            break
        elif choice in ['truco', 'retruco', 'valecuatro']:
            trucoPointsAtRisk += 1
        else:
            pass
        turn = swapTurn(turn)
    return trucoPointsAtRisk


print(callTruco(0, 'player'))
