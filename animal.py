import random
import sys
import os

class Animal:
    __name = None
    __height = 0
    __weight = 0
    __sound = 0

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def set_sound(self, sound):
        self.__sound = sound

    def get_sound(self):
        return self.__sound

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is a {} ft tall and {} KG Animal, sounding like {}".format(self.__name,
                                                                              self.__height,
                                                                              self.__weight,
                                                                              self.__sound)


class Pet(Animal):
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Pet, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print('Pet')

    def toString(self):
        return "{} is a {} ft tall and {} KG Animal, sounding like {} and owned by {}".format(self.__name,
                                                                                              self.__height,
                                                                                              self.__weight,
                                                                                              self.__sound,
                                                                                              self.__owner)

    def makeSound(self, howmany = None):
        if howmany is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * howmany)


class AnimalType:
    def get_type(self, animal):
        animal.get_type()
