import cv2 as cv

data_path = 'data/'

right_ear_cascade = cv.CascadeClassifier(
    data_path + 'haarcascade_mcs_rightear.xml')

left_ear_cascade = cv.CascadeClassifier(
    data_path + 'haarcascade_mcs_leftear.xml')

if right_ear_cascade.empty():
    raise IOError('Unable to load the right ear cascade classifier xml file')

if left_ear_cascade.empty():
    raise IOError('Unable to load the left ear cascade classifier xml file')

img = cv.imread(data_path + '1.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

green = (100, 170, 40)
blue = (170, 40, 40)

# http://answers.opencv.org/question/10654/how-does-the-parameter-scalefactor-in-detectmultiscale-affect-face-detection/
scale_factor = 1.05
# https://stackoverflow.com/questions/22249579/opencv-detectmultiscale-minneighbors-parameter
min_neighbors = 10

right_ears = right_ear_cascade.detectMultiScale(gray, scale_factor, min_neighbors)
for (x, y, w, h) in right_ears:
    cv.rectangle(img, (x, y), (x + w, y + h), green, 1)

left_ears = left_ear_cascade.detectMultiScale(gray, scale_factor, min_neighbors)
for (x, y, w, h) in left_ears:
    cv.rectangle(img, (x, y), (x + w, y + h), blue, 1)

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()
