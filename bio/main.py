import os, re
import cv2 as cv

from bio.detection import detect


green = (100, 170, 40)
blue = (170, 40, 40)

def run(data_path):
    ear_data_path = data_path + '/ucho/'
    pattern = r"\w*\.BMP"

    for entry in os.listdir(ear_data_path):
        if re.search(pattern, entry, re.IGNORECASE):
            ears = detect(ear_data_path + entry)
            # print(ears)


# def show(img_path):
#     img = cv.imread(img_path)
#     gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#
#
#     for (x, y, w, h) in right_ears:
#         cv.rectangle(img, (x, y), (x + w, y + h), green, 1)
#
#     right_ears = left_ear_cascade.detectMultiScale(gray, scale_factor, min_neighbors)
#     for (x, y, w, h) in left_ears:
#         cv.rectangle(img, (x, y), (x + w, y + h), blue, 1)
#
#     cv.imshow('img', img)
#     cv.waitKey(0)
#     cv.destroyAllWindows()
