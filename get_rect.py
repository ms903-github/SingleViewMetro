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
        # self.start_x = tkinter.StringVar()
        # self.start_y = tkinter.StringVar()
        # self.stop_x = tkinter.StringVar()
        # self.stop_y = tkinter.StringVar()
        # self.distance = tkinter.IntVar()
        self.current_x = tkinter.StringVar()
        self.current_y = tkinter.StringVar()
        self.savename = tkinter.StringVar()
        self.zvalues = tkinter.StringVar()
        self.points = []

        self.label_description = tkinter.ttk.Label(
            self, text='current position')
        self.label_description.grid(row=0, column=1)
        self.label_p1_x = tkinter.ttk.Label(self, textvariable=self.current_x)
        self.label_p1_x.grid(row=1, column=1)
        self.label_p1_y = tkinter.ttk.Label(self, textvariable=self.current_y)
        self.label_p1_y.grid(row=2, column=1)

        self.save_button = tkinter.ttk.Button(
            self, text="save", command=self.save_points)
        self.save_button.grid(row=3, column=1)

        self.test_canvas = tkinter.Canvas(
            self, bg='lightblue', width=1000, height=800, highlightthickness=0)
        self.test_canvas.create_image(0, 0, image=self.img, anchor=tkinter.NW)
        self.test_canvas.grid(row=0, column=0, rowspan=8)
        self.test_canvas.bind('<ButtonPress-1>', self.pickup_point)
        self.test_canvas.bind('<Key-s>', self.save_points)

    def pickup_point(self, event):
        self.test_canvas.create_oval(
            event.x-2, event.y-2, event.x+2, event.y+2, fill="red")
        self.current_x.set('x : ' + str(event.x))
        self.current_y.set('y : ' + str(event.y))
        self.points.append((int(event.x), int(event.y)))

    def save_points(self):
        self.savewidget = tkinter.Toplevel(self.master)
        self.savewidget.title("save")
        self.savewidget.geometry("300x100+100+100")
        self.ent_label = tkinter.ttk.Label(
            self.savewidget, text="savename:")
        self.ent_label.grid(row=0, column=0)
        self.ent_name = tkinter.ttk.Entry(
            self.savewidget, textvariable=self.savename)
        self.ent_name.grid(row=0, column=1)

        self.zent_label = tkinter.ttk.Label(
            self.savewidget, text="zvalues:")
        self.zent_label.grid(row=1, column=0)
        self.ent_zval = tkinter.ttk.Entry(
            self.savewidget, textvariable=self.zvalues)
        self.ent_zval.grid(row=1, column=1)

        self.save_button = tkinter.ttk.Button(
            self.savewidget, text="save", command=self.save_npy)
        self.save_button.grid(row=2, column=0)

    def save_npy(self):
        self.test_canvas.delete("all")
        self.test_canvas.create_image(0, 0, image=self.img, anchor=tkinter.NW)
        np.save(self.savename.get()+".npy",
                {"coords": self.points, "zval": [self.zvalues.get().split()]})
        self.points = []


root = tkinter.Tk()
app = Application(master=root)
app.mainloop()
