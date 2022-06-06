from calculate_histogram import calc_hist
import numpy as np


def compare_imgs(target_img, img_list, size=(100, 100)):
    # Target image  için histogram hesaplamaktadır
    target_hist = calc_hist(target_img, size)
    dict_image_hist = dict()
    for i in img_list:
        # Karşılaştırılacak görsellerin her biri için
        # historgramları hesaplamaktadır.
        img_hist = calc_hist(i, size, True)
        # Hedef görsel ile diğer görsellerin histogramlarına
        # göre cosinus benzenzerliğini hesaplanmaktadır.
        dot = np.dot(target_hist.T[0], img_hist.T[0])
        norm_target = np.linalg.norm(target_hist.T[0])
        norm_img = np.linalg.norm(img_hist.T[0])
        cos_sim = dot/(norm_target*norm_img)
        # Hesaplamanın sonuçları key : value   yani path : score
        # olacak şekilde bir sözlük yapısında saklanmaktadır.
        dict_image_hist[i] = cos_sim
    # dict_image_hist adlı sözlükten score değeri en yüksek olan
    # itemi path : score olacak şekilde outuput alıyoruz.
    closest = [k for k, v in dict_image_hist.items() if v == max(dict_image_hist.values())]
    print(closest[0] + " : " + str(dict_image_hist[closest[0]]))
