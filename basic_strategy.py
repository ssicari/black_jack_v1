import sqlite3


connection = sqlite3.connect("basic_strategy.db")


cursor = connection.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS basic_strategy (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        player_hand TEXT NOT NULL,
        dealer_upcard INTEGER NOT NULL,
        recommended_move TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS illustrious_eighteen (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        player_hand TEXT NOT NULL,
        dealer_upcard INTEGER NOT NULL,
        true_count_threshold INTEGER NOT NULL,
        adjusted_move TEXT NOT NULL
    )
""")

basic_strategy_data = [
    # Hard Totals
    ("17", 2, "Stand"), ("17", 3, "Stand"), ("17", 4, "Stand"), ("17", 5, "Stand"), ("17", 6, "Stand"),
    ("17", 7, "Stand"), ("17", 8, "Stand"), ("17", 9, "Stand"), ("17", 10, "Stand"), ("17", 11, "Stand"),
    ("16", 2, "Stand"), ("16", 3, "Stand"), ("16", 4, "Stand"), ("16", 5, "Stand"), ("16", 6, "Stand"),
    ("16", 7, "Hit"), ("16", 8, "Hit"), ("16", 9, "Hit"), ("16", 10, "Hit"), ("16", 11, "Hit"),
    ("15", 2, "Stand"), ("15", 3, "Stand"), ("15", 4, "Stand"), ("15", 5, "Stand"), ("15", 6, "Stand"),
    ("15", 7, "Hit"), ("15", 8, "Hit"), ("15", 9, "Hit"), ("15", 10, "Hit"), ("15", 11, "Hit"),
    ("14", 2, "Stand"), ("14", 3, "Stand"), ("14", 4, "Stand"), ("14", 5, "Stand"), ("14", 6, "Stand"),
    ("14", 7, "Hit"), ("14", 8, "Hit"), ("14", 9, "Hit"), ("14", 10, "Hit"), ("14", 11, "Hit"),
    ("13", 2, "Stand"), ("13", 3, "Stand"), ("13", 4, "Stand"), ("13", 5, "Stand"), ("13", 6, "Stand"),
    ("13", 7, "Hit"), ("13", 8, "Hit"), ("13", 9, "Hit"), ("13", 10, "Hit"), ("13", 11, "Hit"),
    ("12", 2, "Hit"), ("12", 3, "Hit"), ("12", 4, "Stand"), ("12", 5, "Stand"), ("12", 6, "Stand"),
    ("12", 7, "Hit"), ("12", 8, "Hit"), ("12", 9, "Hit"), ("12", 10, "Hit"), ("12", 11, "Hit"),
    ("11", 2, "Double"), ("11", 3, "Double"), ("11", 4, "Double"), ("11", 5, "Double"), ("11", 6, "Double"),
    ("11", 7, "Double"), ("11", 8, "Double"), ("11", 9, "Double"), ("11", 10, "Double"), ("11", 11, "Double"),
    ("10", 2, "Double"), ("10", 3, "Double"), ("10", 4, "Double"), ("10", 5, "Double"), ("10", 6, "Double"),
    ("10", 7, "Double"), ("10", 8, "Double"), ("10", 9, "Double"), ("10", 10, "Hit"), ("10", 11, "Hit"),
    ("9", 2, "Hit"), ("9", 3, "Double"), ("9", 4, "Double"), ("9", 5, "Double"), ("9", 6, "Double"),
    ("9", 7, "Hit"), ("9", 8, "Hit"), ("9", 9, "Hit"), ("9", 10, "Hit"), ("9", 11, "Hit"),
    ("8", 2, "Hit"), ("8", 3, "Hit"), ("8", 4, "Hit"), ("8", 5, "Hit"), ("8", 6, "Hit"),
    ("8", 7, "Hit"), ("8", 8, "Hit"), ("8", 9, "Hit"), ("8", 10, "Hit"), ("8", 11, "Hit"),

    # Surrender Rules
    ("16", 9, "Surrender"), ("16", 10, "Surrender"), ("16", 11, "Surrender"),
    ("15", 10, "Surrender"),

    # Soft Totals
    ("A,9", 2, "Stand"), ("A,9", 3, "Stand"), ("A,9", 4, "Stand"), ("A,9", 5, "Stand"), ("A,9", 6, "Stand"),
    ("A,9", 7, "Stand"), ("A,9", 8, "Stand"), ("A,9", 9, "Stand"), ("A,9", 10, "Stand"), ("A,9", 11, "Stand"),
    ("A,8", 2, "Stand"), ("A,8", 3, "Stand"), ("A,8", 4, "Stand"), ("A,8", 5, "Stand"), ("A,8", 6, "Double"),
    ("A,8", 7, "Stand"), ("A,8", 8, "Stand"), ("A,8", 9, "Hit"), ("A,8", 10, "Hit"), ("A,8", 11, "Hit"),
    ("A,7", 2, "Double"), ("A,7", 3, "Double"), ("A,7", 4, "Double"), ("A,7", 5, "Double"), ("A,7", 6, "Double"),
    ("A,7", 7, "Stand"), ("A,7", 8, "Stand"), ("A,7", 9, "Hit"), ("A,7", 10, "Hit"), ("A,7", 11, "Hit"),
    ("A,6", 2, "Hit"), ("A,6", 3, "Double"), ("A,6", 4, "Double"), ("A,6", 5, "Double"), ("A,6", 6, "Double"),
    ("A,6", 7, "Hit"), ("A,6", 8, "Hit"), ("A,6", 9, "Hit"), ("A,6", 10, "Hit"), ("A,6", 11, "Hit"),
    ("A,5", 2, "Hit"), ("A,5", 3, "Hit"), ("A,5", 4, "Double"), ("A,5", 5, "Double"), ("A,5", 6, "Double"),
    ("A,5", 7, "Hit"), ("A,5", 8, "Hit"), ("A,5", 9, "Hit"), ("A,5", 10, "Hit"), ("A,5", 11, "Hit"),
    ("A,4", 2, "Hit"), ("A,4", 3, "Hit"), ("A,4", 4, "Double"), ("A,4", 5, "Double"), ("A,4", 6, "Double"),
    ("A,4", 7, "Hit"), ("A,4", 8, "Hit"), ("A,4", 9, "Hit"), ("A,4", 10, "Hit"), ("A,4", 11, "Hit"),
    ("A,3", 2, "Hit"), ("A,3", 3, "Hit"), ("A,3", 4, "Hit"), ("A,3", 5, "Double"), ("A,3", 6, "Double"),
    ("A,3", 7, "Hit"), ("A,3", 8, "Hit"), ("A,3", 9, "Hit"), ("A,3", 10, "Hit"), ("A,3", 11, "Hit"),
    ("A,2", 2, "Hit"), ("A,2", 3, "Hit"), ("A,2", 4, "Hit"), ("A,2", 5, "Double"), ("A,2", 6, "Double"),
    ("A,2", 7, "Hit"), ("A,2", 8, "Hit"), ("A,2", 9, "Hit"), ("A,2", 10, "Hit"), ("A,2", 11, "Hit"),
    
    # Pair Splitting
    ("A,A", 2, "Split"), ("A,A", 3, "Split"), ("A,A", 4, "Split"), ("A,A", 5, "Split"), ("A,A", 6, "Split"),
    ("A,A", 7, "Split"), ("A,A", 8, "Split"), ("A,A", 9, "Split"), ("A,A", 10, "Split"), ("A,A", 11, "Split"),
    ("10,10", 2, "Don't Split"), ("10,10", 3, "Don't Split"), ("10,10", 4, "Don't Split"), ("10,10", 5, "Don't Split"),
    ("10,10", 6, "Don't Split"), ("10,10", 7, "Don't Split"), ("10,10", 8, "Don't Split"), ("10",9, "Don't Split"),
    ("10,10", 10, "Don't Split"), ("10,10", 11, "Don't Split"), ("9,9", 2, "Split"), ("9,9", 3, "Split"), ("9,9", 4, "Split"), 
    ("9,9", 5, "Split"), ("9,9", 6, "Split"), ("9,9", 7, "Split"), ("9,9", 8, "Stand"), ("9,9", 9, "Split"), 
    ("9,9", 10, "Stand"), ("9,9", 11, "Stand"), ("8,8", 2, "Split"), ("8,8", 3, "Split"), ("8,8", 4, "Split"), 
    ("8,8", 5, "Split"), ("8,8", 6, "Split"), ("8,8", 7, "Split"), ("8,8", 8, "Split"), ("8,8", 9, "Split"), 
    ("8,8", 10, "Split"), ("8,8", 11, "Split"), ("7,7", 2, "Split"), ("7,7", 3, "Split"), ("7,7", 4, "Split"),
    ("7,7", 5, "Split"), ("7,7", 6, "Split"), ("7,7", 7, "Split"), ("7,7", 8, "Hit"), ("7,7", 9, "Hit"), 
    ("7,7", 10, "Hit"), ("7,7", 11, "Hit"), ("6,6", 2, "Split if DAS"), ("6,6", 3, "Split"), ("6,6", 4, "Split"),
    ("6,6", 5, "Split"), ("6,6", 6, "Split"), ("6,6", 7, "Hit"), ("6,6", 8, "Hit"), ("6,6", 9, "Hit"), 
    ("6,6", 10, "Hit"), ("6,6", 11, "Hit"), ("2,2", 2, "Split if DAS"), ("2,2", 3, "Split"), ("2,2", 4, "Split"), 
    ("2,2", 5, "Split"), ("2,2", 6, "Split"), ("2,2", 7, "Hit"), ("2,2", 8, "Hit"), ("2,2", 9, "Hit"), ("2,2", 10, "Hit"), ("2,2", 11, "Hit"),
]

illustrious_eighteen_data = [
    ("16", 10, 0, "Stand"),
    ("15", 10, 4, "Stand"),
    ("T,T", 5, 5, "Stand/Split"),
    ("T,T", 6, 4, "Stand/Split"),
    ("10", 10, 4, "Double"),
    ("12", 3, 2, "Stand"),
    ("12", 4, 3, "Stand"),
    ("11", 11, 1, "Double"),
    ("9", 2, 1, "Double"),
    ("10", 11, 4, "Double"),
    ("9", 7, 3, "Double"),
    ("16", 9, 5, "Stand"),
    ("13", 2, -1, "Hit"),
    ("12", 4, 0, "Stand"),
    ("12", 5, -2, "Hit"),
    ("12", 6, -1, "Stand"),
    ("13", 3, -2, "Hit"),
]

# Insert the data
cursor.executemany("""
    INSERT INTO basic_strategy (player_hand, dealer_upcard, recommended_move)
    VALUES (?, ?, ?)
""", basic_strategy_data)

# Insert the data
cursor.executemany("""
    INSERT INTO illustrious_eighteen (player_hand, dealer_upcard, true_count_threshold, adjusted_move)
    VALUES (?, ?, ?, ?)
""", illustrious_eighteen_data)




connection.commit()
connection.close()
