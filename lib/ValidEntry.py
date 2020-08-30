'''import tkinter as tk
from tkinter import ttk

class Valid_Entry(ttk.Entry):

    def __init__(self, master, tam_maximo, *args, **kwargs):
        super().__init__(master, validate="key")
        self.tk
        self.vall = master.register(self.validate_input)
        super(Valid_Entry, self).__init__(master, validade="key", validatecommand=(self.vall, "%P", max_length), *args, **kwargs)



    def validate_input(self, new_value, max_length):
        valid = new_value .isdigit() and len(new_value) <= max_length
        return valid


###EXAMPLE###
#entry = tk.Entry(root, validate="key", validatecommand=(validate, "%P"))
#entry.pack(side="top", fill="x")'''