from Animals import Animal
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class Dog(Animal): ...

if __name__ == '__main__':
    shadow = Dog('shadow','germansheppard',3,4,'bow bow')
    timmy = Dog('timmy', 'street', 15, 4, 'bow bow')
    print(shadow.play(timmy))
