import tkinter as tk
from tkinter import *
import os
from wikiCrawler.settings import DOWNLOAD_DELAY


def window():
    window = tk.Tk()
    window.geometry('600x600')

def start_system():
    os.system("start /B start cmd.exe @cmd /k scrapy crawl wikiSpyder")

def stop_system():
    os.chdir(r'C:\Windows\System32')
    os.system('taskkill /F /IM cmd.exe /T')

def inc_delay():
    global DOWNLOAD_DELAY
    DOWNLOAD_DELAY += 1
    print(DOWNLOAD_DELAY)

def dec_delay():
    global DOWNLOAD_DELAY
    DOWNLOAD_DELAY -= 1
    print(DOWNLOAD_DELAY)

mWindow = tk.Tk()
mWindow.geometry('545x520+0+0')
mWindow.title('SpyderUI')
mWindow.config(bg='black')


wtitle = tk.Label(mWindow, height = 2, text="WikiSpyder", font=('Ariel', 20, 'bold'), fg='green', bg='black')
wtitle.grid(row=0, column=3, columnspan=2)

blank_space_left = tk.Label(mWindow, width = 1, text=" ", font=('Ariel', 20, 'bold'), fg='green', bg='black')
blank_space_left.grid(row=1, column=1)

start_button = tk.Button(mWindow, height=5, width=16, font=('Helvetica', 12, 'bold'), text="Start", command=start_system)
start_button.grid(row=1, column=2)

blank_space = tk.Label(mWindow, height = 3, text=" ", font=('Ariel', 20, 'bold'), fg='green', bg='black')
blank_space.grid(row=2, column=2)

stop_button = tk.Button(mWindow, height=5, width=16, font=('Helvetica', 12, 'bold'), text="Stop", command=stop_system)
stop_button.grid(row=3, column=2)

blank_space = tk.Label(mWindow, height = 2, text=" ", font=('Ariel', 20, 'bold'), fg='green', bg='black')
blank_space.grid(row=4, column=2)

increment_button = tk.Button(mWindow, height=5, width=16, font=('Helvetica', 12, 'bold'), text="Increment", command=inc_delay)
increment_button.grid(row=1, column=5)

decrement_button = tk.Button(mWindow, height=5, width=16, font=('Helvetica', 12, 'bold'), text="Decrement", command=dec_delay)
decrement_button.grid(row=3, column=5)

entry_box = Entry(mWindow, width = 60)
entry_box.grid(row=4, column=2, columnspan=4)

search_button = tk.Button(mWindow, font=('Helvetica', 12, 'bold'), text="Search", command=window)
search_button.grid(row=5, column=3)

quit_button = tk.Button(mWindow, text="QUIT", font=('Helvetica', 12, 'bold'), fg="red",command=mWindow.destroy)
quit_button.grid(row=5, column=4)

mWindow.mainloop()
