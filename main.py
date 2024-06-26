import sys
import time
# import pyttsx3
from lib.admin import Admin
from lib.config import DATABASE as DB
from lib.store import Store
from lib.category import Category
from lib.product import Product
from lib.description import Description

# engine = pyttsx3.init()
# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

if __name__ == "__main__":
    admin = Admin()
    print("\n\t\t\t\t WELCOME TO STORE MANAGEMENT SYSTEM!!")
    # speak("WELCOME TO STORE MANAGEMENT SYSTEM")
    # Stores operations
    def store_menu():
        while True:
            print("\n")
            print("|======================================|")
            print("|==============STORE MENU==============|")
            print("|        1. Add Store                  |")
            print("|        2. Update Store               |")
            print("|        3. Delete Store by ID         |")
            print("|        4. Get All Stores             |")
            print("|        5. Get Store by ID            |")
            print("|        6. Get Store by Name          |")
            print("|        7. Get All products in Store  |")
            print("|        8. Main Menu                  |")
            print("|======================================|")

            choice = input("Enter your choice: ")
            store = Store()
            products_module = Product()
            if choice == "1":
                name = input("Enter store name: ")
                added_store = store.add_store(name)
                if added_store:
                    print(f"Added store: {added_store}")
                else:
                    print("Failed to add store.")

            elif choice == "2":
                store_id = int(input("Enter store ID: "))
                if not store.get_store_by_id(store_id):
                    print("\nStore not found. Please try again.")
                    continue
                name = input("Enter store name: ")
                store.update_store_by_id(store_id, name)
                print(f"\nUpdated store: {store_id} ({name}) successfully.")

            elif choice == "3":
                store_id = int(input("Enter store ID: "))
                confirm = input("Are you sure you want to delete this store? (y/n): ") # confirm deletion
                if confirm.lower() != "y":
                    print("Deletion canceled.")
                    continue
                store.delete_store_by_id(store_id)
                print(f"\nDeleted store: {store_id} successfully.")

            elif choice == "4":
                stores = store.get_all_stores()
                print("|==========All Stores==========|\n")
                for store in stores:
                    print(f"| ID: {store[0]}, Name: {store[1]}") # print all stores (id, store)

            elif choice == "5":
                store_id = input("Enter store ID: ")
                store = store.get_store_by_id(store_id)
                if store:
                    print(f"\nStore found: {store}")
                else:
                    print("\nStore not found.")

            elif choice == "6":
                store_name = input("Enter store name: ")
                store = store.get_store_by_name(store_name)
                if store:
                    print(f"\nStore found: {store}")
                else:
                    print("\nStore not found.")

            elif choice == "7":
                store_id = input("Enter store ID: ")
                products = products_module.get_all_products_in_store(store_id)
                if products:
                    print(f"\nProducts in store {store_id}:\n")
                    for product in products:
                        print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Category: {product[3]}, Description: {product[4]}")
                else:
                    print("\nNo products found in this store.")

            elif choice == "8":
                main_menu()
            else:
                print("Invalid choice. Please try again.")

    # Categories operations
    def category_menu():
        while True:
            print("\n")
            print("|======================================|")
            print("|=============CATEGORY MENU============|")
            print("|        1. Add Category               |")
            print("|        2. Update Category by ID      |")
            print("|        3. Delete Category by ID      |")
            print("|        4. Get category by name       |")
            print("|        5. Get All Categories         |")
            print("|        6. Get Category by ID         |")
            print("|        7. Main Menu                  |")
            print("|======================================|")

            choice = input("Enter your choice: ")
            category = Category()
            if choice == "1":
                name = input("Enter category name: ")
                store_id = int(input("Enter store ID: "))
                added_category = category.add_category(name, store_id)
                if added_category:
                    print(f"\nAdded category: {added_category}" + " to store: " + str(store_id))
                else:
                    print("\nFailed to add category.")

            elif choice == "2":
                category_id = int(input("Enter category ID: "))
                name = input("Enter category name: ")
                category.update_category_by_id(category_id, name)
                print(f"\nUpdated category: {category_id} ({name}) successfully.")

            elif choice == "3":
                category_id = int(input("Enter category ID: "))
                confirm = input("Are you sure you want to delete this category? (y/n): ") # confirm deletion
                category_name = category.get_category_by_id(category_id)[1]
                if confirm.lower() != "y":
                    print("\nDeletion canceled.")
                    continue
                category.delete_category_by_id(category_id)
                print(f"\nDeleted category: {category_id} ({category_name}) successfully.")

            elif choice == "4":
                category_name = input("Enter category name: ")
                category = category.get_category_by_name(category_name)
                if category:
                    print(f"\nCategory found: {category}")
                else:
                    print("\nCategory not found.")

            elif choice == "5":
                categories = category.get_all_categories()
                print("\n|==========All Categories==========|\n")
                for category in categories:
                    print(f"| ID: {category[0]}, Name: {category[1]}") # print all categories (id, category)

            elif choice == "6":
                category_id = input("Enter category ID: ")
                category = category.get_category_by_id(category_id)
                if category:
                    print(f"\nCategory found: {category}")
                else:
                    print("\nCategory not found.")

            elif choice == "7":
                print("\nReturning to main menu...")
                main_menu()
            else:
                print("Invalid choice. Please try again.")

    # Products operations
    def product_menu():
        while True:
            print("\n")
            print("|=====================================|")
            print("|============PRODUCT MENU=============|")
            print("|        1. Add Product               |")
            print("|        2. Update Product by ID      |")
            print("|        3. Update Product description|")
            print("|        4. Delete Product by ID      |")
            print("|        5. Delete product by name    |")
            print("|        6. Get All Products in Store |")
            print("|        7. Get Products by Category  |")
            print("|        8. Get Product by ID         |")
            print("|        9. Main Menu                 |")
            print("|=====================================|")

            choice = input("Enter your choice: ")
            product = Product()
            category_module = Category()
            if choice == "1":
                name = input("Enter product name: ")
                price = float(input("Enter product price: "))
                category = input("Enter product category: ")
                description = input("Enter product description: ")
                store_id = int(input("Enter store ID: "))
                added_product = product.add_product(name, price, category, description, store_id)
                if added_product:
                    print(f"\nAdded product: {added_product}")
                else:
                    print("\nFailed to add product.")

            elif choice == "2":
                product_id = int(input("Enter product ID: "))
                name = input("Enter product name: ")
                price = float(input("Enter product price: "))
                category = input("Enter product category: ")
                description = input("Enter product description: ")
                store_id = int(input("Enter store ID: "))
                product.update_product_by_id(product_id, name, price, category, description, store_id)
                print(f"\nUpdated product: {product_id} ({name}) successfully.")

            elif choice == "3":
                product_id = int(input("Enter product ID: "))
                new_description = input("Enter new product description: ")
                product.update_product_description(product_id, new_description)
                print(f"\nUpdated product description: {product_id} ({new_description}) successfully.")

            elif choice == "4":
                product_id = int(input("Enter product ID: "))
                confirm = input("Are you sure you want to delete this product? (y/n): ") # confirm deletion
                if confirm.lower() != "y":
                    print("\nDeletion canceled.")
                    continue
                product.delete_product_by_id(product_id)
                print(f"\nDeleted product: {product_id} ({name}) successfully.")

            elif choice == "5":
                product_name = input("Enter product name: ")
                product = product.get_product_by_name(product_name)
                if product:
                    print(f"\nProduct found: {product}")
                else:
                    print("\nProduct not found.")

            elif choice == "6":
                store_id = int(input("Enter store ID: "))
                products = product.get_all_products_in_store(store_id)
                print(f"\nProducts in store {store_id}:")
                for product in products:
                    print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Category: {product[3]}, Description: {product[4]}, Store ID: {product[5]}")

            elif choice == "7":
                category = input("Enter product category: ")
                category_name = category_module.get_category_by_name(category)
                if not category_name:
                    print(f"\nCategory {category} not found.")
                    continue
                products = product.get_products_by_category(category)
                if not products:
                    print(f"\nNo products found in category {category}.")
                    continue
                print(f"\nProducts in category {category}:\n")
                for product in products:
                    print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Category: {product[3]}, Description: {product[4]}, Store ID: {product[5]}")

            elif choice == "8":
                product_id = int(input("Enter product ID: "))
                product = product.get_product_by_id(product_id)
                if product:
                    print(f"\nProduct found: {product}")
                else:
                    print("\nProduct not found.")

            elif choice == "9":
                print("\nReturning to main menu...")
                main_menu()
            else:
                print("Invalid choice. Please try again.")

    # description operations
    def description_menu():
        while True:
            print("\n")
            print("|=====================================|")
            print("|===========DESCRIPTION MENU==========|")
            print("|           PID: Product ID           |")
            print("|        1. Add Description by PID    |")
            print("|        2. Update Description by PID |")
            print("|        3. Delete Description by PID |")
            print("|        4. Get Description by PID    |")
            print("|        5. Main Menu                 |")
            print("|=====================================|")

            choice = input("Enter your choice: ")
            description_module = Description()
            desc = Product()

            if choice == "1":
                product_id = int(input("Enter product ID: "))
                description = input("Enter product description: ")
                description_module.add_description(product_id, description)
                print(f"\nAdded description: {product_id} ({description}) successfully.")
                
            elif choice == "2":
                product_id = int(input("Enter product ID: "))
                if not desc.get_product_by_id(product_id):
                    print("\nProduct not found. Please try again.")
                    continue
                new_description = input("Enter new product description: ")
                desc.update_product_description(product_id, new_description)
                print(f"\nUpdated description: {product_id} ({new_description}) successfully.")

            elif choice == "3":
                product_id = int(input("Enter product ID: "))
                description_module.delete_description_by_product_id(product_id)
                print(f"\nDeleted description: {product_id} successfully.")

            elif choice == "4":
                product_id = int(input("Enter product ID: "))
                description = desc.get_product_description_by_product_id(product_id)
                if description:
                    print(f"\nDescription found: {description}")
                else:
                    print("\nDescription not found.")

            elif choice == "5":
                print("\nReturning to main menu...")
                main_menu()
            else:
                print("Invalid choice. Please try again.")

    # main menu
    def main_menu():
        while True:
            print("\n")
            print("\t\t\t\t|======================================|")
            print("\t\t\t\t|==============MAIN MENU===============|")
            print("\t\t\t\t|        1. Manage Stores              |")
            print("\t\t\t\t|        2. Manage Categories          |")
            print("\t\t\t\t|        3. Manage Products            |")
            print("\t\t\t\t|        4. Manage Descriptions        |")
            print("\t\t\t\t|        5. Change Password            |")
            print("\t\t\t\t|        6. Quit Application           |")
            print("\t\t\t\t|======================================|")
            choice = input("\t\t\t\tEnter your choice: ")
            if choice == "1":
                store_menu()
            elif choice == "2":
                category_menu()
            elif choice == "3":
                product_menu()
            elif choice == "4":
                description_menu()
            elif choice == "5":
                username = input("\n\t\t\t\tEnter your username: ")
                password = input("\t\t\t\tEnter your new password: ")
                # admin = Admin()
                admin.update_admin(username, password)
                print("\n\t\t\t\tPassword changed successfully.")
                print("\n\t\t\t\tReturning to main menu...")
                time.sleep(1)
                main_menu()
            elif choice == "6":
                print("\n\t\tThank you for using the Store Management System!\n")
                # speak("Thank you for using the Store Management System")
                DB.close()
                time.sleep(1)
                sys.exit()
            else:
                print("\t\t\nInvalid choice. Please try again.")

    def admin_login():
        print("\n")
        print("\n\t\t\t\t Log in to admin account!\n")
        username = input("\t\t\t\t Enter username: ")
        password = input("\t\t\t\t Enter password: ")
        login_status = admin.login(username, password)
        if login_status:
            print("\n\t\t\t\tLogin successful!")
            time.sleep(1)
            main_menu()
        else:
            print("\n\t\t\t\tLogin failed. Please try again.")
            time.sleep(1)
            admin_login()

    def admin_menu():
        print("\n")
        print("\t\t\t\t|======================================|")
        print("\t\t\t\t|==============ADMIN MENU==============|")
        print("\t\t\t\t|        1. Log in to admin account    |")
        print("\t\t\t\t|        2. Exit                       |")
        print("\t\t\t\t|======================================|")

        choice = input("\t\t\t\tEnter your choice: ")
        if choice == "1":
            admin_login()
        elif choice == "2":
            print("\n\t\t\t\tQuitting application...\n")
            DB.close()
            time.sleep(1)
            sys.exit()
        else:
            print("\n\t\t\t\tInvalid choice. Please try again.")
            time.sleep(2)
            admin_menu()

    admin_menu()