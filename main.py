class Dog:
    def __init__(self, name='Безыммянная', gender='male'):
        self.name = name
        self.gender = gender
        self.age = 0
        print("Родилась собака")

    def bark(self, age):
        if self.age < 2:
            self.sound = 'тяф-тяф'
        elif self.age < 5:
            self.sound = 'вуф-вуф'
        else:
            self.sound = 'гав-гав'
        print(self.sound)

dog1 = Dog('Шарик')
while dog1.age < 7:
    print(dog1.age)
    dog1.bark(dog1.age)
    dog1.age += 1

    
    УДОЛИ!!!
