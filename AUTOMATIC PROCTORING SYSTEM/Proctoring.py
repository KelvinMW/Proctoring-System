#This is an auto proctoring system for a RaspBerryPi
#...................................................#
#Packeges to be installed in the RaspBerryPi
#
#
#..................................................#
import RPi.GPIO as GPIO
import picamera
from time import sleep
from datetime import datetime
from subprocess import call
from FaceRecognition import *

#Media Storage Location
SpicturePath="/home/user/Desktop/PYTHON/AUTOMATIC PROCTORING SYSTEM/Media/Student_Image"
IDpicturePath="/home/user/Desktop/PYTHON/AUTOMATIC PROCTORING SYSTEM/Media/ID_Image"
Env_Video_Path="/home/user/Desktop/PYTHON/AUTOMATIC PROCTORING SYSTEM/Media/Environment"
Exam_video_Path="/home/user/Desktop/PYTHON/AUTOMATIC PROCTORING SYSTEM/Media/Exam"
#Timestamp for naming the files
def getTime():
	currentTime = datetime.now()
	return currentTime

#Capture student image
def CaptureStudentImage(SpicturePath, currentTime):
	print ("Taking a picture, Look at the camera : ")
	with picamera.PiCamera() as camera:
		camera.resolution = (1024, 768)
		S_Image_name = currentTime.strftime("%Y. %m. %d%H%M%S")+'.jpg'
		camera.capture = (SpicturePath+S_Image_name)
		return ID_Image_name
#Student ID
def CaptureStudentID(picturePath, currentTime):
	print ("Take picture of Your Student ID card: ")
	with picamera.PiCamera() as camera:
		camera.resolution = (1024, 768)
		ID_Image_name = currentTime.strftime("%Y. %m. %d%H%M%S")+'.jpg'
		camera.capture = (picturePath+ID_Image_name)
		return ID_Image_name

#Start Video Recording For The Environment

def RecordEnvironment(Env_Video_Path, currentTime):
	print(".....................ENVIRONMENT VIDEO RECORDING..............")
	with picamera.PiCamera() as camera:
		Env_Video_name = currentTime.strftime("%Y. %m. %d%H%M%S")
		camera.start_recording(Env_Video_Path+Env_Video_name)
		sleep(100)
		camera.stop_recording
		#convert the file format to MP4 [using call import]
		ConvertCommand = "MP4Box -add *.H264 converted video.mp4"
		call([ConvertCommand], shell=True )

#Start Video Recording For The Exam After Detecting Face
def RecordExamSession():
	#Face Recogntion ---+ START RECORDING----
	FaceRecognition.FaceR()
	
#LEDs
#Step 1 For Student Image Capture
GPIO.setmode(GPIO.BCM)
SlightPin= 1
buttonPin= 17
GPIO.setup(SlightPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN pull_up_down=GPIO.PUD_UP)
try:
	while True:
		GPIO.output(SlightPin, GPIO.input(buttonPin))
		print("Face the Camera for picture:")
		CaptureStudentImage()
finally:
	GPIO.output(SlightPin,False)
	GPIO.cleanup()

#Step 2 For Student ID Capture
IDlightPin= 2
buttonPin= 17
GPIO.setup(IDlightPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN pull_up_down=GPIO.PUD_UP)
try:
	while True:
		GPIO.output(IDlightPin, GPIO.input(buttonPin))
		print("Take a picture of your Student ID card :")
		CaptureStudentID()
finally:
	GPIO.output(IDlightPin,False)
	GPIO.cleanup()

#Step 3 Recording the Environment
EnvlightPin= 3
buttonPin= 17
GPIO.setup(EnvlightPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN pull_up_down=GPIO.PUD_UP)
try:
	while True:
		GPIO.output(EnvlightPin, GPIO.input(buttonPin))
		print("Record The surrounding envronment where you will do the exam :")
		RecordEnvironment()
finally:
	GPIO.output(EnvlightPin,False)
	GPIO.cleanup()

#Step 5 Face Recognition
FacelightPin= 4
buttonPin= 17
GPIO.setup(FacelightPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN pull_up_down=GPIO.PUD_UP)
try:
	while True:
		GPIO.output(FacelightPin, GPIO.input(buttonPin))
		print("Detecting Face........Look at the camera: ")
		FaceR()
finally:
	GPIO.output(FacelightPin,False)
	GPIO.cleanup()
#Step 6 Start Exam Recording(if face detected)
FacelightPin= 4
buttonPin= 17
GPIO.setup(FacelightPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN pull_up_down=GPIO.PUD_UP)
try:
	while True:
		GPIO.output(FacelightPin, GPIO.input(buttonPin))
		print("Detecting Face........Look at the camera: ")
		RecordExamSession()
finally:
	GPIO.output(FacelightPin,False)
	GPIO.cleanup()


print("END OF EXAM")
#Stop Recording




