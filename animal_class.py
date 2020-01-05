# Define Animal Class

class Animal():
    # class is a cookie cutter for objects:
        # wraps its characteristics and its behaviours

    # define some characteristics
    def __init__(self, name, eyes, legs, age = 0):
        self.name = name
        self.bones = True
        self.alive = True
        self.number_eyes = eyes
        self.number_legs = legs
        self.__age = age

    # define some behaviours - methods
        # Things an instance of an object can do
        # Functions that are dependent on an object type

    def eat(self, food):
        return 'Nom NOM NOM! ' + food

    def mating(self):
        self.__rejuvenate()
        return ' <3 '

    def mate_calling(self):
        return 'Swipe right ;)'

    def sleep(self):
        self.__age += 1
        return 'zzzzz'

    def go_potty(self):
        return 'HHUMMM!!! ... O.O ! -.-      --- zen'

    # This is a getter
    def get_age(self):
        return self.__age

    # This is a setter
    def set_age(self, age):
        self.__age = age

    def __rejuvenate(self):
        self.__age -= 1

    def _display_members(self):
        return f'look ate these fine claws and members :) I got {self.number_legs} of them'
