import tkinter as tk
from PIL import ImageTk, Image
import time
from config import SPLASH_LOADING1, SPLASH_LOADING2, SPLASH_WIDTH, SPLASH_HEIGHT, MAIN_WIDTH, MAIN_HEIGHT
from dashboard import MainApp

class SplashApp(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.__init()

    def __init(self):

        self.splash_frame = tk.Frame(self.master, width=427, height=250, bg='#272727')

        self.label_title = tk.Label(self.master, text="Emulators", fg='white', bg='#272727')
        self.label_title.configure(font=("Game Of Squids", 24, 'bold'))

        self.label_loading = tk.Label(self.master, text="Loading...", fg='white', bg='#272727')
        self.label_loading.configure(font=("Calibri", 11))

        self.image_a = ImageTk.PhotoImage(Image.open(SPLASH_LOADING1))
        self.image_b = ImageTk.PhotoImage(Image.open(SPLASH_LOADING2))

        self.__placing()
        
    def __placing(self):
        self.splash_frame.place(x=0, y=0)
        self.label_title.place(x=90, y=90)
        # self.label_loading.place(x=10, y=215)
        # for i in range(5):
        #     tk.Label(self.master, image=self.image_a, border=0, relief=tk.SUNKEN).place(x = 180, y = 145)
        #     tk.Label(self.master, image=self.image_b, border=0, relief=tk.SUNKEN).place(x = 200, y = 145)
        #     tk.Label(self.master, image=self.image_b, border=0, relief=tk.SUNKEN).place(x = 220, y = 145)
        #     tk.Label(self.master, image=self.image_b, border=0, relief=tk.SUNKEN).place(x = 240, y = 145)
        #     self.master.update_idletasks()
        #     time.sleep(0.5)
        #     tk.Label(self.master, image=self.image_b, border=0, relief=tk.SUNKEN).place(x = 180, y = 145)
        #     tk.Label(self.master, image=self.image_a, border=0, relief=tk.SUNKEN).place(x = 200, y = 145)
        #     tk.Label(self.master, image=self.image_b, border=0, relief=tk.SUNKEN).place(x = 220, y = 145)
        #     tk.Label(self.master, image=self.image_b, border=0, relief=tk.SUNKEN).place(x = 240, y = 145)
        #     self.master.update_idletasks()
        #     time.sleep(0.5)
        #     tk.Label(self.master, image=self.image_b, border=0, relief=tk.SUNKEN).place(x = 180, y = 145)
        #     tk.Label(self.master, image=self.image_b, border=0, relief=tk.SUNKEN).place(x = 200, y = 145)
        #     tk.Label(self.master, image=self.image_a, border=0, relief=tk.SUNKEN).place(x = 220, y = 145)
        #     tk.Label(self.master, image=self.image_b, border=0, relief=tk.SUNKEN).place(x = 240, y = 145)
        #     self.master.update_idletasks()
        #     time.sleep(0.5)
        #     tk.Label(self.master, image=self.image_b, border=0, relief=tk.SUNKEN).place(x = 180, y = 145)
        #     tk.Label(self.master, image=self.image_b, border=0, relief=tk.SUNKEN).place(x = 200, y = 145)
        #     tk.Label(self.master, image=self.image_b, border=0, relief=tk.SUNKEN).place(x = 220, y = 145)
        #     tk.Label(self.master, image=self.image_a, border=0, relief=tk.SUNKEN).place(x = 240, y = 145)
        #     self.master.update_idletasks()
        #     time.sleep(0.5)
        self.master.destroy()
        self.newDashBoard()

    def newDashBoard(self):
        mainapp = tk.Tk()
        mainapp.title("Dashboard-Emulators")
        screen_width = mainapp.winfo_screenwidth()
        screen_height = mainapp.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (MAIN_WIDTH / 2)
        y_coordinate = (screen_height / 2) - (MAIN_HEIGHT / 2)
        mainapp.geometry("%dx%d+%d+%d" %(MAIN_WIDTH, MAIN_HEIGHT, x_coordinate, y_coordinate))
        app = MainApp(mainapp)
        app.mainloop()
        

def main():
    root = tk.Tk()
    root.overrideredirect(1)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (SPLASH_WIDTH / 2)
    y_coordinate = (screen_height / 2) - (SPLASH_HEIGHT / 2)
    root.geometry("%dx%d+%d+%d" %(SPLASH_WIDTH, SPLASH_HEIGHT, x_coordinate, y_coordinate))
    SplashApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()