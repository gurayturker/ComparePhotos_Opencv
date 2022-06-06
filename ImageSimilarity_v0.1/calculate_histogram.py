import cv2
from skimage import io
# resize_img fonksiyonu ile gelen görsellerin boyutlarını
# belirlenen boyutlara göre eşitliyoruz.


def resize_img(image, size):
    return cv2.resize(image, size)

# calc_hist fonksiyonu görsellerin okunup renk ve boyut işlemlerini
# yaptıktan sonra histogramlarını hesaplamaktadır.


def calc_hist(img, size, url=False):
    if url:
        image = io.imread(img)
    else:
        image = cv2.imread(img)
    image = resize_img(image, size)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_hist = cv2.calcHist([image_gray], [0], None, [256], [0, 256])
    return image_hist
