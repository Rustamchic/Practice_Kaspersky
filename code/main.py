import cv2 as cv
import numpy as np





if __name__ == '__main__':
    cv.namedWindow( "result" )
    cap = cv.VideoCapture(0)

    hsv_min = np.array((90, 55, 10), np.uint8)
    hsv_max = np.array((132, 255, 255), np.uint8)

    color_blue = (255,0,0)
    color_red = (0,0,128)

    while True:
        flag, img = cap.read()
        img = cv.flip(img,1)
        try:


            hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV )
            thresh = cv.inRange(hsv, hsv_min, hsv_max)
            contours, hierarchy = cv.findContours( thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

            for cnt in contours:
                rect = cv.minAreaRect(cnt)
                box = cv.boxPoints(rect)
                box = np.int0(box)
                center = (int(rect[0][0]),int(rect[0][1]))
                area = int(rect[1][0]*rect[1][1])
                if area > 1000:
                    cv.drawContours(img,[box],0,color_blue,2)
                    cv.circle(img, center, 2, color_red, 2)
                    text = "(" + str(center[0]) + ", " + str(center[1]) + ")"
                    cv.putText(img, text, (center[0] + 10, center[1] + 10), cv.FONT_HERSHEY_PLAIN, 1.5, color_red, 1, 8, 0)
                    print(center)
            cv.imshow('result', img)
        except:
            cap.release()
            raise
        ch = cv.waitKey(5)
        if ch == 27:
            break

    cap.release()
    cv.destroyAllWindows()
