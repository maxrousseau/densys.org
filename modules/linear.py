#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
sys.path.append("../")
import numpy as np

class Linear(object):
    """This class is a linear mathematical function"""

    def __init__(self, coords_ax, coords_ay, coords_bx, coords_by):
        """Linear mathematical function object
        Initialize with two coordinates to determine the constant and slope.

        Contains method to determine Y given X.

        Parameters
        ----------
        coords_ax : numpy array
            x coordinate for first landmark
        coords_ay : numpy array
            y coordinate for first landmark
        coords_bx : numpy array
            x coordinate for second landmark
        coords_bx : numpy array
            y coordinate for second landmark

        Returns
        ------
        None
        """
        self.x1 = coords_ax
        self.y1 = coords_ay
        self.x2 = coords_bx
        self.y2 = coords_bx
        self.slope = (self.y2 - self.y1) / (self.x2 - self.x1)
        self.constant = self.y1 - self.slope*self.x1

    def solve(self, input_slope, input_constant):
        """calculates Y coordinate for a given X

        Parameters
        ----------
        input_slope : int
           value of the slope of the function we want to compare
        input_constant : int
           value of the constant of the function we want to compare

        Returns
        ------
        output_y : int
            resulting Y from the arithmetic computations
        """
        a = input_slope
        b = input_constant
        c = self.slope
        d = self.constant
        inter_x = (d - b)/(a - c)
        inter_y = (a*c) + d

        return inter_x, inter_y

    def euc_dist(self, ldmk_ax, ldmk_ay, ldmk_bx, ldmk_by):
        """compute the Euclidean distance between 2 landmarks
        Calculates the Euclidean distance between 2 landmarks and returns it as
        output.

        Parameters
        ----------
        ldmk_ax : numpy array
            X values for the first landmarks
        ldmk_ay : numpy array
            Y values for the first landmarks
        ldmk_bx : numpy array
            X values for the second landmarks
        ldmk_by : numpy array
            Y values for the second landmarks

        Returns
        -------
        distance : numpy array
            Euclidean between the two landmarks
        """
        height = ldmk_ay - ldmk_by
        width = ldmk_ax - ldmk_bx
        distance = np.sqrt((np.square(height)+np.square(width)))

        return distance


