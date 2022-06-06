from compare_imgs import compare_imgs


class CompareImages:
    # args yapısı istediğimiz kadar parametre almak için kullanılmaktadır.
    def __init__(self, args):
        # args[1] ile alınan birinci parametrenin
        # target image olduğunu belirmektedir.
        self.target_image = args[1]
        # Birinci parametreden sonraki parametreler oluşturulan
        # boş listeye eklemektedir.
        self.other_images = []
        for i in range(2, len(args)):
            self.other_images.append(args[i])

    def main(self):
        # Oluşturulan parametreler hesaplamaların yapılacağı
        # fonksiyona göndermektedir.
        compare_imgs(target_img=self.target_image, img_list=self.other_images)
