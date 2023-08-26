import tkinter
import ttkbootstrap as ttk
from ttkbootstrap import Style
from ttkbootstrap.dialogs.dialogs import Messagebox
from ttkbootstrap.constants import *
from tkinter.filedialog import askopenfilename
from file import DataFile


class SimpleTextEdit(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title('Simple Text Edit')
        self.geometry('600x400')
        self.style = Style('darkly')
        self.text = ttk.Text()
        self.path_file = ttk.StringVar()
        self.file_frame()
        self.edit_frame()

    def file_frame(self):
        file_edit = ttk.LabelFrame(master=self, text='File:')
        file_edit.pack(fill=X, padx=(5, 5), pady=(5, 5))
        label_file_path = ttk.Label(master=file_edit, text='Path to file:')
        label_file_path.pack(side=LEFT, pady=(0, 10))
        label_path_to_file = ttk.Entry(master=file_edit, textvariable=self.path_file)
        label_path_to_file.pack(fill=X, expand=True, side=LEFT, pady=(0, 10))
        btn_open_file = ttk.Button(master=file_edit, bootstyle="default", text='Open File', command=self.btn_open_file)
        btn_open_file.pack(side=LEFT, padx=(10, 0), pady=(0, 10))
        self.btn_save_file = ttk.Button(master=file_edit, text='Save File', command=self.btn_save_file)
        self.btn_save_file.pack(side=LEFT, padx=(10, 0), pady=(0, 10))
        self.btn_save_file.config(state='disabled')
        self.btn_close_file = ttk.Button(master=file_edit, text='Close File', command=self.btn_close_file)
        self.btn_close_file.pack(side=RIGHT, padx=(10, 10), pady=(0, 10))
        self.btn_close_file.config(state='disabled')

    def edit_frame(self):
        edit_label = ttk.LabelFrame(master=self, text='Edit File:')
        edit_label.pack(fill=BOTH, expand=True, padx=(5, 5), pady=(5, 5))
        self.text = ttk.Text(master=edit_label)
        self.text.pack(fill=BOTH, expand=True, side=TOP, padx=(5, 5), pady=(5, 5))

    def btn_open_file(self):
        types_open_file = (
            ('Python files or Text files', '*.py *.txt'),
            ('All files', '*.*')
        )
        path = askopenfilename(title='Browse File', filetypes=types_open_file)
        if path:
            self.path_file.set(path)
            text_data = DataFile(self.path_file.get())
            self.text.insert(1.0, text_data.read())
            self.btn_close_file.config(state='active', bootstyle="default")
            self.btn_save_file.config(state='active', bootstyle="default")

    def btn_save_file(self):
        text_data_write = DataFile(self.path_file.get())
        text_data_write.write(self.text.get(1.0, END))
        Messagebox.ok(title='Save file', message=f'File {self.path_file.get()} - save success!')

    def btn_close_file(self):
        self.path_file.set(value='')
        self.text.delete(1.0, END)
        self.btn_close_file.config(state='disabled')
        self.btn_save_file.config(state='disabled')


if __name__ == "__main__":
    SimpleTextEdit().mainloop()
