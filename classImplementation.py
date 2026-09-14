class Volleyball:
    def __init__(self, brand, weight, elasticity, balls):
        self.brand = brand
        self.weight = weight
        self.__elasticity = elasticity
        self.__balls = balls

    def UpdateBrand(self, newbrand):
        self.brand = newbrand

    def displayInfo(self):
        print("Brand:", self.brand)
        print("Weight:", self.weight)
        print("Elasticity:", self.__elasticity)
        print("Number of balls:", self.__balls)

    def changeWeight(self, newweight):
        self.weight = newweight

    def getElasticity(self):
        return self.__elasticity

    def getBalls(self):
        return self.__balls

    def addBalls(self, amount):
        if amount > 0:
            self.__balls += amount
        else:
            print("Amount must be positive.")


# Create two different objects
volleyball1 = Volleyball("Mikasa", False, True, 2)
volleyball2 = Volleyball("Molten", True, True, 5)

# Display initial
print("--- BEFORE ---")
print("Object 1:")
volleyball1.displayInfo()

print("Object 2:")
volleyball2.displayInfo()

# Change only Object 1
print("Changing Object 1's weight...")
volleyball1.changeWeight(True)

# Display final 
print("--- AFTER ---")
print("Object 1:")
volleyball1.displayInfo()

print("Object 2:")
volleyball2.displayInfo()
