import cv2
import time
import os
import HandTrackingModule as htm

#height and width of screen
wCam, hCam = 640, 480

#turn on webcam
cap = cv2.VideoCapture(0)

#screen size
cap.set(3,wCam)
cap.set(4,hCam)

#store images
folderPath = "Hands" #folder path
myList = os.listdir(folderPath) #give os directory

#fps previous time
pTime = 0

#import list of images and create paths
overlayList = []
for imPath in myList:
    #read the given path
    image = cv2.imread(f'{folderPath}/{imPath}')
    #save images
    overlayList.append(image)

#object from handtracker #change detection confidence
detector = htm.handDetector(detectionCon=0.8)

while True:
    success, img = cap.read()

    #find hand and give it an image and return the drawn image
    img = detector.findHands(img)

    #find position of fingers
    lmList = detector.findPostion(img, draw=False)

    #if there is a point / finger present
    if len(lmList) != 0:
        #check mediapipe hand landscape image
        if lmList[8][2] < lmList[6][2]:
            print("index")
        if lmList[12][2] < lmList[10][2]:
            print("middle")
        if lmList[16][2] < lmList[14][2]:
            print("ring")
        if lmList[20][2] < lmList[18][2]:
            print("pinky")
        if lmList[4][2] < lmList[2][2]:
            print("thumb")
        # if lmList[8][2] < lmList[6][2]:
        #
        # if lmList[8][2] < lmList[6][2]:
        #
        # if lmList[8][2] < lmList[6][2]:
        #
        # if lmList[8][2] < lmList[6][2]:
        #
        # if lmList[8][2] < lmList[6][2]:

    #display image of any size
    h,w,c = overlayList[0].shape

    #slice display to put image
    img[0:h,0:w] = overlayList[0]

    # create framerate
    cTime = time.time()  # get current time
    fps = 1 / (cTime - pTime)  # formula to get fps
    pTime = cTime  # change previous time to current time

    # display fps
    cv2.putText(img, f'FPS: {int(fps)}', (500, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)

    # show the image
    cv2.imshow("img", img)

    # delay for one millisecond
    cv2.waitKey(1)