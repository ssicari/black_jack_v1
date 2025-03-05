Blackjack AI - Proof of Concept

© 2025 Sal Sicari

Overview

This project leverages YOLOv8 for real-time playing card detection, trained on a dataset from Kaggle. The system assigns detected cards to either the player or dealer, tracks the running and true count, and queries an SQLite database to determine optimal moves using Blackjack's basic strategy and strategy deviations based on card count.

Due to resource limitations, the model currently has some inconsistencies, requiring feature trade-offs. At this stage, the AI operates solely in a 1v1 player vs. dealer scenario.

Future Upgrades & Improvements

Code Structure & Optimization

Refactor the codebase to use object-oriented programming (OOP) by migrating functionality into dedicated classes instead of standalone functions.

Improve efficiency and readability for better maintainability.

Reliability & Performance Enhancements

Implement unit tests to handle edge cases and improve stability.

Retrain the YOLOv8 model for higher accuracy and reliability in card detection.

Introduce object tracking to prevent duplicate detections and improve game flow.

Implement deck penetration tracking to enhance strategic decision-making.

Advanced AI & Expanded Functionality

Train an end-to-end AI model that not only detects cards but also plays Blackjack and counts cards autonomously.

Explore reinforcement learning techniques to improve decision-making beyond basic strategy.

Investigate porting the AI to Meta AR glasses for an augmented reality Blackjack experience.

Current Limitations

The model is still finicky, requiring improvements in detection consistency.

Only supports a 1v1 scenario (player vs. dealer) at this time.

Object tracking is currently handled in a basic way, leading to occasional re-triggering of detections.

This is an evolving project with exciting potential. Contributions and suggestions are always welcome!
