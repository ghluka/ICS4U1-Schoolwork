import random
from typing import Self

#-------------------------------------------------------------------------------

# Put your Product class here

class Product(object):
    """A class that models a product with a quantity, price, name, and numerical identifier."""

    ids = []
    
    def get_unique_id():
        """Returns a unique 5-digit integer ID."""
        return int(f"{max(Product.ids) + 1:0>5}")

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
        return f"{self.__name} ({self.__id}): {self.get_quantity} items @ ${self.__price} each"

    def __repr__(self) -> str:
        return f"Product({self.__quantity}, {self.__price}, '{self.__name}', {self.__id})"

#-------------------------------------------------------------------------------

# Put your Inventory class here






#----===  TESTING CODE ===------------------------------------------------------
if __name__ == "__main__":
    BAR = f"\n{'-'*80}"

    ##Read the data file into Inventory
    #store = Inventory()

    #inv_file = open("store_inventory.csv")

    #for line in inv_file:
        #product_line = line.rstrip("\n").split(",")
        #qty = int(product_line[0])
        #price = float(product_line[1])
        #name = product_line[2]
        #id_number = int(product_line[3])
        #p = Product(qty, price, name, id_number)
        #store.add_product(p)

    ##---== Test 'Product' class ==----------------------------------------------
    #test_product = Product(99, 9.99, "Test Product")
    
    #new_id = Product.get_unique_id()
    #test_product2 = Product(1000, 9.99, "Other Product", new_id)

    #print(BAR)
    #print("1. Test basic Product methods")
    #print(test_product.get_quantity())
    #print(test_product.get_price())
    #print(test_product.get_name())
    #print(test_product.get_id())

    #print(BAR)
    #print("2. Test Product comparison methods")    
    #print(test_product > test_product2)
    #print(test_product < test_product2)
    #print(test_product == test_product2)

    #print(BAR)
    #print("3. Test set_quantity, str, and repr")
    #test_product.set_quantity(999)
    #print(str(test_product))
    #print(repr(test_product))

    ##---== Test 'Inventory' class ==----------------------------------------------
    #print(BAR)
    #print("4. Test first set of Inventory methods")
    #print(store.avg_qty_per_product())
    #print(store.qty_of_most_expensive())
    #print(store.total_inventory_value())
    #print(store.most_valuable_product())

    #print(BAR)
    #print("5. Test next set of Inventory methods")
    #print(store.avg_price_per_item())
    #print(store.median_price_per_product())
    #store.add_product(test_product)
    #print(store.median_price_per_product())

    #print(BAR)
    #print("6. Test pretty_inventory()")
    #print(store.pretty_inventory())

    #print(BAR)
    #print("7. Test more Inventory methods")
    #print(store.products_in_price_range(2.22, 2.40))
    #print(store.get_product(42274))
    #print(store.search_products('pers'))
    #print(store.find_low_stock(1))

    #print(BAR)
    #print("8. Test products_by_price()")
    #ps = store.products_by_price()
    #print("First 5:", ps[:5])
    #print("Last 5:", ps[-5:])

    #print(BAR)
    #print("9. Test availability and selling methods")
    #print(store.is_product_available(15, 42274))
    #print(store.sell_product(5, 42274))
    #print(store.is_product_available(5, 42274))
    #print(store.sell_product(5, 42274))
    #print(store.is_product_available(5, 42274))
    #print(store.sell_product(5, 42274))

    #print(BAR)
    #print("10. Test search and consolidate methods")
    #print(store.search_products("Mango"))
    #print(store.search_products("Starfruit"))
    #store.consolidate()
    #print(store.search_products("Mango"))
    #print(store.search_products("Starfruit"))
    
    #store.export_to_csv("backup.csv")
