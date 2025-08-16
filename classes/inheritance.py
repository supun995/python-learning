class Animal:
    def __init__(self, name, age, weight_kg):
        print(f'Animal.__init__({name=}, {age=}, {weight_kg=})')
        self.name = name
        self.age = age
        self.weight_kg = weight_kg

    @classmethod
    def from_pounds(cls, name, age, weight):
        return cls(name, age, weight / 2.2046)

    def play(self, *others):
        return ' '.join([
            f'{a.name} says {a.says}!' for a in [self] + list(others)
        ])


class HouseCat(Animal):
    says = 'meow'

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

if __name__ == '__main__':
    ada = HouseCat('Ada', 3, 6.3)
    print(f'Meet {ada.name} the {ada.age} year old house cat.')

    gus = HouseCat('Gus', 4, 5.1)
    print(f'Meet {gus.name} the {gus.age} year old house cat. ')

    hal = HouseCat.from_pounds('Hal', 2, 13)
    print(f'Meet {hal.name} the {hal.age} year old, {hal.weight_kg:.1f} kg. house cat. ')

