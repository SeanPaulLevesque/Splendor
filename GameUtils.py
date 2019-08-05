from datetime import date

def serialize(obj):
    if isinstance(obj, date):
        serial = obj.isoformat()
        return serial

    return obj.__dict__

def print_play_state(boardstate):

    all_cards = []
    # print(boardstate.noble1.Red)
    for name, rows in boardstate.__dict__.items():
        for cards, values in rows.__dict__.items():
            print_card = []
            print_card.append("***************")
            print_card.append("** " + str(values.points) + "    " + str(values.color) + "**")
            print_card.append("** B W R L G **")
            print_card.append("** " + str(values.black) + " " + str(values.white) + " " + str(values.red) + " " + str(values.blue) + " " + str(values.green) + " **")
            print_card.append("***************")
            all_cards.append(print_card)

    for cards in all_cards:
        for line in cards:
            print(line)

    return