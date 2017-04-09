import tkinter as tk
from tkinter import *


def window():
    window = tk.Tk()
    window.geometry('600x600')

mWindow = tk.Tk()
mWindow.geometry('545x520+0+0')
mWindow.title('SpyderUI')
mWindow.config(bg='black')


wtitle = tk.Label(mWindow, height = 2, text="WikiSpyder", font=('Ariel', 20, 'bold'), fg='green', bg='black')
wtitle.grid(row=0, column=3, columnspan=2)

# You can set any height and width you want
blank_space_left = tk.Label(mWindow, width = 1, text=" ", font=('Ariel', 20, 'bold'), fg='green', bg='black')
blank_space_left.grid(row=1, column=1)

start_button = tk.Button(mWindow, height=5, width=16, font=('Helvetica', 12, 'bold'), text="Start", command=window)
start_button.grid(row=1, column=2)

blank_space = tk.Label(mWindow, height = 3, text=" ", font=('Ariel', 20, 'bold'), fg='green', bg='black')
blank_space.grid(row=2, column=2)

stop_button = tk.Button(mWindow, height=5, width=16, font=('Helvetica', 12, 'bold'), text="Stop", command=window)
stop_button.grid(row=3, column=2)

blank_space = tk.Label(mWindow, height = 2, text=" ", font=('Ariel', 20, 'bold'), fg='green', bg='black')
blank_space.grid(row=4, column=2)

increment_button = tk.Button(mWindow, height=5, width=16, font=('Helvetica', 12, 'bold'), text="Increment", command=window)
increment_button.grid(row=1, column=5)

decrement_button = tk.Button(mWindow, height=5, width=16, font=('Helvetica', 12, 'bold'), text="Decrement", command=window)
decrement_button.grid(row=3, column=5)

entry_box = Entry(mWindow, width = 60)
entry_box.grid(row=4, column=2, columnspan=4)

search_button = tk.Button(mWindow, font=('Helvetica', 12, 'bold'), text="Search", command=window)
search_button.grid(row=5, column=3)

quit_button = tk.Button(mWindow, text="QUIT", font=('Helvetica', 12, 'bold'), fg="red",command=mWindow.destroy)
quit_button.grid(row=5, column=4)

mWindow.mainloop()

#    def create_widgets(self):
#        self.start_button = tk.Button(self)
#        self.start_button.config(height = 50, width = 100)
#        self.start_button.grid(row=0, column=1)
#        self.start_button["text"] = "Start"
#        self.start_button["command"] = self.start_crawler
#        self.start_button.pack(side="top")

#        self.stop_button = tk.Button(self)
#        self.stop_button.config(height = 50, width = 100)
#        self.start_button.grid(row=1, column=1)
#        self.stop_button["text"] = "Stop"
#        self.stop_button["command"] = self.stop_crawler
#        self.stop_button.pack(side="top")

#        self.quit = tk.Button(self, text="QUIT", fg="red",
#                              command=root.destroy)
#        self.quit.pack(side="bottom")

#    def start_crawler(self):
#        print("Starting WikiSpyder")


#    def stop_crawler(self):
#        print("Stopping WikiSpyder")