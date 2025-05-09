import pandas as pd
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification
from groq import Groq
import threading
import time
import os
from dotenv import load_dotenv 
load_dotenv()

class GenData:
    def __init__(self, df: pd.Series, column, text, main_frm: ttk.Frame):
        self.prompt = text
        self.main_frm = main_frm
        self.df = df
        self.column_name = column
        self.flood = ttk.Floodgauge(
                master=self.main_frm,
                bootstyle='primary',
                font=(None, 16, 'bold'),
                mask='{}%',
                value=0,
                name='progressBar',
                 maximum=100
            )

        data_entry_frm = ttk.Frame(master=self.main_frm, name='data_entry_field')
        naming_lbl = ttk.Label(data_entry_frm, text='Save As: ', font=(None, 16), bootstyle='light')
        naming_txt = ttk.Text(data_entry_frm, font=(None, 16), height=1, width=20)
        generate_btn = ttk.Button(data_entry_frm, text='Generate', bootstyle='light', command=self.execute)
        naming_lbl.pack(side='left')
        naming_txt.pack(side='left', expan=True, fill='both', padx=5)
        generate_btn.pack(side='left', expan=True, fill='both')

        data_entry_frm.place(relx=0.5, rely=0.45, anchor='center', relwidth=.6)
        self.flood.place(relx=0.5, rely=0.55, anchor='center', relwidth=.9)


    def execute(self):
        # self.main_frm.children['data_entry_field'].winfo_children()[1].state(["disabled"])
        # self.main_frm.children['data_entry_field'].winfo_children()[2].state(["disabled"])
        try:
            client = Groq(
                api_key=os.getenv('GROQ_API_KEY'),
            )
            print("api key initialization successeded")
        except:
            print("api key initialization failed")

       

        def generate_summary(url, prompt):
            # applying the prompt to each link
            full_prompt = f"{prompt}\n\nLink: {url}"
            response = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": full_prompt,
                    }
                ],
                model="llama3-8b-8192",
            )
            summary = response.choices[0].message.content
            return summary

        def process_excel():
            def update(val):
                self.flood['value'] = val
            # Create a list to store the summaries
            summaries = []
            len_data = len(self.df)
            # Iterate over each link and generate a summary
            for index, row in self.df.iterrows():
                
                url = row[self.column_name]
                try:
                    summary = generate_summary(url, self.prompt)
                except Exception as e:
                    summary = f"Error: {str(e)}"
                summaries.append(summary, )
                time.sleep(3)
                self.main_frm.after(0, update((index+1)/len_data * 100))
               

                # Add the summaries as a new column
            self.df['Summary'] = summaries

            # Save the results to a new Excel file
            name = self.main_frm.children['data_entry_field'].winfo_children()[1].get("1.0", "end-1c")
            output_file = "summarized_links.xlsx" if name == '' else f'{name}.xlsx'
            self.df.to_excel(output_file, index=False)
            toast = ToastNotification(
                bootstyle='success',
                alert=True,
                title="Message",
                message="your summery generated successfully!",
                duration=5000,
            )
            toast.show_toast()

            #print(f"Summaries saved to {output_file}")

        threading.Thread(target=process_excel).start()
