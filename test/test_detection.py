import os, re
from bio.detection import detect

data_path = 'test/data/'


def test_no_ear():
    ear = detect(data_path + 'noear.jpg')

    assert len(ear['left']) <= 0 and len(ear['left']) <= 0, \
        'Detection not working propertly'


def test_detect_in_all_images():
    ear_data_path = 'data/ucho/'
    pattern = r"\w*\.BMP"

    not_detected = []

    for file in os.listdir(ear_data_path):
        if re.search(pattern, file, re.IGNORECASE):
            path = ear_data_path + file
            ear = detect(path)
            if len(ear['left']) < 1 and len(ear['right']) < 1:
                not_detected.append(path)

    assert len(not_detected) < 1, \
        'Not all inputs were detected:\n'+str(not_detected)
