import Window

class Compute:
    def compute(self,app):
        self.raw_data =app.retData()
        #concat data
        self.l1 = self.raw_data[0]
        self.l2 = self.raw_data[1]
        self.l3 = self.raw_data[2]
        self.l4 = self.raw_data[3]
        self.l5 = self.raw_data[4]
        self.l6 = self.raw_data[5]
        self.d = self.raw_data[6]
        self.e = self.raw_data[7]
        self.theta = self.raw_data[8]
        self.psi = self.raw_data[9]
        print('raw data')
        print(self.raw_data)
        Window.GUI.calulate = 0
        pass


if __name__ == "__main__":
    root = Window.tk.Tk()
    gui = Window.GUI(root)
    back = Compute()
    root.mainloop()
    # while():
    #     if Window.GUI.calulate == 1:
    #         back.compute(app=gui)
        


    
