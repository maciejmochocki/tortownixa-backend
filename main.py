from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Extend.DataExchange import write_step_file, read_step_file
from OCC.Core.STEPControl import STEPControl_Reader
from OCC.Display.SimpleGui import init_display

# Inicjalizacja wyświetlania
display, start_display, add_menu, add_function_to_menu = init_display()

# Tworzenie pudełka
box = BRepPrimAPI_MakeBox(10, 20, 30).Shape()

# Zapisywanie pudełka do pliku w formacie data przy pomocy step
output_step_file = "box.data"
write_step_file(box, output_step_file)

# Wczytywanie pudełka z pliku STEP
reader = STEPControl_Reader()
reader.ReadFile(output_step_file)
reader.TransferRoots()

# Pobieranie wczytanego obiektu
loaded_box = reader.OneShape()

# Wyświetlenie oryginalnego pudełka
display.DisplayShape(box)

# Wyświetlenie wczytanego pudełka
display.DisplayShape(loaded_box, color="RED")

# Uruchomienie interaktywnego widoku
start_display()
