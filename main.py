import csv
import tkinter as tk
from tkinter import ttk

with open('title.basics.tsv', newline='') as file:
    reader = csv.reader(file, delimiter='\t')
    print(type(reader))
#pranav likes dick
#genre, release date, movie name, cast

# Initialize the main window
root = tk.Tk()
root.title("Movie Finder")
root.geometry("600x400")

# Fonts
TITLE_FONT = ("Helvetica", 24, "bold")
SUBTITLE_FONT = ("Helvetica", 16)
LABEL_FONT = ("Helvetica", 12)

# Title
tk.Label(root, text="Welcome to Movie Finder!", font=TITLE_FONT, justify="center").pack(pady=10)

# Search bar frame
search_frame = tk.Frame(root)
search_frame.pack(pady=10)
search_icon = tk.Label(search_frame, text="🔍", font=SUBTITLE_FONT)
search_icon.pack(side="left")
search_entry = tk.Entry(search_frame, width=50, font=LABEL_FONT)
search_entry.insert(0, "search")
search_entry.pack(side="left")

# Filters frame
filters_frame = tk.Frame(root)
filters_frame.pack(pady=20)

# Cast
tk.Label(filters_frame, text="Cast:", font=LABEL_FONT).grid(row=0, column=0, padx=5, pady=5, sticky="e")
cast_combo = ttk.Combobox(filters_frame, values=["Select Cast"])
cast_combo.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

# Genre
tk.Label(filters_frame, text="Genre:", font=LABEL_FONT).grid(row=0, column=3, padx=5, pady=5, sticky="e")
crew_combo = ttk.Combobox(filters_frame, values=["Select Crew"])
crew_combo.grid(row=0, column=4, columnspan=2, padx=5, pady=5)

# Release Date (Slider)
tk.Label(filters_frame, text="Release Date:", font=SUBTITLE_FONT).grid(row=1, column=0, padx=2, pady=3, sticky="e")
tk.Label(filters_frame, text="Minimum:", font=LABEL_FONT).grid(row=1, column=1, padx=3, pady=3, sticky="e")
release_scale_mini = tk.Scale(filters_frame, from_=1980, to=2025, orient="horizontal", length=100)
release_scale_mini.grid(row=1, column=2, padx=2, pady=3)
tk.Label(filters_frame, text="Maximum:", font=LABEL_FONT).grid(row=1, column=3, padx=3, pady=3, sticky="e")
release_scale_max = tk.Scale(filters_frame, from_=1980, to=2025, orient="horizontal", length=100)
release_scale_max.grid(row=1, column=4, padx=5, pady=3)

# Rating (Slider)
tk.Label(filters_frame, text="Rate:", font=SUBTITLE_FONT).grid(row=2, column=0, padx=2, pady=3, sticky="e")
tk.Label(filters_frame, text="Minimum:", font=LABEL_FONT).grid(row=2, column=1, padx=3, pady=3, sticky="e")
release_rate_mini = tk.Scale(filters_frame, from_=0.0, to=10.0, orient="horizontal", length=100, resolution=0.1)
release_rate_mini.grid(row=2, column=2, padx=2, pady=3)
tk.Label(filters_frame, text="Maximum:", font=LABEL_FONT).grid(row=2, column=3, padx=3, pady=3, sticky="e")
release_rate_max = tk.Scale(filters_frame, from_=0.0, to=10.0, orient="horizontal", length=100, resolution= 0.1)
release_rate_max.grid(row=2, column=4, padx=5, pady=3)

# Run the app
root.mainloop()