import tkinter as tk
import subprocess


def run_terminal_command():
    command = "python my_read.py"
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, result.stdout)
        output_text.insert(tk.END, result.stderr)
    except subprocess.CalledProcessError as e:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Error: {e}")


root = tk.Tk()
root.title("Run Terminal Command")

run_button = tk.Button(root, text="Run Terminal Command", command=run_terminal_command)
run_button.pack()

output_text = tk.Text(root, wrap=tk.WORD)
output_text.pack()

root.mainloop()
