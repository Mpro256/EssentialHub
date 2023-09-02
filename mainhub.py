import tkinter as tk
from tkinter import ttk
import subprocess


class GUIHub:
    def __init__(self, root):
        self.root = root
        self.root.title("Essential Hub")
        self.root.geometry("400x710")

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x = (screen_width - 400) // 2
        y = (screen_height - 700) // 2

        self.root.geometry(f"400x710+{x}+{y}")

        self.pink_color = "#FFC0CB"
        self.blue_color = "#87CEEB"

        self.style = ttk.Style()
        self.style.configure("TButton",
                             font=("Helvetica", 14, "bold"),
                             padding=10,
                             background=self.blue_color,
                             foreground="black",
                             bordercolor=self.blue_color,
                             focuscolor=self.pink_color,
                             highlightcolor=self.pink_color)

        self.button_frame = tk.Frame(root, bg=self.pink_color)
        self.button_frame.pack(fill=tk.BOTH, expand=True)

        self.buttons = []

        copyright_label = tk.Label(
            root, text="\u00A9 2023 Mpro256", font=("Helvetica", 10))
        copyright_label.pack(side="bottom")

    def add_button(self, text, command):
        button = ttk.Button(self.button_frame, text=text,
                            command=command, style="TButton")
        button.pack(fill=tk.X, pady=10)
        self.buttons.append(button)


if __name__ == "__main__":
    root = tk.Tk()
    hub = GUIHub(root)

    def example_function():
        print("Button clicked!")

    def calc():
        subprocess.Popen(["python", "calcfrontback.py"])

    def wordcombo():
        subprocess.Popen(["python", "wordcombos.py"])

    def passwordgen():
        subprocess.Popen(["python", "passwordgen.py"])

    hub.add_button("Calculator", calc)
    hub.add_button("Word Combo", wordcombo)
    hub.add_button("Password Generator", passwordgen)
    hub.add_button("Coming Soon", example_function)
    hub.add_button("Coming Soon", example_function)
    hub.add_button("Coming Soon", example_function)
    hub.add_button("Coming Soon", example_function)
    hub.add_button("Coming Soon", example_function)
    hub.add_button("Coming Soon", example_function)
    hub.add_button("Coming Soon", example_function)

    root.mainloop()
