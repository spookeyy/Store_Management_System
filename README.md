# Store Management CLI App

This is a command-line interface (CLI) application written in Python for managing stores, products, and categories. It allows users to create and manage stores, add and update products, assign categories to products, and perform various other operations.

## Features

- Create a new store
- Update an existing store
- Fetch store details by ID
- Delete a store
- Add a product to a store
- Delete a product
- Update a product (name, price, category, description)
- Count the number of products in a store
- Add a category to a product
- Add a description to a product
- Delete a category
- View all products
- Fetch products by user ID
- Update a product description
- Fetch all product details by product ID
- Fetch all products in a store by store ID

## Prerequisites

- Python 3.x
- SQLite3 (included in Python standard library)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/spookeyy/store_mgt_CLI_app.git
```
2. Navigate to the cloned directory:
```bash
cd store-mgt-CLI-app
```
3. (Optional) Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate # On Windows, use: source venv/Scripts/activate
```
4. Install the required dependencies:
```bash
pip install -r requirements.txt
```
5. Run the application:
```bash
python3 main.py
```

## Project Structure

- store_mgt_CLI_app
    - data/
        - database.db
    - lib/
        - category.py
        - config.py
        - description.py
        - product.py
        - store.py
    - main.py
    - README.md
    - readonly.py
    - requirements.txt

- `data/database.db`: SQLite database file
- `lib/config.py`: Database configuration and table creation/deletion
- `lib/store.py`: Functions for managing stores
- `lib/product.py`: Functions for managing products
- `lib/category.py`: Functions for managing categories
- `lib/description.py`: Functions for managing product descriptions
- `main.py`: Entry point of the application
- `README.md`: Project README
- `requirements.txt`: List of required dependencies

## Dependencies

- Python 3.x
- SQLite3 (included in Python standard library)

## Configuration

- Database: `data/database.db`
- Cursor: `CURSOR`

## Running the Application

To run the application, simply type `python3 main.py` in your terminal.

## Usage
The application is run from the command line using the `main.py` script. Upon running the script, the application will initialize the database, create the necessary tables, and perform some example operations.

You can modify the `main.py` script to include your desired operations or create additional scripts to interact with the application.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please create a new issue or submit a pull request.

## License
This project is licensed under the MIT License.

## Author
- [Spookie](https://github.com/spookeyy)

## Version
- 1.0.0