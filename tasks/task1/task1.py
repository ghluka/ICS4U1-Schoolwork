"""Provides solutions for the 2 classes in task 1's assignment
"""

import random
from typing import Self

BAR = f"\n{'-'*80}"


class Product(object):
    """A class that models a product with a quantity, price, name, and numerical identifier."""

    __ids:list[int] = []

    @classmethod
    def get_unique_id(cls) -> int:
        """Returns a unique 5-digit integer ID."""
        id = random.randrange(10_000, 100_000)
        while id in Product.__ids:
            id = random.randrange(10_000, 100_000)

        Product.__ids.append(id)
        return id

    def __init__(self, quantity: int, price: float, name: str, id: int = -1):
        """Initializes the Product class with a given quantity, price, name, and numeric identifier."""
        if id == -1:
            id = Product.get_unique_id()

        self.__quantity = quantity
        self.__price = price
        self.__name = name
        self.__id = id

    def get_name(self) -> str:
        """Accessor for the product's name."""
        return self.__name

    def get_quantity(self) -> int:
        """Accessor for the product's quantity."""
        return self.__quantity

    def get_price(self) -> float:
        """Accessor for the product's price."""
        return self.__price

    def get_id(self) -> int:
        """Accessor for the product's id."""
        return self.__id

    def set_quantity(self, quantity: int) -> None:
        """Mutator for the product's quantity. Doesn't allow for negative quantities."""
        if quantity >= 0:
            self.__quantity = quantity

    def __gt__(self, product2: Self) -> bool:
        """Compares two Product classes.
        Returns a bool stating if self's prices are greater than product2's.
        If both prices are the same it returns if self's name is greater than product2's. 
        """
        if self.__price == product2.get_price():
            return self.__name > product2.get_name()
        return self.__price > product2.get_price()

    def __lt__(self, product2: Self) -> bool:
        """Compares two Product classes.
        Returns a bool stating if self's prices are lower than product2's.
        If both prices are the same it returns if self's name is lower than product2's. 
        """
        if self.__price == product2.get_price():
            return self.__name < product2.get_name()
        return self.__price < product2.get_price()

    def __eq__(self, product2: object) -> bool:
        """Compares two Product classes.
        Returns a bool stating if self's name and price is the same as product2's.
        """
        if not isinstance(product2, Product):
            return NotImplemented
        return self.__price == product2.get_price() and self.__name == product2.get_name()

    def __str__(self) -> str:
        """Returns a string containing information about the class in the specified format:
        {name} ({id}):  {quantity} items @ ${price} each
        """
        return f"{self.__name} ({self.__id}):  {self.__quantity} items @ ${self.__price} each"

    def __repr__(self) -> str:
        """Returns a string containing information about the class in the specified format:
        Product({quantity}, {price}, '{name}', {id})
        """
        return f"Product({self.__quantity}, {self.__price}, '{self.__name}', {self.__id})"


