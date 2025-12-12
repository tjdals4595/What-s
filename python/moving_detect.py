import cv2
import numpy as np
import os

class DetectMoving() :
    def __init__(self) :
        self.thr = 20
        self.difference = 40

    def read_images_with_extension(self, directory):
        image_list = []
        for filename in os.listdir(directory):
            if filename.endswith('.jpg'):
                image_path = os.path.join(directory, filename)
                if image_path is not None:
                    print(image_path)
                    image_list.append(image_path)
        return image_list

    def MoveingOfFrame(self, frame1, frame2, frame3):
        Frame = frame3.copy()

        frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        frame3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2GRAY)
        
        diff_12 = cv2.abs(frame1, frame2)
        diff_23 = cv2.abs(frame2, frame3)

        diff_12 = cv2.threshold(diff_12, self.thr, 255, cv2.THRESH_BINARY)[1]
        diff_23 = cv2.threshold(diff_23, self.thr, 255, cv2.THRESH_BINARY)[1]
        
        diff = cv2.bitwise_and(diff_12, diff_23)
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
        diff = cv2.morphologyEx(diff, cv2.MORPH_OPEN, kernel)
        
        diff_cnt = cv2.countNoneZero(diff)
        if diff_cnt > self.difference :
            signal = 1
            #self.visualize(Frame, diff)
        else :
            signal = 0

        frame1 = frame2
        frame2 = frame3

        return signal

    def visualize(self, frame, draw_array):
        Nonzero = np.nonzero(draw_array)
        cv2.rectangle(frame, (min(Nonzero[1]), min(Nonzero[0])), (max(Nonzero[1]), max(Nonzero[0])), (0,255,0), 4)
        cv2.imshow('show', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
