#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
import os
import uuid
import json
import cv2
import dlib
import numpy as np

class Job(object):
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
        # modification to the default encoder for uuid serilization
        json.JSONEncoder_olddefault = json.JSONEncoder.default
        def JSONEncoder_newdefault(self, o):
            if isinstance(o, uuid.UUID): return str(o)
            return json.JSONEncoder_olddefault(self, o)
        json.JSONEncoder.default = JSONEncoder_newdefault

        # create dictionnary of paths used in this file
        self.hash = uuid.uuid4()
        curr_dir = os.path.dirname(os.path.abspath((__file__)))
        prototxt = os.path.abspath("./models/deploy2.prototxt")
        model = os.path.abspath("./models/deploy2.caffemodel")
        shape_model = os.path.abspath("./models/68_landmarks.dat")
        joblist = os.path.abspath(str("./db/jobs/"+str(self.hash)+".json"))
        self.paths = {
            "curr_dir" : curr_dir,
            "prototxt" : prototxt,
            "model" : model,
            "joblist" : joblist,
            "shape_model" : shape_model
        }
        self.image = image
        self.task = task
        self.is_complete = False
        # initialize the json object for this job
        self.json_obj = {
            "hash" : self.hash,
            "img_raw" : image,
            "task" : self.task,
            "is_complete" : self.is_complete,
            "face_coord" : [],
            "ldmk_coord" : [],
            "result" : 0
        }
        self.confidence = 0.7

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
        print("this ran")

        return 0

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


        ###########################################################
        # face detetion: load network - prepare image - run network
        ###########################################################

        face_net = cv2.dnn.readNetFromCaffe(self.paths["prototxt"],
                                            self.paths["model"])
        image = cv2.imread(self.image)
        (height, width) = image.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)),
                                     1.0,
                                     (300, 300),
                                     (103.93, 116.77, 123.68))
        face_net.setInput(blob)
        detections = face_net.forward()

        for i in range(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > self.confidence:

                # multiple face warning!!!! --> if detections.shape[2] != 
                count = 0;
                if count > 0:
                    print("[ERROR] NO OR MULTIPLE FACES DETECTED IN IMAGE")
                    print("[INFO] cancelling job")

                else:
                    box = detections[0, 0, i, 3:7] * np.array([width, height, width,
                                                             height])
                    (startX, startY, endX, endY) = box.astype("int")
                    np_int_array = [startX, startY, endX, endY]
                    int32_array = []
                    for a in np_int_array:
                        int32_array.append(int(a))
                    self.json_obj["face_coord"] = int32_array

                    count += 1

        ###########################################################
        # facial landmarks: load face - create predictor - annotate
        ###########################################################
        dlib_rect = dlib.rectangle(int32_array[0],
                                   int32_array[1],
                                   int32_array[2],
                                   int32_array[3])
        predictor = dlib.shape_predictor(self.paths["shape_model"])

        landmarks = predictor(image, dlib_rect).parts()

        tuples_array = [(p.x, p.y) for p in landmarks]
        ldmk_coords = {}
        count = 1
        for x,y in tuples_array:
            x_coord = "X"+str(count)
            y_coord = "Y"+str(count)
            ldmk_coords[x_coord] = x
            ldmk_coords[y_coord] = y
            count += 1

        self.json_obj["ldmks_coords"] = ldmk_coords


        # run analysis functions
        if self.json_obj["task"] == "asym":
            self.asym()

        elif self.json_obj["task"] == "lfh":
            self.lfh()

        elif self.json_obj["task"] == "med":
            self.med()

        elif self.json_obj["task"] == "ratio1":
            self.ratio1()

        elif self.json_obj["task"] == "ratio2":
            self.ratio2()

        elif self.json_obj["task"] == "ratio3":
            self.ratio3()

        else:
            print("[ERROR] TASK DOES NOT EXIST")
            print("[INFO] cancelling job")



        # write results to 
        if not os.path.isfile(self.paths["joblist"]):
            with open(self.paths["joblist"], "w") as outfile:
                json.dump(self.json_obj, outfile)

        return result_int


