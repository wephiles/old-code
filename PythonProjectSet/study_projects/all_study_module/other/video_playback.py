# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/2/13 17:39:37
# @Project: Pycharm_Project_Set
# @File : video_playback.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun


from PIL import Image, ImageSequence
# 读取 GIF
im = Image.open("1.gif")
# GIF 图片流的迭代器
iter_ = ImageSequence.Iterator(im)
index = 1
# 遍历图片流的每一帧
for frame in iter_:
    print("image %d: mode %s, size %s" % (index, frame.mode, frame.size))
    frame.save("./images/img%d.png" % index)
    index += 1
# 把 GIF 拆分为图片流
imgs = [frame.copy() for frame in ImageSequence.Iterator(im)]
# 图片流反序
imgs.reverse()
# 将反序后的所有帧图像保存下来
imgs[0].save("reverse.gif", save_all=True, append_images=imgs[1:])
