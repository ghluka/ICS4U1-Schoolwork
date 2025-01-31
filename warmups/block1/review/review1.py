from random import choice, randrange


def make_input_file(quantity: int, filename: str) -> None:
    '''
    Creates a file called with the given 'filename' full of random
    quantities and prices for 'quantity' items, one per line.
    Sample line format: 57$16.27
    '''
    out_file = open(filename, 'w')

    for i in range(quantity):
        q = randrange(1, 6) + randrange(0, 8) + choice([0, 0, 0, 0, 0, 0, 5, 11]) * 10
        p1 = randrange(1, 6) + randrange(0, 20, 3)
        p2 = randrange(0, 100)

        out_file.write(f"{q}${p1}.{p2:0>2}\n") 
      
    out_file.close()


def avg_qty_per_product(qtys) -> float:
    """
    Returns the average quantity per product
    """
    return sum(qtys) / len(qtys)


def qty_of_most_expensive(qtys, prices) -> int:
    """
    Returns the quantity of the most expensive product
    """
    return qtys[prices.index(max(prices))]


def total_inventory_value(qtys, prices) -> float:
    """
    Returns the total value of the inventory
    """
    value = 0

    for i in range(len(prices)):
        value += prices[i] * qtys[i]

    return value


def avg_price_per_item(qtys, prices) -> float:
    """
    Returns the average price per product
    """
    return sum(prices) / len(prices)


def median_price_per_product(prices) -> float:
    """
    Returns the median price per product
    """
    prices.sort()
    median = 0

    if len(prices) % 2 == 0:
        median = prices[len(prices)//2]
    else:
        median = (prices[len(prices)//2 - 1] + prices[len(prices)//2]) / 2

    return median


def pretty_inventory(qtys, prices) -> str:
    widest_qty = len(str(max(qtys)))
    widest_price = len(str(max(prices)))
    
    inventory = ""
    
    for i in range(len(prices)):
        inventory += f"| {qtys[i]:>{widest_qty}} | {prices[i]:<{widest_price}} |\n"
    
    return inventory


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
    print(pretty_inventory(qtys, prices))
