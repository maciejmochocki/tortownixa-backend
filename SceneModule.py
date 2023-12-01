import os
import base64

from OCC.Core.BRep import BRep_Builder
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeTorus
from OCC.Core.TopLoc import TopLoc_Location
from OCC.Core.TopoDS import TopoDS_Compound
from OCC.Core.gp import gp_Vec, gp_Trsf
from OCC.Extend.DataExchange import write_stl_file, read_stl_file, read_step_file, read_iges_file
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
    
    def export_to_stl_base64(self):
        path = "assets/models/tmp.stl"
        compound = TopoDS_Compound()
        BRep_Builder().MakeCompound(compound)

        # dodaj wszystkie obiekty na scenie
        for obj in self.objects:
            BRep_Builder().Add(compound, obj)

        # Zapisz do pliku STL
        write_stl_file(compound, path, mode="binary", linear_deflection=0.5, angular_deflection=0.3)

        file_text = open(path, 'rb')
        file_read = file_text.read()
        file_encode = base64.encodebytes(file_read).decode('ascii')
        return file_encode

    def import_model(self, file_path, file_format, x=0, y=0, z=0):
        if file_format.lower() == "stl":
            shape = read_stl_file(file_path)
        elif file_format.lower() == "step":
            shape = read_step_file(file_path)
        elif file_format.lower() == "iges":
            shape = read_iges_file(file_path)
        else:
            raise ValueError("Unsupported file format")

        self.translate_object(shape, x, y, z)
        self.add_object(shape)

    def translate_object(self, obj, x, y, z):
        translation_vector = gp_Vec(x, y, z)
        trsf = gp_Trsf()
        trsf.SetTranslation(translation_vector)
        location = TopLoc_Location(trsf)
        obj.Move(location)
