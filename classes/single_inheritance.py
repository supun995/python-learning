"""
Object oriented programming consists of bundling data and code together into a single entity referred to as an object. Objects are the atomic building block of the Python runtime. One of the more powerful features of objects is their ability to inhert attributes from other object types. The ability to inherit attributes enables objects to augment and/or extend their functionality.

NOTE: From the perspective of the Python runtime methods are basically callable attributes. The use of the term attributes in this lab is overloaded to represent attributes and/or methods unless the distinction matters.

New Terms:

Base class
The class being inherited is referred to as a base class.
Derived class
The class inheriting from a base class is referred to as a derived class.
Inheritance allows objects to be created based on a hierarchy of base classes. The Python runtime includes a generic
object
, opens in a new tab that serves as the root base class.
"""


class Animal:
    def __init__(self, name, age, weight_kg):
        print(f'Animal.__init__({name=}, {age=}, {weight_kg=})')
        self.name = name
        self.age = age
        self.weight_kg = weight_kg
#This method provides an alternate way to create an object,
#Calls the actual class constructor: cls(name, age, weight_in_kg)
#Returns a new instance of the class
    @classmethod
    def from_pounds(cls, name, age, weight):
        return cls(name, age, weight / 2.2046)
#*others allows any number of extra positional arguments
    def play(self, *others):
        return ' '.join([
            f'{a.name} says {a.says}!' for a in [self] + list(others)
        ])
#[self] + list(others)-> Combines self with the others into a single list of all animals participating.
'''NOTE: The super callable is a powerful mechanism
for delegating method calls to base classes in the inheritance hierarchy. 
It will be covered more in-depth in another step.'''

class HouseCat(Animal):
    says = 'meow'
    def __init__(self, name, age, weight_kg, extrovertion_scale=3):
        print(f'HouseCat.__init__({name=}, {age=}, {weight_kg=}, {extrovertion_scale=})')
        super().__init__(name, age, weight_kg)
        # Set the level of introversion / extroversion
        # 0 = Introvert
        # 5 = Extrovert
        self.extrovertion_scale = extrovertion_scale

    #method overrides the base class implementation
    def play(self, *others):
        if self.extrovertion_scale <= 2:
            return f'{self.name} wants to be alone right now.'
        return super().play(
            *[animal for animal in others if getattr(animal, 'extrovertion_scale', 3) > 2]
        )
#*[a, b, c]	Unpacks a list into individual arguments: a, b, c
class Dog(Animal):
    says = 'woof'
    bark = 'awooooooo'

    def howl(self, times=3):
        return ' '.join([self.bark] * 3)

    def play(self, *others):
        def build_message(self, animal):
            if isinstance(animal, self.__class__):
                return f'{animal.name} says {animal.howl()}!'
            else:
                return f'{animal.name} says {animal.says}!'

        message = build_message(self, self)
        animals = [animal for animal in others if getattr(animal, 'extrovertion_scale', 3) > 2]
        animals = ' '.join([build_message(self, m) for m in animals])

        return f'{message} {animals}'





# class HouseCat:
#     ''' Models a standard house cat. '''
#     says = 'meow'

#     def __init__(self, name, age, weight_kg):
#         self.name = name
#         self.age = age
#         self.weight_kg = weight_kg

#     @classmethod
#     def from_pounds(cls, name, age, weight):
#         return cls(name, age, weight / 2.2046)

#     def play(self, *others):
#         if others:
#             players = ', '.join([o.name for o in others])
#             players = f'with {players}'
#         else:
#             players = 'alone'

#         return f'{self.name} is playing {players}. {self.says}'

class Husky(Dog):
    says = 'woo woo'
    bark = 'raa'

class Terrier(Dog):
    says = 'yip'
    bark = 'yap'

if __name__ == '__main__':

    def play_with(person: str, animals: list[Animal]):
        print(f'{person} is playing with: {" ".join([a.play() for a in animals])}')


    ada = HouseCat('Ada', 3, 6.3)
    print(f'Meet {ada.name} the {ada.age} year old house cat.')

    gus = HouseCat('Gus', 4, 5.1)
    print(f'Meet {gus.name} the {gus.age} year old house cat. ')

    hal = HouseCat.from_pounds('Hal', 2, 13)
    print(f'Meet {hal.name} the {hal.age} year old, {hal.weight_kg:.1f} kg. house cat. ')

    kara = Dog.from_pounds('Kara', 13, 15)
    rolo = Dog.from_pounds('Rolo', 8, 13)
    pogo = HouseCat('Pogo', 4, 5.3, 1)

    print(kara.play(ada, gus, hal, pogo, rolo))
    print(pogo.play(kara, gus, hal, pogo, rolo))


    play_with('This developer', [kara, gus, hal, pogo, rolo, ada])

    jojo = Husky.from_pounds('Jojo', 3, 40)
    lolo = Terrier.from_pounds('Lolo', 4, 20)

    play_with('This developer', [jojo, lolo])

    print(f'{jojo.name} is a {type(jojo).__name__}.')
    print(f'{lolo.name} is a {type(lolo).__name__}.')

    print(f'Husky is a subclass of Animal: {issubclass(Husky, Animal)}')
    print(f'Husky is a subclass of HouseCat: {issubclass(Husky, HouseCat)}')

    print(f'{jojo.name} is a Husky: {isinstance(jojo, Husky)}')

    print(f'{jojo.name} is an Animal: {isinstance(jojo, Animal)}')

    print(f'3.1415 is numeric: {isinstance(3.1415, (int, float))}')