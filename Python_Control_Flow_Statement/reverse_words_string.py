class dog:
    def __init__(self, name,breed):
        self.name = name
        self.breed = breed

Dog1 = dog("buddy","labrador")
print(Dog1) # it will print the memory address of the object.
print(Dog1.name)
print(Dog1.breed)
