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
    def image_setup_asym(self):
        sample_job = job.Job("http://optipng.sourceforge.net/pngtech/img/lena.png", "asym")
        return sample_job

    @pytest.fixture
    def image_setup_lfh(self):
        sample_job = job.Job("http://optipng.sourceforge.net/pngtech/img/lena.png", "lfh")
        return sample_job

    @pytest.fixture
    def image_setup_ratio1(self):
        sample_job = job.Job("http://optipng.sourceforge.net/pngtech/img/lena.png", "ratio1")
        return sample_job

    @pytest.fixture
    def image_setup_ratio2(self):
        sample_job = job.Job("http://optipng.sourceforge.net/pngtech/img/lena.png", "ratio2")
        return sample_job
    @pytest.fixture
    def image_setup_ratio3(self):
        sample_job = job.Job("http://optipng.sourceforge.net/pngtech/img/lena.png", "ratio3")
        return sample_job

    def test_init(self, image_setup_asym):
        sample_job = image_setup_asym
        print(len(sample_job.json_obj))
        assert len(sample_job.json_obj) == 15

    def test_execute(self, image_setup_asym):
        sample_job = image_setup_asym
        assert sample_job.execute() != 0

    def test_asym(self, image_setup_asym):
        sample_job = image_setup_asym
        test_result = sample_job.execute()
        assert (float(test_result) > 7.4) & (float(test_result) < 7.7)

    def test_lfh(self, image_setup_lfh):
        sample_job = image_setup_lfh
        test_result = sample_job.execute()
        assert (float(test_result) > 0.4) & (float(test_result) < 0.6)

    #def test_med(self, image_setup):

    def test_ratio1(self, image_setup_ratio1):
        sample_job = image_setup_ratio1
        test_result = sample_job.execute()
        assert (float(test_result) > 0.6) & (float(test_result) < 0.7)

    def test_ratio2(self, image_setup_ratio2):
        sample_job = image_setup_ratio2
        test_result = sample_job.execute()
        assert (float(test_result) > 0.7) & (float(test_result) < 0.8)

    def test_ratio3(self, image_setup_ratio3):
        sample_job = image_setup_ratio3
        test_result = sample_job.execute()
        assert (float(test_result) > 1) & (float(test_result) < 1.2)




