import tkinter as tk
from tkinter import ttk
import functions

# Initialize the main window
root = tk.Tk()
root.title("Movie Finder")
root.geometry("600x400")

# Fonts
TITLE_FONT = ("Helvetica", 24, "bold")
SUBTITLE_FONT = ("Helvetica", 16)
LABEL_FONT = ("Helvetica", 12)

# Title
title = tk.Label(root, text="Welcome to Movie Finder!", font=TITLE_FONT, justify="center")

# Search bar frame
search_frame = tk.Frame(root)
search_icon = tk.Label(search_frame, text="🔍", font=SUBTITLE_FONT)
search_entry = tk.Entry(search_frame, width=50, font=LABEL_FONT)
search_button = tk.Button(search_frame, text="Search", font=SUBTITLE_FONT, command=functions.search)

# Filters frame
filters_frame = tk.Frame(root)

#Cast
cast_label = tk.Label(filters_frame, text="Cast:", font=LABEL_FONT)
cast_combo = ttk.Combobox(filters_frame, values=["Select Cast"])

# Genre
genre_label = tk.Label(filters_frame, text="Genre:", font=LABEL_FONT)
crew_combo = ttk.Combobox(filters_frame, values=["Select Crew"])

# Release Date
release_label = tk.Label(filters_frame, text="Release Date:", font=SUBTITLE_FONT)
release_min_date_label = tk.Label(filters_frame, text="Minimum:", font=LABEL_FONT)
release_max_date_label = tk.Label(filters_frame, text="Maximum:", font=LABEL_FONT)
release_scale_min = tk.Scale(filters_frame, from_=1980, to=2025, orient="horizontal", length=100)
release_scale_max = tk.Scale(filters_frame, from_=1980, to=2025, orient="horizontal", length=100)

# Rating
rating_label = tk.Label(filters_frame, text="Rate:", font=SUBTITLE_FONT)
rating_min_date_label = tk.Label(filters_frame, text="Minimum:", font=LABEL_FONT)
rating_max_date_label = tk.Label(filters_frame, text="Minimum:", font=LABEL_FONT)
release_rate_min = tk.Scale(filters_frame, from_=0.0, to=10.0, orient="horizontal", length=100, resolution=0.1)
release_rate_max = tk.Scale(filters_frame, from_=0.0, to=10.0, orient="horizontal", length=100, resolution= 0.1)