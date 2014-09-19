# -*- coding: utf-8 -*-
from matplotlib.colors import LinearSegmentedColormap as LSC
from math import pi
import numpy as np


def cmap(start=0.5, rot=-1.5, gamma=1.0, reverse=False, nlev=256.,
         minSat=1.2, maxSat=1.2, minLight=0., maxLight=1.,
         **kwargs):
    """
    A full implementation of Dave Green's "cubehelix" for Matplotlib.
    Based on the FORTRAN 77 code provided in
    D.A. Green, 2011, BASI, 39, 289.

    http://adsabs.harvard.edu/abs/2011arXiv1108.5083G

    User can adjust all parameters of the cubehelix algorithm.
    This enables much greater flexibility in choosing color maps, while
    always ensuring the color map scales in intensity from black
    to white. A few simple examples:

    Default color map settings produce the standard "cubehelix".

    Create color map in only blues by setting rot=0 and start=0.

    Create reverse (white to black) backwards through the rainbow once
    by setting rot=1 and reverse=True.

    Parameters
    ----------
    start : scalar, optional
        Sets the starting position in the color space. 0=blue, 1=red,
        2=green. Defaults to 0.5.
    rot : scalar, optional
        The number of rotations through the rainbow. Can be positive
        or negative, indicating direction of rainbow. Negative values
        correspond to Blue->Red direction. Defaults to -1.5
    gamma : scalar, optional
        The gamma correction for intensity. Defaults to 1.0
    reverse : boolean, optional
        Set to True to reverse the color map. Will go from black to
        white. Good for density plots where shade~density. Defaults to False
    nlev : scalar, optional
        Defines the number of discrete levels to render colors at.
        Defaults to 256.
    sat : scalar, optional
        The saturation intensity factor. Defaults to 1.2
        NOTE: this was formerly known as "hue" parameter
    minSat : scalar, optional
        Sets the minimum-level saturation. Defaults to 1.2
    maxSat : scalar, optional
        Sets the maximum-level saturation. Defaults to 1.2
    startHue : scalar, optional
        Sets the starting color, ranging from [0, 360], as in
        D3 version by @mbostock
        NOTE: overrides values in start parameter
    endHue : scalar, optional
        Sets the ending color, ranging from [0, 360], as in
        D3 version by @mbostock
        NOTE: overrides values in rot parameter
    minLight : scalar, optional
        Sets the minimum lightness value. Defaults to 0.
    maxLight : scalar, optional
        Sets the maximum lightness value. Defaults to 1.

    Returns
    -------
    matplotlib.colors.LinearSegmentedColormap object

    Example
    -------
    >>> import cubehelix
    >>> import matplotlib.pyplot as plt
    >>> import numpy as np
    >>> x = np.random.randn(1000)
    >>> y = np.random.randn(1000)
    >>> cx = cubehelix.cmap(start=0., rot=-0.5)
    >>> plt.hexbin(x, y, gridsize=50, cmap=cx)

    Revisions
    ---------
    2014-04 (@jradavenport) Ported from IDL version
    2014-04 (@jradavenport) Added kwargs to enable similar to D3 version,
                            changed name of "hue" parameter to "sat"
    """

# override start and rot if startHue and endHue are set
    if kwargs is not None:
        if 'startHue' in kwargs:
            start = (kwargs.get('startHue') / 360. - 1.) * 3.
        if 'endHue' in kwargs:
            rot = kwargs.get('endHue') / 360. - start / 3. - 1.
        if 'sat' in kwargs:
            minSat = kwargs.get('sat')
            maxSat = kwargs.get('sat')

# set up the parameters
    fract = np.linspace(minLight, maxLight, nlev)
    angle = 2.0 * pi * (start / 3.0 + rot * fract + 1.)
    fract = fract**gamma

    satar = np.linspace(minSat, maxSat, nlev)
    amp = satar * fract * (1. - fract) / 2.

# compute the RGB vectors according to main equations
    red = fract + amp * (-0.14861 * np.cos(angle) + 1.78277 * np.sin(angle))
    grn = fract + amp * (-0.29227 * np.cos(angle) - 0.90649 * np.sin(angle))
    blu = fract + amp * (1.97294 * np.cos(angle))

# find where RBB are outside the range [0,1], clip
    red[np.where((red > 1.))] = 1.
    grn[np.where((grn > 1.))] = 1.
    blu[np.where((blu > 1.))] = 1.

    red[np.where((red < 0.))] = 0.
    grn[np.where((grn < 0.))] = 0.
    blu[np.where((blu < 0.))] = 0.

# optional color reverse
    if reverse is True:
        red = red[::-1]
        blu = blu[::-1]
        grn = grn[::-1]

# put in to tuple & dictionary structures needed
    rr = []
    bb = []
    gg = []
    for k in range(0, int(nlev)):
        rr.append((float(k) / (nlev - 1.), red[k], red[k]))
        bb.append((float(k) / (nlev - 1.), blu[k], blu[k]))
        gg.append((float(k) / (nlev - 1.), grn[k], grn[k]))

    cdict = {'red': rr, 'blue': bb, 'green': gg}
    return LSC('cubehelix_map', cdict)
