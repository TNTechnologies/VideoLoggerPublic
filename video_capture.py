import cv2
import datetime



vid_cap = cv2.VideoCapture(0)

vid_cod = cv2.VideoWriter_fourcc(*'XVID')

output = cv2.VideoWriter("cam_video.mp4", vid_cod, 20.0, (640,480))

while(True):

    ret,frame = vid_cap.read()
    cv2.imshow("My cam video", frame)
    output.write(frame)

    if cv2.waitKey(1) &0XFF == ord('x'):
        break

vid_cap.release()
output.release()
cv2.destroyAllWindows()
