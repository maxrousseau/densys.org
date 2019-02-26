#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
sys.path.append("../")
import os
import uuid
import json
import cv2
import numpy as np
from modules import job
import pytest

class TestJob(object):
    """Testing the Job class
    This object will be testing the job class and its associated functions.

    This class contains methods to mirror those of the Job class and assert
    their functionalities.

    Parameters
    ----------
    None

    Returns
    ------
    None
    """

    @pytest.fixture
    def image_setup(self):
        # create a job for testing
        sample_job = job.Job("http://optipng.sourceforge.net/pngtech/img/lena.png", "asym")
        return sample_job

    def test_init(self, image_setup):
        sample_job = image_setup
        print(len(sample_job.json_obj))
        assert len(sample_job.json_obj) == 15

    #def test_asym(self, image_setup):

    #def test_lfh(self, image_setup):

    #def test_med(self, image_setup):

    #def test_ratio1(self, image_setup):

    #def test_ratio2(self, image_setup):

    #def test_ratio3(self, image_setup):

    def test_execute(self, image_setup):
        sample_job = image_setup
        assert sample_job.execute() != 0



