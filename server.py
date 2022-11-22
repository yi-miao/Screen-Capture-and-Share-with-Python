import socket
import cv2
import threading
import pickle, struct

host = "192.168.0.219"
port = 5000
packet_size = 4096

def Streaming(name, sock):
	data = b""
	payload_size = struct.calcsize("Q")
	while True:
		try:
			while len(data) < payload_size:
				packet = sock.recv(packet_size)
				if not packet: break
				data += packet

			packed_msg_size = data[:payload_size]
			data = data[payload_size:]
			msg_size = struct.unpack("Q",packed_msg_size)[0]
	
			while len(data) < msg_size:
				data += sock.recv(packet_size)
			frame_data = data[:msg_size]
			data = data[msg_size:]

			frame = pickle.loads(frame_data)
			cv2.imshow("Streaming ",frame)
			cv2.waitKey(1)
		except:
			cv2.destroyAllWindows()
			sock.close()
			break

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)
print("Listening at", (host, port))

while True:
	client, addr = server.accept()
	print('Connected from :', addr)
	t = threading.Thread(target = Streaming, args = ("Streaming", client))
	t.start()

server.close()
cv2.destroyAllWindows()