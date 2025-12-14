# -*- coding: utf-8 -*-
# @CreateTime : 2024/2/25 025 17:20
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/download_file.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles


# # 安装第三方模块进行下载
# import requests
#
url_list = [
    "https://pic.3gbizhi.com/uploadmark/20230825/979bcabfd305afce4b5b5d00e467e01f.jpg",
    "https://pic.3gbizhi.com/uploadmark/20220916/35c9f1a1e642ba133b0efc2b58b9ae02.png",
    "https://pic.3gbizhi.com/uploadmark/20190912/6d7abd46d1531635e9b187cdea724345.jpg",
    "https://pic.3gbizhi.com/uploadmark/20231120/004a59dc1b775ee4ea19cb9f350682bc.jpg",
    "https://pic.3gbizhi.com/uploadmark/20231030/d74c8cbc8bb461cef094e6b686990fde.jpg",
    "https://pic.netbian.com/uploads/allimg/230405/000245-168062416593ad.jpg",
    "https://pic.3gbizhi.com/uploadmark/20231120/004a59dc1b775ee4ea19cb9f350682bc.jpg",
    "https://dogefs.s3.ladydaily.com/~/source/wallhaven/full/vq/wallhaven-vqppz8.jpg?w=2560&h=1440&fmt=webp"
]
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.3.306"
# }
# i = 0
# for item in url_list:
#     # 下载文件
#     res = requests.get(
#         url=item,
#         headers=headers
#     )
#     # 保存文件
#
#     with open("./images/image" + str(i) + ".jpg", "wb") as fp:
#         print("downloading", i)
#         fp.write(res.content)
#     i += 1


# 安装第三方模块进行下载
# import requests
#
# # 下载图片
# url_list = [
#     r"https://v3-web.douyinvod.com/5f859c5bcc8097014fe28d4aa0a51c85/65da090c/video/tos/cn/tos-cn-ve-15/oMGs"
#     r"fhDALWBH8UmrCmFEAeDhBqA7L14IQBfmE6/?a=6383&ch=5&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1721&bt="
#     r"1721&cs=0&ds=6&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pikecsejKJV7TYeo0P3-I&mime_type=video_mp4&qs=0&rc=OGY1Oz"
#     r"VmNWQ5aTU4OWY1OEBpM2RnO205cjt3cTMzNGkzM0AzMy1iMzA1XmMxYjAxNmA1YSMtM24tMmRjY15gLS1kLS9zcw%3D%3D&btag"
#     r"=e00028000&dy_q=1708784219&feature_id=f0150a16a324336cda5d6dd0b69ed299&l=20240224221658C1E7B1B597C2"
#     r"A7D01ABA",
#
#     "https://v3-web.douyinvod.com/f3e00fdf66b9fa32014f76739ce9a6c2/65da0964/video/tos/cn/tos-cn-ve-15"
#     r"/ocw45QDzyBEJirkfhQCGnAIsAA7ZN7MgAeE5LX/?a=6383&ch=5&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br="
#     r"817&bt=817&cs=0&ds=6&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pi9vcsejKJV7TYeo0P3-I&mime_type=video_mp4&qs="
#     r"0&rc=N2U2OGc0OGhkZWZmaGlnOUBpMzVoMzw6ZmVncTMzNGkzM0AxMjBjMzUzXzUxMDQuNi5gYSNsNjRqcjRnbGBgLS1kLT"
#     r"Bzcw%3D%3D&btag=e00028000&dy_q=1708784308&feature_id=f0150a16a324336cda5d6dd0b69ed299&l=20240224"
#     r"221827BDAEFE7D705F16E75C4C",
# ]
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.3.306"
# }
# i = 0
# for item in url_list:
#     # 下载文件
#     res = requests.get(
#         url=item,
#         headers=headers
#     )
#     # 保存文件
#
#     with open("./videos/video" + str(i) + ".mp4", "wb") as fp:
#         print("downloading", i)
#         fp.write(res.content)
#     i += 1

# --END--
