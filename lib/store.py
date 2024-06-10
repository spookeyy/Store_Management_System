from lib.config import DATABASE, CURSOR

class Store:
    @classmethod
    def add_store(cls, name):
        CURSOR.execute("INSERT INTO store (name) VALUES (?)", (name,))
        DATABASE.commit()

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
        stores = CURSOR.fetchall()
        for store in stores:
            print(store)
        return stores