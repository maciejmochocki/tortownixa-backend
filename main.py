import os
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeTorus
from OCC.Extend.DataExchange import write_stl_file, read_stl_file
from OCC.Display.SimpleGui import init_display

# Inicjalizacja wyświetlania
display, start_display, add_menu, add_function_to_menu = init_display()

# ustawienie folderu do eksportu obiektów
stl_output_dir = os.path.abspath(os.path.join("assets", "models"))

# Tworzenie obiektów
box = BRepPrimAPI_MakeBox(10, 20, 30).Shape()
my_torus = BRepPrimAPI_MakeTorus(20.0, 10.0).Shape()

# sprawdzenie sciezki
if not os.path.isdir(stl_output_dir):
    raise AssertionError("wrong path provided")

# ustawienie nazwy dla pliku
stl_file_torus = os.path.join(stl_output_dir, "torus.stl")

# eskport do pliku
write_stl_file(
    my_torus,
    stl_file_torus,
    mode="binary",
    linear_deflection=0.5,
    angular_deflection=0.3,
)

# Wczytywanie STL
stl_torus = read_stl_file(stl_file_torus)

# Wyświetlenie wczytanego pudełka
display.DisplayShape(stl_torus, update=True, color="RED")

# Uruchomienie interaktywnego widoku
start_display()
