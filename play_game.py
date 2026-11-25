from tiles import create_pool,deal_deck,draw_tile,play_set,get_tile_index
from turn import read_player_move,find_computer_move
def play_game():
    table = []
    count = 0
    deck = create_pool()
    player,comp = deal_deck(deck)
    while True:
        print(f"Table: {table}")
        if count % 2 == 0:
            hand = player
            print(f"tiles:\n{player}")
            move = read_player_move(player)
        else:
            hand = comp
            move = find_computer_move(comp)
        if move == None:
            draw_tile(deck,hand)
        else:
            indexes = get_tile_index(move,hand)
            print(indexes)
            print(len(hand))
            play_set(hand,table,indexes)
        count += 1



play_game()

