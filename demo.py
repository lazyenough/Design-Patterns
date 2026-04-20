class House:
    def __init__(self):
        self.components = []
    
    def show_details(self):
        print(f"Components of house: {','.join(str(c) for c in self.components) if self.components else 'No components till now'}")

class HouseBuilder:
    def __init__(self):
        self.house = House()

    def set_walls(self, type):
        self.house.components.append({"walls": type})
        return self
    
    def set_roof(self, type):
        self.house.components.append({"roof": type})
        return self

    def set_windows(self, count):
        self.house.components.append({"windows": count})
        return self
    
    def set_doors(self, count):
        self.house.components.append({"doors": count})
        return self
    
    def set_garage(self, type):
        self.house.components.append({"garage": type})
        return self
    
    def build(self):
        return self.house
    
class Director:
    def __init__(self, house_builder):
        self.builder = house_builder
    
    def create_house_without_garage(self, walls_type, roof_type, no_of_windows, no_of_doors):
        return self.builder.set_walls(walls_type).set_roof(roof_type).set_windows(no_of_windows).set_doors(no_of_doors).build()
    
    def create_house_with_garage(self, walls_type, roof_type, no_of_windows, no_of_doors, garage_type):
        return self.builder.set_walls(walls_type).set_roof(roof_type).set_windows(no_of_windows).set_doors(no_of_doors).set_garage(garage_type).build()
    

if __name__ == "__main__":
    house_builder = HouseBuilder()
    direc = Director(house_builder)

    # house1 = direc.create_house_with_garage("cement", "flat", "5", "3", "garage")
    # house1.show_details()
    house2 = direc.create_house_without_garage("wood", "dome", "3", "1")
    house2.show_details()
