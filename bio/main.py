import os, re
import cv2 as cv

from bio.detection import detect

green = (100, 170, 40)
blue = (170, 40, 40)


def run(data_path):
    ear_data_path = data_path + '/ucho/'
    pattern = r"\w*\.BMP"

    files = ['04-4.BMP', '72-4.BMP']

    # files = os.listdir(ear_data_path)
    for entry in files:
        if re.search(pattern, entry, re.IGNORECASE):
            ear = detect(ear_data_path + entry)
            show(ear_data_path + entry, ear)


def show(img_path, ear):
    img = cv.imread(img_path)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    ears = [ear]

    for (x, y, w, h) in ears:
        cv.rectangle(img, (x, y), (x + w, y + h), green, 1)

    cv.imshow(img_path, img)
    cv.waitKey(0)
    cv.destroyAllWindows()



# def show(img_path, ears):
#     img = cv.imread(img_path)
#     gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#
#     for (x, y, w, h) in ears['right']:
#         cv.rectangle(img, (x, y), (x + w, y + h), green, 1)
#
#     for (x, y, w, h) in ears['left']:
#         cv.rectangle(img, (x, y), (x + w, y + h), blue, 1)
#
#     cv.imshow('img', img)
#     cv.waitKey(0)
#     cv.destroyAllWindows()
