import random


class player(object):
    # The class "constructor" - It's actually an initializer
    def __init__(self):
        self.hand = []
        self.purse = purse()
        self.points = 0
        self.nobles = []


class purse(object):
    # The class "constructor" - It's actually an initializer
    def __init__(self):
        self.black = 0
        self.white = 0
        self.red = 0
        self.blue = 0
        self.green = 0


def init_player():
    curr_player = player()
    return curr_player


def add_to_hand(id, player, boardstate):

    rowcol = get_row_card_from_id(id, boardstate)
    Row = rowcol[0]
    Column = rowcol[1]

    # add card to hand
    player.hand.append(eval("boardstate.row" + str(Row) + ".card" + str(Column)))

    #add points
    player.points = player.points + eval("boardstate.row" + str(Row) + ".card" + str(Column) + ".points")

    #remove coins
    card_cost = get_card_cost(id, boardstate)
    pay_coins(card_cost, player)
    return 0


def decide_card(player, boardstate):

    rng_list1 = [1, 2, 3]
    rng_list2 = [1, 2, 3, 4]
    random.shuffle(rng_list1)
    for num1 in rng_list1:
        for num2 in rng_list2:
            if eval("boardstate.row" + str(num1) + ".card" + str(num2) + ".black") > player.purse.black + get_hand_value(player, "black"):
                continue
            if eval("boardstate.row" + str(num1) + ".card" + str(num2) + ".white") > player.purse.white + get_hand_value(player, "white"):
                continue
            if eval("boardstate.row" + str(num1) + ".card" + str(num2) + ".red") > player.purse.red + get_hand_value(player, "red"):
                continue
            if eval("boardstate.row" + str(num1) + ".card" + str(num2) + ".blue") > player.purse.blue + get_hand_value(player, "blue"):
                continue
            if eval("boardstate.row" + str(num1) + ".card" + str(num2) + ".green") > player.purse.green + get_hand_value(player, "green"):
                continue
            return eval("boardstate.row" + str(num1) + ".card" + str(num2) + ".ID")

    return 0


def decide_coins(player, boardstate):

    coins_to_take = [0, 0, 0, 0, 0]
    coins = 0
    #Randomize coins
    while coins < 3:
        rng = random.randrange(5)
        if coins_to_take[rng] == 0:
            coins_to_take[rng] = 1
            coins = coins + 1

    return coins_to_take


def get_card_cost(id, boardstate):

    Row = get_row_card_from_id(id, boardstate)[0]
    Column = get_row_card_from_id(id, boardstate)[1]

    card_cost = [0, 0, 0, 0, 0]

    # add card to hand
    curr_card = (eval("boardstate.row" + str(Row) + ".card" + str(Column)))

    card_cost[0] = curr_card.black
    card_cost[1] = curr_card.white
    card_cost[2] = curr_card.red
    card_cost[3] = curr_card.blue
    card_cost[4] = curr_card.green

    return card_cost


def take_coins(curr_purse, player):
    # add coins from purse to player
    player.purse.black = player.purse.black + curr_purse[0]
    player.purse.white = player.purse.white + curr_purse[1]
    player.purse.red = player.purse.red + curr_purse[2]
    player.purse.blue = player.purse.blue + curr_purse[3]
    player.purse.green = player.purse.green + curr_purse[4]
    return 0


def pay_coins(card_cost, player):

    # add coins from purse to player
    player.purse.black = player.purse.black + get_hand_value(player, "black") - card_cost[0]
    player.purse.white = player.purse.white + get_hand_value(player, "white") - card_cost[1]
    player.purse.red = player.purse.red + get_hand_value(player, "red") - card_cost[2]
    player.purse.blue = player.purse.blue + get_hand_value(player, "blue") - card_cost[3]
    player.purse.green = player.purse.green + get_hand_value(player, "green") - card_cost[4]
    return 0


def can_afford_card(player, card):

    for card_attr, card_value in card.__dict__.items():
        for purse_attr, purse_value in player.purse.__dict__.items():
            if card_attr == purse_attr:
                hand_value = get_hand_value(player, purse_attr)
                if card_value > (purse_value+hand_value):
                    return False

    return True


def can_afford_any_card(player, boardstate):

    for row_name, row in boardstate.__dict__.items():
        for card_name, card in row.__dict__.items():
            if can_afford_card(player, card):
                return True

    return False


def get_row_card_from_id(id, boardstate):
    row_card = [0,0]
    for row_name, row in boardstate.__dict__.items():
        for card_name, card in row.__dict__.items():
            if card.ID == id:
                row_card[0] = int(row_name[3:])
                row_card[1] = int(card_name[4:])
                return row_card

    return False


def decide_turn(player, boardstate):
    rng = random.randrange(2)
    take_card = False

    if can_afford_any_card(player, boardstate):
        if rng:
            if get_coin_num(player) > 7:
                take_card = True

    return take_card


def get_hand_value(player, color):
    points = 0
    if player.hand:
        for curr_card in player.hand:
            if curr_card.color == color:
                points = points + 1


    return points


def get_coin_num(player):
    coins = 0
    for color, value in player.purse.__dict__.items():
        coins = value + coins

    return coins


def check_for_nobles(playstate):

    # check if you can buy any nobles
    for indx, noble_card in enumerate(playstate.nobles):
        for noble_attr, attr_value in noble_card.__dict__.items():
            for purse_attr, purse_value in playstate.player.purse.__dict__.items():
                if noble_attr == purse_attr:
                    hand_value = get_hand_value(playstate.player, purse_attr)
                    if attr_value > hand_value:
                        return False
        # add points
        playstate.player.points = playstate.player.points + int(playstate.nobles[indx].points)
        # add noble to hand
        playstate.player.nobles.append(playstate.nobles.pop(indx))

    return 0


