#!/usr/bin/python3
""" modeule for base class """


class Base:
    """ representation for the base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructore for base class """
    if id is not None:
        self.id = id
    else:
        Base.__nb_objects += 1
        self.id = Base.__nb_objects