import Core
import math
import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from tkinter.ttk import*
import numpy as np

class GUI:
    calulate = 0
    backend = Core.Compute()
    def __init__(self,master):
        self.master = master
        self.master.title("ZASADY BUDOWY ROBOTÓW: Projekt 1")
        master.geometry("1000x950")
        master.resizable(False,False)
        self.style= tk.ttk.Style()
        self.style.theme_use("clam")
        #self.style.configure("TCombobox", foreground="black", background="blue")

        mainwindow = tk.Frame(master) #,bg="black"
        mainwindow.pack(side="top", fill="both", expand="True")
        mainwindow.grid_columnconfigure(2,minsize=200)
        
        

        bottom = tk.Frame(master)
        bottom.pack(side="bottom", fill="both",expand="True")

        self.quit_button = Button(master,text="Exit",command=master.quit, cursor="star")
        self.quit_button.grid(in_=bottom,row=0,column=1,pady=10,padx=10)
        self.run_button = Button(master,text="Run",command = self.getData, cursor="trek")
        self.run_button.grid(in_=bottom,row=0,column=0,pady=10,padx=10)
        self.name_label=tk.Label(master,text="Michał Kiełczykowski,2018/19")
        self.name_label.place(relx=1.0, rely=1.0, anchor='se')


######################first data collumn#####################

        self.input_label = tk.Label(text="Dane Wejściowe")
        self.input_label.grid(in_=mainwindow,row=0, column=0,pady=10)

        self.inl1 = tk.Label(text="l1[m]")
        self.inl1.grid(in_=mainwindow,row=1, column=0, sticky="e")
        self.enl1 = tk.Entry(master)
        self.enl1.insert(0,'0.3')
        self.enl1.grid(in_=mainwindow, row=1, column=1)

        self.inl2 = tk.Label(text="l2[m]")
        self.inl2.grid(in_=mainwindow,row=2, column=0, sticky="e")
        self.enl2 = tk.Entry(master)
        self.enl2.insert(0,'1.2')
        self.enl2.grid(in_=mainwindow, row=2, column=1)

        self.inl3 = tk.Label(text="l3[m]")
        self.inl3.grid(in_=mainwindow,row=3, column=0, sticky="e")
        self.enl3 = tk.Entry(master)
        self.enl3.insert(0,'0.7')
        self.enl3.grid(in_=mainwindow, row=3, column=1)

        self.inl4 = tk.Label(text="l4[m]")
        self.inl4.grid(in_=mainwindow,row=4, column=0, sticky="e")
        self.enl4 = tk.Entry(master)
        self.enl4.insert(0,'0.7')
        self.enl4.grid(in_=mainwindow, row=4, column=1)

        self.inl5 = tk.Label(text="l5[m]")
        self.inl5.grid(in_=mainwindow,row=5, column=0, sticky="e")
        self.enl5 = tk.Entry(master)
        self.enl5.insert(0,'0.1')
        self.enl5.grid(in_=mainwindow, row=5, column=1)

        self.inl6 = tk.Label(text="l6[m]")
        self.inl6.grid(in_=mainwindow,row=6, column=0, sticky="e")
        self.enl6 = tk.Entry(master)
        self.enl6.insert(0,'0.2')
        self.enl6.grid(in_=mainwindow, row=6, column=1)

        self.inl7 = tk.Label(text="d[m]")
        self.inl7.grid(in_=mainwindow,row=7, column=0, sticky="e")
        self.enl7 = tk.Entry(master)
        self.enl7.insert(0,'0.2')
        self.enl7.grid(in_=mainwindow, row=7, column=1)

        self.inl8 = tk.Label(text="e[m]")
        self.inl8.grid(in_=mainwindow,row=8, column=0, sticky="e")
        self.enl8 = tk.Entry(master)
        self.enl8.insert(0,'0.1')
        self.enl8.grid(in_=mainwindow, row=8, column=1)

        self.inl9 = tk.Label(text="theta [st]")
        self.inl9.grid(in_=mainwindow,row=9, column=0, sticky="e")
        self.enl9 = tk.Entry(master)
        self.enl9.insert(0,'30')
        self.enl9.grid(in_=mainwindow, row=9, column=1)

        self.inl10 = tk.Label(text="psi [st]")
        self.inl10.grid(in_=mainwindow,row=10, column=0, sticky="e")
        self.enl10 = tk.Entry(master)
        self.enl10.insert(0,'40')
        self.enl10.grid(in_=mainwindow, row=10, column=1)

        self.inld1 = tk.Label(text="delta1")
        self.inld1.grid(in_=mainwindow,row=11, column=0, sticky="e")
        self.d1 = Combobox(master,state='readonly')
        self.d1['values']=(1,-1)
        self.d1.current(1)
        self.d1.grid(in_=mainwindow, row=11, column=1)

        self.inld2 = tk.Label(text="delta2")
        self.inld2.grid(in_=mainwindow,row=12, column=0, sticky="e")
        self.d2 = Combobox(master,state='readonly')
        self.d2['values']=(1,-1)
        self.d2.current(1)
        self.d2.grid(in_=mainwindow, row=12, column=1,padx=5)

        self.inld3 = tk.Label(text="delta3")
        self.inld3.grid(in_=mainwindow,row=13, column=0, sticky="e")
        self.d3 = Combobox(master,state='readonly')
        self.d3['values']=(1,-1)
        self.d3.current(0)
        self.d3.grid(in_=mainwindow, row=13, column=1)

