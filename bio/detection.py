import cv2 as cv
from scipy import ndimage

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
    # print(img_path)
    img = cv.imread(img_path)
    res = _detect(img)
    # TODO refactor
    # if len(res['left']) < 1 and len(res['right'] < 1):
    #     for angle in angles:
    #         rotated = ndimage.rotate(img, angle)
    #         res = _detect(rotated)
    #         if len(res['left']) >= 1 or len(res['right'] >= 1):
    #             return res

    return res


def _detect(img):
    preprocessed_img = preprocess(img)

    left_ears = right_ear_cascade.detectMultiScale(preprocessed_img, scale_factor, min_neighbors)
    right_ears = left_ear_cascade.detectMultiScale(preprocessed_img, scale_factor, min_neighbors)

    return {
        'left': left_ears,
        'right': right_ears
    }


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
