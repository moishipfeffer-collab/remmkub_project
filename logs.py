import os
def clear_terminal():
    os.system('cls' if os.name == 'nt' else "clear")

def show_player_hand(hand):
    for i in range(len(hand)):
        print(f"[{i+1}] {hand[i]}")

def show_table(table):
    if not table:
        print("empty")
    else:
        for i in range(len(table)):
            print(f"[{i+1}] {table[i]}")

def show_playd_tiles(player,tiles):
    if player == "comp":
        print(f"\nComputer played: {tiles}")
    else:
        print(f"\nYou played: {tiles}")


    