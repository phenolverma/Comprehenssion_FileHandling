import tkinter as tk
from tkinter import filedialog
import subprocess


def run_main_py():
    try:
        subprocess.run(["python", "my_read.py"], check=True)
    except subprocess.CalledProcessError:
        # Handle any errors that may occur during the execution of main.py
        pass


# def write_data():
#     data = output_label.cget("text")
#     file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
#     if file_path:
#         with open(file_path, "w") as file:
#             file.write(data)


root = tk.Tk()
root.title("Data Read and Write")

# Input widget
input_entry = tk.Entry(root)
input_entry.pack()

# Output widget
output_label = tk.Label(root, text="")
output_label.pack()

# Buttons
run_button = tk.Button(root, text="Run main.py", command=run_main_py)
run_button.pack()

# write_button = tk.Button(root, text="Write Data", command=write_data)
# write_button.pack()

root.mainloop()
