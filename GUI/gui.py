import tkinter as tk
from PIL import Image, ImageTk

# Load the Romania map image
MAP_PATH = "map.webp"
MAP_WIDTH = 900
MAP_HEIGHT = 700

# Define all major city coordinates based on the image positioning
cities = {
    "Bucharest": (630, 600),
    "Cluj-Napoca": (325, 245),
    "Timișoara": (160, 460),
    "Iași": (750, 160),
    "Constanța": (780, 650),
    "Brașov": (530, 430),
    "Sibiu": (410, 350),
    "Oradea": (270, 190),
    "Craiova": (480, 580),
    "Galați": (760, 350),
    "Arad": (190, 370),
    "Pitești": (560, 510),
    "Bacău": (690, 280),
    "Suceava": (680, 140),
    "Târgu Mureș": (425, 270),
    "Ploiești": (600, 470),
    "Brăila": (760, 380),
    "Buzău": (660, 460),
    "Baia Mare": (330, 135),
    "Satu Mare": (257, 113),
    "Alba Iulia": (400, 310),
    "Bistrița": (500, 190),
    "Drobeta-Turnu Severin": (250, 580),
    "Târgu Jiu": (350, 520),
    "Reșița": (200, 500),
    "Slatina": (450, 550),
    "Râmnicu Vâlcea": (460, 490),
    "Focșani": (720, 350),
    "Botoșani": (710, 110),
    "Deva": (370, 370),
    "Hunedoara": (360, 390),
    "Sfântu Gheorghe": (570, 400),
    "Zalău": (290, 160),
    "Tulcea": (850, 450),
}

# Function to handle city clicks
def on_city_click(city_name):
    print(f"Selected city: {city_name}")

# Initialize Tkinter window
root = tk.Tk()
root.title("Clickable Romania Map")
root.geometry(f"{MAP_WIDTH}x{MAP_HEIGHT}")

# Load and display the map image
image = Image.open(MAP_PATH)
image = image.resize((MAP_WIDTH, MAP_HEIGHT), Image.LANCZOS)
map_image = ImageTk.PhotoImage(image)
canvas = tk.Canvas(root, width=MAP_WIDTH, height=MAP_HEIGHT)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=map_image)

# Draw clickable cities on the map
for city, (x, y) in cities.items():
    city_oval = canvas.create_oval(x-5, y-5, x+5, y+5, fill="red", outline="black")
    canvas.create_text(x+10, y, text=city, anchor="w", font=("Arial", 10), fill="black")
    canvas.tag_bind(city_oval, "<Button-1>", lambda event, city_name=city: on_city_click(city_name))

# Run the GUI
root.mainloop()
