cards = ['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e10', 'e11', 'e12', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b10', 'b11',
         'b12', 'o1', 'o2', 'o3', 'o4', 'o5', 'o6', 'o7', 'o10', 'o11', 'o12', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c10', 'c11', 'c12']
# CARDS_SUITS = {'espada': ['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e10', 'e11', 'e12'],
#                'basto': ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b10', 'b11', 'b12'],
#                'oro': ['o1', 'o2', 'o3', 'o4', 'o5', 'o6', 'o7', 'o10', 'o11', 'o12'],
#                'copa': ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c10', 'c11', 'c12']}
CARD_VALUES = {'e1': 14, 'b1': 13, 'e7': 12, 'o7': 11, 'e3': 10, 'b3': 10, 'o3': 10, 'c3': 10, 'e2': 9, 'b2': 9, 'o2': 9, 'c2': 9, 'o1': 8, 'c1': 8, 'e12': 7, 'b12': 7, 'o12': 7, 'c12': 7, 'e11': 6, 'b11': 6,
               'o11': 6, 'c11': 6, 'e10': 5, 'b10': 5, 'o10': 5, 'c10': 5, 'b7': 4, 'c7': 4, 'e6': 3, 'b6': 3, 'o6': 3, 'c6': 3, 'e5': 2, 'b5': 2, 'o5': 2, 'c5': 2, 'e4': 1, 'b4': 1, 'o4': 1, 'c4': 1, }


def swapTurn(turn):
    if turn == 'computer':
        turn = 'player'
    else:
        turn = 'computer'
    return turn


ENVIDO_PATHS = {'passpass': 0, 'passeq': 2, 'passen': 1, 'passe2eq': 4, 'passe2en': 2, 'passe2ereq': 7, 'passe2eren': 4, 'passe2erefeq': 10, 'passe2erefen': 7, 'passe2efeq': 10,
                'passe2efen': 4, 'passereq': 5, 'passeren': 2, 'passerefeq': 10, 'passerefen': 5, 'passefeq': 10, 'passefen': 2, 'passreq': 10, 'passren': 1, 'passrefeq': 10, 'passrefen': 3, 'passfeq': 10, 'passfen': 1, 'eq': 2, 'en': 1, 'e2eq': 4, 'e2en': 2, 'e2ereq': 7, 'e2eren': 4, 'e2erefeq': 10, 'e2erefen': 7, 'e2efeq': 10,
                'e2efen': 4, 'ereq': 5, 'eren': 2, 'erefeq': 10, 'erefen': 5, 'efeq': 10, 'efen': 2, 'req': 3, 'ren': 1, 'refeq': 10, 'refen': 3, 'feq': 10, 'fen': 1}
