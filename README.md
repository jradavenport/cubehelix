cubehelix
=========

A full implementation of Dave Green's [cubehelix](http://adsabs.harvard.edu/abs/2011arXiv1108.5083G) colormap for Python.

The user can adjust all parameters of the cubehelix algorithm. 
This enables much greater flexibility in choosing color maps, while (by default) ensuring the color map scales in brightness from black to white.

A few simple example flavors of cubehelix:

- Default color map settings produce the standard "cubehelix": ``cubehelix.cmap()`` 

![Reversed Standard cubehelix scheme](http://i.imgur.com/d0VwfK9.png?raw=true)
- Create color map in only blues: ``cubehelix.cmap(rot=0, start=0)``
- Create reverse (white to black) backwards through the rainbow once: ``cubehelix.cmap(rot=1, reverse=True)`` 

![A nice blue cubehelix scheme](http://i.imgur.com/Kub0kgA.png)
- Similar to [Matteo Niccoli’s perceptual rainbow](http://mycarta.wordpress.com/2013/02/21/perceptual-rainbow-palette-the-method/): ``cubehelix.cmap(startHue=240,endHue=-300,minSat=1,maxSat=2.5,minLight=.3,maxLight=.8,gamma=.9)``

![a better rainbow](http://i.imgur.com/XXM1r6f.png)


Discussion and examples shown on my blog: [If We Assume](http://www.ifweassume.com/2014/04/cubehelix-colormap-for-python.html)

Basic Usage
-----

    import cubehelix
    cx = cubehelix.cmap(start=0., rot=-0.5)
    plot(x,cmap=cx)


Installation
------------

Download:

- Place cubehelix.py in your Python path.

From source::

    setup.py install

or with pip::

    pip install git+git://github.com/jradavenport/cubehelix.git
