import tkinter as tk
from PIL import Image, ImageTk
from IDAScript.script import idADistance

# Load the Romania map image
MAP_PATH = "map.webp"
MAP_WIDTH = 900
MAP_HEIGHT = 700

cities = {
    "București": (560, 550),         # Schimbare: Bucharest -> București
    "Slobozia": (676, 534),
    "Cluj-Napoca": (325, 245),
    "Piatra Neamț": (576, 219),      # Schimbare: Piatra Neamt -> Piatra Neamț
    "Timișoara": (92, 380),
    "Iași": (698, 199),
    "Constanța": (810, 618),
    "Miercurea Ciuc": (530, 297),
    "Brașov": (510, 402),            # Schimbare: Brasov -> Brașov
    "Sibiu": (383, 390),
    "Oradea": (165, 205),
    "Craiova": (326, 577),
    "Galați": (743, 423),
    "Arad": (100, 320),
    "Pitești": (440, 508),
    "Bacău": (635, 276),
    "Vaslui": (709, 278),
    "Suceava": (564, 135),
    "Târgu Mureș": (425, 270),
    "Ploiești": (547, 493),
    "Călărași": (673, 593),          # Schimbare: Calarasi -> Călărași
    "Giurgiu": (543, 640),
    "Brăila": (727, 447),
    "Buzău": (623, 470),
    "Baia Mare": (330, 135),
    "Satu Mare": (257, 113),
    "Alba Iulia": (325, 340),
    "Bistrița": (403, 193),          # Schimbare: Bistrita -> Bistrița
    "Drobeta-Turnu Severin": (226, 528),
    "Târgu Jiu": (290, 480),
    "Reșița": (165, 442),
    "Slatina": (400, 570),
    "Râmnicu Vâlcea": (390, 479),
    "Târgoviște": (493, 501),        # Schimbare: Targoviste -> Târgoviște
    "Focșani": (645, 393),
    "Botoșani": (611, 118),
    "Deva": (255, 355),
    "Sfântu Gheorghe": (533, 370),
    "Zalău": (270, 190),             # Schimbare: Zalau -> Zalău
    "Tulcea": (820, 460),
    "Alexandria": (483, 620),
}


selected_cities = []
city_ovals = {}

# Function for selecting the cities buttons
def on_city_click(city_name, city_oval):
    global selected_cities

    if city_name in selected_cities:
        # If city is already selected, deselect it
        selected_cities.remove(city_name)
        canvas.itemconfig(city_oval, fill="yellow")
    else:
        if len(selected_cities) == 2:
            # Remove the oldest selected city
            old_city = selected_cities.pop(0)
            canvas.itemconfig(city_ovals[old_city], fill="yellow")

        # Add new city and highlight it
        selected_cities.append(city_name)
        canvas.itemconfig(city_oval, fill="red")

    print(f"Selected cities: {selected_cities}")

# Function that computes the distance between 2 cities
def calculeaza_distanta():
    if len(selected_cities) != 2:
        print("Trebuie sa selectezi exact 2 orase pentru a calcula distanta.")
        return

    city1, city2 = selected_cities
    print(f"Calculam distanta intre {city1} si {city2}...")
    idADistance(city1, city2)

root = tk.Tk()
root.title("Romania")
root.geometry(f"{MAP_WIDTH}x{MAP_HEIGHT + 50}")

image = Image.open(MAP_PATH)
image = image.resize((MAP_WIDTH, MAP_HEIGHT), Image.LANCZOS)
map_image = ImageTk.PhotoImage(image)

canvas = tk.Canvas(root, width=MAP_WIDTH, height=MAP_HEIGHT)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=map_image)

for city, (x, y) in cities.items():
    city_oval = canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="yellow", outline="black")
    city_ovals[city] = city_oval
    canvas.create_text(x + 10, y, text=city, anchor="w", font=("Arial", 10), fill="black")
    canvas.tag_bind(city_oval, "<Button-1>",
                    lambda event, city_name=city, oval=city_oval: on_city_click(city_name, oval))

button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, anchor=tk.W, padx=10, pady=10)

distance_button = tk.Button(button_frame, text="Calculează Distanța", command=calculeaza_distanta)
distance_button.pack()

root.mainloop()
