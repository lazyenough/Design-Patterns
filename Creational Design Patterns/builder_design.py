# We use this design pattern when creating complex objects as the class may contain many optional parameters.
class Pizza:
    def __init__(self):
        self.toppins = []

    def __str__(self):
        return f"Pizza with toppins: {','.join(self.toppins) if self.toppins else 'not toppings'}"

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()
    
    def add_cheese(self):
        self.pizza.toppins.append("cheese")
        return self
    
    def add_olives(self):
        self.pizza.toppins.append("olives")
        return self
    
    def add_paneer(self):
        self.pizza.toppins.append("paneer")
        return self

    def build(self):
        return self.pizza

class Director:
    def __init__(self, builder):
        self.builder = builder
    
    def create_olive_pizza(self):
        return self.builder.add_cheese().add_olives().build()
    
    def create_paneer_pizza(self):
        return self.builder.add_cheese().add_paneer().build()
    
if __name__ == "__main__":
    # builder1 = PizzaBuilder()
    # pizza1 = builder1.add_cheese().add_olives().build()
    # print(pizza1)

    # builder2 = PizzaBuilder()
    # pizza2 = builder2.add_cheese().add_paneer().build()
    # print(pizza2)

    # builder3 = PizzaBuilder()
    # pizza3 = builder3.build()
    # print(pizza3)

    builder = PizzaBuilder()
    direc = Director(builder)

    pizza1 = direc.create_olive_pizza()
    print(pizza1)

    pizza2 = direc.create_paneer_pizza()
    print(pizza2)