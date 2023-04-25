import tkinter as tk
from PIL import ImageTk, Image
from emulator_manage import *
from config import SPLASH_WIDTH, SPLASH_HEIGHT, SPLASH_LOADING1, SPLASH_LOADING2
import threading
import time

class InstaceFrame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        print("1111111")
        self.__init()
    def __init(self):
        self.header_frame = tk.Frame(self, width=300, height=100, bg='#272727')
        self.label_title = tk.Label(self.header_frame, text="Emulators")
        self.label_title.configure(font=("Calibri", 11, 'bold'))
        self.btn_restart = tk.Button(self.header_frame, bd=0, relief="groove", compound=tk.CENTER, bg="#88EE14", fg="white", activeforeground="black", 
            activebackground="white", font="arial 12", text="Close", pady=10, command=self.fnRestart
        )
        self.btn_close = tk.Button(self.header_frame, bd=0, relief="groove", compound=tk.CENTER, bg="#F54E00", fg="white", activeforeground="black", 
            activebackground="white", font="arial 12", text="Close", pady=10, command=self.fnClose
        )
        self.instance_frame = tk.Frame(self, width=300, height=200, bg='#272727')
        self.__placing()
    def __placing(self):
        self.header_frame.place(x=0, y=0)
        self.instance_frame.place(x=0, y=100)
        self.label_title.pack()
        self.btn_restart.pack()
        self.btn_close.pack()
    def fnRestart(self):
        pass
    def fnClose(self):
        pass

