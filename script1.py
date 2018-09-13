import cv2, time
from datetime import datetime as dt
import pandas

first_frame=None
status_list=[None, None]
times=[]
df=pandas.DataFrame(columns=["Start","End"])

video=cv2.VideoCapture(0)#Also movie.mp4 can be passed

while True:
    check, frame = video.read()
    status=0
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame=gray
        continue

    delta_frame=cv2.absdiff(first_frame,gray)

    thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_frame,None, iterations=2)

    (__,cnts,___)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 3000:
            continue
        status=1
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)

    status_list.append(status)

    status_list=status_list[-2:]

    if status_list[-1]==1 and status_list[-2]==0:
        times.append(dt.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(dt.now())

    #cv2.imshow("Gray Frame",gray)
    #cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Threshold Frame",thresh_frame)
    cv2.imshow("Frame",frame)

    key=cv2.waitKey(1)

    if key==ord('q'):
        if status==1:
            times.append(dt.now())
        break

    print(status)

print(status_list)
print(times)

for i in range(0,len(times),2):
    df=df.append( {"Start":times[i],"End":times[i+1]} , ignore_index=True)

df.to_csv("Times_new.csv")

cv2.imshow("First",first_frame)
cv2.waitKey(2000)

video.release()
cv2.destroyAllWindows()
