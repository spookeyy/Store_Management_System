#product module

from lib.config import DATABASE, CURSOR

class Product:

# creating a new product operation
    @classmethod
    def add_product(cls, name, price, category, description, store_id):
        sql = "INSERT INTO product (name, price, category, description, store_id) VALUES (?, ?, ?, ?, ?)"
        CURSOR.execute(sql, (name, price, category, description, store_id))
        DATABASE.commit()

# updating an existing product
    @classmethod
    def update_product(cls, product_id, name=None, price=None, category=None, description=None):
        updates = [] # list of columns to be updated
        values = [] # list of values to be passed to the query
        if name: # check if name is not None
            updates.append("name = ?") 
            values.append(name)
        if price: 
            updates.append("price = ?") # add price column to updates
            values.append(price)
        if category:
            updates.append("category = ?")
            values.append(category)
        if description:
            updates.append("description = ?")
            values.append(description)
        sql = "UPDATE product SET {} WHERE id = ?".format(", ".join(updates)) # formatting sql query
        values.append(product_id) # adding product_id to values
        CURSOR.execute(sql, tuple(values)) 
        DATABASE.commit() 

    @classmethod
    def update_product_by_id(cls, id, name, price, category, description, store_id):
        sql = "UPDATE product SET name = ?, price = ?, category = ?, description = ?, store_id = ? WHERE id = ?"
        CURSOR.execute(sql, (name, price, category, description, store_id, id))
        DATABASE.commit()

    @classmethod
    def update_product_description(cls, product_id, new_description):
        sql = "UPDATE product SET description = ? WHERE id = ?"
        CURSOR.execute(sql, (new_description, product_id))
        DATABASE.commit()

# counting products
    @classmethod
    def count_products_in_store(cls, store_id):
        sql = "SELECT COUNT(*) FROM product WHERE store_id = ?"
        CURSOR.execute(sql, (store_id,))
        return CURSOR.fetchone()[0] # fetchone returns a tuple

# getting/fetching products
    @classmethod
    def get_all_products_in_store(cls, store_id):
        sql = "SELECT * FROM product WHERE store_id = ?"
        CURSOR.execute(sql, (store_id,))
        return CURSOR.fetchall()

    @classmethod
    def get_product_by_id(cls, id):
        sql = "SELECT * FROM product WHERE id = ?"
        CURSOR.execute(sql, (id,))
        return CURSOR.fetchone()

    @classmethod
    def get_product_by_name(cls, name):
        sql = "SELECT * FROM product WHERE name = ?"
        CURSOR.execute(sql, (name,))
        return CURSOR.fetchone()

    @classmethod
    def get_products_by_category(cls, category):
        sql = "SELECT * FROM product WHERE category = ?"
        CURSOR.execute(sql, (category,))
        return CURSOR.fetchall()

    @classmethod
    def get_product_details_by_id(cls, peoduct_id):
        sql = "SELECT * FROM product WHERE id = ?"
        CURSOR.execute(sql, (peoduct_id,))
        return CURSOR.fetchone()

    @classmethod
    def get_products_by_store_id(cls, store_id):
        sql = "SELECT * FROM product WHERE store_id = ?"
        CURSOR.execute(sql, (store_id,))
        return CURSOR.fetchall()

# Delete operations
    @classmethod
    def delete_product_by_id(cls, id):
        sql = "DELETE FROM product WHERE id = ?"
        CURSOR.execute(sql, (id,))
        DATABASE.commit()
    @classmethod
    def delete_all_products_in_store(cls, store_id):
        sql = "DELETE FROM product WHERE store_id = ?"
        CURSOR.execute(sql, (store_id,))
        DATABASE.commit()
    
    @classmethod
    def delete_all_products(cls):
        sql = "DELETE FROM product"
        CURSOR.execute(sql)
        DATABASE.commit()
    
    @classmethod
    def delete_product_by_name(cls, name):
        sql = "DELETE FROM product WHERE name = ?"
        CURSOR.execute(sql, (name,))
        DATABASE.commit()