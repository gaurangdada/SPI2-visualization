#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Spline and component objects created as shown in "objects_example" can be manipulated and plotted by useful functions implemented in the respective class files
# This notebook has information on how to call these functions

# -- Component functions --

components = [comp1, comp2]
# array of two component objects 
plotShapes(components)
# plots all components in the component array

comp1.introComponent()
# calling this function gives the shapetype, center, radius, and color

comp1.createShape()
# makes a shape on the pyvista interface ready to plot

comp1.plotShape()
# plots the created shape




# -- Spline functions --

avoidCollision(s1,s2)
# averts collision between two splines

s4.NinetyBend(2.23)
# bends a straight spline at an input point 

plotSplines(splines)
# plots an object array of splines

s2.introSpline()
# calling this function introduces the spline, giving its name, radius, coordinates, and color

