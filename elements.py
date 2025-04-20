import tkinter as tk
from tkinter import ttk
import GUI_functions

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
search_button = tk.Button(search_frame, text="Search", font=SUBTITLE_FONT)

# Filters frame
filters_frame = tk.Frame(root)

#Cast
cast_label = tk.Label(filters_frame, text="Range:", font=LABEL_FONT)
cast_combo = ttk.Combobox(filters_frame, values=["Select Range"])

# Genre
genre_label = tk.Label(filters_frame, text="Genre:", font=LABEL_FONT)
crew_combo = ttk.Combobox(filters_frame, values=["Select Genre"])

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

# Database selection
structure_var = tk.StringVar(value="")
btree_radiobutton = tk.Radiobutton(search_frame, text="B tree", variable=structure_var, value="btree")
bplus_radiobutton = tk.Radiobutton(search_frame, text="B+ tree", variable=structure_var, value="bplus")

# Result table
results_frame = tk.Frame(root)
columns = ("tconst", "title_type", "primary_title", "start_year", "genres")
results_tree = ttk.Treeview(
    results_frame,
    columns=columns,
    show="headings",
    height=10
)
for col in columns:
    results_tree.heading(col, text=col.replace("_", " ").title())
    results_tree.column(col, width=120, anchor="w")

vsb = ttk.Scrollbar(results_frame, orient="vertical", command=results_tree.yview)
results_tree.configure(yscrollcommand=vsb.set)

# let the tree+scrollbar expand to fill results_frame
results_frame.rowconfigure(0, weight=1)
results_frame.columnconfigure(0, weight=1)