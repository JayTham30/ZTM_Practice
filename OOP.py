"""
# OOP Practice 1

# For Class the naming convention is Capitalizing and using Camel Case.
class BigObject: #Class
    pass

obj1 = BigObject() #Instanciate

print(type(BigObject))
print(type(obj1)) 

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

