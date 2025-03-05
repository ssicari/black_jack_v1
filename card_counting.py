import game_logic
import query

card_values = {
    "2" : 1, "3" : 1, "4" : 1, "5": 1, "6" : 1, # plus one
    "7" : 0, "8" : 0, "9" : 0, # neutral 
    "10" : -1, "J" : -1, "Q" : -1, "K" : -1, "A" : -1 # minus one
}

count = 0
dealer_face_up_card = None
players_hand = []
dealers_hand = []
counted_cards = set()
status_msg = ""
best_move = ""

def update_count(card_label):
    global count
    
    if card_label in counted_cards:
        return
    
    counted_cards.add(card_label)
    
    num = card_values.get(card_label, None)
    
    if num == 1:
        count += 1
        
    elif num == (-1):
        count -= 1
        
    print(f"Updated count: {count}") 

def update_player_hand(card_label):
    
    global status_msg 
    
    if card_label not in players_hand:
        players_hand.append(card_label)
        update_count(card_label)
        
        if game_logic.check_black_jack(players_hand):
            status_msg = "Blackjack!"
        elif game_logic.check_bust(players_hand):
            status_msg = "Bust"

def update_dealer_hand(card_label):
    global dealer_face_up_card
    
    if dealer_face_up_card is None:
        dealer_face_up_card = card_label
        update_count(card_label)
    
    if card_label not in dealers_hand:
        dealers_hand.append(card_label)
        update_count(card_label)
        
def query_best_move():
    global best_move
    
    best_move = query.find_best_move(players_hand, dealer_face_up_card, count)

def reset_hands_in_between_rounds():
    global status_msg
    global best_move
    global dealer_face_up_card
    
    dealer_face_up_card = None
    players_hand.clear()
    dealers_hand.clear()
    counted_cards.clear()
    status_msg = ""
    best_move = ""