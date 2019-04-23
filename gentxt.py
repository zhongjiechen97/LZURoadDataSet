
import os

from os import listdir, getcwd

from os.path import join

def listdirInMac(path):
    os_list = os.listdir(path)
    for item in os_list:
        if item.startswith('.') and os.path.isfile(os.path.join(path, item)):
            os_list.remove(item)
    return os_list

if __name__ == '__main__':

    source_folder='/Users/chenzhj/Desktop/YOLOV3/darknet/scripts/VOCdevkit/VOC2018/JPEGImages/'

    dest='/Users/chenzhj/Desktop/YOLOV3/darknet/scripts/VOCdevkit/VOC2018/ImageSets/Main/train.txt'

    dest2='/Users/chenzhj/Desktop/YOLOV3/darknet/scripts/VOCdevkit/VOC2018/ImageSets/Main/val.txt'

    file_list=listdirInMac(source_folder)
    train_file=open(dest,'a')

    val_file=open(dest2,'a')

    for file_obj in file_list:

        file_path=os.path.join(source_folder,file_obj)

 
        file_name,file_extend=os.path.splitext(file_obj)
        file_num=int(file_name[5:])
        if(file_num<50):

 
            train_file.write(file_name+'\n')

        else :

            val_file.write(file_name+'\n')

    train_file.close()

    val_file.close()