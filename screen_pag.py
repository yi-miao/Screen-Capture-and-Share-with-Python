import pyautogui
import numpy as np
import cv2

window_size = (640, 640)

# img = pyautogui.screenshot()	# full screen
img = pyautogui.screenshot(region=(0, 0, 640, 640))	# part of screen

frame = np.array(img)
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# frame = cv2.resize(frame, window_size)	# display window
cv2.imshow('Screenshot', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()