import logging

class Animal:
    def __init__(self,name , type, age ,legs , sound):
        self.logger = logging.getLogger('animal')
        self.name = name
        self.type = type
        self.age = age
        self.legs = legs
        self.sound = sound

    def play(self,*others):
        self.logger.info(f'{self.name} invoked play')
        return ''.join([f'{a.name} says {a.sound}*3 !' for a in [self] + list(others)])

    @classmethod
    def from_pounds(cls,name , type, age ,legs , sound):
        return cls(name , type, age ,legs , sound)



