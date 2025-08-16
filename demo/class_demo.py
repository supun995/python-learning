class animal:
    default_legs = 4

    def __init__(self,name,variant,breed,age):
        self.name = name
        self.variant = variant
        self.breed = breed
        self.age = age

    def speak(self):
        if self.variant == "dog":
            print("bow bow bow")
        else:
            print("meaw meaw")

    @classmethod
    def walk(cls):
        print(cls.default_legs)


dog = animal("shadow","dog","gsd",8)
dog.speak()
dog.walk()
