import numpy 
import math
import cv2


def psnr(img1, img2):
    mse = numpy.mean( (img1 - img2) ** 2 )
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

original = cv2.imread("../datasets/cow/cow00001.png")
contrast = cv2.imread("../datasets/cow/cow00200.png")
#revantsMom =cv2.imread("")

print(psnr(original,original))
print(psnr(original,contrast))
#print(psnr(original,revantsMom))
