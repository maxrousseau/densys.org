#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
sys.path.append("../")
import os
import pytest
from modules import linear as ln
import numpy as np

class TestLinear(object):
    """Testing for the Linear class

    This object will be testing the Linear class and its associated methods.

    This class contains methods that will mirror those of the Linear class and
    assert their functionalities.

    Parameters
    ----------
    None

    Returns
    ------
    None
    """

#   system of equations:
#        f(x)=1^x+0 coords((3,3)(6,6)) slope=1 constant=0
#        f(x)=-1^x+4 coords((0,4)(4,0)) slope=-1 constant=4
#        midline = 0^x + 5 ((0,5)(5,5)) slope=0 constant=5

    @pytest.fixture
    def array_setup(self):
        # create a system of equations to solve
        test_midline_coords_ax = np.array([0])
        test_midline_coords_ay = np.array([5])
        test_midline_coords_bx = np.array([5])
        test_midline_coords_by = np.array([5])

        test_coords_ax = np.array([3,0])
        test_coords_ay = np.array([3,4])
        test_coords_bx = np.array([6,4])
        test_coords_by = np.array([6,0])

        midline = ln.Linear(test_midline_coords_ax,
                         test_midline_coords_ay,
                         test_midline_coords_bx,
                         test_midline_coords_by)

        sys_eq = ln.Linear(test_coords_ax,
                        test_coords_ay,
                        test_coords_bx,
                        test_coords_by)

        return midline, sys_eq

    def test_init(self, array_setup):

        midline, sys_eq = array_setup

        midline_sl = (midline.slopes == np.array([0]))
        midline_cst = (midline.constants == np.array([5]))

        sys_eq_sl = (sys_eq.slopes == np.array([1,-1]))
        sys_eq_cst = (sys_eq.constants == np.array([0,4]))


        assert True == sys_eq_sl[0]
        assert True == sys_eq_sl[1]
        assert True == sys_eq_cst[0]
        assert True == sys_eq_cst[1]
        assert True == midline_sl[0]
        assert True == midline_cst[0]


    def test_solve(self, array_setup):

        midline, sys_eq = array_setup

        x_inter, y_inter = sys_eq.solve(midline.slopes, midline.constants)

        astx = (x_inter == np.array([5, -1]))
        asty = (y_inter == np.array([5, 5]))

        assert True == astx[0]
        assert True == astx[1]
        assert True == asty[0]
        assert True == asty[1]


