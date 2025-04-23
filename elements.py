import tkinter as tk
from tkinter import ttk

# Initialize the main window
root = tk.Tk()
root.title("Movie Finder")
root.geometry("1200x800")

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
search_button_Bplustree = tk.Button(search_frame, text="Search in B+ Tree", font=SUBTITLE_FONT)
search_button_BRtree = tk.Button(search_frame, text="Search in B Tree", font=SUBTITLE_FONT)

# Log
log_label = tk.Label(root, font=LABEL_FONT)

# Filters frame
filters_frame = tk.Frame(root)

#Duration range
duration_range_label = tk.Label(filters_frame, text="Duration Range:", font=LABEL_FONT)
duration_range_combo = ttk.Combobox(filters_frame, values=['', 'less than 30 min', '31-59 min', '1-2 hours', '2-3 hours', '3-5 hours', '5-10 hours', 'more than 10 hours'])

# Genre
genre_label = tk.Label(filters_frame, text="Genre:", font=LABEL_FONT)
genre_combo = ttk.Combobox(filters_frame, values=['', 'Action', 'Adult', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Film-Noir', 'Game-Show', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News', 'Reality-TV', 'Romance', 'Sci-Fi', 'Short', 'Sport', 'Talk-Show', 'Thriller', 'War', 'Western'])

# Release Date
release_label = tk.Label(filters_frame, text="Release Date:", font=SUBTITLE_FONT)
release_min_date_label = tk.Label(filters_frame, text="Minimum:", font=LABEL_FONT)
release_max_date_label = tk.Label(filters_frame, text="Maximum:", font=LABEL_FONT)
release_scale_min = tk.Scale(filters_frame, from_=1800, to=2025, orient="horizontal", length=200)
release_scale_max = tk.Scale(filters_frame, from_=1801, to=2025, orient="horizontal", length=200)

# Rating
rating_label = tk.Label(filters_frame, text="Rate:", font=SUBTITLE_FONT)
rating_min_date_label = tk.Label(filters_frame, text="Minimum:", font=LABEL_FONT)
rating_max_date_label = tk.Label(filters_frame, text="Maximum:", font=LABEL_FONT)
rating_scale_min = tk.Scale(filters_frame, from_=0.0, to=10.0, orient="horizontal", length=200, resolution=0.1)
rating_scale_max = tk.Scale(filters_frame, from_=0.1, to=10.0, orient="horizontal", length=200, resolution= 0.1)

# Null Rating
take_null_rating_var = tk.BooleanVar(value=False)
take_null_rating_checkbox = tk.Checkbutton(filters_frame, text="Include movies without ratings",variable=take_null_rating_var)

# Result table
results_frame = tk.Frame(root)
columns = ("tconst", "title_type", "primary_title", "start_year", "runtime_minutes", "genres", "rating")
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