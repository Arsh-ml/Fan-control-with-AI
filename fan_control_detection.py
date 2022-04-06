# importing libraries
import cv2
import mediapipe as mp
import serial

# Data to be sent to Arduino via Serial Communication
serialData = serial.Serial("COM3", 115200)


# Initializing the camera
width = 1280
height = 720

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))


# Objects of corresponding classes
findFace = mp.solutions.face_detection.FaceDetection()
drawFace = mp.solutions.drawing_utils


while True:
    _, frame = cam.read()

    # Converting the frame read by openCV to RGB as mediapipe operates in RGB and not BGR like OpenCV
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    results = findFace.process(frameRGB) # finding faces in the frame

    if results.detections != None:
        
        person = "present" + "\r"  # Defining value to be sent to arduino

        # Iterating over the faces one-by-one founded
        for face in results.detections:
            boundBox = face.location_data.relative_bounding_box

            topLeft = (int(boundBox.xmin * width), int(boundBox.ymin * height))
            bottomRight = (int((boundBox.xmin + boundBox.width) * width), int((boundBox.ymin + boundBox.height) * height))

            cv2.rectangle(frame, topLeft, bottomRight, (255, 0, 0), 2) # Creating a bounding box on the frame
 
    if results.detections == None:
        person = "absent" + "\r"
    
    serialData.write(person.encode()) # Writing data to Serial

    cv2.imshow("my WebCam", frame)
    cv2.moveWindow("my WebCam", 0, 0)

    if cv2.waitKey(1) & 0xff == ord("q"):
        break

cam.release()