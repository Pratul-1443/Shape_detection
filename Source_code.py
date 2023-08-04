import cv2
img = cv2.imread("shape.jpg")
imgray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

# to find the thresh max and min valuse use trackbar

_, thresh = cv2.threshold(imgray, 226, 255, cv2.THRESH_BINARY)

#For finding the Contours of all image

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#print(len(contours))

for i in contours:
    a = cv2.approxPolyDP(i, 0.01 * cv2.arcLength(i, True), True)
    cv2.drawContours(img, [a], 0, (0, 255, 0), 2)
    x=a.ravel()[0]
    y=a.ravel()[1]-10
    if len(a) == 3:
        cv2.putText(img,"Triange",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,5))
    elif len(a) == 4:
        x1,y1,w,h=cv2.boundingRect(a)
        aspectRatio=float(w)/h
        if aspectRatio >=1 and  aspectRatio<=1:
            print("")
            cv2.putText(img,"square",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,5))
        else:
            cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 5))
    elif len(a) == 5:
        cv2.putText(img,"pentgon",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,5))
    else:
        cv2.putText(img,"circle",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,5))


cv2.imshow("frame", img)
cv2.waitKey(0)
