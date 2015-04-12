import numpy as np
import cv2


def clock():
    return cv2.getTickCount() / cv2.getTickFrequency()

def draw_str(dst, (x, y), s):
    # ex:         draw_str(vis, (20, 20), 'time: %.1f ms' % (dt*1000))
    cv2.putText(dst, s, (x+1, y+1), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 0), thickness = 2, lineType=cv2.CV_AA)
    cv2.putText(dst, s, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 255, 255), lineType=cv2.CV_AA)

def to_minutes(t):
    hours = t / 3600
    minutes = (t - (hours * 3600)) / 60
    secs = t - (hours * 3600) - (minutes * 60)
    return "%d-%d-%d" % (hours,minutes, secs)

def save_img_time(img, prefix, t):
    cv2.imwrite("/Users/anthonya/Downloads/frames/%s_%s.jpg" % (prefix, to_minutes(t)), img)

def diffImg(t0, t1, t2):
    d1 = cv2.absdiff(t2, t1)
    d2 = cv2.absdiff(t1, t0)
    return cv2.bitwise_and(d1, d2)


if __name__ == '__main__':

    cap = cv2.VideoCapture('/Users/anthonya/Downloads/set1.mov')
    winName = "Movement Indicator"

    # Read three images first:
    t_minus = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)
    t = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)

    while(cap.isOpened()):
        t_plus = cap.read()[1]

        dt = cap.get(0)
        sec = int(dt/1000)

        if sec % 30 == 0:
            #diffed = diffImg(t_minus, t, cv2.cvtColor(t_plus, cv2.COLOR_RGB2GRAY))
            #save_img_time(diffed, "motion", sec)
            save_img_time(t_plus, "frame", sec)

#        draw_str(frame, (20, 20), '%.1f' % sec)
#        cv2.imshow('frame',frame)

        # Read next image
        t_minus = t
        t = cv2.cvtColor(t_plus, cv2.COLOR_RGB2GRAY)
        t_plus =cap.read()[1]

    cap.release()
    cv2.destroyAllWindows()
