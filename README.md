# README

# Proof of Concept

//Copywrite 2025 Sal Sicari

This project trained the YOLOv8 model on a card dataset from Kaggle. Currenlty it detects the card and assingns the ones dealt to you and the dealer. It keeps track of the count of the cards. It then sends and sqlite query to a database file that has black jacks basic strategy and basic strategy deviations based of the card count. Due to limited resources the current model is finicky, so features had to be cut for the time being. Currently this only works in a 1v1 you vs the dealer scneario. 

Future Upgrads:
- overhaul code and optimize it (I would like to migrate these into separte classes instead of just functions)
- unit tests to handle edge cases
- retrain model to have a higher reliability
- implement object tracking to avoid retriggers of card detection in a cleaner way than currently handled
- implement deck penetration
- potentially train a model to have more than just card detection. i.e. train it to also play black jack and count cards in the model itself. May be resouce intensive
- port to Meta AR glasses
