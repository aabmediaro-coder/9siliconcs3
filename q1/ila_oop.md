**Name:** Ally
**Section:** Silicon
**Last Name:** Mediario
**Date:** August 20, 2026
---

# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation can be used by creating an Item object that keeps the item's name, price, and quantity together in one object. Instead of having separate variables such as item1Name, item1Price, and item1Quantity, each item can have its own properties and methods such as addStock() and removeStock(). This makes the inventory more organized because all information and actions related to an item are contained inside the Item object.

CLASS Item
    name
    price
    quantity

    addStock(amount)
        quantity = quantity + amount

    removeStock(amount)
        quantity = quantity - amount
END CLASS

item = Item("Coke", 20, 10)

item.addStock(5)
item.removeStock(2)

### 2. Abstraction
Abstraction can be used by hiding the complicated details of inventory operations and providing simple methods for the user to interact with. For example, an employee can use the sellProduct() method without needing to know how the program checks the available stock and calculates the remaining quantity. This makes the system easier to understand and use while keeping unnecessary implementation details hidden.

CLASS Inventory

    addItem(name, price, quantity)
        CREATE Item
        ADD Item to inventory

    sellItem(name, quantity)
        FIND Item
        REDUCE Item quantity
END CLASS

inventory.addItem("Coke", 20, 10)
inventory.sellItem("Coke", 2)

### 3. Inheritance
Inheritance can be used when the sari-sari store has different types of products that share common properties. For example, Product can be a parent class containing properties such as name, price, and quantity, while classes such as FoodProduct, DrinkProduct, and HouseholdProduct can inherit these properties and methods. This avoids repeating the same code for every type of product.

CLASS Product
    name
    price
    quantity
END CLASS

CLASS Food INHERITS Product
    expirationDate
END CLASS

CLASS Drink INHERITS Product
    size
END CLASS

food = Food("Lucky Me", 15, 10)
drink = Drink("Coke", 20, 10)


### 4. Polymorphism
Polymorphism can be used when different types of products need to perform the same method in different ways. For example, every product can have a displayInfo() method, but a food product can display its expiration date while a drink product can display its volume. This allows the inventory system to use the same method name for different objects while each object provides its own behavior.

CLASS Food
    displayInfo()
        DISPLAY name, price, quantity, expirationDate
END CLASS

CLASS Drink
    displayInfo()
        DISPLAY name, price, quantity, size
END CLASS

food.displayInfo()
drink.displayInfo()

## Reflection
Among the four pillars of Object-Oriented Programming, I think encapsulation would be the most useful for improving the sari-sari store inventory system. It allows the name, price, and quantity of each product to be grouped together in one object instead of using many separate variables. This makes the inventory more organized and easier to manage. It also makes it easier to add, remove, or update products without changing many parts of the program.



