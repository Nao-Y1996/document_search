import numpy as np
import pandas as pd

def calc_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    # 平均値を計算する
    mean = s / N

    return mean


def calc_var(numbers):
    # 平均値を計算する
    mean = calc_mean(numbers)

    # 差の二乗を計算する
    diff = [(x - mean) ** 2 for x in numbers]

    # 分散を計算する
    var = sum(diff) / len(numbers)

    return var


def calc_std(numbers):
    # 分散を計算する
    var = calc_var(numbers)

    # 標準偏差を計算する
    std = var ** 0.5

    return std
