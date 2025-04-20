import elements


#sort movies according to genre, release date, movie name, cast


# Title
elements.title.pack(pady=10)

# Search bar frame
elements.search_frame.pack(pady=10)
elements.search_icon.pack(side="left")
elements.search_entry.pack(side="left")
elements.search_button.pack(side="left")

# Filters frame
elements.filters_frame.pack(pady=20)

# Cast
elements.cast_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
elements.cast_combo.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

# Genre
elements.genre_label.grid(row=0, column=3, padx=5, pady=5, sticky="e")
elements.crew_combo.grid(row=0, column=4, columnspan=2, padx=5, pady=5)

# Release Date
elements.release_label.grid(row=1, column=0, padx=2, pady=3, sticky="e")
elements.release_min_date_label.grid(row=1, column=1, padx=3, pady=3, sticky="e")
elements.release_scale_min.grid(row=1, column=2, padx=2, pady=3)
elements.release_max_date_label.grid(row=1, column=3, padx=3, pady=3, sticky="e")
elements.release_scale_max.grid(row=1, column=4, padx=5, pady=3)

# Rating
elements.rating_label.grid(row=2, column=0, padx=2, pady=3, sticky="e")
elements.rating_min_date_label.grid(row=2, column=1, padx=3, pady=3, sticky="e")
elements.release_rate_min.grid(row=2, column=2, padx=2, pady=3)
elements.rating_max_date_label.grid(row=2, column=3, padx=3, pady=3, sticky="e")
elements.release_rate_max.grid(row=2, column=4, padx=5, pady=3)

# Database selection
elements.btree_radiobutton.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="w")
elements.bplus_radiobutton.grid(row=3, column=2, columnspan=2, padx=5, pady=5, sticky="w")

# Run the app
elements.root.mainloop()