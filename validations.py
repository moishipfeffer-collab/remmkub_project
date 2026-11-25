def check_index(indexes:list,player_tiles:list):
    for index in indexes:
        if index > len(player_tiles)+1:
            print(f"Thare is just {len(player_tiles)} tiels in your hand! ")
            return False
        if index < 1:
            print("can not choose a tile under then 1!")
            return False
        if indexes.count(index) > 1:
            print("can not choose the same card!")
            return False
    return True

def is_valid_set(tiles:list):
    if len(tiles) < 3:
        return False
    sorted_tiels_num = sorted(tiles,key=lambda t:t[0])
    valid_same_color = True
    valid_same_num = True
    for i in range(len(tiles) - 1):
        if tiles.count(tiles[i]) > 1:
            return False
        if sorted_tiels_num[i][0] != sorted_tiels_num[i+1][0]-1 or sorted_tiels_num[i][1] != sorted_tiels_num[i+1][1]:
            valid_same_color = False
        if sorted_tiels_num[i][0] != sorted_tiels_num[i+1][0]:
            valid_same_num = False

    if valid_same_num or valid_same_color: 
        return True
    
    else:
        return False 