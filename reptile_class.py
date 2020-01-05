from animal_class import *

class Reptile(Animal):
    def __init__(self, name, eyes, legs, n_chamber_hearts, age = 0):
        super().__init__(name, eyes, legs, age)
        self.scales = True
        self.cold_blooded = True
        self.n_chamber_hearts = n_chamber_hearts

    def mate_calling(self): # This is an example of polymorphism
        return 'Look at my scales! They look good!'

    def seek_heat(self):
        return 'hmmm bit chilly, lets get some sun'

    def seek_shade(self):
        return 'Who turn on the heating in this world --> going to find some shade'

    def prey(self):
        return 'Waiiit for it ... aand POUNCE!!!'

    def lay_eggs(self):
        return 'What you looking at? Never seen a lizard lay eggs?'

