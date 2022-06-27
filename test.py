import cv2 as cv
import numpy as np
import sys

import cv2 as cv
import numpy as np

img = cv.imread("derp.jpg")
roi = img[10:100,150:299]

cv.imshow ("twa",roi)
cv.waitKey(0)
cv.destroyAllWindows()

