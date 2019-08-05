import random
import HandUtils as Hand

Deck1 = []
Deck2 = []
Deck3 = []

# Object definitions


class card(object):
    # The class "constructor" - It's actually an initializer
    def __init__(self, color, Deck, points, black, white, red, blue, green, ID):
        self.color = color
        self.Deck = Deck
        self.points = points
        self.black = black
        self.white = white
        self.red = red
        self.blue = blue
        self.green = green
        self.ID = ID


class noble(object):
    # The class "constructor" - It's actually an initializer
    def __init__(self, Points, black, white, red, blue, green):
        self.points = Points
        self.black = black
        self.white = white
        self.red = red
        self.blue = blue
        self.green = green


class row(object):
    # The class "constructor" - It's actually an initializer
    def __init__(self, card1, card2, card3, card4):
        self.card1 = card1
        self.card2 = card2
        self.card3 = card3
        self.card4 = card4


class board_state(object):
    # The class "constructor" - It's actually an initializer
    def __init__(self, row1, row2, row3):
        self.row1 = row1
        self.row2 = row2
        self.row3 = row3

class play_state(object):
    # The class "constructor" - It's actually an initializer
    def __init__(self, decks, nobles, boardstate, player, turn):
        self.decks = decks
        self.nobles = nobles
        self.boardstate = boardstate
        self.player = player
        self.turn = turn


# Functions
def make_card_obj(color, deck, points, black, white, red, blue, green, id):
    card_obj = card(color, deck, points, black, white, red, blue, green, id)
    return card_obj


def make_nobles_obj(points, black, white, red, blue, green):
    nobles_obj = noble(points, black, white, red, blue, green)
    return nobles_obj


def build_decks():

    cardsfile = 'Cards'
    # Cost Order
    # [Color][Deck][Points][Black][White][Red][Blue][Green]
    with open(cardsfile) as Cards:
        for cnt, CurrCard in enumerate(Cards):
            createdcard = make_card_obj(CurrCard.split()[0], int(CurrCard.split()[1]), int(CurrCard.split()[2]), int(CurrCard.split()[3]), int(CurrCard.split()[4]), int(CurrCard.split()[5]), int(CurrCard.split()[6]), int(CurrCard.split()[7]), int(CurrCard.split()[8]))
            if createdcard.Deck == 1:
                Deck1.append(createdcard)
            elif createdcard.Deck == 2:
                Deck2.append(createdcard)
            elif createdcard.Deck == 3:
                Deck3.append(createdcard)

    # Shuffle Decks
    random.shuffle(Deck1)
    random.shuffle(Deck2)
    random.shuffle(Deck3)
    Decks = [Deck1, Deck2, Deck3]

    return Decks


def build_nobles():
    Nobles = []
    nobles_to_return = []
    noblesfile = 'Nobles'
    # Cost Order
    # [Points][Black][White][Red][Blue][Green]
    with open(noblesfile) as nobles:
        for cnt, CurrCard in enumerate(nobles):
            creatednoble = make_nobles_obj(CurrCard.split()[0], int(CurrCard.split()[1]), int(CurrCard.split()[2]), int(CurrCard.split()[3]), int(CurrCard.split()[4]), int(CurrCard.split()[5]))
            Nobles.append(creatednoble)

    # Shuffle Deck
    random.shuffle(Nobles)

    # pop 3
    nobles_to_return.append(Nobles.pop())
    nobles_to_return.append(Nobles.pop())
    nobles_to_return.append(Nobles.pop())

    return nobles_to_return


def init_boardstate():
    blankcard1 = card(0, 0, 0, 0, 0, 0, 0, 0, 0)
    blankcard2 = card(0, 0, 0, 0, 0, 0, 0, 0, 0)
    blankcard3 = card(0, 0, 0, 0, 0, 0, 0, 0, 0)
    blankcard4 = card(0, 0, 0, 0, 0, 0, 0, 0, 0)
    blankcard5 = card(0, 0, 0, 0, 0, 0, 0, 0, 0)
    blankcard6 = card(0, 0, 0, 0, 0, 0, 0, 0, 0)
    blankcard7 = card(0, 0, 0, 0, 0, 0, 0, 0, 0)
    blankcard8 = card(0, 0, 0, 0, 0, 0, 0, 0, 0)
    blankcard9 = card(0, 0, 0, 0, 0, 0, 0, 0, 0)
    blankcard10 = card(0, 0, 0, 0, 0, 0, 0, 0, 0)
    blankcard11 = card(0, 0, 0, 0, 0, 0, 0, 0, 0)
    blankcard12 = card(0, 0, 0, 0, 0, 0, 0, 0, 0)


    blankrow1 = row(blankcard1, blankcard2, blankcard3, blankcard4)
    blankrow2 = row(blankcard5, blankcard6, blankcard7, blankcard8)
    blankrow3 = row(blankcard9, blankcard10, blankcard11, blankcard12)
    #blanknoble = noble(0, 0, 0, 0, 0, 0)
    boardstate = board_state(blankrow1, blankrow2, blankrow3)
    return boardstate


def deal_cards(decks, boardstate):

    # Row 1
    boardstate.row1.card1 = decks[0].pop()
    boardstate.row1.card2 = decks[0].pop()
    boardstate.row1.card3 = decks[0].pop()
    boardstate.row1.card4 = decks[0].pop()
    # Row 2
    boardstate.row2.card1 = decks[1].pop()
    boardstate.row2.card2 = decks[1].pop()
    boardstate.row2.card3 = decks[1].pop()
    boardstate.row2.card4 = decks[1].pop()
    # Row 3
    boardstate.row3.card1 = decks[2].pop()
    boardstate.row3.card2 = decks[2].pop()
    boardstate.row3.card3 = decks[2].pop()
    boardstate.row3.card4 = decks[2].pop()

    #Nobles
    #boardstate.noble1 = nobles.pop()

#    for name, rows in boardstate.__dict__.items():
#        for cards, values in rows.__dict__.items():

    return 0



def deal_one_card(id, decks, boardstate, player):

    RowColum = Hand.get_row_card_from_id(id, boardstate)
    Row = RowColum[0]
    Column = RowColum[1]
    # Draw new card and add to boardstate
    if Row == 1:
        if Column == 1:
            boardstate.row1.card1 = decks[0].pop()
        elif Column == 2:
            boardstate.row1.card2 = decks[0].pop()
        elif Column == 3:
            boardstate.row1.card3 = decks[0].pop()
        elif Column == 4:
            boardstate.row1.card4 = decks[0].pop()
    if Row == 2:
        if Column == 1:
            boardstate.row2.card1 = decks[1].pop()
        elif Column == 2:
            boardstate.row2.card2 = decks[1].pop()
        elif Column == 3:
            boardstate.row2.card3 = decks[1].pop()
        elif Column == 4:
            boardstate.row2.card4 = decks[1].pop()
    if Row == 3:
        if Column == 1:
            boardstate.row3.card1 = decks[2].pop()
        elif Column == 2:
            boardstate.row3.card2 = decks[2].pop()
        elif Column == 3:
            boardstate.row3.card3 = decks[2].pop()
        elif Column == 4:
            boardstate.row3.card4 = decks[2].pop()


    return 0

