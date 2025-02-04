# 🏗️ Rysowanie budynków z plików SHP w AutoCAD za pomocą Python

## 📌 Opis
Ten projekt umożliwia automatyczne rysowanie budynków z plików **SHP** w programie **AutoCAD**. Dane budynków, wraz z ich typami, pochodzą z **[Geofabrik OpenStreetMap](https://download.geofabrik.de/europe.html)**. Skrypt pozwala na wybór pliku SHP, filtrowanie budynków według ich typu i narysowanie ich w otwartym pliku AutoCAD.

## 🚀 Funkcje
✅ Wybór pliku SHP poprzez interfejs graficzny  
✅ Filtrowanie budynków według ich typu  
✅ Automatyczne tworzenie warstw w AutoCAD dla różnych typów budynków  
✅ Rysowanie budynków na podstawie geometrii SHP  

## 🛠️ Wymagania
🔹 **Python 3.8+**  
🔹 **AutoCAD** (uruchomiony w tle)  
🔹 **Biblioteki Python**:
- `geopandas`
- `shapely`
- `pywin32`
- `pyautocad`
- `tkinter` (wbudowany w Pythona)

📦 Możesz zainstalować brakujące pakiety za pomocą:
```bash
pip install geopandas shapely pywin32 pyautocad
```

## 📂 Struktura projektu
```
📁 projekt_autocad_shp
 ├── main.py          # Główny skrypt aplikacji
 ├── README.md        # Dokumentacja projektu
 ├── /sample_data     # Folder z rynkiem Krakowa do przedstawienia działania skryptu 
```

## ▶️ Jak uruchomić?
1️⃣ Uruchom AutoCAD.  
2️⃣ Otwórz terminal w katalogu projektu.  
3️⃣ Wpisz i uruchom:
```bash
python main.py
```
4️⃣ Wybierz plik SHP i typy budynków, które chcesz narysować.  
5️⃣ Kliknij "Rysuj", aby dodać budynki do AutoCAD.  

## 📸 Zrzuty ekranu
![image](https://github.com/user-attachments/assets/a1258c2f-094a-4daf-ade1-554f36556796)
![image](https://github.com/user-attachments/assets/305d8690-14da-4432-9249-411d4757c6b6)
![image](https://github.com/user-attachments/assets/905f1e75-3822-49f6-9aa9-b73c338cf415)




## 📌 Źródła danych
Dane SHP pobrane z **[Geofabrik](https://download.geofabrik.de/europe.html)**, zawierają budynki i ich typy na podstawie OpenStreetMap.

