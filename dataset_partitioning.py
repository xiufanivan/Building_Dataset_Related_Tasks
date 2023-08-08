import os
import random
import shutil


def moveimg(fileDir, tarDir):
    pathDir = os.listdir(fileDir)  # 取图片的原始路径
    filenumber = len(pathDir)
    rate = 0.3  # 自定义抽取图片的比例，比方说100张抽10张，那就是0.1
    picknumber = int(filenumber * rate)  # 按照rate比例从文件夹中取一定数量图片
    sample = random.sample(pathDir, picknumber)  # 随机选取picknumber数量的样本图片
    print(sample)
    for name in sample:
        shutil.move(fileDir + name, tarDir + "\\" + name)
    return


def movelabel(file_list, file_label_train, file_label_val):
    for i in file_list:
        if i.endswith('.jpg'):
            filename = file_label_train + "\\" + i[:-4] + '.txt'  # xml文件将’.txt‘改成'.xml'就可以了
            if os.path.exists(filename):
                shutil.move(filename, file_label_val)
                print(i + "处理成功！")


if __name__ == '__main__':
    fileDir = r"C:\Users\86159\Desktop\hat\JPEGImages" + "\\"  # 源图片文件夹路径
    tarDir = r'C:\Users\86159\Desktop\hat\JPEGImages_val'  # 图片移动到新的文件夹路径
    moveimg(fileDir, tarDir)
    file_list = os.listdir(tarDir)
    file_label_train = r"C:\Users\86159\Desktop\hat\Annotations_yolo"  # 源图片标签路径
    file_label_val = r"C:\Users\86159\Desktop\hat\Annotations_val"  # 标签
    # 移动到新的文件路径
    movelabel(file_list, file_label_train, file_label_val)
