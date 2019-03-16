import Window
import time

class Compute:

    def __controll(self,trigfunc):
        if trigfunc>1:
            trigfunc=1
        if trigfunc<-1:
            trigfunc=-1
        return trigfunc

    def __imaginary(self,value):
        if value < 0:
            return 0
        return value

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
        print("ZASIEG")
        print(self.reach)
        print('XDXDXDXD')

        self.xt = self.__returnPoints(0,self.data_points)#(0,self.start_coordinates,self.passage_coordinates1,self.passage_coordinates2,self.passage_coordinates3,self.end_coordinates) #1
        self.yt = self.__returnPoints(1,self.data_points)
        self.zt = self.__returnPoints(2,self.data_points)
#########DRAWING TRAJECTORY ON PLOT################## 
        
        
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
        print('xp size: ',len(xp))
        # print('xp64:',xp[64],' yp64:',yp[64])

        S1 = []
        C1 = []
        for i in range(0,len(xp)):
            # print(i)
            S1.append(self.__controll((self.e*xp[i] + self.delta1*yp[i]*Window.math.sqrt(self.__imaginary((xp[i]**2)+(yp[i]**2)-(self.e **2))))/((xp[i]**2) + (yp[i]**2))))
            C1.append(self.__controll((-self.e*yp[i] + self.delta1*xp[i]*Window.math.sqrt(self.__imaginary((xp[i]**2)+(yp[i]**2)-(self.e **2))))/((xp[i]**2) + (yp[i]**2))))
        print("S1:\n",S1,"\n")
        print("C1:\n",C1,"\n")
#############Works until here##############################
        S5 = []
        C5 = []
        for i in range(0,len(C1)):
            S5.append(self.__controll(C_theta*(S_psi*C1[i] - C_psi*S1[i])))
            C5.append(self.__controll(self.delta3 * Window.math.sqrt(self.__imaginary(1-(S5[i]**2)))))
        print("S5 size: ",S5)
        print("C5 size: ",C5)
        print(S5,'\n')
        print(C5)

        S234 = []
        C234 = []
        for i in range(0,len(C5)):
            S234.append(self.__controll(S_theta/C5[i]))
            C234.append(self.__controll(C_theta*(C_psi*C1[i] + S_psi*S1[i])/C5[i]))
        print("S234 size: ",S234)
        print("C234 size: ",C234)

        xr = []
        yr = []
        zr = []
        for i in range(0,len(C234)):
            xr.append(self.xt[i] - self.l4*C1[i]*C234[i] - self.l*C_theta*C_psi)
            yr.append(self.yt[i] - self.l4*S1[i]*C234[i] - self.l*C_theta*S_psi)
            zr.append(self.zt[i] - self.l4*S234[i] - self.l*S_theta)
        print(xr)
        print("xr size: ",xr)
        print("yr size: ",yr)
        print("zr size: ",zr)

        a = []
        b = []
        for i in range(0,len(xr)):
            a.append(-self.l1+self.delta1*Window.math.sqrt(self.__imaginary((xr[i]**2)+(yr[i]**2)-self.e**2)))
            b.append(((a[i]**2)+(zr[i]**2)+(self.l2**2)-(self.l3**2))/(2*self.l2))
        print("a size: ",a)
        print("b size: ",b)

        S2 = []
        C2 = []
        for i in range(0,len(a)):
            S2.append(self.__controll((zr[i]*b[i]+self.delta2*a[i]*Window.math.sqrt(self.__imaginary((a[i]**2)+(zr[i]**2)-(b[i]**2))))/((a[i]**2)+(zr[i]**2))))
            C2.append(self.__controll((a[i]*b[i]-self.delta2*zr[i]*Window.math.sqrt(self.__imaginary((a[i]**2)+(zr[i]**2)-(b[i]**2))))/((a[i]**2)+(zr[i]**2))))
        print("S2 size: ",S2)
        print("C2 size: ",C2)

        S3 = []
        C3 = []
        for i in range(0,len(C2)):
            S3.append(self.__controll(-self.delta2*Window.math.sqrt(self.__imaginary((a[i]**2)+(zr[i]**2)-(b[i]**2)))/self.l3))
            C3.append(self.__controll((b[i]-self.l2)/(self.l3)))
        print("S3 size: ",S3)
        print("C3 size: ",C3)


        S23 = []
        C23 = []
        for i in range(0,len(C3)):
            S23.append(self.__controll((zr[i]-self.l2*S2[i])/(self.l3)))######
            C23.append(self.__controll((a[i]-self.l2*C2[i])/(self.l3)))#######
        print("S23 size: ",S23)
        print("C23 size: ",C23)

        S4 = []
        C4 = []
        for i in range(0,len(C23)):
            S4.append(self.__controll(S234[i]*C23[i] - C234[i]*S23[i]))
            C4.append(self.__controll(C234[i]*C23[i] + S234[i]*S23[i]))
        print("S4 size: ",S4)
        print("C4 size: ",C4)

        x10 = []
        y10 = []
        z10 = []

        x11 = []
        y11 = []
        z11 = []
        
        x21 = []
        y21 = []
        z21 = []

        x30 = []
        y30 = []
        z30 = []

        xrr = []
        yrr = []
        zrr = []

        xpr = []
        ypr = []
        zpr = []

        xtr = []
        ytr = []
        ztr = []

        for i in range(0,len(C1)):
            x10.append(self.l1*C1[i])
            y10.append(self.l1*S1[i])
            z10.append(0)

            x11.append(x10[i]+self.d*S1[i])
            y11.append(y10[i]-self.d*C1[i])
            z11.append(0)

            x21.append(x11[i]+self.l2*C2[i]*C1[i])
            y21.append(y11[i]+self.l2*C2[i]*S1[i])
            z21.append(self.l2*S2[i])

            x30.append(x21[i]-(self.d-self.e)*S1[i])
            y30.append(y21[i]+(self.d-self.e)*C1[i])
            z30.append(z21[i])

            xrr.append(x30[i]+self.l3*C1[i]*C23[i])
            yrr.append(y30[i]+self.l3*S1[i]*C23[i])
            zrr.append(z30[i]+self.l3*S23[i])

            xpr.append(xrr[i]+self.l4*C1[i]*C234[i])
            ypr.append(yrr[i]+self.l4*S1[i]*C234[i])
            zpr.append(zrr[i]+self.l4*S234[i])

            xtr.append(xpr[i]+self.l*C_psi*C_theta)
            ytr.append(ypr[i]+self.l*C_theta*S_psi)
            ztr.append(zpr[i]+self.l*S_theta)

        x = []
        y = []
        z = []
        # for i in range(34,35):
        #     x.append(x10[i])
        #     x.append(x11[i])
        #     x.append(x21[i])
        #     x.append(x30[i])
        #     x.append(xrr[i])
        #     x.append(xpr[i])
        #     x.append(xtr[i])

        #     y.append(y10[i])
        #     y.append(y11[i])
        #     y.append(y21[i])
        #     y.append(y30[i])
        #     y.append(yrr[i])
        #     y.append(ypr[i])
        #     y.append(ytr[i])

        #     z.append(z10[i])
        #     z.append(z11[i])
        #     z.append(z21[i])
        #     z.append(z30[i])
        #     z.append(zrr[i])
        #     z.append(zpr[i])
        #     z.append(ztr[i])

        app.a.clear()
        app.a.plot(self.xt,self.yt,self.zt)
        app.a.plot(xtr,ytr,ztr)
        print(self.data_points)
        print(self.xt)
        print(self.yt)
        print(self.zt)
            
            


        




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
        


    
