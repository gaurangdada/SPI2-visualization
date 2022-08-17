#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Creating component objects by giving: shape type, center, radius, and color

comp1 = Component("sphere", (0,0,0), 0.35, "blue")
comp2 = Component("cylinder", (0,2,0), 0.45, "red")

# Creating spline objects by giving: spline name, radius, 3D coordinates, and color

s1 =  Spline("spline_1", 0.51, [[0,0,-3], [0,0,-2], [0,0,-1] ,[0,0,0] ,[0,0,1], [0,0,2] ,[0,0,3]], "blue")
s2 = Spline("spline_2", 0.32, [[0,-3,0], [0,-2,0], [0,-1,0] ,[0,0,0] ,[0,1,0], [0,2,0] ,[0,3,0]], "green")


