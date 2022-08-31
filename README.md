# SPI2-visualization
3-D visualizations for SPI2 systems.

<img width="527" alt="SPI2_network" src="https://user-images.githubusercontent.com/73458503/187379816-01dc92a4-8329-4ec9-9fec-d36e32178491.png">

The code contained in this repository requires installation of Python's PyVista. PyVista is a high level API to the Visualization Toolkit (VTK). Installation information can be found under README.md here: https://github.com/pyvista/pyvista.git

This repository contains python code for obtaining visualizations of SPI2 engineering systems. Essentially, any engineering system with multiple components that have interconnecting splines can be classified as a SPI2 system. These systems have calculated component placement and spline interpolation, and this repository provides an easy, accessible way to create these objects and place them. 

Users can create splines of desired length, radius, color, and coordinates and further interpolate these spline objects with methods in the Spline class. Components are represented as solid shapes of cylinders and spheres, which can be created using the component class. 


