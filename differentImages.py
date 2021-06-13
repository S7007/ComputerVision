import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('lena.jpg',cv2.IMREAD_GRAYSCALE)
lap =cv2.Laplacian(img, cv2.CV_64F,ksize=3)
lap = np.uint8(np.absolute (lap))
sobelX =cv2.Sobel(img,cv2.CV_64F,1,0)
sobelY =cv2.Sobel(img,cv2.CV_64F,0,1)
edges = cv2.Canny(img,100,200)

sobelX=np.uint8(np.absolute (sobelX))
sobelY=np.uint8(np.absolute (sobelY))

sobelCobined = cv2.bitwise_or(sobelX,sobelY)

title = ['image','Laplacian','sobelX','sobelY','sobelCobined','Canny']
images = [img,lap,sobelX,sobelY,sobelCobined,edges]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])

plt.show()
