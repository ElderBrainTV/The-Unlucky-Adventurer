# import tkinter
from tkinter import *

# create window
window = Tk()

# create window title
window.title("Madlibs")

# create window size
window.geometry('500x500')

# create window color
window.configure(background="lightblue")

# create labels
title_label = Label(window, text="Madlibs", font=("Arial Bold", 20), bg="lightblue")
name_label = Label(window, text="Give our character a name!", font=("Arial Bold", 11), bg="lightblue")
objects1_label = Label(window, text="Name an object?", font=("Arial Bold", 11), bg="lightblue")
objects2_label = Label(window, text="Name another object!", font=("Arial Bold", 11), bg="lightblue")
objects3_label = Label(window, text="Name a third object?", font=("Arial Bold", 11), bg="lightblue")
objects4_label = Label(window, text="Name one last object!", font=("Arial Bold", 11), bg="lightblue")
adjectives1_label = Label(window, text="Give us an adjective!", font=("Arial Bold", 11), bg="lightblue")
adjectives2_label = Label(window, text="Give us another adjective!", font=("Arial Bold", 11), bg="lightblue")
adjectives3_label = Label(window, text="And another adjective!", font=("Arial Bold", 11), bg="lightblue")
adjectives4_label = Label(window, text="One more adjective, please?", font=("Arial Bold", 11), bg="lightblue")
verb1_label = Label(window, text="How about a verb?", font=("Arial Bold", 11), bg="lightblue")
verb2_label = Label(window, text="One more verb, please?", font=("Arial Bold", 11), bg="lightblue")

# create entry boxes
name_entry = Entry(window)
objects1_entry = Entry(window)
objects2_entry = Entry(window)
objects3_entry = Entry(window)
objects4_entry = Entry(window)
adjectives1_entry = Entry(window)
adjectives2_entry = Entry(window)
adjectives3_entry = Entry(window)
adjectives4_entry = Entry(window)
verb1_entry = Entry(window)
verb2_entry = Entry(window)

# create button
create_button = Button(window, text="Create Madlib", width=15, height=2, command=lambda: create_madlib())

# create textbox
textbox = Text(window, width=50, height=25)

# bind enter key
window.bind('<Return>', lambda x: create_madlib())

# create madlib function
def create_madlib():
    name = name_entry.get()
    objects1 = objects1_entry.get()
    objects2 = objects2_entry.get()
    objects3 = objects3_entry.get()
    objects4 = objects4_entry.get()
    adjectives1 = adjectives1_entry.get()
    adjectives2 = adjectives2_entry.get()
    adjectives3 = adjectives3_entry.get()
    adjectives4 = adjectives4_entry.get()
    verb1 = verb1_entry.get()
    verb2 = verb2_entry.get()

    textbox.delete(1.0, END)
    textbox.insert(INSERT, "The dark "+objects1+" streched on for what seemed like ages. My feet hitting the wet "+objects2+" was a\n "
    "reminder of reality. My "+objects3+" was nearing the bottom. \"What more will I be forced\n to endure?\" I pondered."
    " It felt as though the forest was calling me. \""+name+"\", it whispered. With not even a\n trace of a"
    " "+objects4+" around, my mind was forced to wonder for other means of entertainment. After what felt like\n a mile"
    " of walking, I finally ended up at a "+adjectives1+" village. At the sight of the first house on\n the corner of "
    "the village, I felt my body nearly collapse out of relief, and then it did. When I finally came to, I caught\n a "
    "glimpse of a "+adjectives2+" "+objects4+" looking through my pack. Somehow they had removed it from my back\n and"
    " were now searching through it. Quickly, I "+verb1+" my belongings\n without so much as a word to the kid. I knew"
    " he was likely a "+adjectives4+" "+objects4+" around these parts, or perhaps they were a thief-in-training\n and"
    " I was being too easy on them. His sins weren\'t mine to pass judgement upon, and\n I wasn\'t"
    " about to "+verb1+" a kid. Out of fear, he "+verb2+" off in a hurry after the encounter.")

