# -*- coding: utf-8 -*-
# @CreateTime : 2024/4/16 016 17:11
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/unzip.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles

import shutil

# rename

file_path = r".\docx_files\demo.docx"
zip_file_path = r".\docx_files\demo.zip"

# # 拷贝并压缩
# shutil.copy(file_path, zip_file_path)

# 解压
shutil.unpack_archive(filename=zip_file_path, extract_dir=r".\target_folder", format="zip")

# --END--
