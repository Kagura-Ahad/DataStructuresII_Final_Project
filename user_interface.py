from data_insertion import insert_from_CSV
from tkinter import ttk
import tkinter as tk


finger_trees = insert_from_CSV()

# GUI design

# create the tkinter window
window = tk.Tk()
window.geometry("800x600")

# create a frame to hold the left widgets
left_frame = tk.Frame(window, width=400, height=300)
left_frame.pack(side=tk.LEFT)

# create the labels and comboboxes for the left side
greenhouse_label = tk.Label(left_frame, text="GreenHouse:")
greenhouse_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
greenhouse_combobox = tk.ttk.Combobox(left_frame, values=["Greenhouse 1", "Greenhouse 2"])
greenhouse_combobox.grid(row=0, column=1, padx=5, pady=5, sticky="w")

start_time_label = tk.Label(left_frame, text="Start Time:")
start_time_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
start_time_combobox = tk.ttk.Combobox(left_frame, values=["00:00", "01:00", "02:00"])
start_time_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="w")

end_time_label = tk.Label(left_frame, text="End Time:")
end_time_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
end_time_combobox = tk.ttk.Combobox(left_frame, values=["23:00", "22:00", "21:00"])
end_time_combobox.grid(row=2, column=1, padx=5, pady=5, sticky="w")

start_day_label = tk.Label(left_frame, text="Start Day:")
start_day_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
start_day_combobox = tk.ttk.Combobox(left_frame, values=["Monday", "Tuesday", "Wednesday"])
start_day_combobox.grid(row=3, column=1, padx=5, pady=5, sticky="w")

end_day_label = tk.Label(left_frame, text="End Day:")
end_day_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
end_day_combobox = tk.ttk.Combobox(left_frame, values=["Thursday", "Friday", "Saturday"])
end_day_combobox.grid(row=4, column=1, padx=5, pady=5, sticky="w")

calculate_button = tk.Button(left_frame, text="Calculate")
calculate_button.grid(row=5, column=0, columnspan=2)

result_textbox = tk.Text(left_frame, height=1, width=50)
result_textbox.grid(row=6, column=0, columnspan=2)

# create a frame to hold the right widgets
right_frame = tk.Frame(window, width=400, height=300)
right_frame.pack(side=tk.RIGHT)

# create the labels and comboboxes for the right side
type_label = tk.Label(right_frame, text="Type:")
type_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
type_combobox = tk.ttk.Combobox(right_frame, values=["Type A", "Type B", "Type C"])
type_combobox.grid(row=0, column=1, padx=5, pady=5, sticky="w")

value_label = tk.Label(right_frame, text="Value:")
value_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
value_combobox = tk.ttk.Combobox(right_frame, values=["Value 1", "Value 2", "Value 3"])
value_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="w")

greenhouse_label_2 = tk.Label(right_frame, text="GreenHouse:")
greenhouse_label_2.grid(row=2, column=0, padx=5, pady=5, sticky="e")
greenhouse_combobox_2 = tk.ttk.Combobox(right_frame, values=["Greenhouse 1", "Greenhouse 2"])
greenhouse_combobox_2.grid(row=2, column=1, padx=5, pady=5, sticky="w")

start_time_label_2 = tk.Label(right_frame, text="Start Time:")
start_time_label_2.grid(row=3, column=0, padx=5, pady=5, sticky="e")
start_time_combobox_2 = tk.ttk.Combobox(right_frame, values=["00:00", "01:00", "02:00"])
start_time_combobox_2.grid(row=3, column=1, padx=5, pady=5, sticky="w")

end_time_label_2 = tk.Label(right_frame, text="End Time:")
end_time_label_2.grid(row=4, column=0, padx=5, pady=5, sticky="e")
end_time_combobox_2 = tk.ttk.Combobox(right_frame, values=["23:00", "22:00", "21:00"])
end_time_combobox_2.grid(row=4, column=1, padx=5, pady=5, sticky="w")

start_day_label_2 = tk.Label(right_frame, text="Start Day:")
start_day_label_2.grid(row=5, column=0, padx=5, pady=5, sticky="e")
start_day_combobox_2 = tk.ttk.Combobox(right_frame, values=["Monday", "Tuesday", "Wednesday"])
start_day_combobox_2.grid(row=5, column=1, padx=5, pady=5, sticky="w")

end_day_label_2 = tk.Label(right_frame, text="End Day:")
end_day_label_2.grid(row=6, column=0, padx=5, pady=5, sticky="e")
end_day_combobox_2 = tk.ttk.Combobox(right_frame, values=["Thursday", "Friday", "Saturday"])
end_day_combobox_2.grid(row=6, column=1, padx=5, pady=5, sticky="w")

search_button = tk.Button(right_frame, text="Search")
search_button.grid(row=7, column=0, columnspan=2)

result_textbox_2 = tk.Text(right_frame, height=1, width=50)
result_textbox_2.grid(row=8, column=0, columnspan=2)
window.mainloop()