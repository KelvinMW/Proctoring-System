#To detect The face and start video recorrding
import io
import picamera
import cv2
import numpy
from Proctoring import *

def FaceR():
	
	#Create a memory stream so photos doesn't need to be saved in a file
	stream = io.BytesIO()

	#Get the picture (low resolution, so it should be quite fast)
	#Here you can also specify other parameters (e.g.:rotate the image)
	with picamera.PiCamera() as camera:
	    camera.resolution = (320, 240)
	    camera.capture(stream, format='jpeg')

	#Convert the picture into a numpy array
	buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)

	#Now creates an OpenCV image
	image = cv2.imdecode(buff, 1)

	#Load a cascade file for detecting faces
	face_cascade = cv2.CascadeClassifier('face.xml')

	#Convert to grayscale
	gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

	#Look for faces in the image using the loaded cascade file
	faces = face_cascade.detectMultiScale(gray, 1.1, 5)

	print "Found "+str(len(faces))+" face(s)"

	#Draw a rectangle around every found face
	for (x,y,w,h) in faces:
	    cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)

	#Start Video Recording
	with picamera.PiCamera() as camera:
		print("Exam Recording Started.......")
		ExamSession_Video_name = currentTime.strftime("%Y. %m. %d%H%M%S")
		camera.start_recording(Exam_video_Path+ExamSession_Video_name)
		sleep(exam_hrs)
		camera.stop_recording
		#convert the file format to MP4 [using call import]
		ConvertCommand = "MP4Box -add *.H264 converted video.mp4"
		call([ConvertCommand], shell=True )
		return ExamSession_Video_name
