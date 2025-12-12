import cv2
import numpy as np
import os

#reference
#https://learnopencv.com/object-detection-using-yolov5-and-opencv-dnn-in-c-and-python/

class DetectObject():
    def __init__(self) :
        # Constants.
        self.INPUT_WIDTH = 640
        self.INPUT_HEIGHT = 640
        self.SCORE_THRESHOLD = 0.2
        self.NMS_THRESHOLD = 0.2
        self.CONFIDENCE_THRESHOLD = 0.2
 
        # Text parameters.
        self.FONT_FACE = cv2.FONT_HERSHEY_SIMPLEX
        self.FONT_SCALE = 0.7
        self.THICKNESS = 1
 
        # Colors.
        self.BLACK  = (0,0,0)
        self.BLUE   = (255,178,50)
        self.YELLOW = (0,255,255)


    def class_file(self, classesFile) :
        classes = None
        with open(classesFile, 'rt') as f:
            classes = f.read().rstrip('\n').split('\n')
        return classes


    def draw_label(self, im, label, x, y):       
        text_size = cv2.getTextSize(label, self.FONT_FACE, self.FONT_SCALE, self.THICKNESS)
        dim, baseline = text_size[0], text_size[1]
        cv2.rectangle(im, (x,y), (x + dim[0], y + dim[1] + baseline), (0,0,0), cv2.FILLED);
        cv2.putText(im, label, (x, y + dim[1]), self.FONT_FACE, self.FONT_SCALE, self.YELLOW, self.THICKNESS, cv2.LINE_AA)


    def pre_process(self, input_image, net):
          blob = cv2.dnn.blobFromImage(input_image, 1/255,  (self.INPUT_WIDTH, self.INPUT_HEIGHT), [0,0,0], 1, crop=False)
          net.setInput(blob)
          outputs = net.forward(net.getUnconnectedOutLayersNames())

          return outputs


    def need_label(self, label) : #COCO DATASET 중 필요한 class만
        str_label = str(label)
        label_list = ['bus', 'bicycle', 'car', 'skateboard', 'sports ball', 'person', 'traffic light', 'truck']
        for element in label_list:
            if element == str_label:
                return label
        return None  # 만약 리스트에 일치하는 항목이 없으면 None 반환


    def check_direction_and_roi(self, image, x1, y1, weight, height):
        img_h, img_w = image.shape[:2]
        x2 = x1 + weight
        y2 = y1 + height

        if img_h//3 > y2 : #시야 내로 범위 제한, TODO
            return None

        return 1


    def post_process(self, input_image, outputs, classes):
        class_ids = []
        confidences = []
        boxes = []
        
        rows = outputs[0].shape[1]
        image_height, image_width = input_image.shape[:2]
        
        x_factor = image_width / self.INPUT_WIDTH
        y_factor =  image_height / self.INPUT_HEIGHT
        
        for r in range(rows):
            row = outputs[0][0][r]
            confidence = row[4]
            
            if confidence >= self.CONFIDENCE_THRESHOLD:
                classes_scores = row[5:]
                
                class_id = np.argmax(classes_scores)
               
                if (classes_scores[class_id] > self.SCORE_THRESHOLD):
                    confidences.append(confidence)
                    class_ids.append(class_id)
                    cx, cy, w, h = row[0], row[1], row[2], row[3]
                    left = int((cx - w/2) * x_factor)
                    top = int((cy - h/2) * y_factor)
                    width = int(w * x_factor)
                    height = int(h * y_factor)
                    box = np.array([left, top, width, height])
                    boxes.append(box)

        indices = cv2.dnn.NMSBoxes(boxes, confidences, self.CONFIDENCE_THRESHOLD, self.NMS_THRESHOLD)

        for i in indices:
            box = boxes[i]
            left = box[0] #x1
            top = box[1] #y1
            width = box[2] #x2 = width + left
            height = box[3] #y2 = height + top             
            
            label = classes[class_ids[i]]
            #label = "{}:{:.2f}".format(classes[class_ids[i]], confidences[i])             

            result = self.need_label(label)  #장애물에 해당이 된다면 class_id를 아니면 None
            
            ## visualize ##
            if result is not None :
                signal = self.check_direction_and_roi(input_image, left, top, width, height)
                if signal is not None :
                    cv2.rectangle(input_image, (left, top), (left + width, top + height), self.BLUE, 3*self.THICKNESS)
                    self.draw_label(input_image, result, left, top)

        return input_image, result      

            

        ## visualize ##
        #cv2.putText(input_image, label, (20, 40), self.FONT_FACE, self.FONT_SCALE,  (0, 0, 255), self.THICKNESS, cv2.LINE_AA)
        #cv2.imshow('Output', input_image)
        #cv2.waitKey(0)

        
