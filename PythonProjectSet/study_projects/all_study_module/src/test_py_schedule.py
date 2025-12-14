#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime  :2024/09/04 20:16
# @Author      :wephiles@20866
# @IDE         :PyCharm
# @ProjectName :all_study_module
# @FileName    :all_study_module/test_py_schedule.py
# @Description :This is description of this script.
# @Interpreter :Python 3.0+
# @Motto       :You must take your place in the circle of life!
# @AuthorSite  :https://github.com/wephiles or https://gitee.com/wephiles

import helper
import time
import schedule
from schedule import repeat, every
import threading


# def task():
#     print('Doing task ...', helper.get_time())
#
#
# schedule.every(5).seconds.do(task)
# # schedule.every(5).minutes.do(task)
# # schedule.every(5).hours.do(task)
# # schedule.every(5).days.do(task)
# # schedule.every(5).weeks.do(task)
# #
# # schedule.every().minute(':15').do(task)  # 每当到15分钟的时候执行task
# # schedule.every().hour(':15').do(task)  # 每当到15点的时候执行task
# # schedule.every(10).minute(':15').do(task)  # 每隔10小时后在15分钟时运行
#
# # schedule.every().day.at('15:15:40').do(task)  # 每一天的15:15:40干这个
# schedule.every().monday.at('15:15:40').do(task)  # 每周一的15:15:40干这个
#
# while True:
#     # 每5秒运行一次task
#     schedule.run_pending()
#     time.sleep(1)
#     break
#
#
# # ===========================================================================
# @repeat(every(10).seconds)
# def task_1():
#     print('Do something: task 1')
#
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)

# ===========================================================================

# def task(arg1, arg2):
#     print(f'Doing task, arg1={arg1}, arg2={arg2}. At: {helper.get_time()}')
#
#
# schedule.every(2).seconds.do(task, '10', 12)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)

# ===========================================================================
# @repeat(every(5).seconds, 5, 'OhHou')
# @repeat(every(6).seconds, 0, 'OhNo')
# def task(arg1, arg2):
#     print(f'Doing task, arg1={arg1}, arg2={arg2}. At: {helper.get_time()}')
#
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)

# ===========================================================================
# def task(arg1, arg2):
#     print(f'Doing task, arg1={arg1}, arg2={arg2}. At: {helper.get_time()}')
#     # # 若想只运行一次 那么要return schedule.CancelJob
#     # return schedule.CancelJob
#
#
# schedule.every(2).seconds.do(task, 1, 2).tag('Work', 1)
# schedule.every(2).seconds.do(task, 1, 2).tag('Fun', 1)
# schedule.every(2).seconds.do(task, 1, 2).tag('Work', 1)
# schedule.every(2).seconds.do(task, 1, 2).tag('Fun', 1)
#
# fun = schedule.get_jobs('Fun')
# work = schedule.get_jobs('Work')
#
# print(fun)
# print(work)
#
# # schedule.cancel_job(job)  # 取消task
# # print(schedule.get_jobs())
#
# while True:
#     schedule.run_pending()
#     print('Jobs:', len(schedule.get_jobs()))
#     schedule.clear('Fun')  # 清除有关fun标签的task
#     time.sleep(1)
#     # print('Jobs:', len(schedule.get_jobs()))
#     # schedule.clear()  # 清除所以的job


def task():
    print('Doing task ...', helper.get_time())
    time.sleep(5)
    print('Task done')


def start_thread(func):
    job_one = threading.Thread(target=func)
    job_one.start()


schedule.every(1).seconds.do(start_thread, task)

while True:
    schedule.run_pending()
    time.sleep(1)

# --END--
