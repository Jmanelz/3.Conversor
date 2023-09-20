import math

class ConversorGradosRadianes:
    def __init__(self):
        pass

    def grados_a_radianes(self, grados):
        radianes = grados * math.pi / 180
        return radianes

    def radianes_a_grados(self, radianes):
        grados = radianes * 180 / math.pi
        return grados