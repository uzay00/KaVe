from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths


import numpy as np

import argparse
import imutils
import cv2
import sys
import os
import threading
import time

run = False

def sesCal(dosya):
	global run
	os.system('aplay '+ dosya +'.wav')
	time.sleep(3)
	run = False
	

camera = cv2.VideoCapture(0)

while True:
	ret, image = camera.read()
	image = imutils.resize(image, width=300)

	image = cv2.cvtColor(image, cv2.COLOR_RGB2HLS)

	lower = np.uint8([90, 20,   50])
	upper = np.uint8([100, 170, 200])
	yellow_mask = cv2.inRange(image, lower, upper)
	yellow = cv2.bitwise_and(image, image, mask = yellow_mask)
	yellow = cv2.cvtColor(yellow, cv2.COLOR_BGR2GRAY)

	blur = cv2.GaussianBlur(yellow,(5,5),0)

	ret,th1 = cv2.threshold(yellow,35,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	ret1,th2 = cv2.threshold(th1,127,255,cv2.THRESH_TOZERO)
	
	_, contours, hierarchy = cv2.findContours(th2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	image = cv2.cvtColor(image, cv2.COLOR_HLS2RGB)

	if len(contours)>0:
		c = max(contours, key=cv2.contourArea)
		M = cv2.moments(c)
		area = cv2.contourArea(c)
		if area > 2000:
			cx = int(M['m10']/M['m00'])
			cy = int(M['m01']/M['m00'])
			

			cv2.line(image,(cx,0),(cx,720),(255,0,0),1)
			cv2.line(image,(0,cy),(1280,cy),(255,0,0),1)

			cv2.circle(image,(cx,cy), 3, (0,0,255), -1)
			cv2.drawContours(image, contours, -1, (0,255,0), 2)

			if cx < 100:
				print('sol')
				if not run:
					run = True
					threading.Thread(target=sesCal, args=("sol", )).start()

			elif cx > 200:
				print('sag')
				if not run:
					run = True
					threading.Thread(target=sesCal, args=("sag", )).start()
			else:
				print('duz git')

	
	cv2.imshow("input", image)
	key = cv2.waitKey(10)
	if key == 27:
		break
	
cv2.destroyAllWindows()
cv2.VideoCapture(0).release()

