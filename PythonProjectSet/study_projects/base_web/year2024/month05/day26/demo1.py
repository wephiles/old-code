# -*- coding: utf-8 -*-
# @CreateTime : 2024/5/26 026 14:14
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : studyProject
# @FileName : studyProject/demo1.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.
"""
下载三个视频
"""
import requests
from concurrent.futures.thread import ThreadPoolExecutor

video_list = [
    ("video1.mp4",
     r"https://v5-hl-hw-cn-coldy.douyinvod.com/b2c0bb253a0040fd060a6017436554f1/6652e1f8/video/tos/cn/tos-cn-ve-15/ce00e2ed68f14214ac12ed395afa5c0e/?a=1128&ch=0&cr=0&dr=0&lr=aweme_search_suffix&cd=0%7C0%7C0%7C0&cv=1&br=1644&bt=1644&cs=0&ds=3&ft=rVQ6egwwZRd0shPo1PDS6kFgAX1tG1f3Af9eFQ0NrsO12nzXT&mime_type=video_mp4&qs=0&rc=OjRnO2VnaGZnaTc6Zzg3NUBpanI4b2t5M2ZweTMzOmkzM0BhYmExMzAvNTQxXl8vNF5iYSNsMGw0YGRiXl9fLS0yLTBzcw%3D%3D&btag=c0010e00098000&cquery=100y&dy_q=1716704199&l=20240526141639B0059BA42C78201CF896"),
    ("video2.mp4",
     r"https://v3-web.douyinvod.com/26c5e6d7ef8c02536a511f6a2a921f40/6652e336/video/tos/cn/tos-cn-ve-15c001-alinc2/ooeLDmtyD163Ae001QNIEgAgQxmCBnnBAE7b9a/?a=6383&ch=5&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1881&bt=1881&cs=0&ds=4&ft=rVWEerwwZRd0shPo1PDS6kFgAX1tGNJ3Af9eFQ0NrsO12nzXT&mime_type=video_mp4&qs=0&rc=NmY1ZTMzOzQ5NTs6NDo7OEBpanR1bzM6ZnZxcjMzNGkzM0AzMC0wYjQvNmMxXmMuNjRgYSNnXmtwcjRfLjJgLS1kLWFzcw%3D%3D&btag=c0000e00028000&cquery=100z_100a_101s_100B_100x&dy_q=1716704385&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=2024052614194357D53474622B8046DD2E"),
    ("video3.mp4",
     r"https://v3-web.douyinvod.com/26c5e6d7ef8c02536a511f6a2a921f40/6652e336/video/tos/cn/tos-cn-ve-15c001-alinc2/ooeLDmtyD163Ae001QNIEgAgQxmCBnnBAE7b9a/?a=6383&ch=5&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1881&bt=1881&cs=0&ds=4&ft=rVWEerwwZRd0shPo1PDS6kFgAX1tGNJ3Af9eFQ0NrsO12nzXT&mime_type=video_mp4&qs=0&rc=NmY1ZTMzOzQ5NTs6NDo7OEBpanR1bzM6ZnZxcjMzNGkzM0AzMC0wYjQvNmMxXmMuNjRgYSNnXmtwcjRfLjJgLS1kLWFzcw%3D%3D&btag=c0000e00028000&cquery=100z_100a_101s_100B_100x&dy_q=1716704385&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=2024052614194357D53474622B8046DD2E")
]


# 多线程并行下载
def task(url):
    res = requests.get(url=url,
                       headers={
                           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.3.306"
                       }
                       )
    return res.content


# 下载完成之后 Python多线程内部会执行的函数
def outer(file_name):
    def done(arg):
        """

        Args:
            arg (): 规定必须要有 下载完成后返回的那个值

        Returns:

        """
        # 视频内容
        content = arg.result()
        with open(file_name, "wb") as fp:
            fp.write(content)

    return done


# 线程池
POOL = ThreadPoolExecutor(max_workers=10)
for item in video_list:
    # 去线程池取一个人 让这个人帮我们执行task函数  函数内部定义下载逻辑
    future_obj = POOL.submit(task, url=item[1])
    # 当执行完task函数之后（下载完成）自动执行一个done函数
    future_obj.add_done_callback(outer(item[0]))
    print(item)

# --END--
