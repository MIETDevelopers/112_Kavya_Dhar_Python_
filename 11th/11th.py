#Class and Instance variable.
class snake:
# Class Variable
    animal = 'snake'
# The init method or constructor
    def __init__(self, breed, color):
# Instance Variable
        self.breed = breed
        self.color = color

# Objects of snake class
Rodger = snake("Black_mamba", "black")
Buzo = snake("Viper", "black")
print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)
print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)
# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")

print(snake.animal)