######################second data collumn#####################
        # self.coordinates_label = Label(master,text="Współrzędne maszynowe")
        # self.coordinates_label.grid(in_=mainwindow,row=0,column=2,pady=10)

        # self.fi1= tk.StringVar()
        # self.fi2= tk.StringVar()
        # self.fi3= tk.StringVar()
        # self.fi4= tk.StringVar()
        # self.fi5 = tk.StringVar()

        # self.fi1.set("fi1 =")
        # self.fi2.set("fi2 =")
        # self.fi3.set("fi3 =")
        # self.fi4.set("fi4 =")
        # self.fi5.set("fi5 =")

        # self.fi1_label = Label(master,textvariable=self.fi1)
        # self.fi2_label = Label(master,textvariable=self.fi2)
        # self.fi3_label = Label(master,textvariable=self.fi3)
        # self.fi4_label = Label(master,textvariable=self.fi4)
        # self.fi5_label = Label(master,textvariable=self.fi5)

        # self.fi1_label.grid(in_=mainwindow,row=1, column=2)
        # self.fi2_label.grid(in_=mainwindow,row=2, column=2)
        # self.fi3_label.grid(in_=mainwindow,row=3, column=2)
        # self.fi4_label.grid(in_=mainwindow,row=4, column=2)
        # self.fi5_label.grid(in_=mainwindow,row=5, column=2)

        self.route_label = Label(master,text="   Parametry toru ruchu\n(Współrzędne Postaci: 'x,y,z')",)
        self.route_label.grid(in_=mainwindow,row=0,column=2,pady=10,rowspan=2)

        self.route1_label = Label(master,text="Współrzędne punktu startowego")
        self.route1_label.grid(in_=mainwindow,row=2,column=2)

        self.route2_label = Label(master,text="Współrzędne punktu przejścia1")
        self.route2_label.grid(in_=mainwindow,row=4,column=2)

        self.route3_label = Label(master,text="Współrzędne punktu przejścia2")
        self.route3_label.grid(in_=mainwindow,row=6,column=2)

        self.route4_label = Label(master,text="Współrzędne punktu przejścia3")
        self.route4_label.grid(in_=mainwindow,row=8,column=2)

        self.route5_label = Label(master,text="Współrzędne punktu końcowego")
        self.route5_label.grid(in_=mainwindow,row=10,column=2)

        self.route1_entry = tk.Entry(master)
        self.route1_entry.insert(0,"1,1,1")
        self.route1_entry.grid(in_=mainwindow, row=3, column=2)

        self.route2_entry = tk.Entry(master)
        self.route2_entry.insert(0,"0,1,1")
        self.route2_entry.grid(in_=mainwindow, row=5, column=2)

        self.route3_entry = tk.Entry(master)
        self.route3_entry.insert(0,"1,0,1")
        self.route3_entry.grid(in_=mainwindow, row=7, column=2)

        self.route4_entry = tk.Entry(master)
        self.route4_entry.insert(0,"1,0,0")
        self.route4_entry.grid(in_=mainwindow, row=9, column=2)

        self.route5_entry = tk.Entry(master)
        self.route5_entry.insert(0,"0,1,0")
        self.route5_entry.grid(in_=mainwindow, row=11, column=2)



