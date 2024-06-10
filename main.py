from lib.store import Store
import lib.config as config
# from lib.category import Category
# from lib.product import Product

print("Initializing database...\n")
print("Dropping tables...")
config.drop_tables()

print("Creating tables...\n")
config.create_tables()

print("Creating store...")
Store.add_store("My Store")
print("Store created successfully")
# Category.create_all_categories()
# Product.create_all_products()

print("STORES:")
stores = Store.get_all_stores()
for store in stores:
    print(store)


print("\nClosing database...")
config.close_db()