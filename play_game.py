from tiles import create_pool,deal_deck
from display import play_set,choose_turn
def play_game():
    table = []
    count = 0
    deck = create_pool()
    player,comp = deal_deck(deck)
    if count % 2 == 0:
        hand = player
    else:
        hand = comp
    choise = choose_turn(hand)
    if type(choise) == list:
        choosen_tiles = play_set(hand,table,choise) 
        print(choosen_tiles)



play_game()

