#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def scene(splines, components):
    p = pv.Plotter(1,1)
    p.subplot(0,0)
    
    for spline in splines:
        Spline = pv.Spline(spline.points, 100).tube(radius = spline.radius)
        p.add_mesh(Spline, color = spline.color, show_edges = False)
            
    for component in components:
        if component.shapetype == "sphere":
            sphere = pv.Sphere(component.radius, center = component.center)
            p.add_mesh(sphere, color = component.color, show_edges = False)
        
        if component.shapetype == "cylinder":
            cylinder = pv.Cylinder(component.center, radius = component.radius)
            p.add_mesh(cylinder, color = component.color, show_edges = False)
            
    p.add_bounding_box(color='grey', corner_factor=0.5, line_width=None, opacity=1.0, render_lines_as_tubes=False, lighting=None, reset_camera=None, outline=True, culling='front')
    p.show()

