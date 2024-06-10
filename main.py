from lib.store import Store
import lib.config as config
from lib.category import Category
from lib.product import Product

print("Initializing database...\n")
print("Dropping tables...")
config.drop_tables()

print("Creating tables...\n")
config.create_tables()

print("Creating store...")
Store.add_store("My Store")
Store.add_store("My Store 2")
Store.add_store("My Store 3")
print("Store created successfully")
Category.create_a_category("Electronics", 1)
print("Category created successfully")
Product.add_product("iPhone", 1000, "Electronics", "This is an iPhone", 1)
print("Product created successfully")

print("Updating product...")
Product.update_product(1, name="iPhone 13", price=1100, category="Electronics", description="This is an iPhone 13")
Product.update_product_by_id(1, name="iPhone 13", price=1100, category="Electronics", description="This is an iPhone 13", store_id=1)
Product.update_product_description(1, "This is an iPhone 13!")
print("Product updated successfully")

# print("Deleting product...")
# Product.delete_product_by_id(1)
# Product.delete_product_by_name("iPhone 13")
# print("Product deleted successfully")

print("Counting products in store...")
print(Product.count_products_in_store(1))

print("Getting products in store...")

print("STORES:")
Store.get_all_stores()

print("\nClosing database...")
config.close_db()