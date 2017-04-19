#imports
import tkinter as tk
from tkinter import *
import os
from wikiCrawler.settings import DOWNLOAD_DELAY

#create a window 600x600
def window():
    window = tk.Tk()
    window.geometry('600x600')

#start crawling button
def start_system():
    os.system("start /B start cmd.exe @cmd /k scrapy crawl wikiSpyder")

#stop crawling button    
def stop_system():
    os.chdir(r'C:\Windows\System32')
    os.system('taskkill /F /IM cmd.exe /T')

#increase delay of crawler
def inc_delay():
    global DOWNLOAD_DELAY
    DOWNLOAD_DELAY += 1
    print(DOWNLOAD_DELAY)

#decrease delay of crawler
def dec_delay():
    global DOWNLOAD_DELAY
    DOWNLOAD_DELAY -= 1
    print(DOWNLOAD_DELAY)

#create main window 545x520 with title SpyderUI - black background
mWindow = tk.Tk()
mWindow.geometry('545x520+0+0')
mWindow.title('SpyderUI')
mWindow.config(bg='black')

#separte function to search a specific article in wiki
def summary_algorithm():
    output = ment.get()
    get_summary = lambda output: wikipedia.summary(output).encode('utf-8').strip()
    print(get_summary(output))

#add title to window
wtitle = tk.Label(mWindow, height = 2, text="WikiSpyder", font=('Ariel', 20, 'bold'), fg='green', bg='black')
wtitle.grid(row=0, column=3, columnspan=2)

#filler space
blank_space_left = tk.Label(mWindow, width = 1, text=" ", font=('Ariel', 20, 'bold'), fg='green', bg='black')
blank_space_left.grid(row=1, column=1)

#add start crawler button
start_button = tk.Button(mWindow, height=5, width=16, font=('Helvetica', 12, 'bold'), text="Start", command=start_system)
start_button.grid(row=1, column=2)

#filler space
blank_space = tk.Label(mWindow, height = 3, text=" ", font=('Ariel', 20, 'bold'), fg='green', bg='black')
blank_space.grid(row=2, column=2)

#add stop crawler button
stop_button = tk.Button(mWindow, height=5, width=16, font=('Helvetica', 12, 'bold'), text="Stop", command=stop_system)
stop_button.grid(row=3, column=2)

#filler space
blank_space = tk.Label(mWindow, height = 2, text=" ", font=('Ariel', 20, 'bold'), fg='green', bg='black')
blank_space.grid(row=4, column=2)

#create increment button
increment_button = tk.Button(mWindow, height=5, width=16, font=('Helvetica', 12, 'bold'), text="Increment", command=inc_delay)
increment_button.grid(row=1, column=5)

#create decrement button
decrement_button = tk.Button(mWindow, height=5, width=16, font=('Helvetica', 12, 'bold'), text="Decrement", command=dec_delay)
decrement_button.grid(row=3, column=5)

#create search box
entry_box = Entry(mWindow, width=60 ,textvariable = ment)
entry_box.grid(row=4, column=2, columnspan=4)

#add search button to grid
search_button = tk.Button(mWindow, font=('Helvetica', 12, 'bold'), text="Search", command = summary_algorithm )
search_button.grid(row=5, column=3)

#add quit_button to grid
quit_button = tk.Button(mWindow, text="QUIT", font=('Helvetica', 12, 'bold'), fg="red",command=mWindow.destroy)
quit_button.grid(row=5, column=4)

#keeps window open
mWindow.mainloop()
