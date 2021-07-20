import cv2
import numpy as np  

class YoloInf:

    def __init__(self,p,t,h,w,path):
        self.p = float(p) 
        self.t = float(t) 
        self.h = int(h) 
        self.w = int(w) 
        self.configPath = path

    def load_config(self):
        with open('{}\classes.txt'.format(self.configPath)) as f:
            self.labels = [line.strip() for line in f]
    
        self.network = cv2.dnn.readNetFromDarknet('{}\yolo.cfg'.format(self.configPath),
                                            '{}\yolo_final.weights'.format(self.configPath))

        self.network.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        self.network.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

        self.layers_names_all = self.network.getLayerNames()
        self.layers_names_output = [self.layers_names_all[i[0] - 1] for i in self.network.getUnconnectedOutLayers()]

    def inference(self,frame):
        self.blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (320, 320),swapRB=True, crop=False)

        self.network.setInput(self.blob) 
        self.output_from_network = self.network.forward(self.layers_names_output)

        self.bounding_boxes = []
        self.confidences = []
        self.class_numbers = []

        for result in self.output_from_network:
            for detected_objects in result:
                self.scores = detected_objects[5:]
                self.class_current = np.argmax(self.scores)
                self.confidence_current = self.scores[self.class_current]

                if self.confidence_current > self.p:
                    self.box_current = detected_objects[0:4] * np.array([self.w, self.h, self.w, self.h])
                    self.x_center, self.y_center, self.box_width, self.box_height = self.box_current
                    self.x_min = int(self.x_center - (self.box_width / 2))
                    self.y_min = int(self.y_center - (self.box_height / 2))

                    self.bounding_boxes.append([self.x_min, self.y_min, int(self.box_width), int(self.box_height)])
                    self.confidences.append(float(self.confidence_current))
                    self.class_numbers.append(self.class_current)
        
        self.results = cv2.dnn.NMSBoxes(self.bounding_boxes, self.confidences,
                            self.p, self.t)

        if len(self.results)>0:

            for i in self.results.flatten():
                self.x_min, self.y_min = self.bounding_boxes[i][0], self.bounding_boxes[i][1]
                self.box_width, self.box_height = self.bounding_boxes[i][2], self.bounding_boxes[i][3]

                self.x_max = int(self.x_min + self.box_width)
                self.y_max = int(self.y_min + self.box_height)

                self.x = int(self.x_min+(self.box_width)/2)
                self.y = int(self.y_min+(self.box_height)/2)
                self.curCls = self.labels[int(self.class_numbers[i])]

                return frame,[[self.curCls,self.x_min,self.y_min,self.x_max,self.y_max,self.x,self.y]]

        else:

            return frame,[]



