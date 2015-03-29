import numpy as np
import cv2


def clock():
    return cv2.getTickCount() / cv2.getTickFrequency()

def draw_str(dst, (x, y), s):
    cv2.putText(dst, s, (x+1, y+1), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 0), thickness = 2, lineType=cv2.CV_AA)
    cv2.putText(dst, s, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 255, 255), lineType=cv2.CV_AA)


if __name__ == '__main__':

    cap = cv2.VideoCapture('/Users/anthonya/Downloads/set2.mov')

    while(cap.isOpened()):
        ret, frame = cap.read()
        dt = cap.get(0)

        draw_str(frame, (20, 20), '%f' % (dt/1000))

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
