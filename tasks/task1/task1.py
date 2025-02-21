"""Provides solutions for the 2 classes in task 1's assignment
"""
import random
from typing import Self

#-------------------------------------------------------------------------------

# Put your Product class here

class Product(object):
    """A class that models a product with a quantity, price, name, and numerical identifier."""

    __ids = []
    
    def get_unique_id() -> int:
        """Returns a unique 5-digit integer ID."""
        id = random.randrange(10_000, 100_000)
        while id in Product.__ids:
            id = random.randrange(10_000, 100_000)

        Product.__ids.append(id)
        return id

    def __init__(self, quantity:int, price:float, name:str, id:int=None):
        if not id:
            id = Product.get_unique_id()

        self.__quantity = quantity
        self.__price = price
        self.__name = name
        self.__id = id

    def get_name(self) -> int:
        """Accessor for the product's name."""
        return self.__name

    def get_quantity(self) -> float:
        """Accessor for the product's quantity."""
        return self.__quantity

    def get_price(self) -> str:
        """Accessor for the product's price."""
        return self.__price

    def get_id(self) -> int:
        """Accessor for the product's id."""
        return self.__id

    def set_quantity(self, quantity:int) -> None:
        """Mutator for the product's quantity."""
        self.__quantity = quantity

    def __gt__(self, product2) -> bool:
        if self.__price == product2.get_price():
            return self.__name > product2.get_name()
        return self.__price > product2.get_price()

    def __lt__(self, product2) -> bool:
        if self.__price == product2.get_price():
            return self.__name < product2.get_name()
        return self.__price < product2.get_price()

    def __eq__(self, product2) -> bool:
        return self.__price == product2.get_price() and self.__name == product2.get_name()

    def __str__(self) -> str:
        return f"{self.__name} ({self.__id}): {self.__quantity} items @ ${self.__price} each"

    def __repr__(self) -> str:
        return f"Product({self.__quantity}, {self.__price}, '{self.__name}', {self.__id})"

#-------------------------------------------------------------------------------

# Put your Inventory class here

class Inventory(object):
    """A class that models product inventory with a list of products."""

    def __init__(self):
        self.__products = []

    def avg_qty_per_product(self) -> float:
        """
        Returns the average quantity per Product in the Inventory.
        If the Inventory is empty, this should return 0.0.
        """
        raise NotImplementedError

    def qty_of_most_expensive(self) -> int:
        """
        Returns the quantity of the most expensive Product in the Inventory.
        If the Inventory is empty, this should return 0.
        """
        raise NotImplementedError

    def total_inventory_value(self) -> float:
        """Returns the total monetary value of all items in the Inventory."""
        raise NotImplementedError

    def most_valuable_product(self) -> Product|None:
        """
        Returns the Productthat represents the most total monetary value in the Inventory.
        If the Inventory is empty, this returns None.
        """
        raise NotImplementedError

    def avg_price_per_item(self) -> float:
        """
        Returns the unrounded average price per single inventory item.
        If the Inventory is empty, this should return 0.0.
        """
        raise NotImplementedError

    def median_price_per_product(self) -> float:
        """Returns the median price of all Products in the Inventory."""
        raise NotImplementedError

    def pretty_inventory(self) -> str:
        """Returns a large string showing all Products in the Inventory."""
        raise NotImplementedError

    def products_in_price_range(self, end1:float, end2:float) -> list:
        """
        Returns a list of references to Products in the Inventory that have a
        price between the two boundaries.
        """
        raise NotImplementedError

    def add_product(self, new_product:Product) -> None:
        """Adds the given Product argument to the Inventory."""
        raise NotImplementedError

    def get_product(self, id_num:int) -> Product|None:
        """
        Returns a reference to the Product in the Inventory that has the given
        id number.
        """
        raise NotImplementedError

    def search_products(self, substring:str) -> list[Product]:
        """
        Returns a list of references to Products in the Inventory whose names
        contain the given substring.
        """
        raise NotImplementedError

    def find_low_stock(self, threshold:int) -> list[Product]:
        """
        Returns a list of references to Products in the Inventory whose quantities
        are below or equal to the given threshold.
        """
        raise NotImplementedError

    def products_by_price(self) -> list[Product]:
        """
        Returns a list of references to Products in the Inventory ordered from
        lowest price to highest price.
        """
        raise NotImplementedError

    def is_product_available(self, quantity:int, id_num:int) -> bool:
        """
        Returns a boolean True or False based on if the Product in the Inventory
        with the given id has the specified quantity available in the Inventory.
        """
        raise NotImplementedError

    def sell_product(self, quantity:int, id_num:int) -> bool:
        """
        Returns boolean True or False based on the success of the attempt to sell
        the given quantity of the Product in the Inventory with the given id.
        """
        raise NotImplementedError

    def export_to_csv(self, filename:str) -> None:
        """Writes the entire Inventory of Products to a text based CSV file."""
        raise NotImplementedError

    def consolidate(self) -> None:
        """
        Reduces the number of Products in the Inventory by combining any that
        appear to be duplicates.
        
        If multiple Products have the same name and price, the Product that has
        the smaller id number will absorb all the quantities, and the other Product(s)
        will be fully removed from the Inventory.
        """
        raise NotImplementedError

