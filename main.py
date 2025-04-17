import csv
import tkinter as tk

with open('title.basics.tsv', newline='') as file:
    reader = csv.reader(file, delimiter='\t')
    print(type(reader))
#pranav likes dick
#genre, release date, movie name, cast