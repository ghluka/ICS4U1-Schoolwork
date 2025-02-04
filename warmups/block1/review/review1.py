from random import choice, randrange


def make_input_file(quantity: int, filename: str) -> None:
    """
    Creates a file called with the given 'filename' full of random
    quantities and prices for 'quantity' items, one per line.
    Sample line format: 57$16.27
    """
    out_file = open(filename, "w")

    for i in range(quantity):
        q = randrange(1, 6) + randrange(0, 8) + choice([0, 0, 0, 0, 0, 0, 5, 11]) * 10
        p1 = randrange(1, 6) + randrange(0, 20, 3)
        p2 = randrange(0, 100)

        out_file.write(f"{q}${p1}.{p2:0>2}\n") 
      
    out_file.close()


def avg_qty_per_product(qtys:list[int]) -> float:
    """
    Return the average quantity per item.
    """
    return sum(qtys) / len(qtys)


def qty_of_most_expensive(qtys:list[int], prices:list[float]) -> int:
    """
    Returns the quantity in inventory of the most expensive product.
    """
    return qtys[prices.index(max(prices))]


def total_inventory_value(qtys:list[int], prices:list[float]) -> float:
    """
    Returns the total monetary value of all items in inventory.
    """
    value = 0

    for i in range(len(prices)):
        value += prices[i] * qtys[i]

    return value


def avg_price_per_item(qtys:list[int], prices:list[float]) -> float:
    """
    Returns average price per single inventory item.
    """
    return total_inventory_value(qtys, prices) / sum(qtys)


def median_price_per_product(prices:list[float]) -> float:
    """
    Returns average price per single inventory item.
    """
    prices.sort()
    median = 0

    if len(prices) % 2 == 0:
        median = prices[len(prices)//2]
    else:
        median = (prices[len(prices)//2 - 1] + prices[len(prices)//2]) / 2

    return median


def pretty_inventory(qtys:list[int], prices:list[float]) -> str:
    """
    Returns a large string showing all quantities and prices in the inventory,
    one product per line with format: ".10 items @ $__2.91 each"
    where the quantity is in 3 characters, price is in 6 characters
    """
    inventory = ""
    
    for i in range(len(prices)):
        inventory += f"{qtys[i]:.>3} items @ ${prices[i]:_>6} each\n"
    
    return inventory[:-1]


def most_valuable_product(qtys:list[int], prices:list[float]):
    """
    Returns a string showing the quantity and price of the product that 
    contains the most value in the inventory (based on its price & quantity).
    The returned string is in the format ".10 items @ $__2.91 each"
    where the quantity is in 3 characters, price is in 6 characters.
    """
    qty = qty_of_most_expensive(qtys, prices)
    price = prices[qtys.index(qty_of_most_expensive(qtys, prices))]
    
    return f"{qty:.>3} items @ ${price:_>6} each"


def products_in_price_range(prices:list[float], end1, end2):
    """
    Returns the number of products that have a price between end1 and end2 (inclusive).
    """


def distinct_prices(prices:list[float]): 
    """
    Returns a list of all distinct price amounts in inventory (i.e., with no
    duplicates), in order from lowest price to highest price.
    """


def price_counts(prices:list[float]):
    """
    Returns a large string showing all distinct prices and the number
    of products that have that price.
    For example:
       $__9.45: 1 product
       $_11.45: 5 products
       $_25.23: 2 products
       etc...
    """


if __name__ == "__main__":
    filename = "inventory.txt"
    #make_input_file(10, filename)

    # Read file
    qtys = []
    prices = []

    in_file = open(filename, "r")

    for i in in_file.readlines():
        qty, price = i.split("$")

        qtys.append(int(qty))
        prices.append(float(price))

    in_file.close()

    # Outputs
    print(f"Avg # per prod: {avg_qty_per_product(qtys):.0f}")
    print(f"# of most $: {qty_of_most_expensive(qtys, prices)}")
    print(f"Total inv. value: ${total_inventory_value(qtys, prices):.2f}")
    print(f"Avg $ per item: ${avg_price_per_item(qtys, prices):.2f}")
    print(f"Median $ per prod: ${median_price_per_product(prices):.2f}")
    #print(pretty_inventory(qtys, prices))
    print(f"Most valuable product: ${most_valuable_product(prices)}")
    ####!products_in_price_range
    print(f"Most valuable product: ${distinct_prices(prices)}")
    print(f"Most valuable product: ${price_counts(prices)}")
