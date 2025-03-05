import card_counting

def check_black_jack(hand):
    hand_val = calculate_hand_value(hand)
    if hand_val == 21:
        card_counting.best_move = ""
        return True
    return False

def check_bust(hand):
    hand_val = calculate_hand_value(hand)
    if hand_val > 21:
        card_counting.best_move = ""  # Clear best move on bust
        return True
    return False

def calculate_hand_value(hand):
    value = 0
    aces = 0
    
    card_values = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, 
        "7": 7, "8": 8, "9": 9, 
        "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11
    }
    
    for card in hand:
        rank = card[:1]
        
        if rank == "1":
            rank = "10"
            
        if rank == "A":
            aces += 1
        value += card_values.get(rank, 0)

    # Adjust Aces from 11 to 1 if necessary
    while value > 21 and aces > 0:
        value -= 10
        aces -= 1

    return value
        
    
    


