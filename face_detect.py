import cv2
from darkflow.net.build import TFNet
import numpy as np
import time

option={
	'model': 'cfg/tiny-yolo-voc-1c.cfg',
	'load' : 625,
	'threshold': 0.75,
}

tfnet= TFNet(option)

capture = cv2.VideoCapture(0)
k=0
while(True):
	stime=time.time()
	ret, frame=capture.read()
	results = tfnet.return_predict(frame)
	if ret:
		for result in results:
			conf=str(result['confidence'])
			tl=(result['topleft']['x'],result['topleft']['y'])
			br=(result['bottomright']['x'],result['bottomright']['y'])
			label = result['label']
			label_conf=label+','+conf
			frame=cv2.rectangle(frame,tl,br,(0,255,0),2)
			frame=cv2.putText(frame,label_conf,tl,cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
			roi_color=frame[result['topleft']['y']:result['bottomright']['y'], result['topleft']['x']:result['bottomright']['x']]

			cv2.imwrite('database\\my_img{:>05}.jpg'.format(k),roi_color)
			k+=1
		cv2.imshow('video',frame)
		if cv2.waitKey(1) & 0xFF==ord('q'):
			break
	else:
		capture.release()
		cv2.destroyAllWindows()
		break