class Inventory(object):
    """A class that models product inventory with a list of products."""

    def __init__(self):
        """Initializes the Inventory class with no given parameters."""
        self.__products = []

    def avg_qty_per_product(self) -> float:
        """Returns the average quantity per Product in the Inventory.
        If the Inventory is empty, this should return 0.0.
        """
        quantities = 0.0

        for product in self.__products:
            quantities += product.get_quantity()

        return quantities / len(self.__products)

    def qty_of_most_expensive(self) -> int:
        """Returns the quantity of the most expensive Product in the Inventory.
        If the Inventory is empty, this should return 0.
        """
        quantity = 0
        most_expensive_price = 0

        for product in self.__products:
             if product.get_price() > most_expensive_price:
                quantity = product.get_quantity()
                most_expensive_price = product.get_price()

        return quantity

    def total_inventory_value(self) -> float:
        """Returns the total monetary value of all items in the Inventory."""
        total_value = 0.0

        for product in self.__products:
            total_value += product.get_price() * product.get_quantity()

        return total_value

    def most_valuable_product(self) -> Product|None:
        """Returns the Product that represents the most total monetary value in the Inventory.
        If the Inventory is empty, this returns None.
        """
        highest_valued_product = None
        most_valuable = 0

        for product in self.__products:
             if product.get_price() * product.get_quantity() > most_valuable:
                highest_valued_product = product
                most_valuable = product.get_price() * product.get_quantity()

        return highest_valued_product

    def avg_price_per_item(self) -> float:
        """Returns the unrounded average price per single inventory item.
        If the Inventory is empty, this should return 0.0.
        """
        quantities = 0.0
        total_value = 0.0

        for product in self.__products:
            total_value += product.get_price() * product.get_quantity()
            quantities += product.get_quantity()

        return total_value / quantities

    def median_price_per_product(self) -> float:
        """Returns the median price of all Products in the Inventory."""
        prices = []

        for product in self.__products:
            prices.append(product.get_price())
        prices.sort()

        if len(prices) % 2 == 1:
            return prices[len(prices) // 2]
        else:
            return (prices[len(prices) // 2 - 1] + prices[len(prices) // 2]) / 2

    def pretty_inventory(self) -> str:
        """Returns a large string showing all Products in the Inventory."""
        out = ""

        for product in self.__products:
            out += f"{product}\n"

        return out[:-1]

    def products_in_price_range(self, end1: float, end2: float) -> list:
        """Returns a list of references to Products in the Inventory that have a
        price between the two boundaries.
        """
        products = []

        for product in self.__products:
            if min(end1, end2) <= product.get_price() and product.get_price() <= max(end1, end2):
                products.append(product)

        return products

    def add_product(self, new_product: Product) -> None:
        """Adds the given Product argument to the Inventory."""
        self.__products.append(new_product)

    def get_product(self, id_num: int) -> Product|None:
        """Returns a reference to the Product in the Inventory that has the given
        id number.
        """
        for product in self.__products:
            if product.get_id() == id_num:
                return product

        return None

    def search_products(self, substring: str) -> list[Product]:
        """Returns a list of references to Products in the Inventory whose names
        contain the given substring.
        """
        products = []

        for product in self.__products:
            if substring.lower() in product.get_name().lower():
                products.append(product)

        return products

    def find_low_stock(self, threshold: int) -> list[Product]:
        """Returns a list of references to Products in the Inventory whose quantities
        are below or equal to the given threshold.
        """
        products = []

        for product in self.__products:
            if product.get_quantity() <= threshold:
                products.append(product)

        return products

    def products_by_price(self) -> list[Product]:
        """Returns a list of references to Products in the Inventory ordered from
        lowest price to highest price.
        """
        return sorted(self.__products)

    def is_product_available(self, quantity: int, id_num: int) -> bool:
        """Returns a boolean True or False based on if the Product in the Inventory
        with the given id has the specified quantity available in the Inventory.
        """
        product = self.get_product(id_num)

        if product:
            return product.get_quantity() >= quantity
        return False

    def sell_product(self, quantity: int, id_num: int) -> bool:
        """Returns boolean True or False based on the success of the attempt to sell
        the given quantity of the Product in the Inventory with the given id.
        """
        product = self.get_product(id_num)

        if product and product.get_quantity() >= quantity:
            product.set_quantity(product.get_quantity() - quantity)
            return True
        return False

    def export_to_csv(self, filename: str) -> None:
        """Writes the entire Inventory of Products to a text based CSV file."""
        out_file = open(filename, "w")

        for product in self.__products:
            out_file.write(f"{product.get_quantity()},{product.get_price()},{product.get_name()},{product.get_id()}\n")

        out_file.close()

    def consolidate(self) -> None:
        """Reduces the number of Products in the Inventory by combining any that
        appear to be duplicates.
        
        If multiple Products have the same name and price, the Product that has
        the smaller id number will absorb all the quantities, and the other Product(s)
        will be fully removed from the Inventory.
        """
        products:list[Product] = []

        for product in self.__products:
            if product in products:
                duplicate = products[products.index(product)]

                duplicate.set_quantity(duplicate.get_quantity() + product.get_quantity())

                # if current product has lower id than duplicate, remove duplicate from list and add current product to list
                if product.get_id() < duplicate.get_id():
                    products.remove(product)
                    product.set_quantity(duplicate.get_quantity())
                    products.append(product)
            else:
                products.append(product)

        self.__products = products

if __name__ == "__main__":
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
    print(test_product.get_quantity())
    print(test_product.get_price())
    print(test_product.get_name())
    print(test_product.get_id())

    print(BAR)
    print("2. Test Product comparison methods")    
    print(test_product > test_product2)
    print(test_product < test_product2)
    print(test_product == test_product2)

    print(BAR)
    print("3. Test set_quantity, str, and repr")
    test_product.set_quantity(999)
    print(str(test_product))
    print(repr(test_product))

    #---== Test 'Inventory' class ==----------------------------------------------
    print(BAR)
    print("4. Test first set of Inventory methods")
    print(store.avg_qty_per_product())
    print(store.qty_of_most_expensive())
    print(store.total_inventory_value())
    print(store.most_valuable_product())

    print(BAR)
    print("5. Test next set of Inventory methods")
    print(store.avg_price_per_item())
    print(store.median_price_per_product())
    store.add_product(test_product)
    print(store.median_price_per_product())

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
    print("First 5: ", ps[:5])
    print("Last 5: ", ps[-5:])

    print(BAR)
    print("9. Test availability and selling methods")
    print(store.is_product_available(15, 42274))
    print(store.sell_product(5, 42274))
    print(store.is_product_available(5, 42274))
    print(store.sell_product(5, 42274))
    print(store.is_product_available(5, 42274))
    print(store.sell_product(5, 42274))

    print(BAR)
    print("10. Test search and consolidate methods")
    print(store.search_products("Mango"))
    print(store.search_products("Starfruit"))
    store.consolidate()
    print(store.search_products("Mango"))
    print(store.search_products("Starfruit"))

    store.export_to_csv("backup.csv")
