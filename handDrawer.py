import handTrackingModule
import cv2

cap = cv2.VideoCapture(0)
detector = handTrackingModule.handDetector(maxHands=1, detection_con=0.7, tracking_con=0.7)


def toolUsing(select, img):
    if select:
        # print(select)

        if (select[1] in list(range(10, 81))) and (select[0] in list(range(10, 91))):
            # print(True)
            cv2.rectangle(img, (10, 10), (90, 80), (0, 0, 0), -1)
            return (255, 105, 180)
        elif (select[1] in list(range(10, 81))) and (select[0] in list(range(190, 271))):
            cv2.rectangle(img, (190, 10), (270, 80), (0, 0, 0), -1)
            return (135, 206, 250)
        elif (select[1] in list(range(10, 81))) and (select[0] in list(range(370, 451))):
            cv2.rectangle(img, (370, 10), (450, 80), (0, 0, 0), -1)
            return (255, 0, 0)
        elif (select[1] in list(range(10, 81))) and (select[0] in list(range(550, 631))):
            cv2.rectangle(img, (550, 10), (630, 80), (255, 255, 255), -1)
            return (0, 0, 0)


def drawTools(img):
    cv2.rectangle(img, (0, 0), (640, 80), (255, 150, 20), -1)
    cv2.rectangle(img, (10, 10), (90, 80), (255, 105, 180), -1)
    cv2.rectangle(img, (190, 10), (270, 80), (135, 206, 250), -1)
    cv2.rectangle(img, (370, 10), (450, 80), (255, 0, 0), -1)
    cv2.rectangle(img, (550, 10), (630, 80), (0, 0, 0), -1)


def selector(l, img):
    x1 = l[8][1]
    y1 = l[8][2]
    x2 = l[12][1]
    y2 = l[12][2]
    dis = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
    center = (int((x1 + x2) / 2), int((y1 + y2) / 2))
    if dis < 40:
        cv2.circle(img, center, 20, (255, 255, 255), -1)
        return center


# imgCanvas = cv2.
while True:
    success, img = cap.read()
    cv2.namedWindow("Image", cv2.WINDOW_KEEPRATIO)
    detector.findHands(img)
    lmlist = detector.findPosition(img, draw=False)
    drawTools(img)
    if len(lmlist) != 0:
        tool = toolUsing(selector(lmlist, img), img)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
