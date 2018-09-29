#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
import os
import uuid
import json

class Job:
    """This class will act as a controller for the analysis pushed to the api"""


    def __init__(self, image, task):
        """Job object to create, store, exectute and post results
        Upon initialization a hash will be assigned to the image which will serve
        as a unique identifier.

        It has two methods create (which will store a new job in the data file) and
        execute which calls the appropriate analysis on an image.

        Task list [med, ratio1, ratio2, ratio3, lfh, asym]

        Parameters
        ----------
        image : string
            path to image uploaded by the user
        task :  int
            int corresponding to the specific analysis requested by the user

        Returns
        ------
        None
        """

        self.hash = uuid.uuid4()
        self.image = image
        self.task = task
        self.complete = False
        self.json_obj = {
            "hash" : self.hash,
            "img_raw" : image,
            "task" : self.task,
            "complete" : complete,
            "haar_coord" : [],
            "ldmk_coord" : [],
            "result" : 0
        }

    def execute(self):
        """Method creating a new job entry to be saved in joblist.json
        Here we call the appropriate analysis depending on the task that was

        This method will store the job's hash, task, image path and current job
        status once completed.

        Parameters
        ----------
        None

        Returns
        ------
        result : string
            result of the specific analysis presented as a string.
        """

        result_str = None
        result_int = 0
        switcher = {
            1 : med,
            2 : ratio1,
            3 : ratio2,
            4 : ratio3,
            5 : lfh,
            6 : asym
        }

        ###################
        # ****************#
        # IMAGE PROCESSING#
        # ****************#
        ###################

        function = switcher.get(self.task, lambda: "Invalid Task ID")

    def med(self):
        """Executes the Mean Euclidean Distance analysis"""

        return result

    def ratio1(self):
        """Computes the value of ratio 1"""

        return result

    def ratio2(self):
        """Computes the value of ratio 2"""

        return result

    def ratio3(self):
        """Computes the value of ratio 3"""

        return result

    def lfh(self):
        """Computes the lower face height"""

        return result

    def asym(self):
        """Compute the asymmetry index"""

        return result


