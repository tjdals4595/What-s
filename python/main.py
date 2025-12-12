import cv2
import numpy as np

from line_recognize import RecognizeLine
from object_detect import DetectObject
from moving_detect import DetectMoving
from send_img import SendImg


find_line = RecognizeLine()
find_object = DetectObject()
find_moving = DetectMoving()
send_img = SendImg()

def main(KEY):
    
    if func1 == KEY:   
        img = sendImg(1)
        
        #func1 line recogize
        edge = find_line.DectectEdge(img)
        mask = find_line.RegionOfInterest(edge)
        signal, img = find_line.HoughLines(mask, 2, np.pi/180, 90, 120, 150)
    
        #func1 object detect
        classesFile = "coco.names"
        classes = find_object.class_file(classesFile)
        modelWeights = "best.onnx"
        net = cv2.dnn.readNet(modelWeights)      
        detections = find_object.pre_process(img, net)
        img, label = find_object.post_process(img.copy(), detections, classes)

        return signal, label

    #func2 moving detect
    if func2 == KEY :
        frame1, frame2, frame3 = sendImg(3)
        signal = find_moving.MoveingOfFrame(frame1, frame2, frame3)
    
        return signal, str(0)
        
   
if __name__ == "__main__":
    #실행시키고자 하는 function을 key값으로 input
	#func1 : 원래 제안서에 있던 기능
    #func2 : 피드백을 기반으로 업데이트한 장애물 인식
    main(func2)
