import cv2


def read_video(path):
    capture = cv2.VideoCapture(path)
    counter = 0

    try:
        while(capture.isOpened()):
            ret,frame = capture.read()
            if ret == True:
                cv2.imwrite('frames/{}.png'.format(str(counter)),frame)
                counter += 1

                if(counter == 1000):
                    break
            else:
                break
    except:
        print("Can't open video file!")