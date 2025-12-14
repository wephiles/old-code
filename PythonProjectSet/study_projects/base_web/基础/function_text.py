# -*- coding: utf-8 -*-
# @CreateTime : 2024/2/25 025 16:41
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/function_text.py
# @Description :
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles


import sys

import requests

# 图片专区
img_data = {
    "1": ("image1", r"https://pic.3gbizhi.com/uploadmark/20230825/979bcabfd305afce4b5b5d00e467e01f.jpg"),
    "2": ("image2", r"https://pic.3gbizhi.com/uploadmark/20220916/35c9f1a1e642ba133b0efc2b58b9ae02.png"),
    "3": ("image3", r"https://pic.3gbizhi.com/uploadmark/20190912/6d7abd46d1531635e9b187cdea724345.jpg"),
    "4": ("image4", r"https://pic.3gbizhi.com/uploadmark/20231120/004a59dc1b775ee4ea19cb9f350682bc.jpg"),
    "5": ("image5", r"https://pic.3gbizhi.com/uploadmark/20231030/d74c8cbc8bb461cef094e6b686990fde.jpg"),
    "6": ("image6", r"https://pic.netbian.com/uploads/allimg/230405/000245-168062416593ad.jpg")
}

# NBA 专区
nba_data = {
    "1": {
        "title": "title1",
        "url": r"https://v3-web.douyinvod.com/5f859c5bcc8097014fe28d4aa0a51c85/65da090c/video/tos/cn/tos-cn-ve-15/oMGs"
               r"fhDALWBH8UmrCmFEAeDhBqA7L14IQBfmE6/?a=6383&ch=5&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1721&bt="
               r"1721&cs=0&ds=6&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pikecsejKJV7TYeo0P3-I&mime_type=video_mp4&qs=0&rc=OGY1Oz"
               r"VmNWQ5aTU4OWY1OEBpM2RnO205cjt3cTMzNGkzM0AzMy1iMzA1XmMxYjAxNmA1YSMtM24tMmRjY15gLS1kLS9zcw%3D%3D&btag"
               r"=e00028000&dy_q=1708784219&feature_id=f0150a16a324336cda5d6dd0b69ed299&l=20240224221658C1E7B1B597C2"
               r"A7D01ABA"},
    "2": {
        "title": "title2",
        "url": r"https://v3-web.douyinvod.com/f3e00fdf66b9fa32014f76739ce9a6c2/65da0964/video/tos/cn/tos-cn-ve-15"
               r"/ocw45QDzyBEJirkfhQCGnAIsAA7ZN7MgAeE5LX/?a=6383&ch=5&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br="
               r"817&bt=817&cs=0&ds=6&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pi9vcsejKJV7TYeo0P3-I&mime_type=video_mp4&qs="
               r"0&rc=N2U2OGc0OGhkZWZmaGlnOUBpMzVoMzw6ZmVncTMzNGkzM0AxMjBjMzUzXzUxMDQuNi5gYSNsNjRqcjRnbGBgLS1kLT"
               r"Bzcw%3D%3D&btag=e00028000&dy_q=1708784308&feature_id=f0150a16a324336cda5d6dd0b69ed299&l=20240224"
               r"221827BDAEFE7D705F16E75C4C"}}

