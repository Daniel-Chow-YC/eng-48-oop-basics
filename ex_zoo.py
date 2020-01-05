from animal_class import *
from reptile_class import *

# create 2 reptiles
reptile1 = Reptile('Ringo', 2, 4, 17)
reptile2 = Reptile('Susan', 2, 4, 16)

# make the reptiles sleep
print(reptile1.sleep())
print(reptile2.sleep())
print(reptile1.n_chamber_hearts)

# print(reptile1.__age) # does not work because it is encapsulated
reptile1.set_age(19)
print(reptile1.get_age())

print(reptile1._display_members()) # Low level encapsulation