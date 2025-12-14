# -*- coding: utf-8 -*-
# @CreateTime : 2024/2/26 026 19:19
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : studyProject/support_java.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles or https://gitee.com/wephiles


import json

from flask import Flask

app = Flask(__name__)


@app.route("/get/info")
def index():
    data = ["computer", "science", "technology", "计算机科学与技术"]
    res = json.dumps(data, ensure_ascii=False)
    return res


@app.route("/do/play")
def play():
    info = {
        "code": 1000,
        "status": True,
        "values": [
            {"id": 1, "name": "Computer"},
            {"id": 2, "name": "Science"},
            {"id": 3, "name": "Technology"},
            {"id": 4, "name": "计算机科学与技术"}
        ]
    }
    res = json.dumps(info, ensure_ascii=False)
    return res


if __name__ == "__main__":
    app.run()

# --END--
