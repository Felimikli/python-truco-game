import math
import random

espada = ['e1', 'e2', 'e3', 'e4', 'e5',
          'e6', 'e7', 'e10', 'e11', 'e12']
basto = ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b10', 'b11', 'b12']
oro = ['o1', 'o2', 'o3', 'o4', 'o5', 'o6', 'o7', 'o10', 'o11', 'o12']
copa = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c10', 'c11', 'c12']
cardValues = {'e1': 1, 'b1': 2, 'e7': 3, 'o7': 4, 'e3': 5, 'b3': 5, 'o3': 5, 'c3': 5, 'e2': 6, 'b2': 6, 'o2': 6, 'c2': 6, 'o1': 7, 'c1': 7, 'e12': 8, 'b12': 8, 'o12': 8, 'c12': 8, 'e11': 9, 'b11': 9,
              'o11': 9, 'c11': 9, 'e10': 10, 'b10': 10, 'o10': 10, 'c10': 10, 'b7': 11, 'c7': 11, 'e6': 12, 'b6': 12, 'o6': 12, 'c6': 12, 'e5': 13, 'b5': 13, 'o5': 13, 'c5': 13, 'e4': 14, 'b4': 14, 'o4': 14, 'c4': 14, }
cards = espada + basto + oro + copa


def truco():
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

    def game():
        data = deal(2)
        playerCards = data['player1']
        computerCards = data['player2']
        playerCardsThrown = []
        computerCardsThrown = []

        def checkWinner(hand):

            computerCardsThrown.append(computerCards.pop(random.randrange(len(computerCards))))
            turn = 'player'
            print(hand)
            print(playerCards, playerCardsThrown)
            print(computerCards, computerCardsThrown)
            print(f"Tiraste el {playerCardsThrown[hand]}")
            print(f"La computadora tiró {computerCardsThrown[hand]}")
            if cardValues[playerCardsThrown[hand]] == cardValues[computerCardsThrown[hand]]:
                print(f"Empate, turno de {turn}")
            if cardValues[playerCardsThrown[hand]] > cardValues[computerCardsThrown[hand]]:
                turn = "computer"
            else:
                turn = "player"
            print(f"\n{turn} ganó la {hand + 1} mano\n")

            if turn == 'player':
                throwCard(hand + 1)

        def throwCard(throwIndex):
            nonlocal playerCards
            if throwIndex == 0:
                msg = f"press 1 for {playerCards[0]}, 2 for {playerCards[1]}, 3 for {playerCards[2]}\n\n"
                playerInput = input(msg)
            elif throwIndex == 1:
                msg = f"press 1 for {playerCards[0]}, 2 for {playerCards[1]}\n\n"
                playerInput = input(msg)

            try:
                player = int(playerInput)
            except ValueError:
                print(f"Invalid input, {msg}")
                throwCard(throwIndex)
            else:
                if player >= 1 and player <= len(playerCards):
                    for playerCard in playerCards:
                        if player-1 == playerCards.index(playerCard):
                            playerCardsThrown.append(playerCards.pop(playerCards.index(playerCard)))
                            checkWinner(throwIndex)
                            break
                        else:
                            continue
                else:
                    print("Invalid input, enter 1, 2 or 3")
                    throwCard(throwIndex)

            # if firstPlayer == 1:
            #     firstPlayerCardThrown = playerCards.pop(0)
            # elif firstPlayer == 2:
            #     firstPlayerCardThrown = playerCards.pop(1)
            # elif firstPlayer == 3:
            #     firstPlayerCardThrown = playerCards.pop(2)
            # else:
            #     print("Invalid input, enter 1, 2 or 3")

        throwCard(0)



#             secondPlayerInput = input(
#                 f"\npress 1 for {playerCards[0]}, 2 for {playerCards[1]}\n")
#             secondPlayer = int(secondPlayerInput)
#             if secondPlayer == 1:
#                 playerCardsThrown.append(playerCards.pop(0))
#             elif secondPlayer == 2:
#                 playerCardsThrown.append(playerCards.pop(1))
#             else:
#                 print("Invalid input, enter 1 or 2\n")

    game()


truco()
