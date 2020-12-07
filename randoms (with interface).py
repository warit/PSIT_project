from tkinter import *
from tkinter import messagebox
import random, string, webbrowser


def Random2Digit():
    """2 digit number random function"""
    r_2digit = random.randint(1, 100) # สุ่มเลข 01 ถึง 99
    messagebox.showinfo(title="Good luck", message="Good Luck Bro! %02d" %(r_2digit))

def Randon3Digit():
    """3 digit number random function"""
    r_3digit = random.randint(1, 1000) # สุ่มเลข 001 ถึง 999
    messagebox.showinfo(title="Good luck", message="Have a good day! %03d " %(r_3digit))

def Random6Digit():
    """6 digit number random function"""
    r_6digit = random.randint(1, 1000000) # สุ่มเลข 000001 ถึง 999999
    messagebox.showinfo(title="Good luck", message="Have a beautiful day! %06d" %(r_6digit))

def RandomTossCoin():
    """Toss coin heads or tails function"""
    r_coin = random.choice(["Heads", "Tails"]) # สุ่มหัว, ก้อย
    messagebox.showinfo(title="Good luck", message="toss coins : " + r_coin)

def RandomPassword():
    """Password random function"""
    character = "abcdefghijklmnopqrstuvwxyz012345678970ABCDEFGHIJKLMNOPQRSTUVWXYZ_" # string อักขระสำหรับสุ่ม
    r_lenght = random.randint(8, 13) # len ของ password เป็นสุ่ม
    password = "".join(random.sample(character, r_lenght)) # สลับที่ตัวอักษรของ password เป็นสุ่ม
    while not password.isidentifier():
        password = "".join(random.sample(character, r_lenght)) # สลับที่ตัวอักษรของ password เป็นสุ่ม
    condition = messagebox.askyesnocancel(title='Your password', message='Press "Yes" to print password'.center(45) + '\n' + 'Press "No" to try a new one'.center(45) + '\n' + '\n' + f'{password}'.center(45))
    if condition == True:
        print('This is your password >>>>>>>>', (password + " ").ljust(20, "<")) # กด "Yes" เพื่อ print ข้อมูลมาใช้
        # RandomPassword()
    elif condition == False:
        RandomPassword() # กด "No" เพื่อสุ่ม password ใหม่อีกรอบ

def RandomMenu():
    """Food random function"""
    menu_ls = ['Stewed pork leg', 'Pork panang curry', 'Fried rice', 'Beef curry', 'Papaya salad',\
            'Chicken wings', 'Chicken legs', 'Grilled pork neck', 'Pan fried seafood', 'Thai Basil Chicken ',\
            'Fried pork with garlic', 'Fermented fish spicy dip', 'Steamed egg', 'Stuffed egg', 'Son-in-law Eggs',\
            'Red pork over rice', 'Chicken rice', 'American fried rice', 'Pad thai', 'Dried noodles', 'Noodles soup',\
            'Egg noodles', 'American fried rice', 'Minced pork omelet', 'Fried egg', 'omelet', 'Stir fried vegetables',\
            'Seafood salad', 'Curry-fried fish', 'Chicken curry', 'Pork curry'] # รายการอาหารที่จะสุ่ม
    menu_select = random.choice(menu_ls) # สุ่มอาหารจาก menu_ls มาหนึ่งรายการ
    select = messagebox.askretrycancel(title="Menu", message="Menu for your meal: %s" %(menu_select))
    if select == True:
        RandomMenu() # กด retry เพื่อสุ่มอาหารใหม่อีกรอบ

def RandomMusicPlaylist():
    """Music playlist random function (YouTube URL)"""
    url = ["https://www.youtube.com/watch?v=SlPhMPnQ58k&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10",\
       "https://www.youtube.com/watch?v=Nj2U6rhnucI&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10&index=11",\
       "https://www.youtube.com/watch?v=dqRZDebPIGs&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10&index=12",\
        "https://www.youtube.com/watch?v=VF-r5TtlT9w&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10&index=15",\
        "https://www.youtube.com/watch?v=9HDEHj2yzew&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10&index=17"] # ลิงค์ของรายการเพลง (YouTube)
    webbrowser.open_new_tab(random.choice(url)) # สุ่มรายการเพลงใน browser ของผู้ใช้โดยเปิด Tab ใหม่

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        # self.pack(fill=BOTH, expand=1)
        self.pack(fill=BOTH, side=LEFT, expand=True)
        button1 = Button(self, text="Lottery 1st prize", font="72", fg="white", bg="red", borderwidth="5", command=Random6Digit) # ปุ่มสุ่มเลข6หลัก
        button2 = Button(self, text="Random Menu ", font="72", fg="white", bg="green", borderwidth="5", command=RandomMenu) # ปุ่มสุ่มอาหาร
        button3 = Button(self, text="Random Password", font="72", fg="white", bg="blue", borderwidth="5", command=RandomPassword) # ปุ่มสุ่ม Password
        button4 = Button(self, text="Listen music playlist", font="72", fg="white", bg="purple", borderwidth="5", command=RandomMusicPlaylist) # ปุ่มสุ่มเพลง
        # ตำแหน่งของปุ่ม
        button1.pack(fill=BOTH, side=TOP, expand=True)
        button2.pack(fill=BOTH, side=TOP, expand=True)
        button3.pack(fill=BOTH, side=TOP, expand=True)
        button4.pack(fill=BOTH, side=TOP, expand=True)
        # button1.grid(row=1, column=1, padx=50, pady=50)
        # button2.grid(row=1, column=2, padx=50, pady=50)
        # button3.grid(row=2, column=1, padx=50, pady=50)
        # button4.grid(row=2, column=2, padx=50, pady=50)

root = Tk()
# root.configure(background="light blue")
root.title("Random Generate")
root.geometry("970x540")

app = Window(root)
root.mainloop()