class MainApp(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.instance_numbers = tk.IntVar()
        self.created_instance_number_check = tk.IntVar()
        self.running_instance_number_check = tk.IntVar()
        self.created_instance_number_check.set(0)
        self.running_instance_number_check.set(0)
        self.current_instances_number = 0
        self.showInputDialog()
        self.__init()
    def __init(self):
        current_state_vm = fnGetCurrentInstancesNumber().splitlines()
        self.current_instances_number = len(current_state_vm) - 1
        if self.current_instances_number < self.instance_numbers.get():
            sub_instances = self.instance_numbers.get() - self.current_instances_number
            m_create_thread = threading.Thread(target=self.fnCreateInstanceParent, args=(sub_instances,))
            m_create_thread.start()
            m_dialog_thread = threading.Thread(target=self.showLoadingDialog, args=())
            m_dialog_thread.start()
        else:
            m_dialog_thread = threading.Thread(target=self.showLoadingDialog, args=())
            m_dialog_thread.start()
            m_runthread = threading.Thread(target=self.fnRunEmulatorThread, args=())
            m_runthread.start()
        self.__iframe = InstaceFrame(self)
        self.__placing()
    def __placing(self):
        self.__iframe.pack(fill="both")
        
    ##################
    def fnCreateInstanceParent(self, sub_instances):
        m_thread_list = []
        for i in range(sub_instances):
            m_thread = threading.Thread(target=self.fnCreateinstanceThread)
            m_thread_list.append(m_thread)
            m_thread.start()
        for i in range(sub_instances):
            m_thread_list[i].join()
        self.fnRunEmulatorThread()
    def fnRunEmulatorThread(self):
        run_thread = threading.Thread(target=self.fnRunningInstanceThread)
        run_thread.start()
        run_thread.join()
    def fnCreateinstanceThread(self):
        try:
            new_instance_state = fnCreateNewInstance().splitlines()
            if new_instance_state[0] == b'SUCCESS: create vm finished.':
                print("Create Instance Success")
                x = self.created_instance_number_check.get()
                x += 1
                self.created_instance_number_check.set(x)
        except:
            print("Create Instance Failed")
    def fnRunningInstanceThread(self):
        try:
            current_state_vm = fnGetCurrentInstancesNumber().splitlines()
            m_thread_list = []
            for i in range(self.instance_numbers.get()):
                m_thread = threading.Thread(target=fnRunInstance, args=(current_state_vm[i].decode("utf-8").split(',')[0],))
                m_thread.start()
                m_thread_list.append(m_thread)
            for i in range(len(m_thread_list)):
                m_thread_list[i].join()
                x = self.running_instance_number_check.get()
                x += 1
                self.running_instance_number_check.set(x)
        except:
            print("Create Instance Failed")
    ##################
    def showLoadingDialog(self):
        d = LoadingDialog(self.master, self.instance_numbers, self.running_instance_number_check,  self.created_instance_number_check)
    def showInputDialog(self):
        d = InstaceNumberDialog(self.master, self.instance_numbers)
        self.master.wait_window(d.top)

class LoadingDialog:
    def __init__(self, parent, instance_numbers, running_instance_number_check, created_instance_number_check):
        self.instance_numbers = instance_numbers
        self.running_instance_number_check = running_instance_number_check
        self.created_instance_number_check = created_instance_number_check
        self.loading_state = tk.StringVar()
        self.top = tk.Toplevel(parent)
        self.top.transient(parent)
        self.top.grab_set()
        # self.top.overrideredirect(1)
        screen_width = self.top.winfo_screenwidth()
        screen_height = self.top.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (SPLASH_WIDTH / 2)
        y_coordinate = (screen_height / 2) - (SPLASH_HEIGHT / 2)
        self.top.geometry("%dx%d+%d+%d" %(SPLASH_WIDTH, SPLASH_HEIGHT, x_coordinate, y_coordinate))
        self.top.lift()
        self.__init()
    def __init(self):
        self.loading_frame = tk.Frame(self.top, width=427, height=250, bg='#272727')
        self.label_title = tk.Label(self.top, text="Loading...", fg='white', bg='#272727')
        self.label_title.configure(font=("Game Of Squids", 24, 'bold'))
        self.label_loading = tk.Label(self.top, text="Loading", fg='white', bg='#272727')
        self.label_loading.configure(font=("Calibri", 11))
        self.image_a = ImageTk.PhotoImage(Image.open(SPLASH_LOADING1))
        self.image_b = ImageTk.PhotoImage(Image.open(SPLASH_LOADING2))
        self.__placing()
    def __placing(self):
        self.loading_frame.place(x = 0, y = 0)
        self.label_title.place(x=90, y=90)
        self.label_loading.place(x=10, y=215)
        while 1:
            tk.Label(self.top, image=self.image_a, border=0, relief=tk.SUNKEN).place(x = 180, y = 145)
            tk.Label(self.top, image=self.image_b, border=0, relief=tk.SUNKEN).place(x = 200, y = 145)
            tk.Label(self.top, image=self.image_b, border=0, relief=tk.SUNKEN).place(x = 220, y = 145)
            tk.Label(self.top, image=self.image_b, border=0, relief=tk.SUNKEN).place(x = 240, y = 145)
            self.top.update_idletasks()
            time.sleep(0.5)
            tk.Label(self.top, image=self.image_b, border=0, relief=tk.SUNKEN).place(x = 180, y = 145)
            tk.Label(self.top, image=self.image_a, border=0, relief=tk.SUNKEN).place(x = 200, y = 145)
            tk.Label(self.top, image=self.image_b, border=0, relief=tk.SUNKEN).place(x = 220, y = 145)
            tk.Label(self.top, image=self.image_b, border=0, relief=tk.SUNKEN).place(x = 240, y = 145)
            self.top.update_idletasks()
            time.sleep(0.5)
            tk.Label(self.top, image=self.image_b, border=0, relief=tk.SUNKEN).place(x = 180, y = 145)
            tk.Label(self.top, image=self.image_b, border=0, relief=tk.SUNKEN).place(x = 200, y = 145)
            tk.Label(self.top, image=self.image_a, border=0, relief=tk.SUNKEN).place(x = 220, y = 145)
            tk.Label(self.top, image=self.image_b, border=0, relief=tk.SUNKEN).place(x = 240, y = 145)
            self.top.update_idletasks()
            time.sleep(0.5)
            tk.Label(self.top, image=self.image_b, border=0, relief=tk.SUNKEN).place(x = 180, y = 145)
            tk.Label(self.top, image=self.image_b, border=0, relief=tk.SUNKEN).place(x = 200, y = 145)
            tk.Label(self.top, image=self.image_b, border=0, relief=tk.SUNKEN).place(x = 220, y = 145)
            tk.Label(self.top, image=self.image_a, border=0, relief=tk.SUNKEN).place(x = 240, y = 145)
            self.top.update_idletasks()
            time.sleep(0.5)
            print(self.running_instance_number_check.get())
            if self.instance_numbers.get() == self.running_instance_number_check.get():
                break
        self.top.destroy()

class InstaceNumberDialog:
    def __init__(self, parent, instance_numbers):
        self.instance_numbers = instance_numbers
        self.top = tk.Toplevel(parent)
        self.top.transient(parent)
        self.top.grab_set()
        screen_width = self.top.winfo_screenwidth()
        screen_height = self.top.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (SPLASH_WIDTH / 2)
        y_coordinate = (screen_height / 2) - (SPLASH_HEIGHT / 2)
        self.top.geometry("%dx%d+%d+%d" %(SPLASH_WIDTH, SPLASH_HEIGHT, x_coordinate, y_coordinate))
        self.top.title("How many Instances do you want use?")
        self.__init()

    def __init(self):
        self.dialog_frame = tk.Frame(self.top, width=427, height=250, bg='#272727')
        self.input_label = tk.Label(self.top, text="Please input number of instances", fg='white', bg='#272727')
        self.input_label.configure(font=("Game Of Squids", 10, 'bold'))
        self.input_entry = tk.Spinbox(self.top, from_=1, to=40)
        self.input_entry.configure(font=("Calibri", 15))
        self.btn_submit = tk.Button(
            self.top,
            bd=0,
            relief="groove",
            compound=tk.CENTER,
            bg="#1485EE",
            fg="white",
            activeforeground="black",
            activebackground="white",
            font="arial 12",
            text="Click me",
            pady=10,
            command=self.ok,
            width=300
            )
        self.__placing()

    def __placing(self):
        self.dialog_frame.place(x=0, y=0)
        self.input_label.place(x = 30, y = 50)
        self.input_entry.place(x = 110, y = 100)
        self.input_entry.focus_set()
        self.btn_submit.place(x = 110, y = 150, width=220)
        self.input_entry.bind("<Return>", self.ok)
        self.input_entry.bind("<Escape>", self.cancel)

    def ok(self, event=None):
        self.instance_numbers.set(int(self.input_entry.get()))
        self.top.destroy()

    def cancel(self, event=None):
        self.top.destroy()
