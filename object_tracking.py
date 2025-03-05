from ultralytics import YOLO
import cv2
import card_counting
import game_logic
import query

# Load the YOLO model
model = YOLO(r"C:\Users\ssica\Documents\coding shit\black_jack_v1\black_jack_models\best_new.pt")

def webcam_loop():
    cap = cv2.VideoCapture(0)  # Open webcam
    last_detected = None

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Run YOLO detection on the current frame
        results = model(frame, verbose = False)  # Get detection results

        # Process each detected card
        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = box.xyxy[0]  # Bounding box coordinates
                conf = box.conf[0]  # Confidence score
                class_id = int(box.cls[0])  # Get the class ID of the detected card
                card_label = model.names[class_id]  # Convert class ID to card name

                # Print the detected card
                print(f"Detected: {card_label} (Confidence: {conf:.2f})")
                if conf >= .45:
                    if last_detected != card_label:
                        last_detected = card_label
                        process_detected_cards(card_label)

                # Draw bounding box and label
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                cv2.putText(frame, f"{card_label} ({conf:.2f})", (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                            0.5, (0, 255, 0), 2)
                
        if card_counting.status_msg:
            cv2.putText(frame, card_counting.status_msg, (250, 250), cv2.FONT_HERSHEY_SIMPLEX, 
                            1, (0, 0, 255), 2)
            
        cv2.putText(frame, f"Count: {card_counting.count}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 
                            1, (0, 255, 255), 2)
            
        if card_counting.best_move:
            cv2.putText(frame, card_counting.best_move, (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                            1, (0, 255, 0), 2)

        # Display the frame
        cv2.imshow("Blackjack Detector", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
def process_detected_cards(card_label):
    
    if card_label != "JOKER":
        card_label = card_label[:1]
        if card_label == "1":
            card_label = "10"

    # Calculate the player's current hand value
    hand_val = game_logic.calculate_hand_value(card_counting.players_hand)
    print(f"Hand: {hand_val}")

    
    # if hand_val == 21:
    #     card_counting.best_move = ""
    #     card_counting.status_msg = "Blackjack"
    #     return
    
    # if hand_val >= 22:
    #     card_counting.best_move = ""
    #     card_counting.status_msg = "Bust"
    #     return  

    # Process the player's cards
    if len(card_counting.counted_cards) < 2:
        card_counting.update_player_hand(card_label)

    elif len(card_counting.counted_cards) == 2 and card_counting.dealer_face_up_card is None:
        card_counting.update_dealer_hand(card_label)
        print(f"{card_counting.players_hand}, {card_counting.dealer_face_up_card}")
        card_counting.update_count(card_label)

       
        card_counting.query_best_move()

    elif card_label == "JOKER":
        card_counting.reset_hands_in_between_rounds()

    else:
        card_counting.update_player_hand(card_label)
        card_counting.update_count(card_label)

        
        hand_val = game_logic.calculate_hand_value(card_counting.players_hand)

        if hand_val == 21:
            card_counting.best_move = ""
            #card_counting.status_msg = "Blackjack"
        elif hand_val >= 22:
            card_counting.best_move = ""
            #card_counting.status_msg = "Bust"
        else:
            card_counting.query_best_move() 

