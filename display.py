from validations import check_index,is_valid_set

def choose_turn(hand):
    while True:
        choise = input("Choose tile positions or D to draw: > ")
        if choise != "D":
            indexes = list(map(int,choise.split()))  
            if check_index(indexes,hand):                
                return indexes
        elif choise.lower() == "d":                
            return choise
        print("Invalid set. Try again.")
        

def choose_cerds(hand:list,table:list,indexes:list):
    choosen_tiels = []
    for index in indexes:
        choosen_tiels.append(hand[index - 1])
    if is_valid_set(choosen_tiels):
        table.append(choosen_tiels)
        return choosen_tiels
    return False
    

