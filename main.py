import tkinter as tk
from selfmodule import *

HEIGHT = 700
WIDTH = 800

def get_output(entered_keyword):
           try:
                 entereddata(entered_keyword)
           except:
                 label1=tk.Label(root,text=" ENTER VALID KEYWORD ",fg="blue",font=("Helvetica", 16))
                 label1.pack()
                 root.after(3000, label1.destroy)

if __name__=="__main__":
            root = tk.Tk()
            root.title("OPINION MINING")
            canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)

            lb=tk.Label(root,text="ENTER SEARCH QUERY",font=("Helvetica",11,'bold'))
            lb.place(relwidth=0.2,relheight=0.3)

            entry = tk.Entry(root, font=40)
            entry.place(relx=0.4,relwidth=0.2, relheight=0.3)

            button = tk.Button(root, text="SEARCH",bg="#ffe6e6",font=("Helvetica", 16,'bold'), command=lambda: get_output(entry.get()))
            button.place(relx=0.25, rely=0.7, relwidth=0.2, relheight=0.3,anchor="center")

            canvas.pack()
            root.mainloop()
