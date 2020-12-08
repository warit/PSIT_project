"""TkinterRandomSortTest"""
import tkinter as tk
import random as ra
from tkinter import messagebox 
#RandomTestSort
def randomtest():
    times = (ent_lenght.get())
    ans = []
    lst = ['Selection Sort', 'Bubble Sort', 'Insertion Sort', 'Quick Sort', 'Merge Sort', 'Linear Search', 'Binary Search']
    if times in ['1' ,'2', '3', '4', '5', '6', '7']:
        for _ in range(int(times)):
            txt = ra.choice(lst)
            lst.remove(txt)
            ans.append(txt)
        lbl_result["text"] = " , ".join(ans)
    else:
        messagebox.showerror(title="Error", message="Must be integer 1-7")

window = tk.Tk()
window.title("Sort Test Random")
frm_entry = tk.Frame(master=window)
ent_lenght = tk.Entry(master=frm_entry, width=10)
lbl_lenght = tk.Label(master=frm_entry, text="How many test you want to random?")
lbl_lenght.grid(row=1, column=0, sticky="e")
ent_lenght.grid(row=1, column=1, sticky="w")
btn_rando = tk.Button(master=window,
text='Generate Now!',
command=randomtest)
lbl_result = tk.Label(master=window, text="You need to do...")
frm_entry.grid(row=1, column=0, padx=10)
btn_rando.grid(row=1, column=1, pady=10)
lbl_result.grid(row=2, column=0, padx=10)
window.mainloop()


randomtest()
