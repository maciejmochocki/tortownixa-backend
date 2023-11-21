import os

from OCC.Core.BRep import BRep_Builder
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeTorus
from OCC.Core.TopoDS import TopoDS_Compound
from OCC.Extend.DataExchange import write_stl_file, read_stl_file
from OCC.Display.SimpleGui import init_display


class Scene:
    def __init__(self):
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def remove_object(self, obj):
        self.objects.remove(obj)

    def export_to_stl(self, path):
        # deklaracja pustego obiektu
        compound = TopoDS_Compound()
        BRep_Builder().MakeCompound(compound)

        # dodaj wszystkie obiekty na scenie
        for obj in self.objects:
            BRep_Builder().Add(compound, obj)

        # Zapisz do pliku STL
        write_stl_file(compound, path, mode="binary", linear_deflection=0.5, angular_deflection=0.3)
