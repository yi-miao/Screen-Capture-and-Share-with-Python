from flask import Flask, render_template, Response
import cv2
import mss
from PIL import Image
import numpy as np

app = Flask(__name__)

sct = mss.mss()
def gen_frames():
	while True:
		mon = sct.monitors[1]
		img = sct.grab(mon)
		img = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")

		frame = np.array(img)
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

		ret, buffer = cv2.imencode('.jpg', frame)
		frame = buffer.tobytes()
		yield (b'--frame\r\n'
			b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/video_feed')
def video_feed():
	return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
	return render_template('index.html')

app.run(host="0.0.0.0", port=5000)