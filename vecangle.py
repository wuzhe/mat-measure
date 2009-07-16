"""
@author: Manuel Metz
@organization: Argelander-Institut fuer Astronomie, University Bonn
@contact: mmetz @ astro.uni-bonn.de
@license: GPL2
@version: 0.1
"""

__author__ = 'Manuel Metz, mmetz @ astro.uni-bonn.de'
__version__ = 0.1
__data__ = '2008-04-15'

import numpy

def _vdot(a,b):
    if len(a.shape)==1:
        return numpy.sum(a*b)
    elif len(a.shape)==2:
        return numpy.sum(a*b,1)

def _vabs(a):
    if len(a.shape)==1:
        return numpy.sqrt( numpy.sum(a**2) )
    elif len(a.shape)==2:
        return numpy.sqrt( numpy.sum(a**2,1) )

def vecangle(a, b, axial=False):
    """Calculate the angles between vectors or axes.
    
    Given two arrays, a & b, representing cartesian vectors,
    the angle between these vectors is calculated.
    
    a & b can be 1d arrays (vectors) or 2d arrays, in the
    latter case each row is a cartesian vector, e.g.:
    
    >>> a = [1.,0.,0.] # the x-axis
    >>> b = [1.,1.,0.] # a diagonal
        
    >>> print vecangle(a,b) # pi/4
    
    >>> a = [[1.,0.,0.],
             [0.,1.,0.]] # the x and y axes
    >>> b = [[1.,1.,0.],
             [1.,1.,0.]] # a diagonal
    
    >>> print vecangle(a,b) # [pi/4, pi/4]
    
    If axial is True, the arrays are interpreted as
    undirected data, i.e. representing an axis. In this
    case the maximum angle between two vectors is
    pi/2 (90 degr).
    """
    a = numpy.asarray(a)
    b = numpy.asarray(b)
    
    if a.shape!=b.shape:
        raise 'vectors have different shape'
    
    if axial:
        return numpy.arccos( numpy.fabs( \
           _vdot(a,b) / ( _vabs(a)*_vabs(b)) ) )
    else:
        return numpy.arccos( \
           _vdot(a,b) / ( _vabs(a)*_vabs(b)) )


if __name__=='__main__':
    a = numpy.array([1.,2.,3.], numpy.float64)
    b = numpy.array([1,0.1,0.3], numpy.float64)

    expected = 1.00613523056
    print vecangle(a,b)
    print vecangle(a.tolist(), b.tolist())
    print expected


    x = numpy.array([[1,2,3],[2,3,4]], numpy.float64)
    y = numpy.array([[1,0.1,0.3], [1.1, 0.2, 0.4]], numpy.float64)

    expected = numpy.array([1.00613523, 0.81194524])
    print vecangle(x,y)
    print vecangle(x.tolist(),y.tolist())
    print expected
