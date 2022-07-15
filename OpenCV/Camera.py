import colors
import cv2 as cv
import numpy as np
import operator



def write_cords(center):
    file = open("C:/Users/Admin/source/cords.txt", "a")
    file.write(str(center) + '\n')
    file.close()

def hist(img): #Функция определения цвета по заданной гистограмме
    for i in colors.flags:

        test1 = cv.imread(i)

        basehsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        test1hsv = cv.cvtColor(test1, cv.COLOR_BGR2HSV)

        histbase = cv.calcHist(basehsv, [0, 1], None, [180, 256], colors.ranges)
        cv.normalize(histbase, histbase, 0, 255, cv.NORM_MINMAX)

        histtest1 = cv.calcHist(test1hsv, [0, 1], None, [180, 256], colors.ranges)
        cv.normalize(histtest1, histtest1, 0, 255, cv.NORM_MINMAX)

        comHist = cv.compareHist(histbase, histtest1, 3)
        valueCompare.append(comHist)
        picDict = {"comhist": comHist, "name": i}
        list_of_pics.append(picDict)

    newlist = sorted(list_of_pics, key=operator.itemgetter('comhist'))
    matched_image = newlist[0]['name']
    return matched_image

def threshold(img, hsv_min, hsv_max):
    basehsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    thresh = cv.inRange(basehsv, hsv_min, hsv_max)
    contours, hirearchy = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    return contours

def rectangle(cnt):
    rect = cv.minAreaRect(cnt)
    box = cv.boxPoints(rect)
    box = np.int0(box)
    center = (int(rect[0][0]), int(rect[0][1]))
    area = int(rect[1][0]*rect[1][1])
    #write_cords(center) #Сильно замедляет работу приложения
    return center, area, box

def cords(img, box, center, matched_image):

    cv.drawContours(img, [box], 0, colors.color_blue, 2)
    cv.circle(img, center, 2, colors.color_red, 2)
    text = "(" + str(center[0]) + ", " + str(center[1]) + ")" + matched_image
    cv.putText(img, text, (center[0] + 10, center[1] + 10), cv.FONT_HERSHEY_PLAIN, 1.5, colors.color_red, 1)




if __name__ == '__main__':

    list_of_pics = []
    valueCompare = []

    cv.namedWindow("result")
    cap = cv.VideoCapture(0)

    while True:
        flag, img = cap.read()
        img = cv.flip(img, 1)
        try:

            matched_image = hist(img)
            blue = threshold(img, colors.blue_min, colors.blue_max)
            red = threshold(img, colors.red_min, colors.red_max)
            yellow = threshold(img, colors.yellow_min, colors.yellow_max)
            green = threshold(img, colors.green_min, colors.green_max)

            for cnt_b in blue:
                center, area, box = rectangle(cnt_b)
                if area > 1000:
                    cords(img, box, center, matched_image)

            for cnt_r in red:
                center, area, box = rectangle(cnt_r)

                if area > 1000:
                    cords(img, box, center, matched_image)

            for cnt_y in yellow:
                center, area, box = rectangle(cnt_y)

                if area > 1000:
                    cords(img, box, center, matched_image)

            for cnt_g in green:
                center, area, box = rectangle(cnt_g)

                if area > 1000:
                    cords(img, box, center, matched_image)

            cv.imshow('result', img)

        except:
            cap.release()
            raise
        ch = cv.waitKey(5)
        if ch == 27:
            break

    cap.release()
    cv.destroyAllWindows()