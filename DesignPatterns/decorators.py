from abc import ABC, abstractmethod


# Component interface (Coffee)
class Coffee(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass


# Concrete component (PlainCoffee)
class PlainCoffee(Coffee):
    def get_description(self):
        return "Plain Coffee"

    def get_cost(self):
        return 2.0


# Decorator (CoffeeDecorator)
class CoffeeDecorator(Coffee):
    def __init__(self, decorated_coffee):
        self.decorated_coffee = decorated_coffee

    @abstractmethod
    def get_description(self):
        # return self.decorated_coffee.get_description()
        pass

    @abstractmethod
    def get_cost(self):
        # return self.decorated_coffee.get_cost()
        pass


# Concrete decorator (MilkDecorator,SugarDecorator)
class MilkDecorator(CoffeeDecorator):
    def get_description(self):
        return self.decorated_coffee.get_description() + ", Milk"

    def get_cost(self):
        return self.decorated_coffee.get_cost() + 0.5


class SugarDecorator(CoffeeDecorator):
    def get_description(self):
        return self.decorated_coffee.get_description() + ", Sugar"

    def get_cost(self):
        return self.decorated_coffee.get_cost() + 0.2


if __name__ == "__main__":
    # Plain Coffee
    coffee = PlainCoffee()
    print("Description: ", coffee.get_description())
    print("Cost: $", coffee.get_cost())

    # Coffee with Milk
    milk_coffee = MilkDecorator(PlainCoffee())
    print("\nDescription: ", milk_coffee.get_description())
    print("Cost: $", milk_coffee.get_cost())

    # Coffee with Sugar and Milk
    sugar_milk_coffee = SugarDecorator(MilkDecorator(PlainCoffee()))
    print("\nDescription:", sugar_milk_coffee.get_description())
    print("Cost: $", sugar_milk_coffee.get_cost())
