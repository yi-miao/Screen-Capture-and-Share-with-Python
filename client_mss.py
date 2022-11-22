import socket
import cv2
import pickle, struct
from pynput import keyboard
from pynput.keyboard import Key
import mss
from PIL import Image
import numpy as np

k=Key.enter

def on_press(key):
    global k
    k=key

listener = keyboard.Listener(
	on_press=on_press)
listener.start()

host = "192.168.0.219"
port = 5000
window_size = (480, 480)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))
sct = mss.mss()
while True:
	mon = sct.monitors[1]
	img = sct.grab(mon)
	img = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")

	frame = np.array(img)
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	frame = cv2.resize(frame, window_size)

	a = pickle.dumps(frame)
	message = struct.pack("Q",len(a))+a
	client.sendall(message)
	if k==Key.esc:
		break

client.close()
listener.stop()

