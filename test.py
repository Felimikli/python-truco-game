import sys
import random

espada = ['e1', 'e2', 'e3', 'e4', 'e5',
          'e6', 'e7', 'e10', 'e11', 'e12']
basto = ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b10', 'b11', 'b12']
oro = ['o1', 'o2', 'o3', 'o4', 'o5', 'o6', 'o7', 'o10', 'o11', 'o12']
copa = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c10', 'c11', 'c12']
CARD_VALUES = {'e1': 1, 'b1': 2, 'e7': 3, 'o7': 4, 'e3': 5, 'b3': 5, 'o3': 5, 'c3': 5, 'e2': 6, 'b2': 6, 'o2': 6, 'c2': 6, 'o1': 7, 'c1': 7, 'e12': 8, 'b12': 8, 'o12': 8, 'c12': 8, 'e11': 9, 'b11': 9,
              'o11': 9, 'c11': 9, 'e10': 10, 'b10': 10, 'o10': 10, 'c10': 10, 'b7': 11, 'c7': 11, 'e6': 12, 'b6': 12, 'o6': 12, 'c6': 12, 'e5': 13, 'b5': 13, 'o5': 13, 'c5': 13, 'e4': 14, 'b4': 14, 'o4': 14, 'c4': 14, }
cards = espada + basto + oro + copa


def deal(numPlayer):
    player = 1
    data = {}
    while numPlayer > 0:
        playerCards = []
        numCardsDealt = 3
        while numCardsDealt > 0:
            randomCard = cards.pop(random.randrange(len(cards)))
            playerCards.append(randomCard)
            numCardsDealt -= 1
        data[f"player{player}"] = playerCards
        player += 1
        numPlayer -= 1

    return data

def truco():
    data = deal(2)
    turn = 'player'
    playerCardsThrown = []
    computerCardsThrown = []
    playerCards = []
    computerCards = []
    playerPoints = 0
    computerPoints = 0



    def game(turn, handIndex, data):
        nonlocal playerCards
        nonlocal computerCards
        playerCards = data['player1']
        computerCards = data['player2']



        def playerThrowCard(throwIndex):
            print(f"playerThrowCard")
            nonlocal playerCards
            nonlocal computerCards
            nonlocal playerCardsThrown
            nonlocal computerCardsThrown

            playerInput = ''
            msg = ''
            if throwIndex == 0:
                msg = f"press 1 for {playerCards[0]}, 2 for {playerCards[1]}, 3 for {playerCards[2]}\n\n"
                playerInput = input(msg)
            elif throwIndex == 1:
                msg = f"press 1 for {playerCards[0]}, 2 for {playerCards[1]}\n\n"
                playerInput = input(msg)
            elif throwIndex == 2:
                msg = f"press 1 for {playerCards[0]}\n\n"
                playerInput = input(msg)
            else:
                checkHandWinner()

            try:
                player = int(playerInput)
            except ValueError:
                print(f"Invalid input, {msg}")
                playerThrowCard(throwIndex)
            else:
                if player >= 1 and player <= len(playerCards):
                    for playerCard in playerCards:
                        if player-1 == playerCards.index(playerCard):
                            playerCardsThrown.append(playerCards.pop(playerCards.index(playerCard)))
                            computerThrowCard(computerCardsThrown)
                            checkHandWinner(throwIndex, playerCardsThrown, computerCardsThrown)
                            break
                        else:
                            continue
                else:
                    print("Invalid input, enter 1, 2 or 3")
                    playerThrowCard(throwIndex)
            pass



        def computerThrowCard(computerCardsThrown):
            print(f"computerThrowCard{computerCards, computerCardsThrown}")
            if computerCards != []:
                computerCardsThrown.append(computerCards.pop(random.randrange(len(computerCards))))
                print(f"momo{computerCards, computerCardsThrown}")
            else:
                pass


        def checkHandWinner(handIndex, playerCardsThrown, computerCardsThrown):
            print("checkHandWinner")
            nonlocal playerPoints
            nonlocal computerPoints
            nonlocal turn


            if CARD_VALUES[playerCardsThrown[handIndex]] == CARD_VALUES[computerCardsThrown[handIndex]]:
                print(f"Empate, turno de {turn}")
                playerPoints += 1
                computerPoints += 1
                checkWinner(playerPoints, computerPoints, turn, handIndex)
            elif CARD_VALUES[playerCardsThrown[handIndex]] > CARD_VALUES[computerCardsThrown[handIndex]]:
                print(f"Tiraste el {playerCardsThrown[handIndex]}")
                print(f"La computadora tiró {computerCardsThrown[handIndex]}")
                turn = "computer"
                computerPoints += 1
                checkWinner(playerPoints, computerPoints, turn, handIndex)
            else:
                print(f"Tiraste el {playerCardsThrown[handIndex]}")
                print(f"La computadora tiró {computerCardsThrown[handIndex]}")
                turn = "player"
                playerPoints += 1
                checkWinner(playerPoints, computerPoints, turn, handIndex)


    
        def checkWinner(playerPoints, computerPoints, turn, handIndex):
            print("checkWinner")
            if playerPoints == 2:
                #print(f"Player WINS!")
                again()
            elif computerPoints == 2:
                #print(f"Computer WINS!")
                again()
            else:
                print("im 0")
                game(turn, handIndex + 1, data)

            print(f"checkWinner: Player points: {playerPoints}")
            print(f"checkWinner: {turn} ganó la {handIndex + 1} mano")
            print(f"checkWinner: Player Cards: {playerCards}, Thrown: {playerCardsThrown}")
            print(f"checkWinner: Computer Cards: {computerCards}, Thrown: {computerCardsThrown}")
            print(f"checkWinner: Tiraste el {playerCardsThrown[handIndex]}")
            print(f"checkWinner: La computadora tiró {computerCardsThrown[handIndex]}")

        def again():
            nonlocal turn
            playAgainInput = input(f"\nPlay again?\nPress Y to play again or Q to quit.\n")
            playAgain = str(playAgainInput)
            print(f"again: playAgain.capitalize {playAgain}")

            if playAgain == "y":
                print("playing again")
                truco()
            elif playAgain == "q":
                print("byebye")
                quit()
            else:
                print("Invalid input, press Y to play again or Q to quit.\n")
                again()
        playerThrowCard(handIndex)
    
    if turn == 'player':
        print("im 1")
        game(turn, 0, data)
    elif turn == 'computer':
        print("im 2")
        game(turn, 0, data)
    else:
        pass
        
        print(f"game")
    print(f"truco")



truco()
