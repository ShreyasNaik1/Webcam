from enum import Enum

class features(Enum):
    FACE = 1
    EYE = 2
    SMILE = 3
    FULLBODY = 4
    UPPERBODY = 5
    LOWERBODY = 6

recog_features = {}

recog_features[features.FACE] = './haarcascades/Orig/haarcascade_frontalface_default.xml'
recog_features[features.EYE] = './haarcascades/Orig/haarcascade_eye.xml'
recog_features[features.SMILE] = './haarcascades/Orig/haarcascade_smile.xml'
recog_features[features.FULLBODY] = './haarcascades/Orig/haarcascade_fullbody.xml'
recog_features[features.UPPERBODY] = './haarcascades/Orig/haarcascade_upperbody.xml'
recog_features[features.LOWERBODY] = './haarcascades/Orig/haarcascade_lowerbody.xml'
