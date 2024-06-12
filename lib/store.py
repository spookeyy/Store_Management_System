from config import DATABASE, CURSOR

class Store:
    @classmethod
    def add_store(cls, name):
        CURSOR.execute("INSERT INTO store (name) VALUES (?)", (name,))
        DATABASE.commit()
        # return CURSOR.lastrowid
        store_id = CURSOR.lastrowid
        CURSOR.execute("SELECT * FROM store WHERE id = ?", (store_id,))
        return CURSOR.fetchone()

    @classmethod
    def update_store_by_id(cls, id, name):
        CURSOR.execute("UPDATE store SET name = ? WHERE id = ?", (name, id))
        
        DATABASE.commit()

    @classmethod
    def get_store_by_name(cls, name):
        CURSOR.execute("SELECT * FROM store WHERE name = ?", (name,))
        return CURSOR.fetchone()
    
   
    @classmethod
    def delete_store_by_id(cls, id):
        CURSOR.execute("DELETE FROM store WHERE id = ?", (id,))
        DATABASE.commit()

    @classmethod
    def delete_all_stores(cls):
        CURSOR.execute("DELETE * FROM store")
        DATABASE.commit()

    @classmethod
    def get_store_by_id(cls, id):
        CURSOR.execute("SELECT * FROM store WHERE id = ?", (id,))
        return CURSOR.fetchone()

    @classmethod
    def get_all_stores(cls):
        CURSOR.execute("SELECT * FROM store")
        return CURSOR.fetchall()


# creating 5 sample stores
# store1 = Store.add_store("Walmart")
# store2 = Store.add_store("Target")
# store3 = Store.add_store("Costco")
# store4 = Store.add_store("Amazon")
# store5 = Store.add_store("Best Buy")
