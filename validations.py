def check_index(indexes:list,player_tiles:list):
    for index in indexes:
        if index > len(player_tiles):
            return False
        if index < 1:
            return False
    return True

def is_valid_set(tiles:list):
    if len(tiles) < 3:
        return False
    sorted_tiels_num = sorted(tiles,key=lambda t:t[0])   
    for i in range(len(sorted_tiels_num) - 1):
        if sorted_tiels_num[i] != sorted_tiels_num[i+1]:
            return False 
        if tiles[i][1] == tiles[i+1][1]:
            return False            
    return True
 
def draw_tile(deck:list,player:list):
    player.append(deck.pop(0))