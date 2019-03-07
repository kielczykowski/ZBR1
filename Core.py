import Window

class Compute:
    def compute(self,app):
        self.raw_data =app.retData()
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
        self.delta1 = self.raw_data[10]
        self.delta2 = self.raw_data[11]
        self.delta3 = self.raw_data[12]
        self.start_coordinates = self.raw_data[13]
        self.passage_coordinates = self.raw_data[14]
        self.end_coordinates = self.raw_data[15]
        #print( self.start_coordinates.size)
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
        


    
