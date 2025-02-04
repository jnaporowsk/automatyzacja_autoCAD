import geopandas as gpd
from win32com.client import Dispatch
import win32com
import win32com.client
import pythoncom
import random
import tkinter as tk
from tkinter import filedialog, messagebox


def vArray(*args):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, *args)

def choose_file():
    global shp_path
    shp_path = filedialog.askopenfilename(filetypes=[("Shapefiles", "*.shp")])
    if shp_path:
        label_plik.config(text=f"Wybrany plik: {shp_path}")
        load_types()

def load_types():
    global gdf
    gdf = gpd.read_file(shp_path)
    if 'type' in gdf.columns:
        typy = gdf['type'].dropna().unique().tolist()
        listbox_typy.delete(0, tk.END)  # Czyszczenie listy
        for typ in typy:
            listbox_typy.insert(tk.END, typ)
    else:
        messagebox.showerror("Błąd", "Plik nie zawiera kolumny 'type'!")

def draw_in_autocad():
    acad = Dispatch("AutoCad.Application")
    acad.visible = 1
    acadDoc = acad.ActiveDocument
    print(f"Połączono z AutoCAD: {acadDoc.Name}")

    # 4. Tworzenie warstw w AutoCAD
    layer_names = [listbox_typy.get(i) for i in listbox_typy.curselection()]
    for layer in layer_names:
        try:
            new_layer = acadDoc.Layers.Add(layer)  # Dodanie warstwy, jeśli nie istnieje
            new_layer.Color = random.randint(1, 255)
        except Exception:
            pass  # Warstwa już istnieje

    # 5. Rysowanie geometrii
    for _, row in gdf[gdf['type'].isin(layer_names)].iterrows():
        geometry = row.geometry
        building_type = row.get('type', 'inne')  # Domyślny typ "default"

        if geometry.geom_type == "Polygon":
            # Współrzędne poligonu
            points = list(geometry.exterior.coords)
            autocad_points = [item for tpl in points for item in tpl]


            # Rysowanie polilinii w AutoCAD
            polyline = acadDoc.ModelSpace.AddLightWeightPolyline(vArray(autocad_points))
            polyline.Closed = True  # Zamknięcie polilinii

            # Przypisanie polilinii do odpowiedniej warstwy
            try:
                polyline.Layer = str(building_type)
            except Exception:
                print(str(building_type), " zła nazwa w typie budynku")

    print("Rysowanie zakończone!")


# --- Tworzenie GUI ---
root = tk.Tk()
root.title("Import SHP do AutoCAD")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

btn_wybierz = tk.Button(frame, text="Wybierz plik SHP", command=choose_file)
btn_wybierz.pack()

label_plik = tk.Label(frame, text="Brak pliku", wraplength=300)
label_plik.pack()

listbox_typy = tk.Listbox(frame, selectmode=tk.MULTIPLE, height=10)
listbox_typy.pack()

btn_rysuj = tk.Button(frame, text="Rysuj w AutoCAD", command=draw_in_autocad)
btn_rysuj.pack()

root.mainloop()