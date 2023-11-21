import os
import SceneModule as scene

from OCC.Core.BRep import BRep_Builder
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeTorus
from OCC.Core.TopoDS import TopoDS_Compound
from OCC.Extend.DataExchange import write_stl_file, read_stl_file
from OCC.Display.SimpleGui import init_display



# Inicjalizacja wyświetlania
display, start_display, add_menu, add_function_to_menu = init_display()

# Tworzenie obiektów
box = BRepPrimAPI_MakeBox(10, 20, 30).Shape()
my_torus = BRepPrimAPI_MakeTorus(20.0, 10.0).Shape()

# Tworzenie sceny
scene = scene.Scene()

# Dodanie obiektow do sceny
scene.add_object(box)
scene.add_object(my_torus)

# Usun box z sceny
scene.remove_object(box)

# sciezka do pliku sceny
stl_output = "assets/models/scene.stl"

# Zapisanie sceny do pliku
scene.export_to_stl(stl_output)

# Wczytanie sceny i wyswietlenie
stl_scene = read_stl_file(stl_output)

# Wyświetlenie wczytanego pudełka
display.DisplayShape(stl_scene, update=True, color="RED")

# Uruchomienie interaktywnego widoku
start_display()
