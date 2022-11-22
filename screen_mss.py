import numpy as np
import cv2
import mss
from PIL import Image

window_size = (480, 480)
# mon = (0, 0, 480, 480)	# part of screen

sct = mss.mss()
mon = sct.monitors[1]	# full screen
img = sct.grab(mon)
img = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")

frame = np.array(img)
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
frame = cv2.resize(frame, window_size)	# display window size
cv2.imshow('Screenshot', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
