class Food(object):
    """A class that models a food item, with a name, number of calories, and identifier."""
    
    food_ids = [None,]

    def __init__(self, name:str, calories:int, id:int=None) -> None:
        if not id:
            id = len(Food.food_ids)
        if id in Food.food_ids:
            raise IndexError # duplicate id
        Food.food_ids.append(id)

        self.__name = name
        self.__calories = calories
        self.__id = id

    def __str__(self) -> str:
        return f"{self.__name} ({self.__calories} cal)"

    def get_id(self) -> int:
        """Returns the id of the food."""
        return self.__id

    def get_calories(self) -> int:
        """Returns the amount of calories in the food."""
        return self.__calories

    def __eq__(self, value) -> bool:
        return self.__calories == value.get_calories()

    def __lt__(self, value) -> bool:
        return self.__calories < value.get_calories()

    def __gt__(self, value) -> bool:
        return self.__calories > value.get_calories()

    def __le__(self, value) -> bool:
        return self.__calories <= value.get_calories()

    def __ge__(self, value) -> bool:
        return self.__calories >= value.get_calories()

    def __radd__(self, food) -> int:
        # implemented to get sum() working
        calories = food
        if type(food) == Food:
            calories = food.get_calories()
        return self.__calories + calories

class Meal(object):
    """A class that models a meal, contains multiple Food items."""

    def __init__(self) -> None:
        self.__foods = []

    def __str__(self) -> str:
        out = ""
        for food in self.__foods:
            out += f"\n{food.__str__()}"
        return out[1:]

    def add_food(self, food:Food) -> None:
        """Adds the food argument to the meal."""
        self.__foods.append(food)

    def total_calories(self) -> int:
        """Returns the total number of calories in the meal."""
        return sum(self.__foods)

    def eat(self, food:Food) -> int:
        """
        Eats the Food that matches the given argument.
        Returns the number of calories eaten.
        """
        if not food:
            return 0

        foods = []

        for f in self.__foods:
            if f.get_id() != food.get_id():
                foods.append(f)

        if len(self.__foods) == len(foods):
            return 0

        self.__foods = foods
        return food.get_calories()

if __name__ == "__main__":
    BAR_WIDTH = 25
    #use these if you auto-generate ID's:
    #chs = Food("cheese", 80)
    #slmi = Food("salami", 120)
    #brd = Food("bread", 80)
    chs = Food("cheese", 80, 12345)
    slmi = Food("salami", 120, 34567)
    brd = Food("bread", 80, 67890)
    meal = Meal()
    meal.add_food(chs)
    meal.add_food(slmi)
    meal.add_food(brd)
    print(meal)
    print(f"{meal.total_calories()} calories")
    print("-" * BAR_WIDTH)

    print("Eating bread:")
    print(f"I ate {meal.eat(brd)} calories")
    print("-" * BAR_WIDTH)

    print(meal)
    print(f"{meal.total_calories()} calories")
    print("-" * BAR_WIDTH)

    print("Eating more bread?")
    print(f"I ate {meal.eat(brd)} calories")
    print("-" * BAR_WIDTH)

    print(meal)
    print(f"{meal.total_calories()} calories")
    print("-" * BAR_WIDTH)

    print("Eating cheese:")
    meal.eat(chs)
    print(meal)
    print(f"{meal.total_calories()} calories")
