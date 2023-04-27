# Identifying Small Body Sphericity and Correlating Factors
- **Team Leader:** Jalen Perkins (Jalen-Perkins)
- **Other Group Members:** Madeline Pastuszek (madelinepast), Nathan Bigelow (Nbig17)
### Project Summary:
- In the past 50 years, NASA and related organizations have worked to collect data about the geometry of many known small bodies in space. The 3D Asteroid Catalogue is a database that catalogues the geometry of thousands of small bodies. Our goal is to use this data to analyze several small bodies and determine how the object's relative sphericity may relate to other influencing factors, such as size, location, orbital characteristics, and other parameters. 
### How to Use this Repository:
- This repository includes all the code and functions required to make these models work. As well, a few sample data files are available for test and simple viewing.
1. Read through this readme file to understand what the goal and purposes of this project were. 
2. Take a look at our environment.yml file to know what python libraries are required to run this project.
3. Clone this respository and its components. You will see the following:
data/
notebooks/
README.md
environment.yml
4. data/ contains the object files used in the example problems and plots. You can download similar asteroid object files from [3D Asteroid Catalogue](https://3d-asteroids.space/) in order to create your own plots.
5. notebooks/ contain all the code that was written during development and finalization. The [] directory contains all .py functions necessary, while [] contains any scratch code we created in our development. A complete demonstration of the whole project's process, as well as our conclusions, is contained in the [] notebook and is a helpful example of what our project and individual functions will do.

### Introduction:

## Background Information:
- According to the 2006 IAU resolution, small bodies are considered to be 'all objects [excluding defined planets, dwarf planets, and satellites] orbiting the Sun' [1]. Thus, small bodies can include comets, asteroids, objects in the Kuiper Belt and the Oort cloud, small planetary satellites, and interplanetary dust and also make up a large percentage of our solar system. The variety of these bodies lends to the variety of found geometries and locations when bodies have been observed. Organizations, such as NASA, have begun an effort to catagorize and document these small bodies, usually using data collected by space craft, probes, radar imaging, and lightcurving inversion [2]. Through these methods, various databases have been created in order to help planetary scientists study and draw conclusions about small bodies in the solar system.

## Problem Statement:
- In the field of Geophysics, we have a large amount of data and knowledge about the earth and its mechanics, yet far less is known about other bodies in space. As we continue to learn about other planets, moons, and bodies in our solar system, we see more and more just how unique the earth is in terms of mechanics, indicating that much of our knowledge about the earth may not apply to most other bodies in space. One area which we know relatively little about is the geometry and mechanics of small bodies, like asteroids, comets, moons, and dwarf planets. By studying the geometry of some of these small bodies and looking for any correlations between their size, mass, and orbits, we may be able to make some interpretations of how these bodies form, and why they exist where they do. If successful, this type of information would be useful for more distal space travel, predictions of collisions, and possibly even space mining resources. 

## Questions:
- What influences a small body's geometry?
- Does where a small body exists in the solar system impact geometry?
- Is small body geometry impacted by what other bodies (large or small) exist around it?
- Do the geological components (rock, ice, dust, etc.) of small bodies impact geometry?
- Can we develop models that are similar to what already exists?
- How can these models and conclusions help us learn more about other small bodies and make predictions about a wider subject?
## Objectives:
- To recreate and develop models similar to that of the 3D Asteroid Catalogue.
- To better our understanding of how small bodies' geometry differs and is influenced by other planetary and solar factors
- To help create a more definitive conclusion about why certain small bodies have particular geometries
- To develop a stronger understanding of python components and methods of modeling and data analysis

### Datasets:
- [SSD](https://ssd.jpl.nasa.gov/tools/gravity.html#/)
- [NASA](https://pdssbn.astro.umd.edu/index.shtml)
- [3D Asteroid Catalogue](https://3d-asteroids.space/) 

### Tools/Packages:
- [matplotlib](https://matplotlib.org/)
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [scipy](https://pypi.org/project/Scripy/)
- [plotly](https://plotly.com/)
- [ipympl]()
  - only needed to make the matplotlib figures interactable

### Methods:
- Write a function that can read the asteroid files and organize the vertices and faces.
- Write a function that will plot the asteroids as models in an interactive, 3-D plot.
- Calculate the center of mass and plot it.
- Calculate the radius of the surface points from the center of mass to identify a vector.
- Calculate the normal vector of each individual face.
- Calculate the dot product of the normal vector and the internal vector to determine how aligned they are, thus how spherical the object is.
- Plot the sphericity of the object.

### Expected Outcome(s):
- We hope that the results of this project will help us understand more about small bodies within our solar system. By organizing data and modeling these bodies, we will be able to draw conclusions about how the sphericity of small bodies is influenced by other factors, such as larger bodies, gravity influences, and body compositiion.
- In addition, this project will help us grow more confortable with using and applying python in geophysical and planetary projects. The processes done in this work will better our abilities to load, manipulate, and process data with python, as well as creating and formulating modeling techniques that correspond with the project's requirements. 

### References:
- [[1]](https://www.iau.org/news/pressreleases/detail/iau0603/#3)
- [[2]](https://3d-asteroids.space/)