# 短视频专区
short_video_data = {
    "1": {
        "title": "title1",
        "url": r"https://v3-web.douyinvod.com/5f859c5bcc8097014fe28d4aa0a51c85/65da090c/video/tos/cn/tos-cn-ve-15"
               r"/oMGsfhDALWBH8UmrCmFEAeDhBqA7L14IQBfmE6/?a=6383&ch=5&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br="
               r"1721&bt=1721&cs=0&ds=6&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pikecsejKJV7TYeo0P3-I&mime_type=video_mp4&qs"
               r"=0&rc=OGY1OzVmNWQ5aTU4OWY1OEBpM2RnO205cjt3cTMzNGkzM0AzMy1iMzA1XmMxYjAxNmA1YSMtM24tMmRjY15gLS1kL"
               r"S9zcw%3D%3D&btag=e00028000&dy_q=1708784219&feature_id=f0150a16a324336cda5d6dd0b69ed299&l=202402"
               r"24221658C1E7B1B597C2A7D01ABA"
    },
    "2": {
        "title": "title2",
        "url": r"https://v3-web.douyinvod.com/f3e00fdf66b9fa32014f76739ce9a6c2/65da0964/video/tos/cn/tos-cn-ve"
               r"-15/ocw45QDzyBEJirkfhQCGnAIsAA7ZN7MgAeE5LX/?a=6383&ch=5&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv"
               r"=1&br=817&bt=817&cs=0&ds=6&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pi9vcsejKJV7TYeo0P3-I&mime_type=video"
               r"_mp4&qs=0&rc=N2U2OGc0OGhkZWZmaGlnOUBpMzVoMzw6ZmVncTMzNGkzM0AxMjBjMzUzXzUxMDQuNi5gYSNsNjRqcjRnb"
               r"GBgLS1kLTBzcw%3D%3D&btag=e00028000&dy_q=1708784308&feature_id=f0150a16a324336cda5d6dd0b69ed29"
               r"9&l=20240224221827BDAEFE7D705F16E75C4C"
    }
}


def image_area():
    print("======================== you are now in image area ========================")
    msg_list = []
    for k, item in img_data.items():
        string = "{}-{}".format(k, item[0])
        msg_list.append(string)
    msg_string = ": ".join(msg_list)
    while True:
        print(msg_string)
        img_num = input("choose the number of images!\n>>> ")
        if img_num.upper() == "N":
            return
        item_tuple = img_data.get(img_num)

        if not item_tuple:
            print("index error, please try again.", file=sys.stderr)
            continue
        print("correct index, downloading image ...")
        # print(img_data[img_num][0], " ", img_data[img_num][1])
        title, url = item_tuple
        download(model=".png", url=url, file_name=title)
        print(title, url)
        print("download image over.")

        # print("if you want to download the image again? If you want, input n/N else input y/Y.")
        # if_repeat = input(">>> ")
        # if if_repeat.upper() == "Y":
        #     image_area()
        # elif if_repeat.upper() == "N":
        #     print()
        #     return
        # else:
        #     raise ValueError("input error: {}".format(if_repeat))
        # print()


def nba_area():
    img_num = input("choose the number of nba images!\n>>> ")

    print("download image ...")
    print(nba_data[img_num]["title"], " ", nba_data[img_num]["url"])
    print("download image over.")

    print("if you want to download the image again? If you want, input n/N else input y/Y.")
    if_repeat = input(">>> ")
    if if_repeat.upper() == "Y":
        nba_area()
    elif if_repeat.upper() == "N":
        print()
        return
    else:
        raise ValueError("input error: {}".format(if_repeat))
    print()


def video_area():
    img_num = input("choose the number of video!\n>>> ")

    print("download image ...")
    print(short_video_data[img_num]["title"],
          " ", short_video_data[img_num]["url"])
    print("download image over.")

    print("if you want to download the image again? If you want, input n/N else input y/Y.")
    if_repeat = input("please input your choice: \n>>> ")
    if if_repeat.upper() == "Y":
        nba_area()
    elif if_repeat.upper() == "N":
        print()
        return
    else:
        raise ValueError("input error: {}".format(if_repeat))
    print()


def download(model=".jpg", url="", file_name=r""):
    """

    Args:
        url (): str
        model (): range from [".jpg", ".mp4"]

    Returns:

    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.3.306"
    }
    res = requests.get(
        url=url,
        headers=headers
    )
    # 保存文件

    with open("./download_files/" + file_name + model, "wb") as fp:
        print("downloading...")
        fp.write(res.content)


def run():
    function_dict = {
        "1": image_area,
        "2": nba_area,
        "3": video_area,
    }

    while True:
        print("1. image 2. nba 3. short video")
        choice = input("choose a number, input Q or q to exit.\n>>> ")
        if choice.upper() == "Q":
            break

        func_obj = function_dict.get(choice)
        if not func_obj:
            # raise ValueError("input error: {}".format(choice))
            print("input error, try again: ", file=sys.stderr)
            continue
        func_obj()
    print()


if __name__ == "__main__":
    run()

# --END--
