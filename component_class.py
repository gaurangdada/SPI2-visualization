#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyvista as pv
import numpy as np

class Component:
    def __init__(self, shapetype, center, radius, color):
        
        self.shapetype = shapetype
        self.center = center
        self.radius = radius
        self.color = color
        
    def introComponent(self):
        print("component type = " + self.shapetype + ", center = " + str(self.center) + ", radius = " + str(self.radius))
        
    def createShape(self):
        
        if self.shapetype == "sphere":
            sphere = pv.Sphere(self.radius, center = self.center)
            # p.add_mesh(sphere, color = self.color, show_edges = True) 
        
        if self.shapetype == "cylinder":
            cylinder = pv.Cylinder(self.center, radius = self.radius)
            # p.add_mesh(cylinder, color = self.color, show_edges = True)
        
    def plotShape(self):
        
        p = pv.Plotter(1,1)
        p.subplot(0,0)
        
        if self.shapetype == "sphere":
            sphere = pv.Sphere(self.radius, center = self.center)
            p.add_mesh(sphere, color = self.color, show_edges = False)
             
        if self.shapetype == "cylinder":
            cylinder = pv.Cylinder(self.center, radius = self.radius)
            p.add_mesh(cylinder, color = self.color, show_edges = False)
        p.show()
       
    def plotShapes(components):
        p = pv.Plotter(1,1)
        p.subplot(0,0)

        for component in components:
            if component.shapetype == "sphere":
                sphere = pv.Sphere(component.radius, center = component.center)
                p.add_mesh(sphere, color = component.color, show_edges = False)
        
            if component.shapetype == "cylinder":
                cylinder = pv.Cylinder(component.center, radius = component.radius)
                p.add_mesh(cylinder, color = component.color, show_edges = False)
        p.show()