#######adding plot to tinkter window#############

        self.f= Figure(figsize=(5,8), dpi=100)
        self.a = self.f.add_subplot(211, projection='3d')
        self.a2 = self.f.add_subplot(212)
        

        canvas = FigureCanvasTkAgg(self.f,master)
        canvas.get_tk_widget().grid(in_=mainwindow,row=0, column=3, rowspan=30)
        toolbar = NavigationToolbar2Tk(canvas,master)
        toolbar.update()
        canvas._tkcanvas.grid(in_=mainwindow,row=1, column=3)
        axes3d.Axes3D.mouse_init(self.a)
        

#########################################


    def stringToNumpy(self,string):
        tmp = string.split(",")
        #print (tmp)
        try:
                matrix = np.array([float(tmp[0]), float(tmp[1]), float(tmp[2])])
        except ValueError: 
                tk.messagebox.showerror("Error","Nieprawidłowa wartość wejściowa!\nNależy poprawić wprowadzone Dane, tak aby wszystkie składowe były liczbami")
                return np.array([])
        
        #print (matrix)
        return matrix

    def retData(self):
            return (self.enl1_data, self.enl2_data,  self.enl3_data, self.enl4_data, self.enl5_data, self.enl6_data, self.enl7_data ,self.enl8_data, self.enl9_data, self.enl10_data, self.d1_data, self.d2_data,self.d3_data, self.route1_entry_data, self.route2_entry_data, self.route3_entry_data, self.route4_entry_data, self.route5_entry_data )



    def getData(self):
        try:
                self.enl1_data = float(self.enl1.get())
                self.enl2_data = float(self.enl2.get())
                self.enl3_data = float(self.enl3.get())
                self.enl4_data = float(self.enl4.get())
                self.enl5_data = float(self.enl5.get())
                self.enl6_data = float(self.enl6.get())
                self.enl7_data = float(self.enl7.get())
                self.enl8_data = float(self.enl8.get())
                self.enl9_data = float(self.enl9.get())
                self.enl10_data = float(self.enl10.get())
                self.d1_data = float(self.d1.get())
                self.d2_data = float(self.d2.get())
                self.d3_data = float(self.d3.get())
        except ValueError:
                tk.messagebox.showerror("Error","Nieprawidłowa wartość wejściowa!\n Dane musza być liczbami")
                return None

        try:
                self.route1_entry_data = self.stringToNumpy(self.route1_entry.get())
                self.route2_entry_data = self.stringToNumpy(self.route2_entry.get()) 
                self.route3_entry_data = self.stringToNumpy(self.route3_entry.get()) 
                self.route4_entry_data = self.stringToNumpy(self.route4_entry.get())
                self.route5_entry_data = self.stringToNumpy(self.route5_entry.get())
        except IndexError:
                tk.messagebox.showerror("Error","Nieprawidłowa wartość wejściowa!\nWszystkie wartości współrzędnych wektorowych muszą zostać uzupełnione!")
                return None


        if self.route1_entry_data.size == 0 or self.route2_entry_data.size == 0 or self.route3_entry_data.size == 0:
                #print("NIENOXD")
                return None    

        self.backend.compute(self)
        pass



       
if __name__ == "__main__":
        root = tk.Tk()
        gui = GUI(root)
        root.mainloop()