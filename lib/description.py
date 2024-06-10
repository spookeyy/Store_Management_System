# product desription module
from lib.config import DATABASE, CURSOR

class Description:

# creating a new description
    @classmethod
    def add_description(cls, product_id, description):
        sql = "INSERT INTO description (product_id, description) VALUES (?, ?)"
        CURSOR.execute(sql, (product_id, description))
        DATABASE.commit()
    
# updating an existing description
    @classmethod
    def update_description(cls, product_id, new_description):
        sql = "UPDATE description SET description = ? WHERE product_id = ?"
        CURSOR.execute(sql, (new_description, product_id))
        DATABASE.commit()

# getting/fetching description
    @classmethod
    def get_description_by_product_id(cls, product_id):
        sql = "SELECT * FROM description WHERE product_id = ?"
        CURSOR.execute(sql, (product_id,))
        return CURSOR.fetchone()[0]
    
# deleting description
    @classmethod
    def delete_description_by_product_id(cls, product_id):
        sql = "DELETE FROM description WHERE product_id = ?"
        CURSOR.execute(sql, (product_id,))
        DATABASE.commit()
    
    @classmethod
    def delete_description_by_id(cls, id):
        sql = "DELETE FROM description WHERE id = ?"
        CURSOR.execute(sql, (id,))
        DATABASE.commit()