# create save madlib function
def save_madlib():
    filename = name_entry.get()
    filenametxt = filename + ".txt"
    file = open(filenametxt,"x")
    name = name_entry.get()
    objects1 = objects1_entry.get()
    objects2 = objects2_entry.get()
    objects3 = objects3_entry.get()
    objects4 = objects4_entry.get()
    adjectives1 = adjectives1_entry.get()
    adjectives2 = adjectives2_entry.get()
    adjectives3 = adjectives3_entry.get()
    adjectives4 = adjectives4_entry.get()
    verb1 = verb1_entry.get()
    verb2 = verb2_entry.get()

    file.write("The dark "+objects1+" streched on for what seemed like ages. My feet hitting the wet "+objects2+" was a\n "
    "reminder of reality. My "+objects3+" was nearing the bottom. \"What more will I be forced\n to endure?\" I pondered."
    " It felt as though the forest was calling me. \""+name+"\", it whispered. With not even a\n trace of a"
    " "+objects4+" around, my mind was forced to wonder for other means of entertainment. After what felt like\n a mile"
    " of walking, I finally ended up at a "+adjectives1+" village. At the sight of the first house on\n the corner of "
    "the village, I felt my body nearly collapse out of relief, and then it did. When I finally came to, I caught\n a "
    "glimpse of a "+adjectives2+" "+objects4+" looking through my pack. Somehow they had removed it from my back\n and"
    " were now searching through it. Quickly, I "+verb1+" my belongings\n without so much as a word to the kid. I knew"
    " he was likely a "+adjectives4+" "+objects4+" around these parts, or perhaps they were a thief-in-training\n and"
    " I was being too easy on them. His sins weren\'t mine to pass judgement upon, and\n I wasn\'t"
    " about to "+verb1+" a kid. Out of fear, he "+verb2+" off in a hurry after the encounter.")
    file.close()
    print("Your madlib has been saved!")

# create button
save_button = Button(window, text="Save Madlib", width=15, height=2, command=lambda: save_madlib())

# place labels and buttons using grid
title_label.grid(column=0, row=0, columnspan=2, padx=10, pady=10)
name_label.grid(column=0, row=1, padx=10, pady=10)
objects1_label.grid(column=0, row=2, padx=10, pady=10)
objects2_label.grid(column=0, row=3, padx=10, pady=10)
objects3_label.grid(column=0, row=4, padx=10, pady=10)
objects4_label.grid(column=0, row=5, padx=10, pady=10)
adjectives1_label.grid(column=0, row=6, padx=10, pady=10)
adjectives2_label.grid(column=0, row=7, padx=10, pady=10)
adjectives3_label.grid(column=0, row=8, padx=10, pady=10)
adjectives4_label.grid(column=0, row=9, padx=10, pady=10)
verb1_label.grid(column=0, row=10, padx=10, pady=10)
verb2_label.grid(column=0, row=11, padx=10, pady=10)
name_entry.grid(column=1, row=1, padx=10, pady=10)
objects1_entry.grid(column=1, row=2, padx=10, pady=10)
objects2_entry.grid(column=1, row=3, padx=10, pady=10)
objects3_entry.grid(column=1, row=4, padx=10, pady=10)
objects4_entry.grid(column=1, row=5, padx=10, pady=10)
adjectives1_entry.grid(column=1, row=6, padx=10, pady=10)
adjectives2_entry.grid(column=1, row=7, padx=10, pady=10)
adjectives3_entry.grid(column=1, row=8, padx=10, pady=10)
adjectives4_entry.grid(column=1, row=9, padx=10, pady=10)
verb1_entry.grid(column=1, row=10, padx=10, pady=10)
verb2_entry.grid(column=1, row=11, padx=10, pady=10)
create_button.grid(column=0, row=12, padx=10, pady=10)
save_button.grid(column=1, row=12, padx=10, pady=10)
textbox.grid(column=0, row=13, columnspan=2, padx=10, pady=10)

# loop to keep window open
window.mainloop()
