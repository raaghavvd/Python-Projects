import cv2, time

video= cv2.VideoCapture(0)

while True:


    check, frame = video.read()

    print(check)
    print(frame)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capture",gray)
    key=cv2.waitKey(1) #waits for 1 ms to show next frame
    if key==ord('q'): #if 'q' is pressed the video is stopped
        break

video.release()
cv2.destroyAllWindows()
