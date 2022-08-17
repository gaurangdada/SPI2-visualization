#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyvista as pv
import numpy as np

class Spline:
    def __init__(self, name, radius, points, color):
        self.name = name
        self.radius = radius
        self.points = points
        self.color = color
        
    def introSpline(self):
        print("spline name = " + self.name + ", radius = " + str(self.radius) + " , spline coordinates = " + str(self.points) + ", color = " + str(self.color))
    
    def plotSpline(self):
        spline = pv.Spline(self.points, 10000).tube(radius = self.radius)
        return spline.plot(scalars = 'arc_length', show_edges = False)
    

    def avoidCollision(spline_1, spline_2):
    
        p = pv.Plotter(1,1)

        points_1 = []
        points_2 = []
        points_1 = spline_1.points
        points_2 = spline_2.points
        
        color_1 = spline_1.color
        color_2 = spline_2.color
        
        
        rad = spline_1.radius

        for point in range(len(spline_1.points)):
            check = np.array_equal(points_1[point], points_2[point])
            if check == True:
                print("collision at " + str(points_1[point]))
                points_2[point] = [points_2[point][0] + 2*rad, points_2[point][1], points_2[point][2]]
            else: 
                print("no collision at " + str(points_1[point]))

        p.subplot(0,0)
        
        spline_1 = pv.Spline(points_1, 50).tube(radius = spline_1.radius)
        spline_2 = pv.Spline(points_2, 50).tube(radius = spline_2.radius)

        p.add_mesh(spline_1, color = color_1, show_edges = False)
        p.add_mesh(spline_2, color = color_2, show_edges = False)

        p.show()
        
    
    def NinetyBend(self, point): # 'arr' stores the striaght line coordinates, 'point' is the point where you want to see the 90 degree bend 
        x_val = [] 
        for element in self.points:
            if element < point:
                x_val.append(element)
            else:
                x_val.append(point)    

        y_val = []
        for element in self.points:
            if element >= point:
                element = element - (point - 1)
                y_val.append(element)

            else:
                element = 0
                y_val.append(element)     

        z_val = np.linspace(0,0, len(x_val))

        points_3 = np.column_stack((x_val,y_val,z_val))
        spline = Spline("spline", self.radius, points_3)

        return spline.plotSpline()
 
    def plotSplines(splines):
        
        p = pv.Plotter(1,1)
        p.subplot(0,0)
        
        for spline in splines:
            Spline = pv.Spline(spline.points, 10000).tube(radius = spline.radius)
            p.add_mesh(Spline, color = spline.color, show_edges = False)
        p.show()

