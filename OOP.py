"""
# OOP Practice 1

# For Class the naming convention is Capitalizing and using Camel Case.
class BigObject: #Class
    pass

obj1 = BigObject() #Instanciate

print(type(BigObject))
print(type(obj1)) 

"""
"""
# OOP Practice 2
class PlayerCharacter: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def run(self):
        print("run")
        return "Done"

player1 = PlayerCharacter("Jay", 28)
player2 = PlayerCharacter("Joe", 25)

print(player1.name)
print(player2.name)
print(player1.age)
print(player2.age)
print(player1.run())
print(player2.run())

"""
"""
#Repel Practice

#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats

cat1 = Cat("Tina", 30)
cat2 = Cat("Selena", 21)
cat3 = Cat("Lisa", 20)

# 2 Create a function that finds the oldest cat

def oldest_cat(*cats):
    return max(cats, key=lambda cat: cat.age)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
oldest = oldest_cat(cat1,cat2,cat3)

print(f"The oldest cat, {oldest.name}, is {oldest.age} years old")

"""
