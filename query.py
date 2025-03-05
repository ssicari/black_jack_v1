import sqlite3


def find_best_move(player_hand, dealer_card, count):
    player_hand = ["10" if card[0] in ["K", "Q", "J"] else card for card in player_hand]
    
    if dealer_card and dealer_card[0] in ["K", "Q", "J"]:
        dealer_card = 10

    # Check if it's a pair (e.g., "T,T" or "9,9")
    if len(player_hand) == 2 and player_hand[0] == player_hand[1]:
        player_hand_str = f"{player_hand[0]},{player_hand[1]}"
    
    else:
        # Convert player hand into a hard total (sum the values)
        total = 0
        aces = 0
        card_values = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, 
            "7": 7, "8": 8, "9": 9, "10": 10, "A": 11
        }

        for card in player_hand:
            if card == "A":
                aces += 1
            total += card_values.get(card, 0)

        # Adjust for Aces (A = 11 unless total exceeds 21, then A = 1)
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1

        # Convert final total to a string for querying
        player_hand_str = str(total)
    
    connection = sqlite3.connect("basic_strategy.db")
    cursor = connection.cursor()
    
    print(f"Querying for: player_hand={player_hand_str}, dealer_upcard={dealer_card}")
    
    cursor.execute("""
        SELECT recommended_move FROM basic_strategy
        WHERE player_hand = ? AND dealer_upcard = ?
    """, (player_hand_str, dealer_card))
    
    best_move = cursor.fetchone()
    
    if best_move:
        best_move = best_move[0]
        
    else:
        connection.close()
        return "Unknown"
    
    cursor.execute("""
        SELECT adjusted_move FROM illustrious_eighteen
        WHERE player_hand = ? AND dealer_upcard = ? AND true_count_threshold <= ?
        ORDER BY true_count_threshold DESC LIMIT 1
    """, (player_hand_str, dealer_card, count))
    
    override_move = cursor.fetchone()
    
    connection.close()
    
    if override_move:
        best_move = override_move[0]
        return best_move
    
    return best_move