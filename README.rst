cubehelix
=========

A full implementation of Dave Green's `cubehelix <http://adsabs.harvard.edu/abs/2011arXiv1108.5083G>`_ colormap for Python.

The user can adjust all parameters of the cubehelix algorithm. 
This enables much greater flexibility in choosing color maps, while (be default) ensuring the color map scales in intensity from black to white.

A few simple example flavors of cubehelix:

- Default color map settings produce the standard "cubehelix": ``cubehelix.cmap()``
- Create color map in only blues: ``cubehelix.cmap(rot=0, start=0)``
- Create reverse (white to black) backwards through the rainbow once: ``cubehelix.cmap(rot=1, reverse=True)``
- Similar to Matteo Niccoli’s perceptual rainbow: ``cubehelix.cmap(startHue=240,endHue=-300,minSat=1,maxSat=2.5,minLight=.3,maxLight=.8,gamma=.9)``


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
