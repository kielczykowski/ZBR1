import Window

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

    def __fiarg(self,S,C):
        fi = []
        deg = 180/Window.math.pi
        for i in range(0,len(S)):
            if S[i]>0 and C[i]>0:
                fi.append(abs(Window.math.asin(S[i]))*deg)
            elif S[i]>0 and C[i]<0:
                fi.append((Window.math.pi - Window.math.asin(S[i]))*deg)
            elif S[i]<0 and C[i]<0:
                fi.append((Window.math.asin(abs(S[i]))+Window.math.pi)*deg)
            elif S[i]<0 and C[i]>0:
                fi.append(((3/2)*Window.math.pi + Window.math.pi/2 - Window.math.asin(abs(S[i])))*deg)
            elif S[i]==0:
                fi.append(0)
            else:
                fi.append(1*deg)
        return fi

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

        self.l = self.l5 + self.l6
        self.reach = self.l1 + self.l2 + self.l3 + self.l4 +self.l5 + self.l6

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
        yp = [y - tempy for y in self.yt]
        zp = [z - tempz for z in self.zt]

        S1 = []
        C1 = []
        S5 = []
        C5 = []
        S234 = []
        C234 = []
        xr = []
        yr = []
        zr = []
        a = []
        b = []
        S2 = []
        C2 = []
        S3 = []
        C3 = []
        S23 = []
        C23 = []
        S4 = []
        C4 = []


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

        for i in range(0,len(xp)):
            
            S1.append(self.__controll((self.e*xp[i] + self.delta1*yp[i]*Window.math.sqrt(self.__imaginary((xp[i]**2)+(yp[i]**2)-(self.e **2))))/((xp[i]**2) + (yp[i]**2))))
            C1.append(self.__controll((-self.e*yp[i] + self.delta1*xp[i]*Window.math.sqrt(self.__imaginary((xp[i]**2)+(yp[i]**2)-(self.e **2))))/((xp[i]**2) + (yp[i]**2))))

            S5.append(self.__controll(C_theta*(S_psi*C1[i] - C_psi*S1[i])))
            C5.append(self.__controll(self.delta3 * Window.math.sqrt(self.__imaginary(1-(S5[i]**2)))))

            S234.append(self.__controll(S_theta/C5[i]))
            C234.append(self.__controll(C_theta*(C_psi*C1[i] + S_psi*S1[i])/C5[i]))

            xr.append(self.xt[i] - self.l4*C1[i]*C234[i] - self.l*C_theta*C_psi)
            yr.append(self.yt[i] - self.l4*S1[i]*C234[i] - self.l*C_theta*S_psi)
            zr.append(self.zt[i] - self.l4*S234[i] - self.l*S_theta)

            a.append(-self.l1+self.delta1*Window.math.sqrt(self.__imaginary((xr[i]**2)+(yr[i]**2)-self.e**2)))
            b.append(((a[i]**2)+(zr[i]**2)+(self.l2**2)-(self.l3**2))/(2*self.l2))

            S2.append(self.__controll((zr[i]*b[i]+self.delta2*a[i]*Window.math.sqrt(self.__imaginary((a[i]**2)+(zr[i]**2)-(b[i]**2))))/((a[i]**2)+(zr[i]**2))))
            C2.append(self.__controll((a[i]*b[i]-self.delta2*zr[i]*Window.math.sqrt(self.__imaginary((a[i]**2)+(zr[i]**2)-(b[i]**2))))/((a[i]**2)+(zr[i]**2))))

            S3.append(self.__controll(-self.delta2*Window.math.sqrt(self.__imaginary((a[i]**2)+(zr[i]**2)-(b[i]**2)))/self.l3))
            C3.append(self.__controll((b[i]-self.l2)/(self.l3)))

            S23.append(self.__controll((zr[i]-self.l2*S2[i])/(self.l3)))######
            C23.append(self.__controll((a[i]-self.l2*C2[i])/(self.l3)))#######

            S4.append(self.__controll(S234[i]*C23[i] - C234[i]*S23[i]))
            C4.append(self.__controll(C234[i]*C23[i] + S234[i]*S23[i]))

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


        self.fi1 = self.__fiarg(S1,C1)
        self.fi2 = self.__fiarg(S2,C2)
        self.fi3 = self.__fiarg(S3,C3)
        self.fi4 = self.__fiarg(S4,C4)
        self.fi5 = self.__fiarg(S5,C5)
        xfi = list(range(0,len(self.fi1)))

        app.a.clear()
        app.a2.clear()
        xd = range(0,10)
        yd = range(0,10)
        app.a2.plot(xfi,self.fi1)
        app.a2.plot(xfi,self.fi2)
        app.a2.plot(xfi,self.fi3)
        app.a2.plot(xfi,self.fi4)
        app.a2.plot(xfi,self.fi5)

        x = []
        y = []
        z = []
        for i in range(0,len(x10)):
            x.append(0)
            y.append(0)
            z.append(0)

            x.append(x10[i])
            x.append(x11[i])
            x.append(x21[i])
            x.append(x30[i])
            x.append(xrr[i])
            x.append(xpr[i])
            x.append(xtr[i])

            y.append(y10[i])
            y.append(y11[i])
            y.append(y21[i])
            y.append(y30[i])
            y.append(yrr[i])
            y.append(ypr[i])
            y.append(ytr[i])

            z.append(z10[i])
            z.append(z11[i])
            z.append(z21[i])
            z.append(z30[i])
            z.append(zrr[i])
            z.append(zpr[i])
            z.append(ztr[i])

            app.a.clear()
            app.a.plot(self.xt,self.yt,self.zt)
            app.a.plot(xtr,ytr,ztr)
            app.a.plot(x,y,z)
            app.f.canvas.draw()
            x = []
            y = []
            z = []
        pass


if __name__ == "__main__":
    root = Window.tk.Tk()
    gui = Window.GUI(root)
    back = Compute()
    root.mainloop()
        


    
