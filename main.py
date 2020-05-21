# Author: Thuan Nguyen
# GitHub: https://github.com/Thuan2000/voc2012-test
# License: MIT
# Creation Date: 21/05/2020
# Description: This code is written to test the architectural workings of uNet.


from tf_unet import unet

if __name__ == "__main__":

    train_txt_file = open("./VOC2012/ImageSets/Segmentation/train.txt", "r")
    train_images = train_txt_file.readlines() # <list>

    