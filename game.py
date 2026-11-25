from tiles import create_pool,deal_deck,draw_tile,play_set,get_tile_index
from turn import read_player_move,find_computer_move,check_winner,check_less_tiles
from logs import show_player_hand,show_table,show_playd_tiles,clear_terminal
def play_game():
    clear_terminal()
    print("""
============== WELCOME TO RUMMIKUB ==========
    """)
    table = []
    count = 0
    deck = create_pool()
    player,comp = deal_deck(deck)
    while True:
        if check_winner(player,comp):
            break
        if len(deck) == 0:
            check_less_tiles(player,comp)
            break
        if count % 2 == 0:
            print(f"\nTable:")
            show_table(table)
            print(f"Computer tiles: {len(comp)}")
            print(f"\nYour hand:")
            show_player_hand(player)
            hand = player
            move = read_player_move(player)
            clear_terminal()
        else:
            hand = comp
            move = find_computer_move(comp)
        if move == None:
            draw_tile(deck,hand)
        else:
            play_set(hand,table,move)
            if count % 2 == 0:
                show_playd_tiles("player",move)
            else:
                show_playd_tiles("comp",move)
        count += 1
        if check_winner(player,comp):
            break





