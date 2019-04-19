class Cat:
    def __init__(self):
        self.name = "Cat"
    def meow(self):
        return "meow!"

class Human:
    def __init__(self):
        self.name = "Human"
    def speak(self):
        return "hello!"

class Adapter:
    def __init__(self, obj, sound):
        self.obj = obj
        self.obj_sound  = sound
    def sound(self):
        return getattr(self.obj, self.obj_sound)()

standard_cat = Adapter(Cat(), 'meow')
print(standard_cat.sound())
standard_human = Adapter(Human(), 'speak')
print(standard_human.sound())