import Window

class Compute:

    def __controll(self,trigfunc):
        if trigfunc>1:
            trigfunc=1
        if trigfunc<-1:
            trigfunc=-1
        return trigfunc

    def __distance(self,point1,point2):
        return Window.math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2 + (point1[2]-point2[2])**2)

    def __trajectory(self,P1,P2,P3,P4,P5,resolution=10):
        n1 = round(resolution*self.__distance(P1,P2))
        n2 = round(resolution*self.__distance(P2,P3))
        n3 = round(resolution*self.__distance(P3,P4))
        n4 = round(resolution*self.__distance(P4,P5))
        print(n1)

        t1 = Window.np.linspace(0,1,n1)
        t1 = Window.np.delete(t1,0)
        t2 = Window.np.linspace(0,1,n2)
        t2 = Window.np.delete(t2,0)
        t3 = Window.np.linspace(0,1,n3)
        t3 = Window.np.delete(t3,0)
        t4 = Window.np.linspace(0,1,n4)
        t4 = Window.np.delete(t4,0)
        print(t1)
        trajectory = Window.np.array([P1])
        print(trajectory)
        for tx in t1:
            trajectory = Window.np.vstack((trajectory,P1 + tx*Window.np.subtract(P2,P1))) #??????????????
        for tx in t2:
            trajectory = Window.np.vstack((trajectory,P2 + tx*Window.np.subtract(P3,P2)))
        for tx in t3:
            trajectory = Window.np.vstack((trajectory,P3 + tx*Window.np.subtract(P4,P3)))
        for tx in t4:
            trajectory = Window.np.vstack((trajectory,P4 + tx*Window.np.subtract(P5,P4)))    
        #P1_2=Window.np.delete(trajectory,0,0)
        print(trajectory)
        return trajectory

    
    def __returnPoints(self,index,*args):
        
        points=[]
        for point in args:
            for i in range(0,point.shape[0]):
                points.append(point[i][index])
        print(points)
        return points

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
        self.theta = Window.math.pi * self.raw_data[8] / 180
        self.psi = Window.math.pi * self.raw_data[9] / 180
        self.delta1 = self.raw_data[10]
        self.delta2 = self.raw_data[11]
        self.delta3 = self.raw_data[12]
        self.start_coordinates = self.raw_data[13]
        self.passage_coordinates1 = self.raw_data[14]
        self.passage_coordinates2 = self.raw_data[15]
        self.passage_coordinates3 = self.raw_data[16]
        self.end_coordinates = self.raw_data[17]

        self.data_points=self.__trajectory(self.start_coordinates,self.passage_coordinates1,self.passage_coordinates2,self.passage_coordinates3,self.end_coordinates)

        print(self.data_points.shape[0])

        self.l = self.l5 + self.l6
        self.reach = self.l1 + self.l2 + self.l3 + self.l4 +self.l5 + self.l6
        print('XDXDXDXD')
        #pomyśleć jak zadać wektor podejścia DANE TYMACZASOWE
        self.xt = self.__returnPoints(0,self.data_points)#(0,self.start_coordinates,self.passage_coordinates1,self.passage_coordinates2,self.passage_coordinates3,self.end_coordinates) #1
        self.yt = self.__returnPoints(1,self.data_points)
        self.zt = self.__returnPoints(2,self.data_points)

        C_theta = Window.math.cos(self.theta)
        S_theta = Window.math.sin(self.theta)
        C_psi = Window.math.cos(self.psi)
        S_psi = Window.math.sin(self.psi)
        
        tempx = self.l*C_theta*C_psi
        tempy = self.l*C_theta*S_psi
        tempz = self.l*S_theta

        xp = [x - tempx for x in self.xt]
        yp = [y - tempy for y in self.yt]#self.yt - self.l*C_theta*S_psi
        zp = [z - tempz for z in self.zt]#self.zt - self.l*S_theta
        print("\neksdi\n")
        print(xp)
        print("\neksdi\n")
        print(yp)
        print("\neksdi\n")
        print(zp)
        print("\nSiup Zium\n")
        print(len(xp))
        print('xd64:',xp[64],' yp64:',yp[64])

        S1 = Window.np.array([0])
        C1 = Window.np.array([0])
        for i in range(0,len(xp)):
            print(i)
            S1 = Window.np.append(S1,self.__controll((self.e*xp[i] + self.delta1*yp[i]*Window.math.sqrt((xp[i]**2)+(yp[i]**2)-(self.e **2)))/((xp[i]**2) + (yp[i]**2))))
            C1 = Window.np.append(C1,self.__controll((-self.e*yp[i] + self.delta1*yp[i]*Window.math.sqrt((xp[i]**2)+(yp[i]**2)-(self.e **2)))/((xp[i]**2) + (yp[i]**2))))
        S1 = Window.np.delete(S1,0)
        C1 = Window.np.delete(C1,0)
        print("S1:\n",S1,"\n")
        print("C1:\n",C1,"\n")
#############Works until here##############################
        S5 = Window.np.array([0])
        C5 = Window.np.array([0])
        S5 = self.__controll(C_theta*(S_psi*C1 - C_psi*S1))
        C5 = self.__controll(self.delta3 * Window.math.sqrt(1-(S5**2)))
        S5 = Window.np.delete(S5,0)
        C5 = Window.np.delete(C5,0)

        S234 = self.__controll(S_theta/C5)
        C234 = self.__controll(C_theta*(C_psi*C1 + S_psi*S1)/C5)

        xr = xp - self.l4*C1*C234
        yr = yp - self.l4*S1*C234
        zr = zp - self.l4*S234

        a = -self.l1+self.delta1*Window.math.sqrt((xr**2)+(yr**2)-self.e**2)
        b = ((a**2)+(zr**2)+(self.l2**2)-(self.l3**2))/(2*self.l2)

        S2 = self.__controll((zr*b+self.delta2*a*Window.math.sqrt((a**2)+(zr**2)-(b**2)))/((a**2)+(zr**2)))
        C2 = self.__controll((a*b-self.delta2*zr*Window.math.sqrt((a**2)+(zr**2)-(b**2)))/((a**2)+(zr**2)))

        S3 = self.__controll(-self.delta2*Window.math.sqrt((a**2)+(zr**2)-(b**2))/self.l3)
        C3 = self.__controll(((a**2)+(zr**2)-(self.l2**2)-(self.l3**2))/(2*self.l2*self.l3))

        S23 = self.__controll((zr-self.l2*(zr*b+self.delta2*a*Window.math.sqrt((a**2)+(zr**2)-(b**2))/((a**2)+(zr**2))))/self.l3)
        C23 = self.__controll((a-self.l2*(a*b-self.delta2*zr*Window.math.sqrt((a**2)+(zr**2)-(b**2))/((a**2)+(zr**2))))/self.l3)

        S4 = self.__controll(S234*C23 - C234*S23)
        C4 = self.__controll(C234*C23 + S234*S23)

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
        


    
