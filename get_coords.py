import tkinter
import tkinter.ttk
from PIL import Image, ImageTk
import numpy as np


class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('tkinter canvas trial')
        self.pack()
        self.img = ImageTk.PhotoImage(
            Image.open("house.jpg").resize((900, 600)))
        self.create_widgets()

    def create_widgets(self):
        self.start_x = tkinter.StringVar()
        self.start_y = tkinter.StringVar()
        self.current_x = tkinter.StringVar()
        self.current_y = tkinter.StringVar()
        self.stop_x = tkinter.StringVar()
        self.stop_y = tkinter.StringVar()
        self.distance = tkinter.IntVar()
        self.savename = tkinter.StringVar()

        self.label_description = tkinter.ttk.Label(self, text='Mouse position')
        self.label_description.grid(row=0, column=1)
        self.label_start_x = tkinter.ttk.Label(self, textvariable=self.start_x)
        self.label_start_x.grid(row=1, column=1)
        self.label_start_y = tkinter.ttk.Label(self, textvariable=self.start_y)
        self.label_start_y.grid(row=2, column=1)
        self.label_stop_x = tkinter.ttk.Label(self, textvariable=self.stop_x)
        self.label_stop_x.grid(row=3, column=1)
        self.label_stop_y = tkinter.ttk.Label(self, textvariable=self.stop_y)
        self.label_stop_y.grid(row=4, column=1)
        self.save_button2 = tkinter.ttk.Button(
            self, text="save points", command=self.save_points)
        self.save_button2.grid(row=5, column=1)

        self.test_canvas = tkinter.Canvas(
            self, bg='lightblue', width=1000, height=800, highlightthickness=0)
        self.test_canvas.create_image(0, 0, image=self.img, anchor=tkinter.NW)
        self.test_canvas.grid(row=0, column=0, rowspan=8)
        self.test_canvas.bind('<ButtonPress-1>', self.start_pickup)
        self.test_canvas.bind('<B1-Motion>', self.pickup_position)
        self.test_canvas.bind('<ButtonRelease-1>', self.stop_pickup)

    def start_pickup(self, event):
        self.start_x.set('x : ' + str(event.x))
        self.start_y.set('y : ' + str(event.y))
        self.stop_x.set('')
        self.stop_y.set('')
        self.test_canvas.create_oval(
            event.x-2, event.y-2, event.x+2, event.y+2, fill="red")
        self.start_x_ = event.x
        self.start_y_ = event.y

    def pickup_position(self, event):
        self.current_x.set('x : ' + str(event.x))
        self.current_y.set('y : ' + str(event.y))

    def stop_pickup(self, event):
        self.stop_x.set('x : ' + str(event.x))
        self.stop_y.set('y : ' + str(event.y))
        self.test_canvas.create_oval(
            event.x-2, event.y-2, event.x+2, event.y+2, fill="red")
        self.stop_x_ = event.x
        self.stop_y_ = event.y

    def save_points(self):
        self.origin = np.array([self.start_x_, self.start_y_])*2
        self.endpoint = np.array([self.stop_x_, self.stop_y_])*2
        self.savewidget = tkinter.Toplevel(self.master)
        self.savewidget.title("save")
        self.savewidget.geometry("300x100+100+100")
        self.ent_label = tkinter.ttk.Label(
            self.savewidget, text="enter the points' name:")
        self.ent_label.grid(row=0, column=0)
        self.ent_savename = tkinter.ttk.Entry(
            self.savewidget, textvariable=self.savename)
        self.ent_savename.grid(row=0, column=1)
        self.ent_label = tkinter.ttk.Label(
            self.savewidget, text="enter the points' distance:")
        self.ent_label.grid(row=1, column=0)
        self.ent_savename = tkinter.ttk.Entry(
            self.savewidget, textvariable=self.distance)
        self.ent_savename.grid(row=1, column=1)
        self.save_button = tkinter.ttk.Button(
            self.savewidget, text="save", command=self.save_npy)
        self.save_button.grid(row=2, column=0)

    def save_npy(self):
        self.results = {"origin": self.origin,
                        "endpoint": self.endpoint, "distance": int(self.distance.get())}
        np.save(self.savename.get()+".npy", self.results)
        self.test_canvas.delete("all")
        self.test_canvas.create_image(0, 0, image=self.img, anchor=tkinter.NW)


root = tkinter.Tk()
app = Application(master=root)
app.mainloop()
