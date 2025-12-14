# @InterpreterLocation : !C:\Users\20866\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
# @Author : 20866
# @CreateTime : 2022/2/12 17:50:02
# @Project: Pycharm_Project_Set
# @File : sort class.py
# @Software : PyCharm
# @Site : https://gitee.com/qiongjulingjun

import time


class Sort(object):
    """This class implements ten classic sorting algorithms.

    Our sorting routine always goes from small to large.
    """

    def __init__(self) -> None:
        # Calculate the number of exchanges.
        self.number_of_exchanges = 0

        # Calculate the number of cycles.
        self.cycles = 0

    def get_num_exchange(self) -> int:
        return self.number_of_exchanges

    def get_num_cycle(self) -> int:
        return self.cycles

    # Bubble sort.
    def bubble_sort(self, list_data: list[int]) -> list:
        """This function implements bubble sort.

        Bubble sorting is stable.

        Time complexity: O(n^2).
        """

        # If the list length is less than or equal to one, we return the list directly.
        if len(list_data) <= 1:
            return list_data

        # If the list length is greater than one, sort_class next。
        else:
            # Need to loop (len(list_data) - 1) rounds.
            for i in range(0, len(list_data)-1):
                # Each round compares the size of two adjacent numbers.
                for j in range(0, len(list_data)-1):
                    # If the first number is less than the last number, the two numbers are interchanged.
                    if list_data[j] > list_data[j+1]:
                        list_data[j], list_data[j+1] = list_data[j+1], list_data[j]
                        self.number_of_exchanges += 1
                    self.cycles += 1
            return list_data

    # Bubble sorting algorithm optimization.
    def bubble_sort_optimization(self, list_data: list[int]) -> list:
        """This function realizes the optimization of bubble sorting.

        Time complexity: O(n^2).
        """

        # If the list length is less than or equal to one, we return the list directly.
        if len(list_data) <= 1:
            # If the list length is greater than one, sort_class next。
            return list_data
        else:
            # # Need to loop (len(list_data) - 1) rounds.
            # for i in range(0, len(list_data) - 1):
            #     # Use a flag bit to determine whether the sorting has been completed
            #     flag_complete = True
            #     # Each round compares the size of two adjacent numbers.
            #     for j in range(0, len(list_data) - 1):
            #         # If the first number is less than the last number, the two numbers are interchanged.
            #         if list_data[j] > list_data[j + 1]:
            #             list_data[j], list_data[j + 1] = list_data[j + 1], list_data[j]
            #             flag_complete = False
            #             self.number_of_exchanges += 1
            #         self.cycles += 1
            #         if flag_complete is True:
            #             break
            # return list_data

            # Need to loop (len(list_data) - 1) rounds.
            # Optimize again.

            last_exchange_offset = 0
            sort_border = len(list_data) - 1

            for i in range(0, len(list_data) - 1):
                # Use a flag bit to determine whether the sorting has been completed
                flag_complete = True
                # Each round compares the size of two adjacent numbers.
                for j in range(0, sort_border):
                    # If the first number is less than the last number, the two numbers are interchanged.
                    if list_data[j] > list_data[j + 1]:
                        list_data[j], list_data[j + 1] = list_data[j + 1], list_data[j]
                        flag_complete = False
                        last_exchange_offset = j
                        self.number_of_exchanges += 1
                    self.cycles += 1
                    sort_border = last_exchange_offset
                    if flag_complete is True:
                        break
            return list_data

    # Selection sort.
    def selection_sort(self, list_data: list[int]) -> list:
        """This function implements selection sort.

        Selection sorting is unstable.

        Time complexity: O(n^2).
        """
        # If the list length is less than or equal to one, we return the list directly.
        if len(list_data) <= 1:
            return list_data

        else:
            # # Spend more time.
            # for i in range(0, len(list_data)-1):
            #     for j in range(i+1, len(list_data)):
            #         if list_data[i] > list_data[j]:
            #             list_data[i], list_data[j] = list_data[j], list_data[i]
            #             self.number_of_exchanges += 1
            #         self.cycles += 1
            #
            # return list_data

            for i in range(0, len(list_data)-1):
                # Let's assume 'i' is the minimum subscript.
                min_index = i
                for j in range(i+1, len(list_data)):
                    self.cycles += 1
                    if list_data[j] < list_data[min_index]:
                        min_index = j
                if i != min_index:
                    list_data[i], list_data[min_index] = list_data[min_index], list_data[i]
                    self.number_of_exchanges += 1

            return list_data

    # Direct insertion sorting.
    def insert_sort(self, list_data):
        """This function implements direct insertion sorting.

        Direct insertion sorting is stable.

        Time complexity: O(n^2).
        """

        if len(list_data) <= 1:
            return list_data

        else:
            for i in range(1, len(list_data)):
                # We set up a sentry and compare it with the number in front of it.
                sentry = list_data[i]
                pre_offset = i - 1
                while pre_offset >= 0 and sentry < list_data[pre_offset]:
                    # list_data[pre_offset], list_data[i] = list_data[i], list_data[pre_offset]

                    # Move back one by one.
                    list_data[pre_offset+1] = list_data[pre_offset]
                    pre_offset -= 1
                    self.number_of_exchanges += 1
                    self.cycles += 1
                list_data[pre_offset+1] = sentry

            return list_data

    # Binary Insertion Sort.
    def binary_insertion_sort(self, list_data: list[int]) -> list:
        """This function implements half insertion sorting.

        Binary insertion sorting is stable.

        Time complexity: O(n^2).
        """

        if len(list_data) <= 1:
            return list_data
        else:
            for i in range(1, len(list_data)-1):
                temp = list_data[i]
                low = 0
                high = i - 1

                while low <= high:
                    mid = (low + high) // 2
                    if temp < list_data[mid]:
                        high = mid - 1
                    else:
                        low = mid + 1
                    self.cycles += 1
                for j in range(i, low+2, -1):
                    list_data[j] = list_data[j-1]
                    self.cycles += 1
                list_data = temp
            return list_data

    # Shell sort.
    def shell_sort(self, list_data: list[int]) -> list:
        if len(list_data) <= 1:
            return list_data
        else:
            return [0]

    def quick_sort(self):
        pass


if __name__ == '__main__':
    test_list = [88, 5, 4, 3, 1, 2, 8, 6, 7, 90, 52, 26, 15, 55, 72, 15, 11, 19, 20, 12, 13, 19, 16]
    # test_list = [5, 4, 3, 1, 2]
    # test_list = [2, 1]
    print(test_list)

    begin = time.perf_counter()

    sort_function = Sort()

    # Bubble sorting.
    # # Obviously, the optimized algorithm is faster.

    # print(sort_function.bubble_sort(test_list))
    # print(sort_function.bubble_sort_optimization(test_list))

    # Selection sorting.
    # print(sort_function.selection_sort(test_list))

    # Insert sorting.
    # print(sort_function.insert_sort(test_list))
    print(sort_function.binary_insertion_sort(test_list))

    # Shell sorting.
    print('Number of exchanges: ', sort_function.get_num_exchange())
    print('Number of cycles: ', sort_function.get_num_cycle())

    end = time.perf_counter()
    print('Total time: ', end - begin)
    pass
