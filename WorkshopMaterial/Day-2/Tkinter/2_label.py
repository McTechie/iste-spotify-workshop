import tkinter as tk

# Using inheritance
class CustomLabel(tk.Label):
    def __init__(self, master, *args, **kwargs):
        tk.Label.__init__(self, master, *args, **kwargs)
        self['background'] = "red"
        self['foreground'] = "blue"
        self['padx'] = 20
        self['pady'] = 20


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Label")
    root.state("zoomed")

    label1 = tk.Label(
        text = "Hello",
        background = "red",
        foreground = "blue", # Changing Text Color
        padx = 20,
        pady = 20
    )

    label2 = CustomLabel(root, text="World")

    # Placing the labels on the window
    label1.pack() # Geometry Manager provided by Tkinter
    label2.pack() # Geometry Manager provided by Tkinter

    root.mainloop()
