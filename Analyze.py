import os.path
import jsonpickle
import json


iterations = 0
hand_length = []
noble_length = []
turn_length = []

while os.path.exists('GameStates\data' + str(iterations) + '.txt'):
    with open('GameStates\data' + str(iterations) + '.txt') as json_file:
        data = json.load(json_file)
        playstate = jsonpickle.decode(data)
        hand_length.append(playstate.player.hand.__len__())
        noble_length.append(playstate.player.nobles.__len__())
        turn_length.append(playstate.turns)
        iterations = iterations + 1

import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Histogram(x=turn_length)],
    layout_title_text="Turns Per Game With Random Strategy"
)
fig.show()
program = "done"



