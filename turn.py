from validations import check_index,is_valid_set

def get_played_tiles(indexes,hand):
    chosen_tiles = []
    for index in indexes:
        chosen_tiles.append(hand[index - 1])
    return chosen_tiles

def read_player_move(hand):
    while True:
        choises = input("\nChoose tile positions or D to draw: > ")
        if choises.strip().lower() == "d":
            return None
        try:
            choises = list(map(int,choises.split()))  
        except ValueError: 
            print("enter nums or D only!")
            continue
        if check_index(choises,hand):
            choosen_tiles = get_played_tiles(choises,hand)
            if is_valid_set(choosen_tiles):                
                return choosen_tiles
            else:
                print("Invalid set. Try again.")



def find_computer_move(hand):
    list_by_num = sorted(hand,key=(lambda h: (h[0],h[1])))
    list_by_color = sorted(hand,key=(lambda h: (h[1],h[0])))
    for i in range(len(list_by_num)-2):
        first = list_by_num[i]
        second = list_by_num[i+1]
        third = list_by_num[i+2]
        choosen_tiels = [first,second,third]
        if is_valid_set(choosen_tiels):
            for i in range(len(list_by_num)):
                if list_by_num[i][0] == choosen_tiels[-1][0] and list_by_num[i] not in choosen_tiels:
                    choosen_tiels.append(list_by_num[i])
            return choosen_tiels
    for i in range(len(list_by_color) - 2):
        first = list_by_color[i]
        second = list_by_color[i+1]
        third = list_by_color[i+2]
        choosen_tiels = [first,second,third]
        if is_valid_set(choosen_tiels):
            for i in range(len(list_by_color)):
                if list_by_color[i][0] == choosen_tiels[-1][0] + 1 and list_by_color[i][1] == choosen_tiels[-1][1] and list_by_color[i] not in choosen_tiels:
                    choosen_tiels.append(list_by_color[i]) 
            return choosen_tiels
    return None
                
def check_winner(player,comp):
    if len(player) == 0:
        print("======= PLAYER IS THE WINNER ========")
        return True
    elif len(comp) == 0:
        print("======= COPUTER IS THE WINNER ========")
        return True
    return None

def check_less_tiles(player,comp):
    if len(player) < len(comp):
        print("\n======= PLAYER WIN =======")
    elif len(player) > len(comp):
        print("\n====== COMPUTER WIN ======")
    else:
        print("\n======= DRAW =======")
