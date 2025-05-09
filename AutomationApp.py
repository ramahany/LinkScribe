import tkinter as tk
import ttkbootstrap as ttk
from tkinter import filedialog
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.toast import ToastNotification
from read_data import get_data
import numpy as np
from GenData import GenData
import re



class AutomationApp:

    def __init__(self, main_win: ttk.Window):
        # Creating the main window 
        self.window = main_win
        self.df = None
        self.main_frm = ttk.Frame(self.window, name='main_frame')
        self.add_data_btn = ttk.Button(self.main_frm, name='add_data_btn', width=50
                                       , text='Import Excel File', command=self.get_data_path)

        self.main_frm.pack(expand=True, fill='both', padx=20, pady=20)
        self.add_data_btn.place(relx=0.5, rely=0.5, anchor='center', height=75)




    def create_main_panel(self):
        self.main_frm.winfo_children()[0].destroy()
        # making the GRID
        num_rows = tuple([x for x in range(16)])
        num_columns = tuple([x for x in range(13)])

        self.main_frm.columnconfigure(num_columns, weight=1, uniform='a')
        self.main_frm.rowconfigure(num_rows, weight=1, uniform='b')

        data_frm = ttk.LabelFrame(self.main_frm, text='DATA',
                                    bootstyle="primary", name='data_frame')

        prompt_frm = ttk.LabelFrame(self.main_frm, text='PROMPT',
                                    bootstyle="primary", name='prompt_frame')
        prompt_txt = ttk.Text(prompt_frm, wrap=tk.WORD, font=(None, 12), height=10)

        prompt_txt.pack(expand=True, fill='both', padx=5, pady=5)

        column_menu_btn = ttk.Menubutton(self.main_frm, bootstyle="primary", text='Choose Column!',
                                         width=20, name='menu_btn', padding=5)
        # Creating inside menu

        def change_menu_var(x):
            column_menu_btn.config(text=x)

        inside_menu = ttk.Menu(column_menu_btn)

        for y in self.df.columns:
            inside_menu.add_radiobutton(label=y, command=lambda x=y: change_menu_var(x))

        column_menu_btn['menu'] = inside_menu

        btn = ttk.Button(self.main_frm, name='run_btn', text='Generate',
                         bootstyle="success", width=20, command=self.check_valid_inputs)

        data_frm.grid(row=0, column=0, columnspan=13, rowspan=10, sticky='nsew', padx=10)
        prompt_frm.grid(row=11, column=0, columnspan=9, rowspan=4, sticky='nsew', padx=10)
        column_menu_btn.grid(row=12, column=10, columnspan=2, rowspan=1, sticky='ew', padx=10)
        btn.grid(row=13, column=10, columnspan=2, rowspan=1, sticky='ew', padx=10)
        # btn.grid(row=6, column=9, columnspan=10, rowspan=1, sticky='nsew', padx=10, pady=10)

        return

    def get_data_path(self):
        init_dir = 'D:\\! --♥\\projects\\automation\\data_visualization'
        title = 'Select csv file'
        # file_types = (('text/csv', '*.csv'), ('all files', '*.csv',))
        file_types = (('Excel files', '*.xlsx;*.xls'), ('all files', '*.xlsx;*.xls'))
        file_path = filedialog.askopenfilename(initialdir=init_dir, title=title, filetypes=file_types)
        if file_path != '':
            self.df = get_data(file_path)
            self.create_main_panel()
            self.show_data()
        return

    def show_data(self):

        temp = self.main_frm.children['data_frame']
        colors = self.window.style.colors


        dt = Tableview(
            master=temp,
            coldata=self.df.columns.values,
            rowdata=np.array(self.df),
            paginated=True,
            searchable=False,
            bootstyle='dark',
        )
        dt.pagesize = 30  # how many records you want to show per page
        dt.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.98, relheight=0.98)

        return

    def check_valid_inputs(self):

        text = self.main_frm.children['prompt_frame'].winfo_children()[0].get("1.0", "end-1c")
        url_column = self.main_frm.children['menu_btn'].cget('text')

        if url_column == "Choose Column!":
            toast = ToastNotification(
                bootstyle='danger',
                alert=True,
                title="Message",
                message="u need to choose a column!",
                duration=5000,
            )
            toast.show_toast()
            return
        url_test = self.df[url_column][0]

        url_pattern = re.compile(
             r'^(https?://)?(www\.)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(/[\w./?%&=-]*)?$'
        )

        # Check if the string matches the pattern
        if text != '' and bool(url_pattern.match(str(url_test))):
            for child in self.main_frm.winfo_children():
                child.destroy()

            GenData(self.df, url_column, text, self.main_frm)
        else: 
            toast = ToastNotification(
                bootstyle='danger',
                alert=True,
                title="Message",
                message="invalid column or prompt pls recheck and try again!",
                duration=5000,
            )
            toast.show_toast()
            return





