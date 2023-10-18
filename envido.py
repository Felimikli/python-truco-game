from icecream import ic


def envido(cards):  # , computerCards, envidoInput):
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