#----===  TESTING CODE ===------------------------------------------------------
if __name__ == "__main__":
    BAR = f"\n{'-'*80}"

    #Read the data file into Inventory
    store = Inventory()

    inv_file = open("store_inventory.csv")

    for line in inv_file:
        product_line = line.rstrip("\n").split(",")
        qty = int(product_line[0])
        price = float(product_line[1])
        name = product_line[2]
        id_number = int(product_line[3])
        p = Product(qty, price, name, id_number)
        store.add_product(p)

    #---== Test 'Product' class ==----------------------------------------------
    test_product = Product(99, 9.99, "Test Product")
    
    new_id = Product.get_unique_id()
    test_product2 = Product(1000, 9.99, "Other Product", new_id)

    print(BAR)
    print("1. Test basic Product methods")
    print(test_product.get_quantity()) # 99
    print(test_product.get_price()) # 9.99
    print(test_product.get_name()) # Test Product
    print(test_product.get_id())

    print(BAR)
    print("2. Test Product comparison methods")    
    print(test_product > test_product2) # True
    print(test_product < test_product2) # False
    print(test_product == test_product2) # False

    print(BAR)
    print("3. Test set_quantity, str, and repr")
    test_product.set_quantity(999)
    print(str(test_product)) # Test Product (id): 999 items @ $9.99 each
    print(repr(test_product)) # Product(999, 9.99, 'Test Product', id)

    #---== Test 'Inventory' class ==----------------------------------------------
    print(BAR)
    print("4. Test first set of Inventory methods")
    print(store.avg_qty_per_product()) # 27.43
    print(store.qty_of_most_expensive()) # 31
    print(store.total_inventory_value()) # 125062.14000000001
    print(store.most_valuable_product()) # Coconut Water (id): 50 items @ $43.22 each

    print(BAR)
    print("5. Test next set of Inventory methods")
    print(store.avg_price_per_item()) # 5437.484347826087
    print(store.median_price_per_product()) # 22.765
    store.add_product(test_product)
    print(store.median_price_per_product()) # 22.63

    print(BAR)
    print("6. Test pretty_inventory()")
    print(store.pretty_inventory())

    print(BAR)
    print("7. Test more Inventory methods")
    print(store.products_in_price_range(2.22, 2.40))
    print(store.get_product(42274))
    print(store.search_products('pers'))
    print(store.find_low_stock(1))

    print(BAR)
    print("8. Test products_by_price()")
    ps = store.products_by_price()
    #print("First 5:", ps[:5])
    #print("Last 5:", ps[-5:])

    print(BAR)
    print("9. Test availability and selling methods")
    print(store.is_product_available(15, 42274)) # False
    print(store.sell_product(5, 42274)) # True
    print(store.is_product_available(5, 42274)) # True
    print(store.sell_product(5, 42274)) # True
    print(store.is_product_available(5, 42274)) # False
    print(store.sell_product(5, 42274)) # False

    print(BAR)
    print("10. Test search and consolidate methods")
    print(store.search_products("Mango"))
    print(store.search_products("Starfruit"))
    store.consolidate()
    print(store.search_products("Mango"))
    print(store.search_products("Starfruit"))

    store.export_to_csv("backup.csv")
