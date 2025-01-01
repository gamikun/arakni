CLASS_ARACHNID = 1

GENUS_SPIDER = 1

"""

"""

FAMILY_THERIDIIDAE = 1
FAMILY_ACHAEARANEA = 2
FAMILY_THERAPHOSIDAE = 3
FAMILY_MICROSTIGMATIDAE = 4

WEB_TANGLED = 1

SILK_WOOLLY = 1
SILK_ECRIBELLATE = 2
SILK_STICKY = 2

class Color:
    BLACK = 0x000000
    WHITE = 0xFFFFFF
    RED = 0xFF0000


class Animal:
    __slots__ = [
        'class', 'order', 'genus', 'family',
        'color', 'spots',
        'legs', 'size',
        ]

    def __init__(self, **kwargs):
        for s in self.__slots__:
            setattr(self, s, kwargs.get(s, None))


class Arachnid(Animal):
    __slots__ = ['spiderweb', 'silk']

    def __init__(self, **kwargs):
        kwargs['class'] = CLASS_ARACHNID
        kwargs['genus'] = GENUS_SPIDER
        kwargs['legs'] = 8
        super(Arachnidae, self).__init__(
            **kwargs
        )