from animal import Animal
from animal import Pet
from animal import AnimalType

tiger = Animal('tigron', 7, 200, 'roar')

print(tiger.toString())


mike = Pet('mike', 4, 30, 'bow wow wow yippie ye yippie yow ', 'snoop')

mike.makeSound()

type_animals = AnimalType()

type_animals.get_type(mike)
