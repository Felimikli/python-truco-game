import random
from envido import envido
envidoTurn = 'computer'
envidoIndex = 0
pointsAtRisk = 0


def getEnvidoPlayer(envidoIndex):
    if envidoIndex == 0:
        playerChoice = str(input(f'press e, re, fe, pass'))
        if playerChoice not in ['e', 're', 'fe', 'pass']:
            print('Invalid Input:\n')
            return getEnvidoPlayer(envidoIndex)
        return playerChoice

    elif envidoIndex == 1:
        playerChoice = str(input(f'press q, n, 2e, re, fe'))
        if playerChoice not in ['q', 'n', '2e', 're', 'fe']:
            print('Invalid Input:\n')
            return getEnvidoPlayer(envidoIndex)
        return playerChoice

    elif envidoIndex == 2:
        playerChoice = str(input(f'press q, n, re, fe'))
        if playerChoice not in ['q', 'n', 're', 'fe']:
            print('Invalid Input:\n')
            return getEnvidoPlayer(envidoIndex)
        return playerChoice

    elif envidoIndex == 3:
        playerChoice = str(input(f'press q, n, fe'))
        if playerChoice not in ['q', 'n', 'fe']:
            print('Invalid Input:\n')
            return getEnvidoPlayer(envidoIndex)
        return playerChoice

    elif envidoIndex == 4:
        playerChoice = str(input(f'press q, n'))
        if playerChoice not in ['q', 'n']:
            print('Invalid Input:\n')
            return getEnvidoPlayer(envidoIndex)
        return playerChoice


def getEnvidoComputer(envidoIndex):
    if envidoIndex == 0:
        return random.choice(['e', 're', 'fe', 'pass'])
    elif envidoIndex == 1:
        return random.choice(['q', 'n', '2e', 're', 'fe'])
    elif envidoIndex == 2:
        return random.choice(['q', 'n', 're', 'fe'])
    elif envidoIndex == 3:
        return random.choice(['q', 'n', 'fe'])
    elif envidoIndex == 4:
        return random.choice(['q', 'n'])


for x in range(6):
    choice = ''
    if envidoTurn == 'player':
        choice = getEnvidoPlayer(envidoIndex)
        envidoTurn = 'computer'
    else:
        choice = getEnvidoComputer(envidoIndex)
        print(f'computer called {choice}')
        envidoTurn = 'player'

    if envidoIndex == 0:
        if choice == 'e':
            envidoIndex = 1
            pointsAtRisk += 1
        elif choice == 're':
            envidoIndex = 3
            pointsAtRisk += 1
        elif choice == 'fe':
            envidoIndex = 4
            pointsAtRisk += 1
        elif choice == 'pass':
            if x > 0:
                break
            pass

    elif envidoIndex == 1:
        if choice == 'q':
            pointsAtRisk += 1
            print(pointsAtRisk)
            # envido()
            break
        elif choice == 'n':
            print(pointsAtRisk)
            break
        elif choice == '2e':
            envidoIndex = 2
            pointsAtRisk += 1
        elif choice == 're':
            envidoIndex = 3
            pointsAtRisk += 1
        elif choice == 'fe':
            envidoIndex = 4
            pointsAtRisk += 1

    elif envidoIndex == 2:
        if choice == 'q':
            pointsAtRisk += 2
            print(pointsAtRisk)
            # envido()
            break
        elif choice == 'n':
            print(pointsAtRisk)
            break
        elif choice == 're':
            envidoIndex = 3
            pointsAtRisk += 2
        elif choice == 'fe':
            envidoIndex = 4
            pointsAtRisk += 2

    elif envidoIndex == 3:
        if choice == 'q':
            pointsAtRisk += 3
            print(pointsAtRisk)
            # envido()
            break
        elif choice == 'n':
            print(pointsAtRisk)
            break
        elif choice == 'fe':
            envidoIndex = 4
            pointsAtRisk += 2

    elif envidoIndex == 4:
        if choice == 'q':
            pointsAtRisk += 30
            print(pointsAtRisk)
            # envido()
            break
        elif choice == 'n':
            print(pointsAtRisk)
            break
