import cv2 as cv
from scipy import ndimage


# 10% gain to width and height
boundary_gain = 0.2

# http://answers.opencv.org/question/10654/how-does-the-parameter-scalefactor-in-detectmultiscale-affect-face-detection/
scale_factor = 1.05
# https://stackoverflow.com/questions/22249579/opencv-detectmultiscale-minneighbors-parameter
min_neighbors = 10

angles = [-15, 15]

data_path = 'data/'

# right_ear_cascade - left ear from person being ear detected, left_ear_cascade - right ...
right_ear_cascade = cv.CascadeClassifier(
    data_path + 'haarcascade_mcs_rightear.xml')
left_ear_cascade = cv.CascadeClassifier(
    data_path + 'haarcascade_mcs_leftear.xml')

if right_ear_cascade.empty():
    raise IOError('Unable to load the right ear cascade classifier xml file')
if left_ear_cascade.empty():
    raise IOError('Unable to load the left ear cascade classifier xml file')


def detect(img_path):
    print(img_path)
    img = cv.imread(img_path)
    detected = _detect(img)
    biggest = selectBigestBoundary(detected)
    enlarged = enlargeBoundary(biggest)

    res = enlarged
    return res


def _detect(img):
    preprocessed_img = preprocess(img)

    left_ears = right_ear_cascade.detectMultiScale(preprocessed_img, scale_factor, min_neighbors)
    right_ears = left_ear_cascade.detectMultiScale(preprocessed_img, scale_factor, min_neighbors)

    return {
        'left': left_ears,
        'right': right_ears
    }


# 04-4, 72-4 detected left and right ear (see screenshots)
# solution
def selectBigestBoundary(ears):
    cooridnates = []
    [cooridnates.append(crd) for crd in ears['left']]
    [cooridnates.append(crd) for crd in ears['right']]

    area = []
    #  (x, y, w, h)
    [area.append(crd[2]*crd[3]) for crd in cooridnates]

    max_surface = max(area)
    max_index = area.index(max_surface)

    return cooridnates[max_index]


# run detection on rotatet input images againt till ear is not found
def rotate():
    pass


# convert to graysclae, use gausian filter to remove fine details not necessary for detection
# try CLAHE
# https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_histograms/py_histogram_equalization/py_histogram_equalization.html#py-histogram-equalization
def preprocess(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    equ = cv.equalizeHist(gray)
    return equ


def enlargeBoundary(cords):
    (x, y, w, h) = cords

    w_gain = int(round(w * boundary_gain))
    h_gain = int(round(h * boundary_gain))
    # w_gain = 0
    # h_gain = 0

    # if x is less than ... then max(0,.. helps
    x = max(0, int(round(x - w_gain / 2)))
    y = max(0, int(round(y - h_gain / 2)))
    w = w + w_gain
    h = h + h_gain

    return [x, y, w, h]


def rotate():
    # if len(res['left']) < 1 and len(res['right'] < 1):
    #     for angle in angles:
    #         rotated = ndimage.rotate(img, angle)
    #         res = _detect(rotated)
    #         if len(res['left']) >= 1 or len(res['right'] >= 1):
    #             return res
    pass



