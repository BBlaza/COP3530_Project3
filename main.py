import elements
import GUI_functions

#sort movies according to genre, release date, movie name, cast
elements.search_button_Btree.config(command=GUI_functions.Btree_search)
elements.search_button_Bptree.config(command=GUI_functions.Bptree_search)

# Title
elements.title.pack(pady=10)

# Search bar frame
elements.search_frame.pack(pady=30)
elements.search_icon.grid(row=0, column=0)
elements.search_entry.grid(row=0, column=1, columnspan=2)
elements.search_button_Btree.grid(row=1, column=1)
elements.search_button_Bptree.grid(row=1, column=2)

# Timer
elements.search_timer.pack()

# Filters frame
elements.filters_frame.pack(pady=20)

# Duration_range
elements.duration_range_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
elements.duration_range_combo.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

# Genre
elements.genre_label.grid(row=0, column=3, padx=5, pady=5, sticky="e")
elements.genre_combo.grid(row=0, column=4, columnspan=2, padx=5, pady=5)

# Release Date
elements.release_label.grid(row=1, column=0, padx=2, pady=3, sticky="e")
elements.release_min_date_label.grid(row=1, column=1, padx=3, pady=3, sticky="e")
elements.release_scale_min.grid(row=1, column=2, padx=2, pady=3)
elements.release_max_date_label.grid(row=1, column=3, padx=3, pady=3, sticky="e")
elements.release_scale_max.grid(row=1, column=4, padx=5, pady=3)

# Rating
elements.rating_label.grid(row=2, column=0, padx=2, pady=3, sticky="e")
elements.rating_min_date_label.grid(row=2, column=1, padx=3, pady=3, sticky="e")
elements.rating_scale_min.grid(row=2, column=2, padx=2, pady=3)
elements.rating_max_date_label.grid(row=2, column=3, padx=3, pady=3, sticky="e")
elements.rating_scale_max.grid(row=2, column=4, padx=5, pady=3)

# Result table
elements.results_frame.pack(fill="both", expand=True, padx=10, pady=10)
elements.results_tree.grid(row=0, column=0, sticky="nsew")
elements.vsb.grid(row=0, column=1, sticky="ns")

# Run the app
elements.root.mainloop()