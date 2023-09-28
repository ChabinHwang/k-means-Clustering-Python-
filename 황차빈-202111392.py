# 선형대수학 K Mean 클러스터링
import math as mt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random as rd

data = pd.read_excel("termDocMatrix.xlsx", engine="openpyxl", header=None)
K = 9
# K는 임의의 중심 갯수
arr = np.array(data)
row = len(arr)
col = len(arr[1])

# A열이 nan값이므로, col-1이 총 열수라고 볼 수 있음
arr2 = np.transpose(arr)
# 문서끼리 비교해야 하므로, 한 열의 값을 한번에 불러올 수 없음. 따라서 행과 열을 전치
# arr2의 각 행은 문서에 해당하고, 각 열들은 단어에 해당함.
print(row, "row 4423임", col, "col 501", arr[3][5])
# 테스트 문장
random_k = rd.sample(range(1, col), K)
# 1~501사이, K개의 중심점의 좌표를 정함.
# 각 중심점과 길이를 비교


def k_means_klustering(data, center_arr, repeat):
    k = len(center_arr)  # 중심의 갯수
    # center_arr[0]<문서 인덱스
    # data[center_arr]<문서 벡터
    for m in range(len(data)):  # 여기서는 m번문서와, 중심문서k 9개를 비교함. 이후 배열함(첫행이 비어서 m+1)
        dist = (np.linalg.norm(data[center_arr[i]]-data[m+1])for i in range(K))


dist = np.linalg.norm(arr2[k+1]-arr2[random_k[i]])
# 각 벡터와 기준과 백터거리계산. 원소(두 백터의 차)의 곱의 합의 제곱근.
