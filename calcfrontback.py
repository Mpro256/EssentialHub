import tkinter as tk
from tkinter import ttk


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x400")

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

        self.entry = ttk.Entry(self.button_frame, font=("Helvetica", 18))
        self.entry.grid(row=0, column=0, columnspan=4,
                        padx=10, pady=10, sticky="nsew")

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'
        ]

        row, col = 1, 0
        for button in buttons:
            ttk.Button(self.button_frame, text=button, command=lambda b=button: self.on_button_click(
                b), style="TButton").grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

        for i in range(5):
            self.button_frame.rowconfigure(i, weight=1)
            self.button_frame.columnconfigure(i, weight=1)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_button_click(self, value):
        if value == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif value == 'C':
            self.entry.delete(0, tk.END)
        else:
            current = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current + value)

    def on_closing(self):
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    calculator = CalculatorApp(root)
    root.mainloop()
