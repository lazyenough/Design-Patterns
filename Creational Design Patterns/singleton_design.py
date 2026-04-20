# Some parts of a software system should exist only once - such as database connection, configuration managers etc. Singleton design pattern ensures that a class has exactly one instance and provides global point of access to it.

# Class variable is a variable that belongs to the class itself rather than to any specifi instance of the class (object).

class Database:
    instance = None

    def __new__(cls):
        if cls.instance == None:
            # Make the instance
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.name = "name"
    

if __name__ == "__main__":
    db1 = Database()
    db2 = Database()

    print(f"Instance 1 name: {db1.name}")
    print(f"Instance 2 name: {db2.name}")

    print(f"Whether both db connections point to same memory: {db1 is db2}")