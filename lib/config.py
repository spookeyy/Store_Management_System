import sqlite3

DATABASE = sqlite3.connect('data/database.db')
CURSOR = DATABASE.cursor()

def create_tables():
    sql1 = """CREATE TABLE IF NOT EXISTS store(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(20) NOT NULL)"""
    CURSOR.execute(sql1)

    sql2 = """CREATE TABLE IF NOT EXISTS product(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(20) NOT NULL,
        price FLOAT NOT NULL,
        category VARCHAR(20) NOT NULL,
        description VARCHAR(100) NOT NULL,
        store_id INTEGER NOT NULL,
        FOREIGN KEY (store_id) REFERENCES store(id))"""
    CURSOR.execute(sql2)

    sql3 = """CREATE TABLE IF NOT EXISTS category(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(20) NOT NULL,
        store_id INTEGER NOT NULL,
        FOREIGN KEY (store_id) REFERENCES store(id))"""
    CURSOR.execute(sql3)

    DATABASE.commit()

def drop_tables():
    sql1 = """DROP TABLE IF EXISTS store"""
    CURSOR.execute(sql1)

    sql2 = """DROP TABLE IF EXISTS product"""
    CURSOR.execute(sql2)

    sql3 = """DROP TABLE IF EXISTS category"""
    CURSOR.execute(sql3)

    DATABASE.commit()

def close_db():
    DATABASE.close()

# print("Initializing database...\n")
# print("Dropping tables...")
# drop_tables()

# print("Creating tables...\n")
# create_tables()

# print("Closing database...")
# close_db()