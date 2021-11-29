#coding: utf-8
"""
采用多进程加快处理。添加了在读取图片时捕获异常，OpenCV对大分辨率或者tif格式图片支持不好
处理数据集 和 标签数据集的代码：（主要是对原始数据集裁剪）
    处理方式：分别处理
    注意修改 输入 输出目录 和 生成的文件名
    output_dir = "./label_temp"
    input_dir = "./label"
"""
from New202109.NetworkGame.Config.GlobalValue import GlobalMap
import multiprocessing
import cv2
import os
import time


def get_img(input_dir):
    img_paths = []
    for (path,dirname,filenames) in os.walk(input_dir):
        for filename in filenames:
            img_paths.append(path+'/'+filename)
    print("img_paths:",img_paths)
    return img_paths


def cut_img(img_paths,output_dir):
    imread_failed = []
    try:
        pass
        # img = cv2.imread(img_paths)
        # height, weight = img.shape[:2]
        # if (1.0 * height / weight) < 1.3:       # 正常发票
        #     cropImg = img[50:200, 700:1500]     # 裁剪【y1,y2：x1,x2】
        #     cv2.imwrite(output_dir + '/' + img_paths.split('/')[-1], cropImg)
        # else:                                   # 卷帘发票
        #     cropImg_01 = img[30:150, 50:600]
        #     cv2.imwrite(output_dir + '/' + img_paths.split('/')[-1], cropImg_01)
    except:
        imread_failed.append(img_paths)
    return imread_failed


def main(input_dir,output_dir):
    img_paths = get_img(input_dir)
    scale = len(img_paths)

    results = []
    pool = multiprocessing.Pool(processes = 4)
    for i,img_path in enumerate(img_paths):
        a = "#"* int(i/10)
        b = "."*(int(scale/10)-int(i/10))
        c = (i/scale)*100
        results.append(pool.apply_async(cut_img, (img_path,output_dir )))
        print('{:^3.3f}%[{}>>{}]'.format(c, a, b)) # 进度条（可用tqdm）
    pool.close()                        # 调用join之前，先调用close函数，否则会出错。
    pool.join()                         # join函数等待所有子进程结束
    for result in results:
        print('image read failed!:', result.get())
    print ("All done.")



if __name__ == "__main__":
    GlobalMap()
    input_dir = "."+GlobalMap().mapconfig['path']['baseimgpath']+"atlases"  # 读取图片目录表
    output_dir = "."+GlobalMap().mapconfig['path']['baseimgpath']+"newatlases"   # 保存截取的图像目录
    main(input_dir, output_dir)
