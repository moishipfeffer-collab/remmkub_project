import random
def create_deck():
    deck = []
    colors = ["R","B","K","O"]
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    for color in colors:
        for number in numbers:
            deck.append((number,color))
    deck += deck

    return deck
        



def shuffle_cards(deck:list):
    count = 0
    while count < 1000:
        index_1 = random.randint(0,103)
        index_2 = random.randint(0,103)
        if index_2 != index_1:
            kipper = deck[index_1]
            deck[index_1] = deck[index_2]
            deck[index_2] = kipper
            count += 1

def create_pool():
    deck = create_deck()
    shuffle_cards(deck)
    return deck



def deal_deck(deck:list):
    comp = []
    player = []
    for i in range(9):
        player.append(deck.pop(0))
        comp.append(deck.pop(0))
    return player,comp

def get_tile_index(tiels,hand):
    indexes = []
    for tiel in tiels:
        indexes.append(hand.index(tiel))
    return indexes

def remove_tiles_from_hand(hand:list,tiles):
    for tile in tiles:
        hand.remove(tile)



def play_set(hand:list, table:list, tiles:list):
    indexes = get_tile_index(tiles,hand)
    play_tiles = []
    for index in indexes:
        play_tiles.append(hand[index])
    table.append(play_tiles)     
    remove_tiles_from_hand(hand,tiles)





def draw_tile(deck:list,hand:list):
    hand.append(deck.pop(0))
