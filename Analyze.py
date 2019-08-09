import os.path
import jsonpickle
import json


iterations = 0
hand_length = []
noble_length = []
turn_length = []
playstate_list = []
min_turns = 50
max_turns = 0
card_fig1 = []
card_fig1.append([])
i=0
while os.path.exists('GameStates\data' + str(iterations) + '.txt'):
    with open('GameStates\data' + str(iterations) + '.txt') as json_file:
        data = json.load(json_file)
        playstate = jsonpickle.decode(data)
        hand_length.append(playstate.player.hand.__len__())
        noble_length.append(playstate.player.nobles.__len__())
        turn_length.append(playstate.turns)
        if playstate.turns < min_turns:
            min_turns = playstate.turns
        if playstate.turns > max_turns:
            max_turns = playstate.turns
        iterations = iterations + 1


        if playstate.turns < 18:
            playstate_list.append(playstate)
        else:
            card_fig1.append([])
            for cards in playstate.player.hand:
                card_fig1[i].append(cards.points)
            i = i + 1

import plotly.graph_objects as go

CardPoints1 = go.Figure()
for trace in card_fig1:
    CardPoints1.add_trace(go.Scatter(y=trace, mode='lines'))
CardPoints1.show()

card_fig2 = []
card_fig2.append([])
i = 0
#analyze good games
for game in playstate_list:
    card_fig2.append([])
    for cards in game.player.hand:
        card_fig2[i].append(cards.points)
    i = i + 1

CardPoints2 = go.Figure()
for trace in card_fig2:
    CardPoints2.add_trace(go.Scatter(y=trace, mode='lines'))
CardPoints2.show()

# TurnsPerGame = go.Figure(data=[go.Histogram(x=turn_length, nbinsx=(max_turns - min_turns)*2)], layout_title_text="Turns Per Game With Random Strategy")
# TurnsPerGame.show()
#
# NoblesvsTurn = go.Figure(data=[go.Scatter(x=turn_length, y=noble_length, size="pop")], layout_title_text="Noble Count vs Turn Count")
# NoblesvsTurn.show()
#
# HandCountvsTurnCount = go.Figure(data=go.Scatter(x=turn_length, y=hand_length, mode='markers'), layout_title_text="Hand Count vs Turn Count")
# HandCountvsTurnCount.show()





program = "done"



