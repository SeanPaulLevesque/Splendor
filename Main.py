import DeckUtils as Deck
import HandUtils as Hand
import GameUtils as Game
import jsonpickle
import json
import copy

turns = 0
turn_check = 50
iterations = 0

# initialize game
Decks = Deck.build_decks()
Nobles = Deck.build_nobles()
boardstate = Deck.init_boardstate()
player1 = Hand.init_player()

# Deal Cards and nobles
Deck.deal_cards(Decks, boardstate)

# create initial playstate and save a copy for recall later
playstate = Deck.play_state(Decks, Nobles, boardstate, player1, turns)
saved = copy.deepcopy(playstate)

# json_object = jsonpickle.encode(playstate)
#
# with open('data.txt', 'w') as outfile:
#     json.dump(json_object, outfile)

with open('data.txt') as json_file:
    data = json.load(json_file)

playstate = jsonpickle.decode(data)
saved = copy.deepcopy(playstate)

# Define strategy



while 1:
    while playstate.player.points < 15:

        # decide if you are buying a card or drawing coins
        take_card = Hand.decide_turn(playstate.player, playstate.boardstate)

        if take_card:
            # Decide which card you want
            cardID = Hand.decide_card(playstate.player, playstate.boardstate)

            # Buy a card
            Hand.add_to_hand(cardID, playstate.player, playstate.boardstate)

            # deal a card to replace the one you bought
            Deck.deal_one_card(cardID, playstate.decks, playstate.boardstate, playstate.player)

            # check for nobles
            Hand.check_for_nobles(playstate)

        if not take_card:
            # decide how many and what color coins
            coins_to_take = Hand.decide_coins(playstate.player, playstate.boardstate)
            # take coins
            Hand.take_coins(coins_to_take, playstate.player)

        #Game.print_play_state(boardstate)
        turns = turns + 1
    playstate.turns = turns
    turns = 0

    json_object = jsonpickle.encode(playstate)

    with open('GameStates\data' + str(iterations) + '.txt', 'w') as outfile:
        json.dump(json_object, outfile)

    iterations = iterations + 1

    playstate = copy.deepcopy(saved)

    #restore playstate
    if iterations > 1000:
        break

game = 'done'


